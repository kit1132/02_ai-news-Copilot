# スケジュールタスク設定

Claude Code on the web の「Scheduled tasks」に以下を設定する。

## 設定値

- **Name**: `ai-news`
- **Environment**: Cloud
- **Internet access**: Full internet
- **Frequency**: Daily, 07:00 AM (JST)
- **Repository**: ai-newsリポジトリを選択

## プロンプト

```
以下の手順でAIニュースダイジェストを生成してください。

1. CLAUDE.md を読み、プロジェクト構成を確認
2. `.claude/rules/` 配下の全ファイルを読み込み
3. `.last-check-state.md` を読み、前回チェック状態を確認
4. daily-sources.md に定義されたソースから情報を収集（WebFetch / WebSearch）
5. 前回状態との差分を判定し、新規情報のみを抽出
6. output-style.md に従い、ダイジェストを生成
7. `digests/YYYY/MM/ai-news-YYYY-MM-DD.md` として保存
8. `.last-check-state.md` を今日の状態で更新
9. `files.json` の配列先頭に新ファイルのパスを追加
10. git add → commit → push (main)
```
