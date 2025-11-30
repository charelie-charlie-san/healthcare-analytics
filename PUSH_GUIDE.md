# 📤 CursorからGitHubへPushする完全ガイド

## 🎯 方法A: Cursorの内蔵機能を使う（超簡単！）

### ステップ1: Source Controlを開く

1. Cursorの左サイドバーで **🌿（Source Control）** アイコンをクリック
2. 「Initialize Repository」ボタンが見えたら、それをクリック
3. プロジェクトフォルダが選択されていることを確認

### ステップ2: ファイルを「Staging」に追加

1. 変更されたファイルのリストが表示されます
2. 各ファイルの右側の **+（プラス）** マークをクリック
3. または、一番上の **+** をクリックして全ファイルを追加

**追加すべきファイル:**
- ✅ `app.py`
- ✅ `data.csv`
- ✅ `requirements.txt`
- ✅ `README.md`
- ✅ `.gitignore`

**追加してはいけないファイル:**
- ❌ `.DS_Store`（.gitignoreで自動除外される）
- ❌ `__pycache__`（.gitignoreで自動除外される）

### ステップ3: コミットメッセージを書く

上部の「Message」欄に、変更内容を書きます。

**✨ AI駆動開発らしいコミットメッセージの例:**

```
🎉 初回リリース: 病院経営分析ダッシュボード

- Streamlitでインタラクティブなダッシュボードを実装
- Plotlyで購入推移・削減コスト推移を可視化
- PDF出力機能（ビジネス文書風レポート）
- 目標達成率ゲージとアラート機能
- Cursor + Gemini で開発
```

または、シンプルに：

```
✨ Initial commit: Hospital dashboard with Streamlit
```

### ステップ4: コミット実行

1. **✓（チェックマーク）** ボタンをクリック（または `Cmd + Enter`）
2. 「Commit」が完了すると、メッセージがクリアされます

### ステップ5: GitHubに公開（Publish）

1. **「Publish to GitHub」** ボタンが表示されたら、それをクリック
2. リポジトリ名を入力: `hospital-dashboard`
3. 説明を入力（任意）: `病院向け経営分析ダッシュボード（Streamlit）`
4. **Public（公開）** または **Private（非公開）** を選択
   - 公開する場合: **Public** （無料、誰でも見られる）
   - 非公開の場合: **Private** （無料、あなただけ見られる）
5. **Publish** ボタンをクリック

6. GitHubへのログインを求められたら：
   - ブラウザが開きます
   - 「Authorize GitHub for VSCode」をクリック
   - GitHubのパスワードを入力
   - 認証完了！

### ステップ6: 確認

1. ブラウザでGitHubを開く: `https://github.com/あなたのユーザー名/hospital-dashboard`
2. ファイルがすべてアップロードされていることを確認
3. README.mdが美しく表示されていることを確認

🎉 **おめでとうございます！GitHubへのアップロード完了です！**

---

## 🎯 方法B: ターミナルを使う（上級者向け）

Cursorの下部パネルで「Terminal」タブを開き、以下を順番に実行：

### ステップ1: Gitの初期化

```bash
# プロジェクトフォルダに移動（すでにいるはず）
cd /Users/moonlitlemon/hospital_dashboard

# Gitを初期化
git init
```

### ステップ2: ファイルを追加

```bash
# 全ファイルを追加（.gitignoreで除外されたファイルは自動で除外される）
git add .

# 何が追加されたか確認
git status
```

緑色で表示されるファイルが「追加されたファイル」です。  
赤色で表示されるファイルがあれば、それは `.gitignore` で除外されています（正常）。

### ステップ3: コミット

```bash
git commit -m "✨ Initial commit: Hospital dashboard with Streamlit"
```

### ステップ4: GitHubにリポジトリを作成

1. ブラウザで https://github.com/new を開く
2. **Repository name:** `hospital-dashboard`
3. **Description:** `病院向け経営分析ダッシュボード（Streamlit）`
4. **Public** または **Private** を選択
5. ⚠️ **「Add README」のチェックを外す**（すでにローカルにあるため）
6. **Create repository** をクリック

### ステップ5: ローカルとGitHubを紐付け

GitHubの画面に表示されるコマンドをコピーして実行：

```bash
# あなたのGitHubユーザー名に置き換えてください
git remote add origin https://github.com/あなたのユーザー名/hospital-dashboard.git

# ブランチ名をmainに変更（最新の推奨）
git branch -M main

# GitHubにPush
git push -u origin main
```

### ステップ6: 認証

初回Pushの際、ユーザー名とパスワードを求められます：

- **Username:** あなたのGitHubユーザー名
- **Password:** ⚠️ **GitHubのパスワードではなく、Personal Access Token を入力！**

Personal Access Tokenの作成方法は `SETUP_GUIDE.md` を参照。

### ステップ7: 確認

```bash
# Pushが成功したか確認
git status
```

「Your branch is up to date with 'origin/main'」と表示されればOK！

---

## 📝 今後の更新時の流れ

一度GitHubにアップロードした後、コードを変更したら：

### Cursor GUIの場合

1. Source Control を開く
2. 変更ファイルの横の **+** をクリック
3. コミットメッセージを書く（例: `🐛 Fix: グラフの色を修正`）
4. **✓** ボタンでコミット
5. **↑（雲マーク）** ボタンで Push

### ターミナルの場合

```bash
git add .
git commit -m "🐛 Fix: グラフの色を修正"
git push
```

---

## 🎨 コミットメッセージの書き方（AI駆動開発スタイル）

### 接頭辞（Emoji Prefix）

| Emoji | 意味 | 使う場面 |
|-------|------|----------|
| ✨ | 新機能 | `✨ Add: PDF出力機能を追加` |
| 🐛 | バグ修正 | `🐛 Fix: グラフが表示されない問題を修正` |
| 🎨 | デザイン改善 | `🎨 Style: ダッシュボードのレイアウト調整` |
| 📝 | ドキュメント | `📝 Docs: README.mdにセットアップ手順を追加` |
| ⚡ | パフォーマンス改善 | `⚡ Perf: データ読み込みを高速化` |
| ♻️ | リファクタリング | `♻️ Refactor: コードをクリーンアップ` |
| 🔥 | コード削除 | `🔥 Remove: 不要なコメントを削除` |
| 🚀 | デプロイ | `🚀 Deploy: Streamlit Cloudに初回デプロイ` |

### 良いコミットメッセージの例

```
✨ Add: 目標達成率ゲージをサイドバーに追加

- Plotlyでゴージチャートを実装
- 目標額と実績額の比較を可視化
- リアルタイムで達成率を表示
```

```
🐛 Fix: PDF生成時のKaleidoエラーを修正

- kaleido==0.2.1に固定
- requirements.txtを更新
```

```
🎨 Style: メディカルブルーのカラースキームに統一

- プライマリカラーを#0056b3に変更
- グラフの色も統一
- 清潔感のあるデザインに
```

---

## ⚠️ トラブルシューティング

### エラー: "failed to push some refs"

**原因:** GitHubのリポジトリとローカルが同期していない

**解決方法:**

```bash
# GitHubの最新を取得してマージ
git pull origin main --allow-unrelated-histories

# 再度Push
git push -u origin main
```

### エラー: "Permission denied (publickey)"

**原因:** SSH認証が設定されていない

**解決方法1:** HTTPSを使う

```bash
# リモートURLをHTTPSに変更
git remote set-url origin https://github.com/あなたのユーザー名/hospital-dashboard.git

# 再度Push
git push -u origin main
```

**解決方法2:** SSH鍵を設定（`SETUP_GUIDE.md` 参照）

### エラー: "Authentication failed"

**原因:** Personal Access Tokenが正しくない、または有効期限切れ

**解決方法:**

1. GitHubで新しいPersonal Access Tokenを生成（`SETUP_GUIDE.md` 参照）
2. 再度Pushして、新しいトークンを入力

### 大きなファイルがアップロードできない

**原因:** GitHubは100MB以上のファイルを受け付けない

**解決方法:**

1. `.gitignore` に大きなファイルを追加
2. すでにコミット済みの場合:

```bash
# キャッシュから削除
git rm --cached 大きなファイル名

# .gitignoreに追加
echo "大きなファイル名" >> .gitignore

# 再度コミット
git add .gitignore
git commit -m "🔥 Remove: 大きなファイルを除外"
git push
```

---

## 🎓 用語解説（超初心者向け）

| 用語 | 意味（簡単に言うと） |
|------|----------------------|
| **Git** | ファイルの変更履歴を記録するツール（タイムマシン） |
| **GitHub** | Gitのデータを保存するクラウドサービス（Dropboxみたいなもの） |
| **リポジトリ** | プロジェクトの保管場所（フォルダ） |
| **コミット** | 変更を記録すること（セーブポイントを作る） |
| **Push** | ローカルの変更をGitHubにアップロードすること |
| **Pull** | GitHubの最新をローカルにダウンロードすること |
| **Clone** | GitHubのリポジトリを自分のPCにコピーすること |
| **ブランチ** | 平行世界（実験用のコピー） |
| **main** | メインのブランチ（昔は master だった） |
| **origin** | GitHub上のリポジトリの呼び名 |

---

<div align="center">

**🎉 これでGitHubマスターの第一歩です！**

次は Streamlit Cloud でWeb公開しましょう 🚀

</div>

