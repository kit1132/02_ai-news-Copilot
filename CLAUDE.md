# AI News Digest

## 基本方針

- 出力は日本語
- 簡潔で実用的な情報を好む。冗長な説明は不要
- 定量的な根拠を重視
- AIエージェント・開発ツールのニュースに特化

## プロジェクト構成

- `digests/YYYY/MM/ai-news-YYYY-MM-DD.md` — デイリーダイジェスト本体
- `.last-check-state.md` — 各ソースの前回チェック状態（差分判定用）
- `IMPROVEMENT-BACKLOG.md` — 改善提案・取得障害の台帳（改善メモの単一情報源。運用ルールはファイル冒頭参照）
- `index.html` — ダイジェストのHTMLビューア（marked.js使用、GitHub Pagesで公開）
- `files.json` — ビューアが参照するダイジェストファイル一覧（新しい順、パスはルートからの相対）

## 実行環境

- Claude Code on the web（クラウド実行）
- スケジュールタスクとして毎朝自動実行
- ネットワーク: Full internet（外部サイトへのWebFetch/WebSearchが必要）
- **ブランチ: 必ず `main` を使用する。`git checkout main` してから作業を開始すること**
- **日付: JST（Asia/Tokyo, UTC+9）で判定する。`TZ=Asia/Tokyo date +%Y-%m-%d` で当日日付を取得すること**

## ダイジェスト生成後の手順

1. `digests/YYYY/MM/ai-news-YYYY-MM-DD.md` を生成（ディレクトリがなければ作成）
2. `.last-check-state.md` を更新
3. `IMPROVEMENT-BACKLOG.md` を更新（新規提案の起票・既出提案の回数更新・障害の最終確認日更新。`output-style.md` の改善メモ規定参照）
4. `files.json` の配列先頭に新ファイルのパス（`digests/YYYY/MM/ai-news-YYYY-MM-DD.md`）を追加
5. 変更（`IMPROVEMENT-BACKLOG.md` 含む）を `main` ブランチに git commit + push する

## ルール参照

詳細なフィルタリング基準・対象サイトは `.claude/rules/` 以下を参照すること。
各タスクは該当するrulesファイルを読み込んでから実行する。
