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
- URL: https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes （旧 `copilot/microsoft-365/release-notes` は 301 で転送される。Learn MCP 経由では 301 が見えず転送先の本文が返る）（B-049採用、2026-10-19）
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: M365 Copilot全体のリリースノート（Word/Excel/PowerPoint/Outlook/Teams各アプリ別）。Agent Mode、ライセンス変更、新エージェント追加
- 頻度: 毎日確認
- 備考: ページが18,000行超と巨大なため、Microsoft Learn MCP で取得し grep で差分確認する（B-002採用）。隔週更新の傾向あり（例: 6/2 の次は 6/16 前後見込み。B-003採用、2026-06-10）。**Learn MCP が使えない場合も WebSearch の二次メディア要約で代替せず、WebFetch で本ページを直接取得し分割読みすること（一次確認基準は `fetch-flow.md` 参照。B-009採用、2026-07-02）**
  ⚠️ **最新バッチの有無を `microsoft_docs_search` の返す日付見出しの並びで判定しない。`microsoft_docs_fetch` でページ本文を取得し、先頭の `## ` 見出し（＝最新バッチ日）を直接読んで判定すること。** docs_search は「新着の存在に気づく」用途に限定する。2026-07-30・07-31 は docs_search が July 15 → July 01 → June 16 の順で返したため「7月の追加バッチはゼロ」と誤判定したが、08-01 に docs_fetch で本文先頭を読むと「July 29, 2026」（対象期間 7/15〜7/29・全10項目）だった。取りこぼした10項目には Agent Builder の SharePoint リスト知識ソース対応（Roadmap 561920）が含まれる（B-019採用、2026-08-02）

### Microsoft 365 Roadmap
- URL: https://www.microsoft.com/en-us/microsoft-365/roadmap
- RSS URL（優先）: https://www.microsoft.com/releasecommunications/api/v2/m365/rss
- API URL: https://www.microsoft.com/releasecommunications/api/v1/m365 （機能 ID 単位の JSON。status・GA 予定月・製品タグを読む）
- 検索キーワード（WebSearch用）: `Microsoft 365 roadmap Copilot Studio agent 2026`
- 取得方法: RSS → API → WebSearch
- 注目点: リリース予定機能、GA時期、プレビュー開始。Release Notesが「過去の変更」なのに対し、こちらは「未来の予定」を追う情報源。**GA の判定は Roadmap 項目の status の変化（`In development` → `Rolling out` → `Launched`、または `Cancelled`）と製品ブログの GA 宣言で行う。What's New の Preview 表記や Release Wave の緑チェックは根拠にしない**
- 新規判定: RSS の `pubDate` をバッチ（同じ時刻帯の一括起票）単位で見て、前回確認以降のバッチを新規とする。総項目数の増減では判定しない（新規バッチの件数と総項目数の増分が一致しない実例がある）
- 頻度: 毎日確認
- 備考: Power Platform / Dynamics 365 のリリース計画（Release Wave）は 2026年10月に Microsoft Learn でアーカイブされ、計画情報はこの Roadmap（AI at Work roadmap。`aka.ms/AIatWorkRoadmap` も同じページへ転送）に統合された。Release Planner は 2026-11-15 までに退役する。旧 `release-plan/` 配下の 301・404 は障害として記録しない。Roadmap の Web ページは SPA で WebFetch では中身が取れないため、RSS・API を使う（B-046・B-047 採用、2026-10-19）

### Microsoft Copilot Blog
- URL: https://www.microsoft.com/en-us/copilot/blog/copilot-studio/
- RSS URL（優先）: https://www.microsoft.com/en-us/copilot/blog/copilot-studio/feed/ （取得時は末尾に `?x=<当日MMDD>` を付ける）
- 検索キーワード（WebSearch用）: `Microsoft Copilot Studio blog update 2026`
- 取得方法: RSS → WebFetch → WebSearch
- 注目点: Copilot Studioの月次「What's New」ブログ、マルチエージェント、MCP対応、新モデル追加、ガバナンス機能
- 頻度: 毎日確認
- 備考: Copilot Studio カテゴリの記事を対象とする。learn.microsoft.com の What's New とは別軸で、背景説明・戦略的文脈が含まれる。RSS URL は2026-06-10に疎通確認済み（microsoft.com は UA により 403 のことがあるため、失敗時は WebSearch へ）。旧 URL（`microsoft-copilot/blog/copilot-studio/` 配下）は 301 で上記へ転送される（RSS で 2026-09-17 に確認）（B-070採用、2026-10-19）。クエリ無しの RSS は CDN のキャッシュ版を返し、当日の新着を落とすことがある（B-077採用、2026-10-19）

### Power Platform Blog
- URL: https://www.microsoft.com/en-us/power-platform/blog/
- RSS URL（優先）: https://www.microsoft.com/en-us/power-platform/blog/feed/ （取得時は末尾に `?x=<当日MMDD>` を付ける）（B-077採用、2026-10-19）
- 代替URL（子カテゴリ）:
  - Power Apps: https://www.microsoft.com/en-us/power-platform/blog/power-apps/
  - Power Automate: https://www.microsoft.com/en-us/power-platform/blog/power-automate/
- 検索キーワード（WebSearch用）: `Power Platform blog update 2026`
- 取得方法: RSS → WebFetch → WebSearch
- 注目点: 月次「What's New in Power Platform」Feature Update記事が最重要。Power Apps/Power Automate/Copilot Studio横断の更新情報、ガバナンス・ライセンス変更、コミュニティ情報
- 頻度: 毎日確認
- 備考: 親ページで全体を確認後、子カテゴリの個別記事も高優先セクションで別途監視する。**HTML 一覧ページは WebFetch が 200 でも記事が欠けることがある**（2026-07〜09 に月次記事を含む新着を最長11日取りこぼした）。新着の判定は親 RSS で行い、HTML 一覧を使うときは最新記事の日付ではなく、既知の公開済み記事が一覧に含まれているかで判断する（B-010採用、2026-10-19）

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

### Copilot Studio ライセンス・課金
- URL:
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-overview
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-understand-display
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-manage-buy-credits
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/enforcement-policy-credits
  - https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management （標準ハーネスの消費レート表）
  - https://learn.microsoft.com/en-us/power-platform/admin/manage-copilot-studio-copilot-credits-capacity （PPAC の容量管理）
  - https://learn.microsoft.com/en-us/power-platform/admin/manage-usage-github-copilot-harness （GitHub Copilot ハーネスの課金統制）
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: ハーネス別の課金方式と課金開始点、Copilot Credits の消費レート、容量割当とオーバレージ、枯渇時のエンフォースメント、購入経路、従量課金の発効日
- 頻度: 毎日確認（`updated_at` / `git_commit_id` の突合。値が動いた日だけ本文を読む）
- 備考: 課金3本（`billing-credit-overview` / `billing-manage-buy-credits` / `enforcement-policy-credits`）は `agents-experience/` 配下へ移り、ルート直下の旧パスは 301 ではなく 404 を返す。**Learn にあるのはクレジットの消費レートまでで、1クレジットあたりの USD 単価は月次 PDF（`aka.ms/CopilotCredits/LicensingGuide`・取得不可）にしか無い。取れない間はダイジェストに単価を載せない。** 状態ファイルでは「Copilot Studio ハーネス・課金」「Copilot Studio 課金レート表」「Copilot Credits の容量管理（PPAC）」の3節に記録する（B-022採用、2026-10-19）

### Copilot Studio ガイダンスハブ What's New
- URL: https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/whats-new
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: 運用ガイダンスの新規記事・改訂、参照アーキテクチャ・事例の追加、Copilot Agent Kit の機能追加
- 頻度: 毎日確認（`updated_at` / `git_commit_id` の突合）
- 備考: モデルのライフサイクル管理・ハーネス比較・クレジット統制など、他の登録ソースに出ない記事がここにだけ載る。新規記事の判定は索引の `updated_at` ではなく、`guidance/toc.json` のリンク集合の前日差分で行う（B-034採用、2026-10-19）

### Copilot Cowork（What's New・モデル・管理者統制）
- URL（What's New）: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/whats-new
- URL（モデル）: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-models
- URL（管理者統制）: https://learn.microsoft.com/en-us/microsoft-365/copilot/cowork/cowork-admin-governance
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: 月次の新機能節、モデルピッカーと effort レベル、管理者統制と使用量ベース課金
- 頻度: 毎日確認（What's New）／週1回確認（`cowork-models`・`cowork-admin-governance` の精読）
- 備考: **モデルの追加・退役は What's New に載らず `cowork-models` にしか現れない。** 状態ファイルでは「Copilot Cowork What's New」「Copilot Cowork（モデル・ブラウザー統制）」の2節に記録する（B-048採用、2026-10-19）

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
- RSS URL（取得はこちら必須）: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=microsoft-copilot-blog （旧 `board.id=Microsoft365CopilotBlog` は 200・`<item>` 0件を返す）（B-063採用、2026-10-19）
- 検索キーワード（WebSearch用）: `site:techcommunity.microsoft.com "Microsoft 365 Copilot" 2026`
- 取得方法: RSS → WebSearch
- 注目点: 月次「What's New in Microsoft 365 Copilot」記事が最重要。公式Release Notesより詳細な背景説明・活用事例・管理者向けガイダンスが含まれる
- 頻度: 毎日確認
- 備考: HTMLページは SSO リダイレクトのため取得不可。board RSS は WebFetch で取得可能と確認済み（2026-06-10。旧備考「robots.txt でブロック」は board RSS には当てはまらない）

### Microsoft 365 Blog（本体）
- URL: https://www.microsoft.com/en-us/copilot/blog/
- RSS URL（優先）: https://www.microsoft.com/en-us/copilot/blog/feed/ （取得時は末尾に `?x=<当日MMDD>` を付ける）
- 検索キーワード（WebSearch用）: `Microsoft 365 blog announcement Copilot 2026`
- 取得方法: RSS → **WebSearch 照合（毎日併用）** → WebSearch
- 注目点: M365 全体の大型発表・ライセンス/料金変更の初出（Microsoft Scout、Work IQ、M365 Copilot 新デザイン等）
- 頻度: 毎日確認
- 備考: 2026-06-10 追加。microsoft.com は UA により 403 を返すことがある。失敗時は WebSearch へ。日次の細かい更新は Release Notes / Roadmap と重複するため大型発表のみ拾う。
  ⚠️ **RSS の WebFetch が 200 でも先頭エントリが最新とは限らない。** `site:microsoft.com/en-us/microsoft-365/blog 2026` 等での WebSearch 照合を毎日併用し、`.last-check-state.md` の最新記事日付と突合すること。2026-08-01 は同一 RSS URL を WebFetch して「6/25 の Copilot in Excel 記事が最新」と判定したが、08-02 の取得では 7/30 の "The next measure of AI momentum is work transformed"（有償3,000万シート・展開ベンチマーク等の一次数値を含む）が先頭にあり、過去の全 digest に未掲載だった。**Release Notes の B-019 と同じ「単一の取得経路が最新項目を落とす」類型**（B-020採用、2026-08-02）
  ⚠️ **旧 URL（`microsoft-365/blog/` 配下）は 301 で `copilot/blog/` 配下へ転送される（RSS で 2026-09-17 に確認）。転送先は Copilot ブログ全体のフィードで、M365 ブログ専用ではない。** Microsoft Copilot Blog（Copilot Studio カテゴリ）と守備範囲が重なる（B-070採用、2026-10-19）。クエリ無しの RSS は CDN のキャッシュ版を返し、当日の新着を落とすことがある（B-077採用、2026-10-19）

### Microsoft Partner Center 月次アナウンス
- URL（索引）: https://learn.microsoft.com/en-us/partner-center/announcements/
- URL（当月）: `https://learn.microsoft.com/en-us/partner-center/announcements/<YYYY>-<month>`（例: https://learn.microsoft.com/en-us/partner-center/announcements/2026-october ）
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: M365 Copilot / Agent 365 のライセンス前提条件、CSP での提供開始、スペシャライゼーション要件、価格改定、プロモーションの期限
- 頻度: 毎日確認（`updated_at` の突合。月内にも項目の追記が続くため）
- 備考: 登録ソースのどれにも出ない、期限つきのライセンス一次が載る。URL は `<年>-<月>` 形式で、旧 `<月>-<年>` 形式は 404 を返す。当月ページは索引から当月のリンクを取って開く（月初の数日は 404 のことがある）。状態ファイルでは「M365 Licensing / Packaging」節に記録する（B-013採用、B-067 を統合、2026-10-19）

### Agent 365 Blog（Tech Community・公式）
- RSS URL（取得はこちら必須）: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=agent-365-blog
- 検索キーワード（WebSearch用）: `site:techcommunity.microsoft.com "Agent 365" 2026`
- 取得方法: RSS → WebSearch
- 注目点: 月次「What's new in Agent 365」記事、Agent Registry と Registry sync、マルチテナント管理、Copilot Credits のコスト管理
- 頻度: 毎日確認
- 備考: `ai-tools.md` が対象とする Microsoft Agent 365 の製品ブログ。HTML ページは取得できないため RSS を使う。旧 `board.id=Agent365Blog` は 200・`<item>` 0件を返す（B-032採用、2026-10-19）

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
- 取得方法: WebFetch → WebSearch。毎日 `curl` で `<meta name="updated_at">` と `git_commit_id` を読み、前日と同じなら本文の再取得を省く。値が動いた日だけ本文を取得して `## ` 見出しの数を突き合わせ、増えた節を先頭から読む（B-058採用、2026-10-19）
- 注目点: Power Apps / Power Automate / Dataverse / コネクタの非推奨・廃止予定の公式一覧。破壊的変更の検知
- 頻度: 毎日確認（`updated_at` の突合のみ）（B-058採用、2026-10-19）
- 備考: 2026-06-10 追加。変更があった項目はダイジェストで「破壊的変更」として目立たせる。研修資料の陳腐化チェックにも使う。**節は発効日を本文に書くだけで、追記から発効まで1週間を切ることがある**（2026-09-04 追記の項目は発効まで5日）（B-058採用、2026-10-19）

### M365 Copilot プロンプト作成コース（MS-4005 動画コレクション）
- URL: https://learn.microsoft.com/collections/d4y3hkm5p12je2
- API URL（取得はこちら必須）: https://learn.microsoft.com/api/lists/d4y3hkm5p12je2?locale=en-us
- 取得方法: WebFetch（API URL）
- 注目点: 講師主導コース「MS-4005 Craft effective prompts for Microsoft 365 Copilot」の全9モジュール動画版コレクション。モジュール追加・内容更新の検知。プロンプト研修コンテンツのネタ元
- 頻度: 週1回確認（ほぼ静的な学習コンテンツのため変更検知のみ）
- 備考: 2026-07-23 追加（kit 指示）。コレクションページ本体は SPA のため WebFetch では中身が取れない。`/api/lists/<コレクションID>` の JSON なら取得可（2026-07-23 疎通確認済み）

---

## メンテナンスノート

- 本ファイルのソース追加・削除時は `fetch-flow.md` 側のフォールバック定義も合わせて更新すること
- **他社 AI 開発ツール（Anthropic / Claude / Cursor / OpenAI / Codex / Devin 等）のソースは本リポジトリには置かない。`kit1132/01_ai-news-Master` の担当。**
  - 2026-07-26 修正。旧記載は「他社ツールのソースは別ファイルに分離済み」という趣旨だったが、**その分離先ファイルは作成されないまま残っていた**。
    分離先が存在しないため生成エージェントが「AI系ツールも自分の担当」と解釈し続け、直近10ファイル中7ファイルで先頭 H2 が「AI開発ツール」になっていた。
    **分離先ファイルを新たに作る必要はない。他社ツールは 01 のリポジトリが既に担当している**
  - 本ファイルに登録されているソースは全て Microsoft エコシステム。他社ツールのソースをここに追加しないこと
