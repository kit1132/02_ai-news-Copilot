# デイリーチェック対象サイト

## 取得方法の凡例

- **WebFetch**: HTMLページを直接取得する
- **RSS**: RSS/Atom フィードを取得し、XMLから新着エントリを抽出する
- **WebSearch**: 検索エンジン経由で情報を取得する
- **Microsoft Learn MCP**: Microsoft Learn MCP サーバー経由でドキュメントを取得する（`learn.microsoft.com` 配下で WebFetch が403の場合も安定して取得できる）

各ソースの「取得方法」は優先順序を示す。フォールバック条件（403/429時の挙動、リトライ手順など）の詳細は `fetch-flow.md` を参照。

RSS URLの記載がないソースはRSS未提供。Cloudflare等のbot対策によりWebFetchが常時403を返すソースは、WebSearchが実質的なプライマリ手段となる。

`learn.microsoft.com` 配下のソースはCloudflare未使用のためWebFetchが安定する傾向がある。

## 優先度の分類基準

- **最優先**: M365 Copilot / Copilot Studio / Power Platform の公式一次情報源。毎日確認必須
- **高優先**: 個別製品ブログ・計画系ドキュメント・コミュニティ情報・トレンド。毎日〜週2回確認
- **週次確認**: 速報性より実装パターンの収集が目的のソース。週1回確認

---

## 最優先

### Copilot Studio - What's New
- URL: https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new
- 取得方法: Microsoft Learn MCP → WebFetch → WebSearch
- 注目点: 新機能リリース（Preview/GA）、モデル変更（GPT-4o→GPT-5等）、破壊的変更、VS Code拡張、エージェント評価機能
- 頻度: 毎日確認
- 備考: 2026-06-07・06-08 に Learn MCP 経由で安定取得を確認（B-001採用、2026-06-10）。WebFetch は403になる日がある

### Microsoft 365 Copilot Release Notes
- URL: https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: M365 Copilot全体のリリースノート（Word/Excel/PowerPoint/Outlook/Teams各アプリ別）。Agent Mode、ライセンス変更、新エージェント追加
- 頻度: 毎日確認
- 備考: ページが18,000行超と巨大なため、Microsoft Learn MCP で取得し grep で差分確認する（B-002採用）。隔週更新の傾向あり（例: 6/2 の次は 6/16 前後見込み。B-003採用、2026-06-10）

### Microsoft 365 Roadmap
- URL: https://www.microsoft.com/en-us/microsoft-365/roadmap
- 検索キーワード（WebSearch用）: `Microsoft 365 roadmap Copilot Studio agent 2026`
- 取得方法: WebSearch
- 注目点: リリース予定機能、GA時期、プレビュー開始。Release Notesが「過去の変更」なのに対し、こちらは「未来の予定」を追う情報源
- 頻度: 毎日確認
- 備考: SPA/動的ページのためWebFetchでは中身が取れない。WebSearchをプライマリとする

### Microsoft Copilot Blog
- URL: https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/
- RSS URL（優先）: https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/feed/
- 検索キーワード（WebSearch用）: `Microsoft Copilot Studio blog update 2026`
- 取得方法: RSS → WebFetch → WebSearch
- 注目点: Copilot Studioの月次「What's New」ブログ、マルチエージェント、MCP対応、新モデル追加、ガバナンス機能
- 頻度: 毎日確認
- 備考: Copilot Studio カテゴリの記事を対象とする。learn.microsoft.com の What's New とは別軸で、背景説明・戦略的文脈が含まれる。RSS URL は2026-06-10に疎通確認済み（microsoft.com は UA により 403 のことがあるため、失敗時は WebSearch へ）

### Power Platform Blog
- URL: https://www.microsoft.com/en-us/power-platform/blog/
- 代替URL（子カテゴリ）:
  - Power Apps: https://www.microsoft.com/en-us/power-platform/blog/power-apps/
  - Power Automate: https://www.microsoft.com/en-us/power-platform/blog/power-automate/
- 検索キーワード（WebSearch用）: `Power Platform blog update 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: 月次「What's New in Power Platform」Feature Update記事が最重要。Power Apps/Power Automate/Copilot Studio横断の更新情報、ガバナンス・ライセンス変更、コミュニティ情報
- 頻度: 毎日確認
- 備考: 親ページで全体を確認後、子カテゴリの個別記事も高優先セクションで別途監視する

### M365 Message Center Archive
- URL: https://mc.merill.net/
- 検索キーワード（WebSearch用）: `Microsoft 365 Message Center Copilot Power Platform 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: テナント管理者向け変更通知のアーカイブ。Roadmapが「予定」、Release Notesが「リリース済」に対し、こちらは「展開中の変更と影響範囲」を扱う
- 頻度: 毎日確認
- 備考: 非公式の個人運営アーカイブ（Merill Fernando氏）。公式Message Center（admin.microsoft.com）とは差分が生じる可能性あり。テナント管理者権限不要で閲覧できる点が利点

### Copilot Studio Blog（Tech Community・公式）
- URL: https://techcommunity.microsoft.com/category/microsoft365copilot/blog/copilot-studio-blog
- RSS URL（取得はこちら必須）: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=copilot-studio-blog
- 検索キーワード（WebSearch用）: `site:techcommunity.microsoft.com Copilot Studio blog 2026`
- 取得方法: RSS → WebSearch
- 注目点: Copilot Studio 製品チーム発の更新・技術・運用記事。マルチエージェント、Computer-using agents、ガバナンス白書（Administering and Governing Agents）等
- 頻度: 毎日確認
- 備考: 2026年春開設の専用公式ブログ（2026-06-10 追加）。**HTMLページは SSO リダイレクト/JSレンダリングのため取得不可。必ず RSS URL 経由で取得すること**

---

## 高優先

### Power Automate Blog
- URL: https://www.microsoft.com/en-us/power-platform/blog/power-automate/
- 検索キーワード（WebSearch用）: `Power Automate blog update new feature 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: Power Automate固有の新機能（クラウドフロー、デスクトップフロー、Process Mining、Computer Use Agent）。月次更新記事あり
- 頻度: 毎日確認
- 備考: Power Platform Blogの子カテゴリ。JCB案件のPower Automate研修に直結する情報源

### Power Apps Blog
- URL: https://www.microsoft.com/en-us/power-platform/blog/power-apps/
- 検索キーワード（WebSearch用）: `Power Apps blog update new feature 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: Power Apps固有の新機能（モダンコントロール、コードアプリGA、vibe.powerapps.com（AIコードアプリビルダー、Public Preview）、MCP Server連携）。月次更新記事あり
- 頻度: 毎日確認
- 備考: Power Platform Blogの子カテゴリ。JCB案件のPower Apps研修に直結する情報源

### Copilot Studio Release Wave（計画機能一覧）
- URL: https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/microsoft-copilot-studio/planned-features
- 検索キーワード（WebSearch用）: `Copilot Studio release wave planned features 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: 半期ごとの計画機能リスト。Preview/GA予定時期が一覧化されている
- 頻度: 週1〜2回確認（更新頻度が低いため）
- 備考: Wave切替時（4月・10月頃）にURLパスが変わる（`2026wave1` → `2026wave2` 等）。WebFetchが404を返した場合はWebSearchで最新Waveページを特定すること

### Power Platform Release Wave（全体版）
- URL: https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/
- 検索キーワード（WebSearch用）: `Power Platform release wave 2026 planned features`
- 取得方法: WebFetch → WebSearch
- 注目点: Copilot Studio以外を含むPower Platform全体の計画機能一覧。Power Apps/Power Automate/Dataverse/Power Pages/ガバナンス・管理のRelease Wave
- 頻度: 週1〜2回確認（更新頻度が低いため）
- 備考: Copilot Studio Release Waveと同じタイミングでWave切替が発生する。WebFetchが404を返した場合はWebSearchで最新Waveページを特定すること

### Power Platform Released Versions
- URL: https://learn.microsoft.com/en-us/power-platform/released-versions/
- 取得方法: WebFetch
- 注目点: Copilot StudioはPower Platform基盤のため、基盤側のバージョン変更が影響する。Power Apps/Power Automate/Copilot Studioの各リージョン展開状況
- 頻度: 毎日確認

### Microsoft 365 Developer Blog
- URL: https://devblogs.microsoft.com/microsoft365dev/
- RSS URL（優先）: https://devblogs.microsoft.com/microsoft365dev/feed/
- RSS URL（Copilot 絞り込み）: https://devblogs.microsoft.com/microsoft365dev/category/microsoft-365-copilot/feed/
- 検索キーワード（WebSearch用）: `Microsoft 365 Developer Blog Copilot agents 2026`
- 取得方法: RSS → WebFetch → WebSearch
- 注目点: declarative agents、Agents SDK、Copilot API、Teams AI、Graph 等の拡張開発一次情報
- 頻度: 毎日確認
- 備考: 2026-06-10 追加。WordPress 系で WebFetch との相性良好

### Tech Community - Microsoft 365 Copilot Blog
- URL: https://techcommunity.microsoft.com/blog/microsoft365copilotblog
- RSS URL（取得はこちら必須）: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=Microsoft365CopilotBlog
- 検索キーワード（WebSearch用）: `site:techcommunity.microsoft.com "Microsoft 365 Copilot" 2026`
- 取得方法: RSS → WebSearch
- 注目点: 月次「What's New in Microsoft 365 Copilot」記事が最重要。公式Release Notesより詳細な背景説明・活用事例・管理者向けガイダンスが含まれる
- 頻度: 毎日確認
- 備考: HTMLページは SSO リダイレクトのため取得不可。board RSS は WebFetch で取得可能と確認済み（2026-06-10。旧備考「robots.txt でブロック」は board RSS には当てはまらない）

### Microsoft 365 Blog（本体）
- URL: https://www.microsoft.com/en-us/microsoft-365/blog/
- RSS URL（優先）: https://www.microsoft.com/en-us/microsoft-365/blog/feed/
- 検索キーワード（WebSearch用）: `Microsoft 365 blog announcement Copilot 2026`
- 取得方法: RSS → WebSearch
- 注目点: M365 全体の大型発表・ライセンス/料金変更の初出（Microsoft Scout、Work IQ、M365 Copilot 新デザイン等）
- 頻度: 毎日確認
- 備考: 2026-06-10 追加。microsoft.com は UA により 403 を返すことがある。失敗時は WebSearch へ。日次の細かい更新は Release Notes / Roadmap と重複するため大型発表のみ拾う

### Qiita タグフィード（日本語実務情報）
- RSS URL（すべて巡回）:
  - https://qiita.com/tags/copilotstudio/feed
  - https://qiita.com/tags/powerplatform/feed
  - https://qiita.com/tags/powerautomate/feed
  - https://qiita.com/tags/powerapps/feed
- 取得方法: RSS
- 注目点: 日本の実務者による検証記事・ハマりどころ・活用事例。研修コンテンツのネタ元
- 頻度: 毎日確認
- 備考: 2026-06-10 追加。フィードには直近4件程度しか含まれないため毎日巡回が前提。ダイジェストには有用な記事のみ厳選して掲載する（全件転載しない）

### Zenn トピックフィード（日本語開発者情報）
- RSS URL（すべて巡回）:
  - https://zenn.dev/topics/copilotstudio/feed
  - https://zenn.dev/topics/powerplatform/feed
  - https://zenn.dev/topics/powerautomate/feed
- 取得方法: RSS
- 注目点: Qiita よりやや開発者寄りの日本語記事
- 頻度: 毎日確認
- 備考: 2026-06-10 追加。ダイジェストには有用な記事のみ厳選して掲載する

### X (トレンド検索)
- 取得方法: WebSearch
- 検索キーワード例:
  - `"Microsoft Copilot update"`
  - `"Copilot Studio new feature"`
  - `"M365 Copilot release"`
  - `"Copilot Studio agent"`
  - `"Power Platform update"`
  - `"Power Automate new feature"`
  - `"Power Apps new feature"`
  - `"Microsoft Copilot 新機能"`
  - `"Copilot Studio 活用"`
  - `"Power Platform 活用"`
  - `"Power Automate 新機能"`
  - `"Power Apps 新機能"`
- 注目点: 新機能のバズ、導入企業の知見共有、不具合報告、日本語コミュニティの反応
- 頻度: 毎日確認

---

## 週次確認

### Microsoft 365 & Power Platform Community
- URL: https://pnp.github.io/
- 検索キーワード（WebSearch用）: `Microsoft 365 Power Platform community call 2026`
- 取得方法: WebSearch
- 注目点: コミュニティコール（デモ・実装例）、PnPサンプル、実務ユースケース
- 頻度: 週1回確認
- 備考: 速報性よりも実装パターンの収集が目的。コミュニティコールは隔週開催

### M365 Copilot 開発者向け What's New
- URL: https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/whats-new
- 取得方法: WebFetch → WebSearch
- 注目点: declarative agent manifest 新版、Agent Builder 新機能、Agent Registration API、Copilot policy settings API 等が月次セクションで蓄積
- 頻度: 週1回確認（月次更新のため）
- 備考: 2026-06-10 追加。learn.microsoft.com のため WebFetch 安定（Microsoft Learn MCP でも取得可）

### Copilot Studio Kit（Power CAT）リリース
- URL: https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/releases
- RSS URL（優先）: https://github.com/microsoft/Power-CAT-Copilot-Studio-Kit/releases.atom
- 取得方法: RSS → WebFetch
- 注目点: Copilot Studio のテスト自動化・ガバナンス支援キットの月次リリース（名称は「Copilot Agent Kit」へ移行中）
- 頻度: 週1回確認（ほぼ月次リリースのため）
- 備考: 2026-06-10 追加

### Power Platform Weekly
- URL: https://www.ppweekly.com/
- RSS URL（優先）: https://www.ppweekly.com/feed
- 取得方法: RSS → WebFetch
- 注目点: コミュニティキュレーションの週刊リンク集。公式＋コミュニティ記事の見落とし拾い（セーフティネット枠）
- 頻度: 週1回確認（毎週月曜発行のため月曜〜火曜に確認）
- 備考: 2026-06-10 追加。リンク集のため、重要記事は元ソースを WebFetch / WebSearch で確認してから掲載する

### Power Platform 重要な変更（非推奨のお知らせ）
- URL: https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- 取得方法: WebFetch → WebSearch
- 注目点: Power Apps / Power Automate / Dataverse / コネクタの非推奨・廃止予定の公式一覧。破壊的変更の検知
- 頻度: 週1回確認
- 備考: 2026-06-10 追加。変更があった項目はダイジェストで「破壊的変更」として目立たせる。研修資料の陳腐化チェックにも使う

---

## メンテナンスノート

- 本ファイルのソース追加・削除時は `fetch-flow.md` 側のフォールバック定義も合わせて更新すること
- AI系ツール（Anthropic / Claude / Cursor / Devin）のソースは `ai-tools-sources.md` に分離済み（未作成の場合は別途作成すること）
