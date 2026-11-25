"""更新タグ検査の単体テスト。

2026-11-23 のフック修正（合格表示を標準エラーへ出す）と、
複合タグの優先順を、git を呼ばずに確かめる。
実行: python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import importlib.util
import io
import json
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_update_tags",
    ROOT / "scripts" / "check-update-tags.py",
)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


def digest(*sections: str) -> str:
    return "\n".join(sections) + "\n"


HIGHLIGHT = """## 今日のハイライト

### 1. [破壊的変更+新機能] 接続を会話の中で設定できる — 自前のキャンバスは改修が必要になる
"""

CATEGORY = """## Copilot Studio / Power Platform

- [料金+新機能] **クレジットの従量** — 既定オンの従量を料金として主にする
  - https://example.com/detail
- [仕様] **移行で失う機能** — Adaptive Cards は残す
- （ハイライト1参照）
- https://example.com/only
- 直近の期限: 12/1 に Code ノードが GA
"""

EXCLUDED = """## 次の節目

- タグの無い行でも、除外見出しの下なら不合格にしない
"""


class TagErrorTest(unittest.TestCase):
    def test_single_and_ordered_compound_tags(self):
        self.assertIsNone(mod.tag_error("新機能"))
        self.assertIsNone(mod.tag_error("料金+新機能"))
        self.assertIsNone(mod.tag_error("破壊的変更+新機能"))
        self.assertIsNone(mod.tag_error("破壊的変更+料金"))

    def test_price_may_lead_breaking_change(self):
        self.assertIsNone(mod.tag_error("料金+破壊的変更"))

    def test_secondary_must_rank_below_primary(self):
        self.assertEqual(mod.tag_error("新機能+料金"), "副は主より優先順が下")
        self.assertEqual(mod.tag_error("セキュリティ+破壊的変更"), "副は主より優先順が下")
        self.assertEqual(mod.tag_error("新機能+新機能"), "副は主より優先順が下")

    def test_shape_and_vocabulary(self):
        self.assertEqual(mod.tag_error("料金+新機能+仕様"), "主は1語、副は1語まで")
        self.assertEqual(mod.tag_error("速報"), "11語以外")
        self.assertEqual(mod.tag_error("料金+"), "11語以外")


class CheckTextTest(unittest.TestCase):
    def test_digest_accepts_compound_tags_and_skips_non_items(self):
        text = digest(HIGHLIGHT, CATEGORY, EXCLUDED)
        self.assertEqual(mod.check_text(text, "digest"), [])

    def test_digest_rejects_missing_tag_and_reversed_compound(self):
        text = digest(
            "## Copilot Studio\n",
            "- タグが無い項目\n",
            "- [新機能+料金] **順序が逆** — 副が主より上\n",
        )
        errors = mod.check_text(text, "digest")
        self.assertEqual(len(errors), 2)
        self.assertIn("項目の行頭に [タグ] が無い", errors[0])
        self.assertIn("[新機能+料金] 副は主より優先順が下", errors[1])

    def test_fullwidth_highlight_reference_is_not_an_item(self):
        text = digest("## 分野\n", "- （ハイライト１参照）\n", "- ハイライト参照\n")
        self.assertEqual(mod.check_text(text, "digest"), [])

    def test_invalid_tag_on_a_highlight_reference_is_still_skipped(self):
        text = "\n".join(
            [
                "## 開発ツール",
                "- [不明] （ハイライト1参照）",
                "- [不明] （ハイライト１参照）",
                "- [不明] ハイライト参照",
                "- [不明] （ハイライト 12 参照）",
                "- [不明] ハイライトの話",
            ]
        )
        self.assertEqual(mod.check_text(text, "digest"), ["6: [不明] 11語以外"])

    def test_daily_category_requires_bold_heading(self):
        text = """## 今日のハイライト
### 1. [新機能] 題 — 含意

## カテゴリ別まとめ
- [新機能] 太字が無い
"""
        errors = mod.check_text(text, "daily")
        self.assertEqual(errors, ["5: カテゴリ行は「- [タグ] **見出し** — 本文」"])

    def test_daily_ignores_sections_outside_highlight_and_category(self):
        text = digest("## その他\n", "- タグが無い\n")
        self.assertEqual(mod.check_text(text, "daily"), [])

    def test_highlight_shape(self):
        text = """## 今日のハイライト
### 1. タグが無い題 — 含意
"""
        errors = mod.check_text(text, "digest")
        self.assertEqual(errors, ["2: ハイライトは「### N. [タグ] タイトル — 含意」"])


class CheckFileTest(unittest.TestCase):
    def test_files_before_rollout_are_skipped(self):
        path = ROOT / "digests/2026/09/ai-news-2026-09-03.md"
        self.assertTrue(path.is_file())
        self.assertEqual(mod.check_file(path), [])

    def test_missing_file_with_a_covered_date(self):
        path = Path("digests/ai-news-2026-11-25.md")
        self.assertEqual(mod.check_file(path), [f"ファイルが無い: {path}"])

    def test_shipped_digests_still_pass(self):
        for name in ("2026-11-25", "2026-11-12"):
            path = ROOT / f"digests/2026/11/ai-news-{name}.md"
            self.assertEqual(mod.check_file(path), [], name)


class HookTargetTest(unittest.TestCase):
    def test_commit_uses_the_index_and_drops_non_news(self):
        with mock.patch.object(
            mod,
            "git_lines",
            return_value=["digests/2026/11/ai-news-2026-11-25.md", "README.md"],
        ) as git:
            got = mod.hook_targets("git commit -m 'digest'")
        git.assert_called_once_with(["diff", "--cached", "--name-only"])
        self.assertEqual(got, [Path("digests/2026/11/ai-news-2026-11-25.md")])

    def test_commit_all_uses_worktree_status_and_rename_destination(self):
        porcelain = [
            " M digests/2026/11/ai-news-2026-11-25.md",
            "R  old.md -> digests/2026/11/ai-news-2026-11-24.md",
            "?? notes.txt",
        ]
        with mock.patch.object(mod, "git_lines", return_value=porcelain) as git:
            got = mod.hook_targets("git commit -a -m 'digest'")
        git.assert_called_once_with(["status", "--porcelain"])
        self.assertEqual(
            got,
            [
                Path("digests/2026/11/ai-news-2026-11-25.md"),
                Path("digests/2026/11/ai-news-2026-11-24.md"),
            ],
        )

    def test_push_falls_back_when_the_main_diff_is_empty(self):
        def fake(args):
            if "origin/main...HEAD" in args:
                return []
            return ["digests/2026/11/ai-news-2026-11-25.md", "CLAUDE.md"]

        with mock.patch.object(mod, "git_lines", side_effect=fake) as git:
            got = mod.hook_targets("git push origin HEAD")
        self.assertEqual(
            git.call_args_list[0].args[0],
            ["diff", "--name-only", "origin/main...HEAD"],
        )
        self.assertEqual(
            git.call_args_list[1].args[0],
            ["diff", "--name-only", "HEAD~1", "HEAD"],
        )
        self.assertEqual(got, [Path("digests/2026/11/ai-news-2026-11-25.md")])


class RunHookTest(unittest.TestCase):
    def invoke(self, payload, targets):
        stdout, stderr = io.StringIO(), io.StringIO()
        raw = payload if isinstance(payload, str) else json.dumps(payload)
        with (
            mock.patch.object(mod, "hook_targets", return_value=targets),
            mock.patch("sys.stdin", io.StringIO(raw)),
            mock.patch("sys.stdout", stdout),
            mock.patch("sys.stderr", stderr),
        ):
            code = mod.run_hook()
        return code, stdout.getvalue(), stderr.getvalue()

    def test_ignores_empty_invalid_and_non_git_input(self):
        self.assertEqual(self.invoke("", [])[0], 0)
        self.assertEqual(self.invoke("{", [])[0], 0)
        code, stdout, stderr = self.invoke(
            {"tool_input": {"command": "python3 scripts/check-update-tags.py"}},
            [],
        )
        self.assertEqual((code, stdout, stderr), (0, "", ""))
        code, stdout, stderr = self.invoke({"tool_input": {"command": 1}}, [])
        self.assertEqual(code, 0)

    def test_pass_message_goes_to_stderr_and_stdout_stays_empty(self):
        path = ROOT / "digests/2026/11/ai-news-2026-11-25.md"
        code, stdout, stderr = self.invoke(
            {"tool_input": {"command": "git commit -m 'digest'"}},
            [path],
        )
        self.assertEqual(code, 0)
        self.assertEqual(stdout, "")
        self.assertIn(f"{path}: 合格", stderr)
        self.assertNotIn("不一致のまま", stderr)

    def test_no_target_message_also_stays_off_stdout(self):
        code, stdout, stderr = self.invoke(
            {"tool_input": {"cmd": "git push"}},
            [],
        )
        self.assertEqual(code, 0)
        self.assertEqual(stdout, "")
        self.assertIn("検査対象の日次・ダイジェストは無い", stderr)

    def test_failure_blocks_the_command_without_writing_stdout(self):
        with mock.patch.object(mod, "check_file", return_value=["2: [速報] 11語以外"]):
            code, stdout, stderr = self.invoke(
                {"tool_input": {"command": "git commit -m 'digest'"}},
                [Path("digests/2026/11/ai-news-2026-11-25.md")],
            )
        self.assertEqual(code, 2)
        self.assertEqual(stdout, "")
        self.assertIn("更新タグの検査が不合格", stderr)
        self.assertIn("[速報] 11語以外", stderr)
        self.assertIn("不一致のままコミット・push しない", stderr)


if __name__ == "__main__":
    unittest.main()
