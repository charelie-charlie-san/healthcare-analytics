# 🚀 今日中にWeb公開！完全マスターガイド

> **非エンジニア × AI駆動開発者のための、最短ルート完全ガイド**  
> このガイド通りに進めば、30分で世界中からアクセスできるWebアプリが完成します。

---

## 📋 目次

1. [🎯 このガイドの使い方](#-このガイドの使い方)
2. [⏱️ タイムライン（30分で完走）](#️-タイムライン30分で完走)
3. [📦 準備するもの](#-準備するもの)
4. [🚀 実行ステップ](#-実行ステップ)
5. [🎉 完了後のアクション](#-完了後のアクション)
6. [⚠️ トラブルシューティング](#️-トラブルシューティング)

---

## 🎯 このガイドの使い方

### ファイル構成

このプロジェクトには、以下のガイドファイルがあります：

| ファイル名 | 内容 | 読むタイミング |
|-----------|------|---------------|
| **このファイル** | 全体のロードマップ | **最初に読む** |
| `SETUP_GUIDE.md` | GitHub認証の詳細 | 認証でつまずいた時 |
| `PUSH_GUIDE.md` | GitHubへのPush方法 | Push時の詳細手順 |
| `DEPLOY_GUIDE.md` | Streamlit Cloudデプロイ | デプロイ時の詳細手順 |

### 推奨の進め方

1. **まず、このファイルを最後まで読む**（全体像を把握）
2. **実際に手を動かしながら進める**（読むだけではダメ）
3. **つまずいたら、対応する詳細ガイドを参照**
4. **完了したら、X（Twitter）でシェア！**

---

## ⏱️ タイムライン（30分で完走）

```
0分   🏁 スタート！
      ↓
5分   ✅ GitHubアカウント設定完了
      ↓
10分  ✅ .gitignoreと秘密保護設定完了
      ↓
15分  ✅ README.mdをプロ仕様に更新
      ↓
20分  ✅ GitHubへ初回Push完了
      ↓
25分  ✅ Streamlit Cloudにデプロイ開始
      ↓
30分  🎉 Web公開完了！世界中からアクセス可能に！
```

---

## 📦 準備するもの

### 必須アイテム

- [ ] **GitHubアカウント**（無料）
  - まだない場合: https://github.com/signup
- [ ] **Googleアカウント**（無料）
  - Streamlit Cloudのログインに使用
- [ ] **Cursorエディタ**（起動済み）
- [ ] **このプロジェクト**（hospital_dashboard）

### 確認事項

- [ ] ローカルでアプリが動作している（`streamlit run app.py` で確認）
- [ ] インターネット接続が安定している
- [ ] 30分ほど集中できる時間がある

---

## 🚀 実行ステップ

---

### ステップ1: GitHubアカウントのプロフィール設定（5分）

#### 1-1. GitHubにログイン

https://github.com にアクセス → ログイン

#### 1-2. プロフィールを編集

1. 右上のプロフィール画像をクリック → **Settings**
2. 左メニューの **Public profile** を選択
3. 以下を入力：

| 項目 | 入力内容 |
|------|----------|
| **Name** | にくまる（AI駆動BizDev） |
| **Bio** | 非エンジニアがAI（Cursor + Gemini）で医療×BizDevツールを開発 \| Streamlit \| データ分析 \| カスタマーサクセス |
| **Company** | （あなたの会社名、または空欄） |
| **Location** | 日本 🇯🇵 |
| **Website** | https://x.com/あなたのXアカウント |

4. **Update profile** をクリック

#### 1-3. プロフィール画像を設定（任意）

- Xと同じ画像を使うと統一感が出ます
- 左メニューの **Profile** → **Edit** → **Upload new picture**

---

### ステップ2: Cursorのターミナルを開く（1分）

1. Cursorを開く
2. 上部メニューの **Terminal** → **New Terminal**
3. 以下のコマンドで、プロジェクトフォルダに移動：

```bash
cd /Users/moonlitlemon/hospital_dashboard
```

#### 確認コマンド

```bash
# 現在の場所を確認
pwd
# → /Users/moonlitlemon/hospital_dashboard と表示されればOK

# ファイル一覧を確認
ls
# → app.py, data.csv, README.md などが表示されればOK
```

---

### ステップ3: .gitignoreファイルの確認（1分）

秘密情報を守るためのファイルが作成されているか確認：

```bash
# .gitignoreファイルがあるか確認
ls -a | grep .gitignore
```

✅ `.gitignore` と表示されればOK！（すでに作成済み）

#### 中身を確認（任意）

```bash
cat .gitignore
```

APIキーや秘密情報を守る設定が書かれていることを確認。

---

### ステップ4: Gitの初期設定（3分）

**初回のみ実行**（2回目以降は不要）

```bash
# あなたの名前を登録
git config --global user.name "にくまる"

# GitHubのメールアドレスを登録（GitHubで登録したメールアドレス）
git config --global user.email "your-github-email@example.com"

# 確認
git config --global user.name
git config --global user.email
```

---

### ステップ5: Gitリポジトリを初期化（1分）

```bash
# Gitを初期化
git init

# 確認メッセージが表示される
# → Initialized empty Git repository in /Users/moonlitlemon/hospital_dashboard/.git/
```

---

### ステップ6: ファイルをステージングしてコミット（3分）

```bash
# 全ファイルを追加（.gitignoreで除外されたファイルは自動で除外される）
git add .

# 何が追加されたか確認
git status
```

**確認ポイント:**
- ✅ `app.py`, `data.csv`, `requirements.txt`, `README.md` などが緑色で表示される
- ✅ `.DS_Store`, `__pycache__` などは表示されない（除外されている）

```bash
# コミット（変更を記録）
git commit -m "✨ Initial commit: Hospital dashboard with Streamlit"

# 成功メッセージが表示される
# → [main (root-commit) xxxxxxx] ✨ Initial commit: Hospital dashboard with Streamlit
```

---

### ステップ7: GitHubにリポジトリを作成（3分）

#### 7-1. ブラウザでGitHubを開く

1. https://github.com/new を開く
2. 以下を入力：

| 項目 | 入力内容 |
|------|----------|
| **Repository name** | `hospital-dashboard` |
| **Description** | 病院向け経営分析ダッシュボード（Streamlit + AI駆動開発） |
| **Public / Private** | **Public**（世界中に公開） |
| **Add a README file** | ❌ **チェックを外す**（すでにローカルにあるため） |
| **Add .gitignore** | **None**（すでにローカルにあるため） |
| **Choose a license** | **MIT License**（自由に使ってOK） |

3. **Create repository** をクリック

#### 7-2. リポジトリのURLをコピー

作成後の画面に表示される、以下のようなURLをコピー：

```
https://github.com/あなたのユーザー名/hospital-dashboard.git
```

---

### ステップ8: ローカルとGitHubを紐付けてPush（3分）

Cursorのターミナルに戻り、以下を実行：

```bash
# GitHubのリポジトリと紐付け（URLは自分のものに置き換える）
git remote add origin https://github.com/あなたのユーザー名/hospital-dashboard.git

# ブランチ名をmainに変更
git branch -M main

# GitHubにPush（アップロード）
git push -u origin main
```

#### 🔐 認証が求められたら

**パターンA: ダイアログが表示される場合**

1. 「Sign in with your browser」をクリック
2. ブラウザが開く → GitHubにログイン
3. 「Authorize」をクリック
4. 自動的にPushが完了

**パターンB: ターミナルで認証を求められる場合**

```
Username: あなたのGitHubユーザー名
Password: （GitHubのパスワードではなく、Personal Access Tokenを入力）
```

**Personal Access Tokenの作成方法:**

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. **Generate new token (classic)**
3. **Note:** `Cursor from Mac`
4. **Expiration:** `90 days`
5. **Select scopes:** ✅ `repo` にチェック
6. **Generate token** → 生成されたトークン（`ghp_xxxxxxxxxxxx`）をコピー
7. ターミナルのPasswordに貼り付け（文字は表示されないが、ちゃんと入力されている）

詳細は `SETUP_GUIDE.md` を参照。

#### 成功メッセージ

```
Enumerating objects: X, done.
Counting objects: 100% (X/X), done.
...
To https://github.com/あなたのユーザー名/hospital-dashboard.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

🎉 **GitHubへのアップロード完了！**

---

### ステップ9: GitHubで確認（1分）

ブラウザで以下のURLを開く：

```
https://github.com/あなたのユーザー名/hospital-dashboard
```

**確認ポイント:**
- ✅ `app.py`, `data.csv`, `requirements.txt` などが表示されている
- ✅ README.mdが美しくフォーマットされて表示されている
- ✅ `.DS_Store`, `__pycache__` などは表示されていない（除外成功）

---

### ステップ10: Streamlit Cloudにログイン（2分）

1. ブラウザで https://share.streamlit.io を開く
2. **「Sign up」** または **「Continue with GitHub」** をクリック
3. GitHubアカウントで認証
   - **「Authorize Streamlit」** をクリック
   - GitHubのパスワードを入力
4. メールアドレスを確認（GitHubのメールアドレスが自動入力される）
5. **「Continue」** をクリック

---

### ステップ11: アプリをデプロイ（5分）

#### 11-1. 新しいアプリを作成

1. Streamlit Cloudのダッシュボードで **「New app」** をクリック
2. 以下を入力：

| 項目 | 入力内容 |
|------|----------|
| **Repository** | `あなたのユーザー名/hospital-dashboard` |
| **Branch** | `main` |
| **Main file path** | `app.py` |
| **App URL (optional)** | 空欄でOK（自動生成される） |

#### 11-2. 詳細設定（任意）

**「Advanced settings」** をクリック:

| 項目 | 推奨設定 |
|------|----------|
| **Python version** | `3.9` または `3.10` |
| **Secrets** | 空欄でOK（APIキーを使う場合のみ設定） |

#### 11-3. デプロイ開始

**「Deploy!」** ボタンをクリック

#### 11-4. デプロイ完了を待つ（5〜10分）

ログが流れます：

```
🚀 Preparing system...
🚀 Preparing environment...
🚀 Installing dependencies...
   - streamlit
   - pandas
   - plotly
   - reportlab
   - kaleido==0.2.1
🚀 Running your app...
```

✅ **「Your app is live!」** と表示されたら完了！

---

### ステップ12: URLを確認してアクセス（1分）

あなたのアプリのURL:

```
https://あなたのユーザー名-hospital-dashboard-app-xxxxxxxx.streamlit.app
```

#### 動作確認

- [ ] ダッシュボードが表示される
- [ ] プルダウンで病院を選択できる
- [ ] グラフが正しく表示される
- [ ] PDF出力ボタンが機能する
- [ ] スマホからもアクセスできる

🎉 **おめでとうございます！Web公開完了です！**

---

## 🎉 完了後のアクション

### 1. GitHubのREADME.mdにアプリリンクを追加

#### 方法A: GitHub Web上で編集

1. https://github.com/あなたのユーザー名/hospital-dashboard を開く
2. `README.md` をクリック
3. 右上の **✏️（鉛筆マーク）** をクリック
4. 一番上に以下を追加：

```markdown
# 🏥 病院経営分析ダッシュボード

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://あなたのアプリ.streamlit.app)

**🚀 デモサイト:** [https://あなたのアプリ.streamlit.app](https://あなたのアプリ.streamlit.app)

---

（以下、既存の内容）
```

5. **Commit changes** をクリック

#### 方法B: Cursorで編集してPush

```bash
# README.mdを編集（Cursorで開いて、上記を追加）

# 変更をコミット
git add README.md
git commit -m "📝 Docs: Add live demo link to README"
git push
```

---

### 2. Xでシェアする

以下のツイートテンプレートをカスタマイズして投稿：

```
🚀 非エンジニアがCursor×Geminiで病院向けダッシュボードを開発＆公開しました！

✨ Streamlit + Plotly + Pandas
📊 購入推移・削減コスト可視化
📄 PDF出力機能
🎨 医療系の清潔感あるデザイン

👉 https://あなたのアプリ.streamlit.app
💻 GitHub: https://github.com/あなたのユーザー名/hospital-dashboard

#AI駆動開発 #Streamlit #Cursor #ノーコード #BizDev
```

---

### 3. プロフィールを更新

#### GitHubのプロフィール

- **Pinned repositories** で `hospital-dashboard` をピン留め
- **Website** にStreamlitアプリのURLを追加

#### Xのプロフィール

- **Website** にStreamlitアプリのURLを追加
- または、固定ツイートでシェア

---

### 4. ポートフォリオに追加

もしポートフォリオサイトを持っている場合：

```markdown
## プロジェクト

### 🏥 病院経営分析ダッシュボード

- **技術スタック:** Streamlit, Pandas, Plotly, Python
- **開発手法:** AI駆動開発（Cursor + Gemini）
- **デモ:** https://あなたのアプリ.streamlit.app
- **GitHub:** https://github.com/あなたのユーザー名/hospital-dashboard
- **特徴:**
  - インタラクティブなデータ可視化
  - PDF出力機能
  - レスポンシブデザイン
```

---

## ⚠️ トラブルシューティング

### 🔴 エラー: "git: command not found"

**原因:** Gitがインストールされていない

**解決方法:**

```bash
# Homebrewを使ってGitをインストール（Macの場合）
brew install git

# 確認
git --version
```

Windowsの場合: https://git-scm.com/download/win からインストール

---

### 🔴 エラー: "failed to push some refs"

**原因:** GitHubのリポジトリとローカルが同期していない

**解決方法:**

```bash
# GitHubの最新を取得してマージ
git pull origin main --allow-unrelated-histories

# 再度Push
git push -u origin main
```

---

### 🔴 エラー: "ModuleNotFoundError: No module named 'xxx'"（Streamlit Cloud）

**原因:** `requirements.txt` にパッケージが記載されていない

**解決方法:**

1. ローカルの `requirements.txt` を確認
2. 不足しているパッケージを追加：
   ```
   missing-package-name==1.2.3
   ```
3. GitHubにPush:
   ```bash
   git add requirements.txt
   git commit -m "🐛 Fix: Add missing package to requirements"
   git push
   ```
4. Streamlit Cloudが自動で再デプロイ

---

### 🔴 Streamlit Cloudのデプロイが遅い・止まる

**解決方法:**

1. Streamlit Cloudのダッシュボードで **「Logs」** を確認
2. エラーメッセージを読む
3. 右上の **「⋮」** → **「Reboot app」** をクリック

---

### 🔴 "Permission denied (publickey)"

**原因:** SSH認証が設定されていない

**解決方法:** HTTPSを使う

```bash
# リモートURLをHTTPSに変更
git remote set-url origin https://github.com/あなたのユーザー名/hospital-dashboard.git

# 再度Push
git push -u origin main
```

---

### 🔴 大きなファイル（100MB以上）がPushできない

**原因:** GitHubは100MB以上のファイルを受け付けない

**解決方法:**

1. `.gitignore` に大きなファイルを追加
2. すでにコミット済みの場合:
   ```bash
   git rm --cached 大きなファイル名
   git commit -m "🔥 Remove large file"
   git push
   ```

---

### 🔴 APIキーが漏れた！

**緊急対応:**

1. **すぐにAPIキーを無効化**（OpenAIやGeminiの管理画面で）
2. **新しいAPIキーを生成**
3. **Streamlit CloudのSecretsに設定**
4. **GitHubのリポジトリから完全に削除**:
   ```bash
   # 履歴から完全削除（慎重に！）
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch .env" \
     --prune-empty --tag-name-filter cat -- --all
   
   # 強制Push
   git push origin --force --all
   ```

**予防:**
- `.gitignore` に `.env` を必ず追加
- コミット前に `git status` で確認

---

## 📚 用語集（初心者向け）

### Git関連

| 用語 | 意味（簡単に言うと） |
|------|----------------------|
| **Git** | ファイルの変更履歴を記録するツール（タイムマシン） |
| **GitHub** | Gitのデータを保存するクラウドサービス |
| **リポジトリ** | プロジェクトの保管場所（フォルダ） |
| **コミット** | 変更を記録すること（セーブポイント） |
| **Push** | ローカルの変更をGitHubにアップロード |
| **Pull** | GitHubの最新をローカルにダウンロード |
| **Clone** | GitHubのリポジトリを自分のPCにコピー |
| **ブランチ** | 平行世界（実験用のコピー） |
| **main** | メインのブランチ（昔は master） |
| **origin** | GitHub上のリポジトリの呼び名 |
| **.gitignore** | GitHubに上げないファイルのリスト |

### デプロイ関連

| 用語 | 意味（簡単に言うと） |
|------|----------------------|
| **デプロイ** | アプリをインターネット上に公開すること |
| **ホスティング** | アプリを動かすサーバーを提供するサービス |
| **環境変数** | アプリに渡す秘密情報（APIキーなど） |
| **CI/CD** | コードを更新したら自動でデプロイする仕組み |
| **URL** | アプリのWeb上の住所 |
| **ドメイン** | Webサイトの名前（例: google.com） |
| **SSL/TLS** | 通信を暗号化する仕組み（https:// の部分） |
| **レスポンシブ** | スマホでも見やすいデザイン |

### 開発関連

| 用語 | 意味（簡単に言うと） |
|------|----------------------|
| **AI駆動開発** | AIにコードを書いてもらう開発手法 |
| **Streamlit** | PythonでWebアプリを作るフレームワーク |
| **Pandas** | データ分析のPythonライブラリ |
| **Plotly** | インタラクティブなグラフを描くライブラリ |
| **requirements.txt** | 必要なPythonパッケージのリスト |
| **ライブラリ** | 便利な機能をまとめたコードの集まり |
| **フレームワーク** | アプリ開発の土台（家で言う設計図） |

---

## 🎓 次のステップ（さらにレベルアップ）

### 1. 新機能を追加する

#### アイデア集

- [ ] **データベース連携**（PostgreSQL, Supabase）
- [ ] **Google Sheets連携**（リアルタイムデータ更新）
- [ ] **認証機能**（パスワードログイン）
- [ ] **ユーザー管理**（病院ごとにアカウント）
- [ ] **通知機能**（購入額減少時にメール送信）
- [ ] **ダッシュボード複数ページ**（タブで切り替え）
- [ ] **データエクスポート**（Excel, CSV出力）
- [ ] **AIチャットボット**（Gemini統合）

#### 開発の流れ

1. ローカルで新機能を開発
2. 動作確認
3. GitHubにPush
4. 自動でStreamlit Cloudに反映

---

### 2. カスタムドメインを取得

**無料の方法:**

- **GitHub Pages** で静的サイトを公開（Streamlitは不可）
- **Vercel** でNext.jsやReactアプリを公開

**有料の方法（推奨）:**

1. **お名前.com** や **Google Domains** でドメイン取得（年間1,000円〜）
2. Streamlit Cloudの有料プラン（$10/month）にアップグレード
3. カスタムドメインを設定
   - 例: `https://dashboard.your-domain.com`

---

### 3. 他のプロジェクトも公開

#### プロジェクトアイデア

- **営業ダッシュボード**（売上推移、KPI管理）
- **在庫管理システム**（発注アラート）
- **顧客管理CRM**（問い合わせ履歴）
- **データ分析レポート自動生成**
- **Webスクレイピング＋分析**
- **チャットボット**（Gemini API）

---

### 4. コミュニティに参加

#### Streamlit Community

- **Forum:** https://discuss.streamlit.io
- **Discord:** https://discord.gg/streamlit
- **Gallery:** https://streamlit.io/gallery

#### GitHub

- **スター**を他のプロジェクトに付ける
- **Issue**を報告する
- **Pull Request**を送る（コントリビュート）

#### X（Twitter）

- **#Streamlit** タグで検索
- **#AI駆動開発** タグで発信
- **#100DaysOfCode** チャレンジに参加

---

## 🏆 あなたの成果

このガイドを完了したあなたは：

- ✅ **GitHubの使い方**をマスターした
- ✅ **Gitの基本**（commit, push）を理解した
- ✅ **秘密情報の管理**（.gitignore, 環境変数）ができる
- ✅ **Streamlit Cloudでデプロイ**できる
- ✅ **CI/CD**（自動デプロイ）を体験した
- ✅ **世界中からアクセスできるWebアプリ**を公開した
- ✅ **ポートフォリオ**に追加できる成果物ができた

---

## 🎊 おめでとうございます！

あなたは今、**AI駆動開発者**として、立派な成果物を世界に公開しました。

**非エンジニアでも、ここまでできる。**

これは始まりに過ぎません。次は何を作りますか？

---

<div align="center">

## 📣 シェアしましょう！

**Xでシェアしてください：**

```
🚀 非エンジニアがCursor×Geminiで病院向けダッシュボードを開発＆公開しました！

✨ Streamlit + Plotly
📊 購入推移・削減コスト可視化
📄 PDF出力機能

👉 https://あなたのアプリ.streamlit.app

#AI駆動開発 #Streamlit #Cursor #ノーコード
```

---

**Made with ❤️ and 🤖 AI**

**開発者:** にくまる（AI駆動BizDev）

</div>

