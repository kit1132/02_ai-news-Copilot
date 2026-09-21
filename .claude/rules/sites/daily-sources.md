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
- 注目点: 新機能リリース（Preview/GA）、モデル変更（GPT-4o→GPT-5等）、破壊的変更、VS Code拡張、エージェント評価機能。**`(Preview)` / `(Production-ready preview)` 表記は GA 根拠にしない**
- 頻度: 毎日確認
- 備考: 2026-06-07・06-08 に Learn MCP 経由で安定取得を確認（B-001採用、2026-06-10）。WebFetch は403になる日がある。
  2026-08-26追加（B-023採用）。What's New の Preview 表記は GA 後も更新が遅れる（GitHub Copilot ハーネスは 2026-08-03 GA 後も June 節が `(Production-ready preview)` のまま）。**提供段階は既存の Copilot Studio Blog（board RSS）の GA 宣言で突合する。** `harnesses-overview` は提供段階の突合先にしない（課金・ライセンスは直後の「Copilot Studio ライセンス・課金」節）。計画項目の GA 判定は B-046 どおり AI at Work roadmap RSS の `status`。ページが編集されても表記が直るとは限らない

### Copilot Studio ライセンス・課金
- URL（ハーネス概要）: https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- URL（クレジット概要）: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-credit-overview
- URL（枯渇時エンフォースメント）: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/enforcement-policy-credits
- URL（ライセンス経路）: https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
- URL（購入・容量管理・Studio 側）: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/billing-manage-buy-credits
- URL（標準ハーネスの消費レート表）: https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management
- URL（生成 AI ツールのトークン建てレート）: https://learn.microsoft.com/ai-builder/message-management
- URL（月次ライセンスガイド PDF・参考）: `aka.ms/CopilotCredits/LicensingGuide`（CDN / fwlink はゲートウェイ拒否のため本文取得不可のことが多い）
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: ハーネス別の課金方式、課金開始点（標準は publish 後／GitHub Copilot ハーネスは構築開始時）、クレジット消費対象、枯渇時のエンフォースメント、購入経路、**消費レート表**（basic / standard / premium・推論モデルの二重課金）、オーバレージ
- 頻度: 週1回確認（`updated_at` が動いた日は即日）
- 備考: 2026-09-21追加（B-022 / B-031採用）。What's New / Release Notes には課金再編が載らない。PPAC の容量管理（直前の節）と対で読む。
  ⚠️ **Learn に無いのは1クレジットあたりの USD 価格だけであり、クレジット消費レートは Learn 上にある**（`requirements-messages-management` / `message-management`）。
  ⚠️ **USD 単価は月次 PDF（Licensing Guide / Credits Guide）のみ。** PDF が取得不可の間はダイジェストに単価数値を載せない（一次未確認と明記）。見積もりは「1回のやり取り＝1クレジット」ではなく消費レート表を使う。
  ⚠️ `billing-manage-buy-credits` は Copilot Studio 直下パスだと 404。実体は `agents-experience/` 配下。

### Copilot Credits の容量管理（PPAC）
- URL: https://learn.microsoft.com/en-us/power-platform/admin/manage-copilot-studio-copilot-credits-capacity
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: Copilot Credits の容量割当、Overage management（テナント空き容量から引く／従量課金プランへ課金）、Manage Agents の月次上限（通知とハードストップ、状態は Nearing / Over / Within limit）、消費データの粒度、3ハーネス横断の統一管理面
- 頻度: 毎日確認
- 備考: 2026-08-26追加（B-045採用）。`updated_at` を毎回突合する。Copilot Studio 側の課金ドキュメント（直前の「Copilot Studio ライセンス・課金」節・B-022 / B-031）と対で読む。
  2026-08-26 再実測: 本ページ HTTP 200、title `Manage Copilot Credits and capacity for Copilot Studio`、`ms.date` 2026-08-14、`updated_at` 2026-08-19T01:04Z。`billing-manage-buy-credits` は Copilot Studio 直下パスだと 404 で、実体は `agents-experience/` 配下。
  ⚠️ **見積もりは本ページ FAQ の「1回のやり取り＝1クレジット」ではなく、消費レート表（`requirements-messages-management`）を使う。** USD 単価は Learn に無い。

### Microsoft 365 Copilot Release Notes
- URL: https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: M365 Copilot全体のリリースノート（Word/Excel/PowerPoint/Outlook/Teams各アプリ別）。Agent Mode、ライセンス変更、新エージェント追加
- 頻度: 毎日確認
- 備考: ページが18,000行超と巨大なため、Microsoft Learn MCP で取得し grep で差分確認する（B-002採用）。隔週更新の傾向あり（例: 6/2 の次は 6/16 前後見込み。B-003採用、2026-06-10）。**Learn MCP が使えない場合も WebSearch の二次メディア要約で代替せず、WebFetch で本ページを直接取得し分割読みすること（一次確認基準は `fetch-flow.md` 参照。B-009採用、2026-07-02）**
  ⚠️ **最新バッチの有無を `microsoft_docs_search` の返す日付見出しの並びで判定しない。`microsoft_docs_fetch` でページ本文を取得し、先頭の `## ` 見出し（＝最新バッチ日）を直接読んで判定すること。** docs_search は「新着の存在に気づく」用途に限定する。2026-07-30・07-31 は docs_search が July 15 → July 01 → June 16 の順で返したため「7月の追加バッチはゼロ」と誤判定したが、08-01 に docs_fetch で本文先頭を読むと「July 29, 2026」（対象期間 7/15〜7/29・全10項目）だった。取りこぼした10項目には Agent Builder の SharePoint リスト知識ソース対応（Roadmap 561920）が含まれる（B-019採用、2026-08-02）

### Copilot の Web 検索統制
- URL: https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: Cloud Policy の `Allow web search in Copilot` の3択、Researcher / Cowork への波及、政府クラウドの既定オフ、生成検索クエリの監査経路と DPA / HIPAA / EU Data Boundary の非適用、ユーザートグル（Web content / Researcher）
- 頻度: 毎日確認
- 備考: 2026-08-26追加（B-044採用）。`updated_at` を毎回突合する。下の「どの Copilot を使うか」と対で読む。
  2026-08-26 再実測: HTTP 200、title `Data, privacy, and security for web search in Microsoft Copilot and Microsoft Copilot Chat`、`ms.date` 2026-08-18、`updated_at` **2026-08-18T22:40:00Z**。冒頭 Note に Microsoft 365 Copilot → Microsoft Copilot / Microsoft 365 Copilot Chat → Microsoft Copilot Chat の改称がある。3択は Enabled in both / Disabled in both / **Disabled in Microsoft Copilot Work mode; Enabled in Microsoft Copilot Web mode and Microsoft Copilot Chat**。3つ目を選ぶと Researcher と Cowork の Web 検索も無効。Researcher は入力ボックスに Web search トグルがあり、Analyst と Cowork にはユーザー向けトグルが無い。未構成時は商用では利用可（`Allow the use of additional optional connected experiences in Office` が Disabled なら止まる）。**GCC or DoD は既定オフ**（本文に GCC High の文字列は無い）。生成検索クエリには DPA / HIPAA / EU Data Boundary が適用されない（プロンプトと応答には DPA が適用される）。
  ⚠️ **ドメイン除外の一次 `copilot/domain-exclusion` は 2026-08-26 再実測で HTTP 404。** 本ソースにドメイン除外ページは登録しない。撤回・停止の照合は B-024（`fetch-flow.md` と M365 Copilot Blog の board RSS）。

### どの Copilot を使うか
- URL: https://learn.microsoft.com/en-us/microsoft-365/copilot/which-copilot-for-your-organization
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: Work IQ ボタンのオン/オフの意味、製品名の対応、Web グラウンディングと Graph グラウンディングの切り替え
- 頻度: 毎日確認
- 備考: 2026-08-26追加（B-044採用）。`updated_at` を毎回突合する。上の「Copilot の Web 検索統制」と対で読む。
  2026-08-26 再実測: HTTP 200、h1 `Which Copilot is right for me or my organization?`、`ms.date` **2026-03-24**（`updated_at` より古い）、`updated_at` **2026-08-18T17:48:00Z**。本文に「Microsoft 365 Copilot」の文字列は 0 件で、改称 Note は上の Web 検索統制ページ側にある。Work IQ がオンのとき Copilot Chat は Microsoft Graph ベース、オフのとき Entra アカウントがアクセスできる結果に**加えて**インターネットの結果も表示する。
  ⚠️ **Work IQ の意味が Release Notes（August 25 バッチ）と正反対**——Release Notes は「オンで業務データへのアクセスが有効」。どちらか一方を正として単独掲載しない（B-041）。`support.microsoft.com` / `mc.merill.net` による第3の一次はゲートウェイ拒否（B-036採用。MC は WebSearch 要旨＋裏取り）。

### Microsoft 365 Roadmap（AI at Work）
- URL: https://www.microsoft.com/en-us/microsoft-365/roadmap
- RSS URL（Feature ID 単位）: https://www.microsoft.com/releasecommunications/api/v2/m365/rss
- 検索キーワード（WebSearch用）: `Microsoft 365 roadmap Copilot Studio agent 2026`
- 取得方法: RSS（Feature ID 単位）→ WebSearch（広報枠 Latest announcements）
- 注目点: Feature ID 単位の状態（`In development` / `Rolling out` / `Launched` / `Cancelled`）、GA / Preview 期日、リリース予定機能。Release Notes が「過去の変更」なのに対し、こちらは「未来の予定」。**GA 判定は RSS `category` の状態変化で行う**（`In development` → `Rolling out` / `Launched`）。Learn Release Wave の GA 列緑チェックは使わない。Copilot Studio / Power Platform（Power Apps / Power Automate / Dataverse）/ ガバナンス・管理の計画項目も本ソースで追う
- 頻度: 毎日確認
- 備考: 2026-08-26更新（B-047採用）。JSON の `features` エンドポイント（`/releasecommunications/api/v2/m365/features`）は HTTP 204・本文0バイト（2026-08-25〜08-26 実測。ゲートウェイ拒否ではなくオリジン応答）。同ホストの `/rss` は **200 / `application/rss+xml` / 約1.70 MB / 1,787項目**（同日再実測。B-047 起票時は 1,785項目）。
  各 `item` は `link` に `?id=<Feature ID>`、`category` に状態、`pubDate` に起票日、`description` 末尾に `GA date` と `Preview date` を持つ。**`modified` は取れない**ため、状態変化の検知は前回取得分との突合で行う。
  ページ本体は SPA のため WebFetch では中身が取れない。広報枠 Latest announcements は WebSearch。
  RSS が `text/html` を返したら失敗（ソフト200）。ブラウザ風 UA では 403 の HTML になることがある。
  MRC MCP（B-040）と `features` JSON 直接照会（B-043）は未採用。`features` が 204 の間は RSS を Feature ID の一次とする。
  **2026-08-26更新（B-046採用）。** 旧「Copilot Studio Release Wave（計画機能一覧）」「Power Platform Release Wave（全体版）」および B-038 で提案していたガバナンス・管理ページは、本セクションへ統合した（URL は本項と同一）。2026年9月以降、新規リリース計画は Learn の Release Plans に掲載されない。2026-11-15 に Release Planner が退役し、Learn 側は履歴参照専用になる。Preview / GA 期日が 2026-06-01 以降の既存項目は 9〜11月に本 URL へ移行する。
  旧 Learn URL（履歴参照。日次巡回しない）:
  - `https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/microsoft-copilot-studio/planned-features`（2026-08-26 実測: HTTP 200 だが **AI at Work Roadmap へリダイレクト**。title `AI at Work Roadmap | Microsoft 365`）
  - `https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/`
  - `https://learn.microsoft.com/en-us/power-platform/release-plan/2026wave1/power-platform-governance-administration/planned-features`
  ⚠️ 2026-08-26 再実測: Wave 概要・ガバナンス・Power Automate `planned-features` は Learn 上に残るが、廃止・移行の注記は一文も無い（B-024 同型）。一次は本セクションの RSS。
  ⚠️ B-018 の「GA 列の緑チェック差分監視」は移行完了後に成立しない。GA 判定は上記 `status` へ移した。

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
- 取得方法: WebSearch → WebFetch
- 注目点: テナント管理者向け変更通知のアーカイブ。Roadmapが「予定」、Release Notesが「リリース済」に対し、こちらは「展開中の変更と影響範囲」を扱う。不可逆な期限（停止・退役・既定オン）
- 頻度: 毎日確認
- 備考: 非公式の個人運営アーカイブ（Merill Fernando氏）。公式Message Center（admin.microsoft.com）とは差分が生じる可能性あり。テナント管理者権限不要で閲覧できる点が利点。
  2026-08-26追加（B-036採用）。`mc.merill.net` はゲートウェイ拒否のため **WebSearch が実質のプライマリ**。MC 番号が索引に出たら、`learn.microsoft.com` の当該機能ページ・Partner Center 月次アナウンス・Tech Community board RSS の3経路で裏取りする。いずれでも本文が取れない場合は **「MC 番号と要旨のみ・一次未確認」** として掲載する。
  Learn の機能ページに記載がないことは *否定* の根拠にしない（手順は `fetch-flow.md`）。
  `m365admin.handsontek.net` / `mwpro.co.uk` / `pupuweb.com` は同じゲートウェイ拒否のため代替にしない。
  Microsoft MCP Server for Enterprise はテナント認証が要るため、本ダイジェストの自動巡回では使わない。`support.microsoft.com` もゲートウェイ拒否のまま登録しない。

### Copilot Studio Blog（Tech Community・公式）
- URL: https://techcommunity.microsoft.com/category/microsoft365copilot/blog/copilot-studio-blog
- RSS URL（取得はこちら必須）: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=copilot-studio-blog
- 検索キーワード（WebSearch用）: `site:techcommunity.microsoft.com Copilot Studio blog 2026`
- 取得方法: RSS → WebSearch
- 注目点: Copilot Studio 製品チーム発の更新・技術・運用記事。マルチエージェント、Computer-using agents、ガバナンス白書（Administering and Governing Agents）等。**What's New が Preview のままの項目の GA 宣言**
- 頻度: 毎日確認
- 備考: 2026年春開設の専用公式ブログ（2026-06-10 追加）。**HTMLページは SSO リダイレクト/JSレンダリングのため取得不可。必ず RSS URL 経由で取得すること**。
  2026-08-26追加（B-023採用）。What's New の `(Preview)` 表記と本 board の GA 宣言が食い違うときは、本 board を提供段階の根拠にする。`harnesses-overview` は提供段階の突合先にしない（課金は「Copilot Studio ライセンス・課金」節）

---

## 高優先

### Agent 365 Blog（Tech Community・公式）
- URL: https://techcommunity.microsoft.com/blog/agent-365-blog
- RSS URL（取得はこちら必須）: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=agent-365-blog
- 検索キーワード（WebSearch用）: `site:techcommunity.microsoft.com "Agent 365" 2026` / `"What's new in Agent 365" 2026`
- 取得方法: RSS → WebSearch
- 注目点: 月次「What's new in Agent 365」記事、Agent Registry のリスクシグナル統合、Registry sync の対応プラットフォーム、マルチテナント管理、Copilot Credit のコスト管理（Cowork / Work IQ）
- 頻度: 週1回確認
- 備考: 2026-09-21追加（B-032採用）。`ai-tools.md` の「Microsoft Agent 365」一次。HTML は SSO/JS のため RSS 必須。2026-08-12 に board RSS 200・本文取得を確認。
  ⚠️ **board RSS のエントリは投稿日の降順に並んでいない。** 先頭N件で打ち切らず、フィード内の全エントリの `pubDate` / `dc:date` を読み、前回確認日より新しいものを全件抽出する（既存 board と同型。横展開の一般化は B-033 で提案中）。
  ⚠️ Partner Center 月次アナウンスと一部重複しうるが、Registry sync GA・ダッシュボード GA・パートナーリスクシグナル・コスト管理は本ブログにしか出ないことが多い。

### Microsoft Partner Center 月次アナウンス
- URL: https://learn.microsoft.com/en-us/partner-center/announcements/2026-august
- URL テンプレート: `https://learn.microsoft.com/en-us/partner-center/announcements/YYYY-month`（月名は英語小文字。例 `2026-september`）
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: M365 Copilot / Agent 365 のライセンス前提条件、CSP 提供開始、スペシャライゼーション要件、価格改定、不可逆な期限（プロモーション終了・名称変更・コンテスト締切）
- 頻度: 毎日確認（月内追記があるため）
- 備考: 2026-08-26追加（B-013採用）。パスは月次で変わる。**当月ページの全 `## ` 見出しと `Date` を突合する。** `ms.date` では追記を検知できない。
  2026-08-26 再実測: 8月ページ HTTP 200、title `August 2026 announcements`、`ms.date` **2026-08-10**（8/24 付追記より古い）。`Date` は **17件**（先頭 8/24 が2件）。`## ` は 19（MAICPP 配下の「Coming soon」等を含む）。索引 `https://learn.microsoft.com/en-us/partner-center/announcements/` も 200 で、8月17件＋7月分を列挙する。
  ⚠️ **翌月ページは公開まで 404。** 2026-08-26 再実測で `2026-september` は HTTP 404。**毎月1〜5日は翌月パスの公開有無を見る。** 7月ページ（`2026-july`）は履歴として残る（200 / `ms.date` 2026-07-29 / `## ` 37）。GitHub raw（`MicrosoftDocs/partner-center-pr`）は 404 のため裏取りに使わない。
  エンドユーザー向けの `support.microsoft.com` はゲートウェイ拒否のまま登録しない（B-036採用）。

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
- RSS URL（取得はこちら必須）: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=Microsoft365CopilotBlog
- 検索キーワード（WebSearch用）: `site:techcommunity.microsoft.com "Microsoft 365 Copilot" 2026`
- 取得方法: RSS → WebSearch
- 注目点: 月次「What's New in Microsoft 365 Copilot」記事が最重要。公式Release Notesより詳細な背景説明・活用事例・管理者向けガイダンスが含まれる。**既報機能の撤回・仕様変更を告げる `Update:` / `rolled back` / `paused` / `retired` / `retiring` 系記事**
- 頻度: 毎日確認
- 備考: HTMLページは SSO リダイレクトのため取得不可。board RSS は WebFetch で取得可能と確認済み（2026-06-10。旧備考「robots.txt でブロック」は board RSS には当てはまらない）。
  2026-08-26追加（B-024採用）。Learn の機能ページ掲載を提供中の根拠にしない。週1回、本 board RSS を機能名込みで照合する（手順は `fetch-flow.md`）。`copilot/domain-exclusion` はソース登録しない（2026-08-26 再実測で HTTP 404）

### SharePoint Blog（Tech Community・公式）
- URL: https://techcommunity.microsoft.com/category/content_management/blog/spblog
- RSS URL（取得はこちら必須）: https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=SPBlog
- 検索キーワード（WebSearch用）: `site:techcommunity.microsoft.com "What's New in Copilot in SharePoint" 2026`
- 取得方法: RSS → WebSearch
- 注目点: 月次「What's New in Copilot in SharePoint」、Copilot in SharePoint の提供形態変更・管理者制御、AI Skills
- 頻度: 週1回確認
- 備考: 2026-08-26追加（B-015採用）。`ai-tools.md` の「SharePoint の AI 機能」に対応する一次。HTML 一覧は必ず RSS 経由で取る。
  2026-08-26 再実測: RSS は HTTP 200 / `text/xml` / 20件 / フィード title `Microsoft SharePoint Blog articles`。先頭は 8/6「What's New in Copilot in SharePoint: August 2026」（記事ID 4535421）。原案 URL `category/microsoft365/blog/spblog` は `category/content_management/blog/spblog` へリダイレクト（200）。`/blog/spblog` は 404。記事 HTML は 200 でも本文がほぼ空（flat 約2.6KB）で、RSS の `description` に本文がある（8月号 7,268文字）。
  ⚠️ **本フィードの `pubDate` は日付降順ではない**（例: 7/8 の Partner Spotlight が 7/9 や 6/30 の後ろに混ざる）。先頭N件で打ち切らず、全エントリの `pubDate` / `dc:date` を読む。既存 board（M365 Copilot Blog / Copilot Studio Blog）への同じ備考の横展開は B-033 で提案中・未採用。
  月次記事の内容を WebSearch 要約で取らない（B-026 で提案中・未採用）。

### Microsoft Purview - What's new
- URL: https://learn.microsoft.com/en-us/purview/whats-new
- 取得方法: Microsoft Learn MCP → WebFetch
- 注目点: DLP for Microsoft 365 Copilot の新条件・アクション、Copilot Studio エージェント／Agent 365／Copilot Cowork への適用範囲、Preview→GA。**当月節だけでなく直近2か月分の月見出しを全項目突合する。** `updated_at` が動いたのに当月節が無変化なら、過去月の節への追記を疑う
- 頻度: 週1回確認
- 備考: 2026-08-26追加（B-016採用）。`ai-tools.md` の「Purview によるガバナンス」に対応する一次。`.last-check-state.md` には月ごとの**分類名と項目数**を残し、次回はその数と突き合わせる。
  2026-08-26 再実測: HTTP 200、h1 `What's new in Microsoft Purview`、`ms.date` **2026-06-30**（当月更新を表さない）。HTML には `updated_at` が出ないため Learn MCP で突合する。8月節は Sensitivity labels の2件のみ。7月節は6分類（Data Governance / Data Loss Prevention / Data lifecycle management / Information Protection / Insider Risk Management / Shared capabilities）。6月節に Copilot Cowork の GA がある。
  ⚠️ **Roadmap 569612（Copilot メモリの保持）は本日も本ページに無い。** fetch-flow への一般化は B-042 で提案中・未採用。

### Microsoft 365 Blog（本体）
- URL: https://www.microsoft.com/en-us/microsoft-365/blog/
- RSS URL（優先）: https://www.microsoft.com/en-us/microsoft-365/blog/feed/
- 検索キーワード（WebSearch用）: `Microsoft 365 blog announcement Copilot 2026`
- 取得方法: RSS → **WebSearch 照合（毎日併用）** → WebSearch
- 注目点: M365 全体の大型発表・ライセンス/料金変更の初出（Microsoft Scout、Work IQ、M365 Copilot 新デザイン等）
- 頻度: 毎日確認
- 備考: 2026-06-10 追加。microsoft.com は UA により 403 を返すことがある。失敗時は WebSearch へ。日次の細かい更新は Release Notes / Roadmap と重複するため大型発表のみ拾う。
  ⚠️ **RSS の WebFetch が 200 でも先頭エントリが最新とは限らない。** `site:microsoft.com/en-us/microsoft-365/blog 2026` 等での WebSearch 照合を毎日併用し、`.last-check-state.md` の最新記事日付と突合すること。2026-08-01 は同一 RSS URL を WebFetch して「6/25 の Copilot in Excel 記事が最新」と判定したが、08-02 の取得では 7/30 の "The next measure of AI momentum is work transformed"（有償3,000万シート・展開ベンチマーク等の一次数値を含む）が先頭にあり、過去の全 digest に未掲載だった。**Release Notes の B-019 と同じ「単一の取得経路が最新項目を落とす」類型**（B-020採用、2026-08-02）

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
