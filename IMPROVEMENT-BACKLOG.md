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

### B-001: Copilot Studio What's New の取得方法を Microsoft Learn MCP 優先に更新
- 状態: 提案中
- 初出: 2026-06-07 / 最終確認: 2026-06-08 / 回数: 2
- 対象: `.claude/rules/sites/daily-sources.md`「Copilot Studio - What's New」取得方法欄・取得方法の凡例
- 変更内容: 取得方法を「Microsoft Learn MCP → WebFetch → WebSearch」に変更し、凡例に Microsoft Learn MCP を追加
- 根拠: 06-07・06-08 と Learn MCP 経由で安定取得できた。WebFetch は 403 になる日がある

### B-002: M365 Copilot Release Notes の取得手順を備考に明記
- 状態: 提案中
- 初出: 2026-06-08 / 最終確認: 2026-06-08 / 回数: 1
- 対象: `.claude/rules/sites/daily-sources.md`「Microsoft 365 Copilot Release Notes」備考
- 変更内容: 「ページが18,000行超と巨大なため、Microsoft Learn MCP で取得し grep で差分確認する」を追加
- 根拠: 06-08 にこの手順で取得成功。手順が記録されていないと毎回試行錯誤になる

### B-003: M365 Copilot Release Notes の更新サイクルを備考に記載
- 状態: 提案中
- 初出: 2026-06-07 / 最終確認: 2026-06-09 / 回数: 2
- 対象: `.claude/rules/sites/daily-sources.md`「Microsoft 365 Copilot Release Notes」備考
- 変更内容: 「隔週更新の傾向（例: 6/2 の次は 6/16 前後見込み）」を追加
- 根拠: 更新サイクルを記録しておけば、未更新期間の確認を軽量化できる

### B-004: 取得不可が続く二次メディア記事の扱い方針を明文化
- 状態: 提案中
- 初出: 2026-06-06 / 最終確認: 2026-06-09 / 回数: 2
- 対象: `.claude/rules/sites/fetch-flow.md`（または daily-sources.md メンテナンスノート）
- 変更内容: アドホックに発見した二次メディア記事（superhub.com.hk / changepilot.cloud / levelupm365.com 等）が WebFetch 403 かつ WebSearch でも本文取得不可の場合、「存在確認のみ記載し本文は手動確認推奨とする」方針を明記
- 根拠: 06-06 に3サイト連続で本文取得不可、06-09 に changepilot.cloud で再発

## 既知の取得障害

- mc.merill.net: 403（初出 2026-06-06 ※それ以前から継続の可能性 / 最終確認 2026-06-10）→ 回避策: WebSearch
- techcommunity.microsoft.com（M365 Copilot Blog）: 403（初出 2026-06-06 / 最終確認 2026-06-10）→ 回避策: WebSearch（RSS は robots.txt ブロック。daily-sources.md 備考に記載済み）
- releasebot.io: 403（初出 2026-06-08 / 最終確認 2026-06-10）→ 回避策: WebSearch。Claude Code 分は code.claude.com を直接 WebFetch
- cursor.com/changelog: 403（初出 2026-06-07 / 最終確認 2026-06-09）→ 回避策: WebSearch
- code.claude.com/docs/en/changelog: 断続的 403（06-08 失敗・06-09/06-10 成功）→ 回避策: 失敗時は WebSearch + releasebot.io
- superhub.com.hk / changepilot.cloud / levelupm365.com: 403、WebSearch でも本文取得不可の場合あり（初出 2026-06-06 / 最終確認 2026-06-09）→ 回避策: なし（存在確認のみ・手動確認推奨）

## アーカイブ（採用済み・見送り）

（まだなし。kit が「提案中」から状態を変更してここへ移動する）
