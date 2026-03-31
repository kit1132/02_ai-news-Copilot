# デイリーチェック対象サイト

## 取得フォールバックフロー

すべてのWebFetchソースに共通で適用する。

1. **WebFetch（主URL）** → 成功すればそのまま使用
2. **403/429/タイムアウト時** → 代替URLがあればWebFetchで代替URLを試行
3. **代替URLも失敗、または代替URLなし** → WebSearchで `site:ドメイン 検索キーワード 当年` を検索
4. **検索結果0件** → `site:` を外して検索キーワードのみで再検索（`site:` オペレータが非対応の場合もあるため）
5. **すべて失敗** → 当該ソースを「取得不可」と記録し、ダイジェスト改善メモにフォールバック結果を記載

### 注意事項
- WebSearchに日付フィルタ機能はない。クエリに年（例: `2026`）を含めて鮮度を担保する
- `site:` オペレータはWebSearchで非対応の場合がある。結果0件時は必ず `site:` なしで再検索する
- フォールバック発生時は改善メモに以下を記録する:
  - 失敗URL
  - ステータスコード（403/429/timeout等）
  - 最終的に成功した取得方法（代替URL / WebSearch / 取得不可）
  - 発生日時

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
- フォールバック検索: `site:microsoft.com/en-us/microsoft-365/roadmap Copilot Studio agent`（WebSearch）
- 取得方法: WebSearch推奨（SPA/動的ページのためWebFetchでは中身が取れないことが多い）
- 注目点: リリース予定機能、GA時期、プレビュー開始。Release Notesが「過去の変更」なのに対し、こちらは「未来の予定」を追う情報源
- 頻度: 毎日確認

## 高優先

### Copilot Studio Release Wave（計画機能一覧）
- URL: https://learn.microsoft.com/en-us/power-platform/release-plan/2025wave2/microsoft-copilot-studio/planned-features
- 取得方法: WebFetch
- 注目点: 半期ごとの計画機能リスト（2025 Wave 2 = 2025年10月〜2026年3月）。Preview/GA予定時期が一覧化されている。Wave切替時（4月・10月頃）にURLが変わる点に注意
- 頻度: 週1〜2回確認（更新頻度が低いため）

### Power Platform Released Versions
- URL: https://learn.microsoft.com/en-us/power-platform/released-versions/
- 取得方法: WebFetch
- 注目点: Copilot StudioはPower Platform基盤のため、基盤側のバージョン変更が影響する。Power Apps/Power Automate/Copilot Studioの各リージョン展開状況
- 頻度: 毎日確認

### Tech Community - Microsoft 365 Copilot Blog
- URL: https://techcommunity.microsoft.com/blog/microsoft365copilotblog
- 取得方法: WebFetch
- 注目点: 月次「What's New in Microsoft 365 Copilot」記事が最重要。公式Release Notesより詳細な背景説明・活用事例・管理者向けガイダンスが含まれる
- 頻度: 毎日確認

### Anthropic News
- URL: https://www.anthropic.com/news
- 代替URL: https://www.anthropic.com/research
- 検索キーワード: `Anthropic Claude release announcement`
- 取得方法: WebFetch（403の場合フォールバックフローに従う）
- 注目点: Claude新モデルリリース、API変更、新機能発表、料金変更
- 頻度: 毎日確認
- 備考: Bot対策により403を返すことが多い

### Claude Support / Release Notes
- URL: https://support.claude.com
- 代替URL: なし
- 検索キーワード: `Claude AI update changelog new feature`
- 取得方法: WebFetch（403の場合フォールバックフローに従う）
- 注目点: Claude製品のリリースノート、既知の問題、機能変更
- 頻度: 毎日確認
- 備考: Bot対策により403を返すことが多い

### Cursor Changelog
- URL: https://www.cursor.com/changelog
- 代替URL: なし
- 検索キーワード: `Cursor AI editor changelog update`
- 取得方法: WebFetch（403の場合フォールバックフローに従う）
- 注目点: AI統合開発環境の新機能、モデル対応状況、エディタ機能改善
- 頻度: 毎日確認
- 備考: Bot対策により403を返すことが多い

### Devin Documentation
- URL: https://docs.devin.ai
- 代替URL: なし
- 検索キーワード: `Devin AI agent update new feature`
- 取得方法: WebFetch（403の場合フォールバックフローに従う）
- 注目点: AIソフトウェアエンジニアエージェントの機能追加、API変更、利用ガイド更新
- 頻度: 毎日確認
- 備考: Bot対策により403を返すことが多い

### X (トレンド検索)
- 取得方法: WebSearch（直接アクセス不可のため検索経由）
- 検索キーワード例:
  - "Microsoft Copilot update"
  - "Copilot Studio new feature"
  - "M365 Copilot release"
  - "Copilot Studio agent"
  - "Microsoft Copilot 新機能"
  - "Copilot Studio 活用"
- 注目点: 新機能のバズ、導入企業の知見共有、不具合報告
- 頻度: 毎日確認