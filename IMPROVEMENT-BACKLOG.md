# 改善バックログ

改善提案・取得障害の台帳（改善メモの単一情報源）。デイリーエージェントが毎日更新し、ルールへの反映可否は kit が判断する。

## 運用ルール（エージェント向け）

- ダイジェストの「改善メモ」を書く**前に**必ずこのファイルを読み、先に台帳を更新する
- **新しい改善案** → 「提案中」に新規ブロックを追記（ID は既存の最大番号 +1。アーカイブ含む）
- **既出の提案を本日も再確認した** → 該当ブロックの「最終確認」を当日に更新し「回数」を +1。内容の重複起票は禁止
- **新しい取得障害** → 「既知の取得障害」に1行追加。**既知の障害が今日も発生** → 最終確認日のみ更新
- **障害が復旧した** → 該当行の行末に `→ 復旧（YYYY-MM-DD）` を追記（行は削除しない）
- 「状態」の変更（採用済み・見送り）とアーカイブへの移動は **kit が行う。エージェントは行わない**
- このファイルにはルール改善の提案と取得障害のみを書く。ニュース内容の気づきは書かない

## 提案中

- B-005: Qiita RSSフィード全4件（copilotstudio / powerplatform / powerautomate / powerapps）が403を返す — 対象: `daily-sources.md` Qiitaセクションの取得方法 / 変更内容: プライマリをWebSearch（`site:qiita.com タグ名 2026`）に変更 / 根拠: 2026-06-11に全フィードで403確認（初出 2026-06-11 / 最終確認 2026-06-11 / 回数 1）
- B-006: Zenn RSSフィード全3件（copilotstudio / powerplatform / powerautomate）が403を返す — 対象: `daily-sources.md` Zennセクションの取得方法 / 変更内容: プライマリをWebSearch（`site:zenn.dev トピック名 2026`）に変更 / 根拠: 2026-06-11に全フィードで403確認（初出 2026-06-11 / 最終確認 2026-06-11 / 回数 1）
- B-007: devblogs.microsoft.com M365 Developer Blog RSSフィードが403 — 対象: `daily-sources.md` M365 Developer Blogセクションの取得方法 / 変更内容: プライマリをWebSearchに変更、RSS URLを代替に降格 / 根拠: 2026-06-11にRSS URL 2件とも403確認（初出 2026-06-11 / 最終確認 2026-06-11 / 回数 1）

## 既知の取得障害

- mc.merill.net: 403（初出 2026-06-06 ※それ以前から継続の可能性 / 最終確認 2026-06-11）→ 回避策: WebSearch
- techcommunity.microsoft.com（M365 Copilot Blog / Copilot Studio Blog）: 403（初出 2026-06-06 / 最終確認 2026-06-11）→ 回避策: WebSearch（board RSS も 2026-06-11 に 403 確認）
- releasebot.io: 403（初出 2026-06-08 / 最終確認 2026-06-11）→ 回避策: WebSearch。Claude Code 分は code.claude.com を直接 WebFetch
- cursor.com/changelog: 403（初出 2026-06-07 / 最終確認 2026-06-11）→ 回避策: WebSearch
- code.claude.com/docs/en/changelog: 断続的 403（06-08 失敗・06-09/06-10/06-11 成功）→ 回避策: 失敗時は WebSearch + releasebot.io
- superhub.com.hk / changepilot.cloud / levelupm365.com: 403、WebSearch でも本文取得不可の場合あり（初出 2026-06-06 / 最終確認 2026-06-11）→ 回避策: なし（存在確認のみ・手動確認推奨）
- qiita.com RSSフィード（4件）: 403（初出 2026-06-11 / 最終確認 2026-06-11）→ 回避策: WebSearch
- zenn.dev RSSフィード（3件）: 403（初出 2026-06-11 / 最終確認 2026-06-11）→ 回避策: WebSearch
- devblogs.microsoft.com/microsoft365dev/feed/: 403（初出 2026-06-11 / 最終確認 2026-06-11）→ 回避策: WebSearch

## アーカイブ（採用済み・見送り）

- B-001: Copilot Studio What's New の取得方法を Microsoft Learn MCP 優先に更新 — **採用済み（2026-06-10）**。`daily-sources.md` の取得方法欄と凡例に反映
- B-002: M365 Copilot Release Notes の取得手順を備考に明記 — **採用済み（2026-06-10）**。`daily-sources.md` 備考に反映（Learn MCP + grep 差分確認）
- B-003: M365 Copilot Release Notes の更新サイクルを備考に記載 — **採用済み（2026-06-10）**。`daily-sources.md` 備考に反映（隔週傾向）
- B-004: 取得不可が続く二次メディア記事の扱い方針を明文化 — **採用済み（2026-06-10）**。`fetch-flow.md`「アドホック二次メディアの扱い」として反映
