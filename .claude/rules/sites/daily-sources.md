# デイリーチェック対象サイト

## 取得方法の凡例

- **WebFetch**: HTMLページを直接取得する
- **RSS**: RSS/Atom フィードを取得し、XMLから新着エントリを抽出する
- **WebSearch**: 検索エンジン経由で情報を取得する

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
- 取得方法: WebFetch
- 注目点: 新機能リリース（Preview/GA）、モデル変更（GPT-4o→GPT-5等）、破壊的変更、VS Code拡張、エージェント評価機能
- 頻度: 毎日確認

### Microsoft 365 Copilot Release Notes
- URL: https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- 取得方法: WebFetch
- 注目点: M365 Copilot全体のリリースノート（Word/Excel/PowerPoint/Outlook/Teams各アプリ別）。Agent Mode、ライセンス変更、新エージェント追加
- 頻度: 毎日確認

### Microsoft 365 Roadmap
- URL: https://www.microsoft.com/en-us/microsoft-365/roadmap
- 検索キーワード（WebSearch用）: `Microsoft 365 roadmap Copilot Studio agent 2026`
- 取得方法: WebSearch
- 注目点: リリース予定機能、GA時期、プレビュー開始。Release Notesが「過去の変更」なのに対し、こちらは「未来の予定」を追う情報源
- 頻度: 毎日確認
- 備考: SPA/動的ページのためWebFetchでは中身が取れない。WebSearchをプライマリとする

### Microsoft Copilot Blog
- URL: https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/
- 検索キーワード（WebSearch用）: `Microsoft Copilot Studio blog update 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: Copilot Studioの月次「What's New」ブログ、マルチエージェント、MCP対応、新モデル追加、ガバナンス機能
- 頻度: 毎日確認
- 備考: Copilot Studio カテゴリの記事を対象とする。learn.microsoft.com の What's New とは別軸で、背景説明・戦略的文脈が含まれる

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

### Tech Community - Microsoft 365 Copilot Blog
- URL: https://techcommunity.microsoft.com/blog/microsoft365copilotblog
- 検索キーワード（WebSearch用）: `site:techcommunity.microsoft.com "Microsoft 365 Copilot" 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: 月次「What's New in Microsoft 365 Copilot」記事が最重要。公式Release Notesより詳細な背景説明・活用事例・管理者向けガイダンスが含まれる
- 頻度: 毎日確認
- 備考: RSSフィードは存在するが robots.txt でブロックされておりWebFetch/curl不可

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

---

## メンテナンスノート

- 本ファイルのソース追加・削除時は `fetch-flow.md` 側のフォールバック定義も合わせて更新すること
- AI系ツール（Anthropic / Claude / Cursor / Devin）のソースは `ai-tools-sources.md` に分離済み（未作成の場合は別途作成すること）
