# AI News Digest

## 基本方針

- 出力は日本語
- 簡潔で実用的な情報を好む。冗長な説明は不要
- 定量的な根拠を重視
- **Microsoft エコシステムの AI ニュースに特化する**（M365 Copilot / Copilot Studio / Power Platform / Azure AI / Microsoft の AI モデル）
- **他社の AI 開発ツール（Cursor / Claude / Anthropic / OpenAI / Codex / Devin / Gemini 等）は `kit1132/01_ai-news-Master` の担当。このリポジトリでは扱わない**
  - 2026-07-26 の実測で、直近10ファイル中7ファイルの先頭 H2 が「AI開発ツール」になっており、Microsoft 一次が「据え置き・新規なし」の日を他社ツールで埋めていた。担当範囲の宣言が 01 のコピーのままだったことが原因
  - Microsoft の一次情報に新規がない日は、`output-style.md` の「情報が少ない日は無理に増やさない（『特筆事項なし』でOK）」に従う。他社ツールで埋めない

## プロジェクト構成

- `digests/YYYY/MM/ai-news-YYYY-MM-DD.md` — デイリーダイジェスト本体
- `.last-check-state.md` — 各ソースの前回チェック状態（差分判定用）
- `IMPROVEMENT-BACKLOG.md` — 改善提案・取得障害の台帳（改善メモの単一情報源。運用ルールはファイル冒頭参照）
- `index.html` — 統合ビューア（https://kit1132.github.io/01_ai-news-Master/ ）へのリダイレクト。実体は 01_ai-news-Master/index.html にある。**このファイルは編集不要**
- `files.json` — ビューアが参照するダイジェストファイル一覧（新しい順、パスはルートからの相対）

## 実行環境

- Claude Code on the web（クラウド実行）
- スケジュールタスクとして毎朝自動実行
- ネットワーク: Full internet（外部サイトへのWebFetch/WebSearchが必要）
- **ブランチ: 必ず `main` を使用する（下記「⚠️ ブランチ運用」参照）**
- **日付: JST（Asia/Tokyo, UTC+9）で判定する。`TZ=Asia/Tokyo date +%Y-%m-%d` で当日日付を取得すること**

## ⚠️ ブランチ運用（最重要・絶対ルール）

**クラウド実行環境はセッションごとに自動で開発ブランチ（`claude/...`）を割り当てるため、2026-06-11 にスケジュールタスクが feature branch（`claude/awesome-cray-h19vj2`）へ digest をコミットする事故が発生した。同じ事故を二度と起こさないため、以下を絶対ルールとする。**

### 開始時（毎セッション必ず）

```bash
TZ=Asia/Tokyo date +%Y-%m-%d        # 当日日付を取得
git fetch origin main --depth=1
git checkout main
git pull --ff-only origin main
git rev-parse --abbrev-ref HEAD     # → 必ず `main` であることを確認
```

`.claude/settings.json` の SessionStart hook が自動で `main` への checkout を試みるが、**ハードコードに頼らず自分でも上記コマンドを必ず実行して確認すること**。

### コミット・push（毎回必ず）

```bash
git add digests/ .last-check-state.md IMPROVEMENT-BACKLOG.md files.json
git commit -m "add daily digest YYYY-MM-DD"
git push origin HEAD:main           # ← 必ず main に直接 push する
```

**`git push` 単体（リモート追跡ブランチへの push）は禁止**。必ず `HEAD:main` 形式を使う。これにより、たとえ作業が feature branch 上であっても結果は main に反映される。

### 禁止事項

- `git checkout -b <new-branch>` — 新規ブランチを切らない
- `git push origin <feature-branch>` — feature branch にだけ push しない
- PR 作成して放置 — 自動マージしないので main に反映されない
- main 以外のブランチで作業終了 — どんな状況でも最後は main に push する

## ⚠️ カバレッジ自己チェック（push 前に毎回必須）

**2026-06-12 のリモートルーチン移行後、「毎日確認」ソースの半数以上（M365 Roadmap / Microsoft Copilot Blog / Power Platform 系ブログ / X トレンド等）が巡回されず、`.last-check-state.md` の最終確認日が 6/12-13 のまま凍結する問題が約3週間続いた（2026-07-02 発覚）。再発防止のため以下を絶対ルールとする。**

- push 前に `grep -B1 "最終確認" .last-check-state.md` を実行し、`daily-sources.md` で頻度「毎日確認」の**全ソース**の最終確認日が当日（JST）になっていることを確認する
- 当日になっていないソースが1つでもあれば、push 前にそのソースを確認して `.last-check-state.md` を更新する。どうしても確認できない場合は、該当ソースの備考に「YYYY-MM-DD スキップ（理由）」と明記する（黙ってスキップしない）
- 「週次確認」ソースは最終確認が7日以内であることを確認し、超過していればその日に確認する

## ダイジェスト生成後の手順

1. `digests/YYYY/MM/ai-news-YYYY-MM-DD.md` を生成（ディレクトリがなければ作成）
2. `.last-check-state.md` を更新
3. **カバレッジ自己チェックを実施する**（上記「⚠️ カバレッジ自己チェック」参照）
4. `IMPROVEMENT-BACKLOG.md` を更新（新規提案の起票・既出提案の回数更新・障害の最終確認日更新。`output-style.md` の改善メモ規定参照）
5. `files.json` の配列先頭に新ファイルのパス（`digests/YYYY/MM/ai-news-YYYY-MM-DD.md`）を追加
6. **`git push origin HEAD:main` で main に直接 push する**（上の絶対ルール参照。`IMPROVEMENT-BACKLOG.md` を含めること）

## ルール参照

詳細なフィルタリング基準・対象サイトは `.claude/rules/` 以下を参照すること。
各タスクは該当するrulesファイルを読み込んでから実行する。
