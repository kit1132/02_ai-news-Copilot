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

- B-005: Qiita RSSフィード全4件（copilotstudio / powerplatform / powerautomate / powerapps）が403を返す — 対象: `daily-sources.md` Qiitaセクションの取得方法 / 変更内容: プライマリをWebSearch（`site:qiita.com タグ名 2026`）に変更 / 根拠: 2026-06-11に全フィードで403確認（初出 2026-06-11 / 最終確認 2026-07-20 / 回数 6）※2026-07-02 に RSS 復旧を確認するも 2026-07-05・07-06・07-20 に copilotstudio で連続403（intermittent）。一時的復旧はあるが 403 が繰り返し再発するため、WebSearch フォールバックを前提化する本提案の価値は残る（採否は kit 判断）
- B-006: Zenn RSSフィード全3件（copilotstudio / powerplatform / powerautomate）が403を返す — 対象: `daily-sources.md` Zennセクションの取得方法 / 変更内容: プライマリをWebSearch（`site:zenn.dev トピック名 2026`）に変更 / 根拠: 2026-06-11に全フィードで403確認（初出 2026-06-11 / 最終確認 2026-07-02 / 回数 2）※2026-07-02 に RSS 復旧を確認。同上
- B-007: devblogs.microsoft.com M365 Developer Blog RSSフィードが403 — 対象: `daily-sources.md` M365 Developer Blogセクションの取得方法 / 変更内容: プライマリをWebSearchに変更、RSS URLを代替に降格 / 根拠: 2026-06-11にRSS URL 2件とも403確認（初出 2026-06-11 / 最終確認 2026-07-02 / 回数 2）※2026-07-02 に RSS 復旧を確認。同上
- B-010: Power Platform Blog の WebFetch が 200 でも記事一覧が不完全 — 対象: `daily-sources.md` Power Platform Blog セクションの取得方法・備考 / 変更内容: 「WebFetch 成功時も最新記事の日付が古い場合は不完全レンダリングとみなし WebSearch で新着有無を照合する」旨を備考に追記 / 根拠: 2026-07-02 に WebFetch 200 だが一覧が 4/27 で止まり 6/11 月次記事が欠落（初出 2026-07-02 / 最終確認 2026-07-18 / 回数 3）
- B-011: Power Platform Blog の WebSearch 照合が月次「What's New feature update」記事に偏り、トピック個別記事を取りこぼす — 対象: `daily-sources.md` Power Platform Blog セクションの検索キーワード・備考 / 変更内容: WebSearch 照合クエリに月次更新以外のトピック記事（`site:microsoft.com/power-platform/blog Dataverse 2026`・`Power Apps`・`Power Automate`・`MCP` 等）を追加し、子カテゴリ記事も日次で拾う旨を明記 / 根拠: MCP カタログ 60+・Dataverse プラグインの Claude/Cursor/GitHub Copilot 展開を扱う 2026-07-06 の Dataverse トピック記事が、月次フィーチャー更新中心の照合により5日間（〜7/11）未回収だった（初出 2026-07-11 / 最終確認 2026-07-20 / 回数 5）

## 既知の取得障害

- mc.merill.net: 403（初出 2026-06-06 ※それ以前から継続の可能性 / 最終確認 2026-06-11）→ 回避策: WebSearch → 復旧（2026-07-02）→ 再発（2026-07-05、WebSearch フォールバック）
- techcommunity.microsoft.com（M365 Copilot Blog / Copilot Studio Blog）: 403（初出 2026-06-06 / 最終確認 2026-07-20）→ 回避策: WebSearch（board RSS も 2026-06-11 に 403 確認）→ 復旧（2026-07-02、board RSS 2本とも WebFetch 200。記事 HTML 本文は JS レンダリングのため引き続き RSS 本文で代替）→ 再発（2026-07-04、board RSS 2本とも 403。intermittent。WebSearch フォールバック。2026-07-20 も両board 403 継続）
- releasebot.io: 403（初出 2026-06-08 / 最終確認 2026-07-02）→ 回避策: WebSearch。Claude Code 分は github.com raw CHANGELOG を直接 WebFetch
- cursor.com/changelog: 403（初出 2026-06-07 / 最終確認 2026-07-19）→ 回避策: WebSearch
- code.claude.com/docs/en/changelog: 断続的 403（06-08 失敗・06-09/06-10/06-11 成功）→ 回避策: 失敗時は WebSearch + releasebot.io
- superhub.com.hk / changepilot.cloud / levelupm365.com: 403、WebSearch でも本文取得不可の場合あり（初出 2026-06-06 / 最終確認 2026-06-11）→ 回避策: なし（存在確認のみ・手動確認推奨）
- qiita.com RSSフィード（4件）: 403（初出 2026-06-11 / 最終確認 2026-07-20）→ 回避策: WebSearch → 復旧（2026-07-02、4フィードすべて 200）→ 再発（2026-07-05、copilotstudio/powerplatform で 403。intermittent。WebSearch フォールバック。2026-07-06・07-20 も copilotstudio で 403 継続）
- zenn.dev RSSフィード（3件）: 403（初出 2026-06-11 / 最終確認 2026-06-11）→ 回避策: WebSearch → 復旧（2026-07-02）
- devblogs.microsoft.com/microsoft365dev/feed/: 403（初出 2026-06-11 / 最終確認 2026-07-04）→ 回避策: WebSearch → 復旧（2026-07-02）→ 再発（2026-07-04、intermittent。WebSearch フォールバック）
- www.microsoft.com/en-us/power-platform/blog/: WebFetch が 200 を返すが記事一覧が不完全（4/27 までしか表示されず、既知の 6/11 月次記事も欠落。403 ではないため従来のフォールバック条件に非該当）（初出 2026-07-02 / 最終確認 2026-07-02）→ 回避策: WebSearch 併用で新着有無を照合

## アーカイブ（採用済み・見送り）

- B-001: Copilot Studio What's New の取得方法を Microsoft Learn MCP 優先に更新 — **採用済み（2026-06-10）**。`daily-sources.md` の取得方法欄と凡例に反映
- B-002: M365 Copilot Release Notes の取得手順を備考に明記 — **採用済み（2026-06-10）**。`daily-sources.md` 備考に反映（Learn MCP + grep 差分確認）
- B-003: M365 Copilot Release Notes の更新サイクルを備考に記載 — **採用済み（2026-06-10）**。`daily-sources.md` 備考に反映（隔週傾向）
- B-004: 取得不可が続く二次メディア記事の扱い方針を明文化 — **採用済み（2026-06-10）**。`fetch-flow.md`「アドホック二次メディアの扱い」として反映
- B-008: 「毎日確認」ソースのカバレッジ自己チェックを push 前に必須化 — **採用済み（2026-07-02、kit 指示によりローカルセッションで反映）**。`CLAUDE.md` に「⚠️ カバレッジ自己チェック」セクションを追加。背景: 2026-06-12 のリモートルーチン移行後、M365 Roadmap / Microsoft Copilot Blog / Power Platform 系ブログ / X トレンドの最終確認が 6/12-13 のまま約3週間凍結していた
- B-009: 一次情報源の「確認済み」基準を明文化（二次メディア要約を確認扱いにしない） — **採用済み（2026-07-02、kit 指示によりローカルセッションで反映）**。`fetch-flow.md` に「一次情報源の『確認済み』基準」を追加、`daily-sources.md` Release Notes 備考に反映。背景: Release Notes 6/16 バッチ（Copilot Chat への Claude 追加・PowerPoint FLUX.2 対応等）が二次要約経由となり 6/30 まで未掲載、Word のデフォルト直接編集（6/2 バッチ）は掲載漏れ
