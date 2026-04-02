# デイリーチェック対象サイト

## 取得方法の凡例

- **WebFetch**: HTMLページを直接取得する
- **RSS**: RSS/Atom フィードを取得し、XMLから新着エントリを抽出する
- **WebSearch**: 検索エンジン経由で情報を取得する

各ソースの「取得方法」は優先順序を示す。フォールバック条件（403/429時の挙動、リトライ手順など）の詳細は `fetch-flow.md` を参照。

RSS URLの記載がないソースはRSS未提供。Cloudflare等のbot対策によりWebFetchが常時403を返すソースは、WebSearchが実質的なプライマリ手段となる。

`learn.microsoft.com` 配下のソースはCloudflare未使用のためWebFetchが安定する傾向がある。

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

## 高優先

### Copilot Studio Release Wave（計画機能一覧）
- URL: https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/microsoft-copilot-studio/planned-features
- 検索キーワード（WebSearch用）: `Copilot Studio release wave planned features 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: 半期ごとの計画機能リスト。Preview/GA予定時期が一覧化されている
- 頻度: 週1〜2回確認（更新頻度が低いため）
- 備考: Wave切替時（4月・10月頃）にURLパスが変わる（`2026wave1` → `2026wave2` 等）。WebFetchが404を返した場合はWebSearchで最新Waveページを特定すること

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

### Anthropic News
- URL: https://www.anthropic.com/news
- 代替URL: https://www.anthropic.com/research
- 検索キーワード（WebSearch用）: `Anthropic Claude release announcement 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: Claude新モデルリリース、API変更、新機能発表、料金変更
- 頻度: 毎日確認

### Claude Support / Release Notes
- URL: https://support.claude.com
- 検索キーワード（WebSearch用）: `Claude AI update changelog new feature 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: Claude製品のリリースノート、既知の問題、機能変更
- 頻度: 毎日確認

### Cursor Changelog
- URL: https://cursor.com/changelog
- 検索キーワード（WebSearch用）: `Cursor AI editor changelog update 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: AI統合開発環境の新機能、モデル対応状況、エディタ機能改善
- 頻度: 毎日確認
- 備考: 2026-04-02時点でWebFetch成功（403解消）。再発時は `cursor-changelog.com/feed`（サードパーティRSS）への切り替えを検討

### Devin Documentation
- URL: https://docs.devin.ai
- 検索キーワード（WebSearch用）: `Devin AI agent update new feature 2026`
- 取得方法: WebFetch → WebSearch
- 注目点: AIソフトウェアエンジニアエージェントの機能追加、API変更、利用ガイド更新
- 頻度: 毎日確認

### X (トレンド検索)
- 取得方法: WebSearch
- 検索キーワード例:
  - `"Microsoft Copilot update"`
  - `"Copilot Studio new feature"`
  - `"M365 Copilot release"`
  - `"Copilot Studio agent"`
  - `"Microsoft Copilot 新機能"`
  - `"Copilot Studio 活用"`
- 注目点: 新機能のバズ、導入企業の知見共有、不具合報告
- 頻度: 毎日確認
