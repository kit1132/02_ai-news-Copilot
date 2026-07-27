# Microsoft エコシステムの AI ツール・プロダクト

**このリポジトリは Microsoft エコシステム専任。** 実用的な AI ツールのリリース・アップデート情報を最重視する。

他社の AI 開発ツール（Cursor / Claude / Anthropic / OpenAI / Codex / Devin / Gemini 等）は
`kit1132/01_ai-news-Master` の担当なので、**このリポジトリでは取り上げない**（下の「除外」参照）。

## 特に追いたいもの

- **Copilot Studio**（エージェント構築レイヤー）: 新機能（オーケストレーションモデル変更、コネクタ追加、VS Code拡張、Computer Use等）・破壊的変更をリリース初日に導入する方針
- **Microsoft 365 Copilot**（エンドユーザーレイヤー）: Word/Excel/PowerPoint/Outlook/TeamsのAgent Mode、Copilot Chat、Researcher、Copilot Notebooks等。新機能・ライセンス変更・料金変更
- **Power Platform**（基盤レイヤー）: Copilot Studioの基盤。Power Automate/Power Apps/Dataverse/AI Builderの変更がCopilot Studioに波及する
- **Microsoft 365 Roadmap / Release Wave**（計画レイヤー）: 未来のリリース予定、GA時期、プレビュー開始。Purview連携、ガバナンス機能の方向性
- **Microsoft の AI エージェント基盤**: Microsoft Agent 365、Azure AI Foundry（Copilot Studio連携部分）、サードパーティ連携（ServiceNow、Workday等）、MCP対応

### Microsoft 一次に新規がない日に広げてよい範囲（2026-07-26 追加）

直近10日中5日が「Microsoft 一次・据え置き確認・新規なし」だった。その日に**他社ツールで埋めるのは禁止**だが、
以下の Microsoft エコシステム内であれば取り上げてよい。

- **Azure AI Foundry / Azure OpenAI Service**: モデル提供開始、リージョン展開、料金変更
- **Microsoft の自社 AI モデル**: MAI 系、Phi 系の発表・仕様変更
- **Microsoft Fabric / Dataverse / Teams / SharePoint の AI 機能**
- **GitHub Copilot の組織導入・ライセンス・管理機能**（Business / Enterprise プラン、管理者制御、テナント統制）
  - ⚠️ **GitHub Copilot CLI のリリースとコーディング機能そのものは `01_ai-news-Master` の担当**
    （01 に `GitHub Copilot CLI Releases`・`GitHub Copilot Changelog` が登録済み）。ここを混ぜると 01 と重複する

## 関心の方向性

- 論文や理論よりも「今日から使えるもの」を優先
- 組織に導入できるかどうかの観点が重要（ライセンス体系、テナント管理、Purviewによるガバナンス、セキュリティ）
- 競合ツール（Google Gemini for Workspace、Salesforce Agentforce 等）は、**Microsoft 製品と直接比較する文脈でのみ1行触れる**。
  単独のニュースとしては取り上げない（2026-07-26 変更。旧「競合・周辺ツールも対象」が他社ツール混入の一因だった）

## 除外

- **他社の AI 開発ツール全般**（Cursor / Claude / Claude Code / Anthropic / OpenAI / ChatGPT / Codex / Devin / Gemini / DeepMind 等）。
  `kit1132/01_ai-news-Master` の担当。**Microsoft 一次に新規がない日でも、これらで枠を埋めない**
  （2026-07-26 追加。直近10ファイル中7ファイルで先頭 H2 が「AI開発ツール」になっていたため）
- **GitHub Copilot CLI のリリース・コーディング機能**（01_ai-news-Master の担当。組織導入・ライセンス・管理機能のみ本リポの対象）
- 学術論文のみの発表（実装を伴わないもの）
- 画像生成AI、音楽生成AI等のクリエイティブ系（趣味範囲では興味あり）
- AIの倫理・規制の議論（大きな政策変更以外）
- Dynamics 365固有のドメイン機能（Sales/Service/Finance等。Copilot Studio連携以外）
- Azure AI Foundryの深い開発者向け機能（MLOpsパイプライン等。Copilot Studio連携以外）
- Windows Copilot（OS統合機能。M365 Copilotとは別軸）