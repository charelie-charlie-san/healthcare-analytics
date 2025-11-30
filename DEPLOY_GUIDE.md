# 🚀 Streamlit Cloudでアプリを世界公開する完全ガイド

## 🌟 Streamlit Community Cloudとは？

- **完全無料**のホスティングサービス
- **Streamlitアプリ専用**（最適化されている）
- **GitHubと自動連携**（コードを更新したら自動でサイトも更新される！）
- **独自URL**が貰える（`https://あなたのアプリ名.streamlit.app`）

---

## 📋 必要なもの（チェックリスト）

- ✅ GitHubアカウント
- ✅ GitHubにアップロードされたプロジェクト（`hospital-dashboard`）
- ✅ Googleアカウント（Streamlit Cloudへのログインに使用）

---

## 🚀 デプロイ手順（所要時間：10分）

### ステップ1: Streamlit Cloudにログイン

1. ブラウザで https://share.streamlit.io を開く
2. **「Sign up」** または **「Continue with GitHub」** をクリック
3. GitHubアカウントで認証
   - 「Authorize Streamlit」をクリック
   - GitHubのパスワードを入力
4. メールアドレスを確認（GitHubのメールアドレスが自動入力される）
5. **「Continue」** をクリック

### ステップ2: アプリをデプロイ

1. ダッシュボードで **「New app」** ボタンをクリック
2. 以下の情報を入力：

| 項目 | 入力内容 |
|------|----------|
| **Repository** | `あなたのユーザー名/hospital-dashboard` |
| **Branch** | `main` |
| **Main file path** | `app.py` |

3. **「Advanced settings」** をクリック（環境変数を使う場合のみ）
   - 今回は環境変数不要なので、スキップしてOK
   - Python versionは **3.9** または **3.10** を推奨

4. **「Deploy!」** ボタンをクリック

### ステップ3: デプロイ完了を待つ

1. デプロイが開始されます（初回は5〜10分かかります）
2. ログが流れます：
   ```
   Preparing system...
   Preparing environment...
   Installing dependencies...
   Running your app...
   ```
3. ✅ **「Your app is live!」** と表示されたら完了！

### ステップ4: URLを確認

あなたのアプリのURLは：

```
https://あなたのユーザー名-hospital-dashboard-app-xxxxxxxx.streamlit.app
```

このURLを：
- ✅ Xのプロフィール（リンク）に追加
- ✅ GitHubのREADME.mdに追加
- ✅ 名刺やポートフォリオに追加

🎉 **おめでとうございます！あなたのアプリが世界中からアクセスできるようになりました！**

---

## 🔧 環境変数の設定（APIキーを使う場合）

### なぜ環境変数が必要？

もしアプリで **OpenAI API** や **Gemini API** などを使う場合、APIキーをコードに直接書くと**危険**です。  
環境変数を使うことで、秘密情報を安全に管理できます。

### 設定方法

#### ステップ1: Streamlit Cloudの設定画面

1. あなたのアプリのダッシュボードを開く
2. 右下の **⚙️（Settings）** をクリック
3. 左メニューの **「Secrets」** をクリック

#### ステップ2: Secrets（秘密情報）を追加

以下のような形式で入力：

```toml
# OpenAI API の例
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"

# Gemini API の例
GOOGLE_API_KEY = "AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxx"

# データベース接続情報の例
[database]
host = "db.example.com"
user = "admin"
password = "super_secret_password"
```

#### ステップ3: Pythonコードで使用

```python
import streamlit as st

# Streamlit Secretsから取得
api_key = st.secrets["OPENAI_API_KEY"]

# または、辞書形式で
db_host = st.secrets["database"]["host"]
```

#### ステップ4: ローカル開発用

ローカル（自分のPC）でも同じように動かすために：

1. プロジェクトフォルダに `.streamlit` フォルダを作成
2. その中に `secrets.toml` ファイルを作成
3. 同じ内容を記述：

```toml
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxx"
GOOGLE_API_KEY = "AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

⚠️ **重要:** `.gitignore` に `secrets.toml` が含まれていることを確認！（すでに含まれています）

---

## 🔄 コードを更新したら自動デプロイ

Streamlit Cloudの最大の魅力は**自動デプロイ**！

### 流れ

1. ローカルでコードを編集（例: グラフの色を変更）
2. Cursorから GitHubにPush
3. **自動的に** Streamlit CloudがGitHubの変更を検知
4. **自動的に** 再デプロイが始まる
5. 数分後、アプリが更新される

### 再デプロイを確認

1. Streamlit Cloudのダッシュボードを開く
2. アプリのステータスが **「Rerunning...」** になる
3. 完了したら **「Running」** に戻る

🎉 手動で何もする必要なし！GitHubにPushするだけでOK！

---

## 📊 アプリの管理（メニュー）

Streamlit Cloudのダッシュボードでできること：

### 📈 Analytics（分析）

- **訪問者数**の確認
- **使用量**（リソース使用状況）
- **エラーログ**

### ⚙️ Settings（設定）

- **App settings**: アプリ名、URL、Pythonバージョン
- **Secrets**: 環境変数（APIキーなど）
- **Resources**: メモリ、CPU割り当て（無料プランは固定）
- **Reboot**: アプリを再起動

### 🔗 Share（共有）

- **Public link**: アプリのURL
- **Embed**: iframeでWebサイトに埋め込む

### 🗑️ Delete app（削除）

- アプリを完全に削除（慎重に！）

---

## 🎨 カスタムドメインを設定（オプション）

無料プランでは独自ドメイン（例: `dashboard.your-domain.com`）は使えませんが、Streamlit Cloudの有料プラン（$10/month）で設定可能です。

### 設定方法（有料プランの場合）

1. 自分のドメインのDNS設定で、CNAMEレコードを追加：
   ```
   CNAME: dashboard → あなたのアプリ.streamlit.app
   ```
2. Streamlit Cloudの Settings → Custom domain で設定

---

## ⚠️ トラブルシューティング

### エラー: "ModuleNotFoundError: No module named 'xxx'"

**原因:** `requirements.txt` にパッケージが記載されていない

**解決方法:**

1. ローカルの `requirements.txt` に追加：
   ```
   missing-package-name==1.2.3
   ```
2. GitHubにPush
3. 自動で再デプロイされる

### エラー: "App is in unhealthy state"

**原因:** アプリがクラッシュしている

**解決方法:**

1. Streamlit Cloudのダッシュボードで **「Logs」** を確認
2. エラーメッセージを読む
3. コードを修正してGitHubにPush

### デプロイが遅い・止まる

**原因:** 大きなファイルを含んでいる、または依存パッケージが多い

**解決方法:**

1. `.gitignore` で不要なファイルを除外
2. `requirements.txt` を見直す（本当に必要なパッケージだけ）
3. ダッシュボードで **「Reboot app」** を試す

### "App wakes up from sleep"

**原因:** 無料プランでは、アプリが使われないと自動でスリープする

**解決方法:**

- 初回アクセス時に「起動中...」と表示されるが、数秒で起動
- 有料プランにアップグレードすると、24時間稼働

---

## 💡 ベストプラクティス

### 1. README.mdにバッジを追加

GitHubのREADME.mdに、アプリへのリンクバッジを追加：

```markdown
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://あなたのアプリ.streamlit.app)
```

表示例：

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

### 2. OGP画像を設定

Xでシェアした時に表示される画像を設定：

```python
st.set_page_config(
    page_title="病院経営分析ダッシュボード",
    page_icon="🏥",
    menu_items={
        'Get Help': 'https://github.com/あなたのユーザー名/hospital-dashboard',
        'Report a bug': "https://github.com/あなたのユーザー名/hospital-dashboard/issues",
        'About': "# 病院経営分析ダッシュボード\nAI駆動開発プロジェクト"
    }
)
```

### 3. ローディング時のメッセージ

データ読み込みが遅い場合、スピナーを表示：

```python
import streamlit as st

with st.spinner('データを読み込んでいます...'):
    df = pd.read_csv('data.csv')
    # 処理...
```

### 4. キャッシュを活用

同じデータを何度も読み込まないように：

```python
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')

df = load_data()  # 初回のみ読み込み、2回目以降はキャッシュから
```

---

## 📱 モバイル対応

Streamlitアプリは自動的にレスポンシブデザインになりますが、さらに改善するには：

```python
# 列の幅を調整
col1, col2 = st.columns([2, 1])  # 2:1の比率

# モバイルで見やすいフォントサイズ
st.markdown("""
<style>
    @media (max-width: 768px) {
        h1 {
            font-size: 24px !important;
        }
        .metric-card {
            padding: 16px !important;
        }
    }
</style>
""", unsafe_allow_html=True)
```

---

## 🎓 用語解説（デプロイ編）

| 用語 | 意味（簡単に言うと） |
|------|----------------------|
| **デプロイ** | アプリをインターネット上に公開すること |
| **ホスティング** | アプリを動かすサーバーを提供するサービス |
| **環境変数** | アプリに渡す秘密情報（APIキーなど） |
| **Secrets** | Streamlit Cloudでの環境変数の呼び方 |
| **CI/CD** | コードを更新したら自動でデプロイする仕組み |
| **URL** | アプリのWeb上の住所 |
| **ドメイン** | Webサイトの名前（例: google.com） |
| **OGP** | XやFacebookでシェアした時の表示情報 |
| **スリープ** | アプリが使われないと自動で停止すること（無料プラン） |

---

## 🎉 完了チェックリスト

デプロイが成功したら、以下を確認：

- [ ] アプリのURLにアクセスして動作確認
- [ ] スマホからもアクセスできるか確認
- [ ] データが正しく表示されているか
- [ ] グラフが動作するか
- [ ] PDF出力機能が動くか
- [ ] GitHubのREADME.mdにアプリリンクを追加
- [ ] Xのプロフィールにリンクを追加
- [ ] 友人や同僚にシェア！

---

## 🚀 次のステップ（さらにレベルアップ）

### 1. カスタムドメインを取得

- **お名前.com** や **Google Domains** でドメイン取得
- Streamlit Cloudの有料プラン（$10/month）にアップグレード
- カスタムドメインを設定

### 2. データをリアルタイム更新

- **Google Sheets** と連携
- **データベース**（PostgreSQL, MySQL）と連携
- **API** からデータを取得

### 3. 認証機能を追加

```python
# パスワード認証の簡単な例
password = st.text_input("パスワードを入力", type="password")

if password == "your_secret_password":
    st.success("ログイン成功！")
    # アプリの内容を表示
else:
    st.warning("パスワードを入力してください")
    st.stop()
```

または、**streamlit-authenticator** パッケージを使用。

### 4. アナリティクスを追加

- **Google Analytics** のトラッキングコードを埋め込む
- **Plausible Analytics**（プライバシー重視）を使う

```python
# Google Analytics の例
st.markdown("""
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
""", unsafe_allow_html=True)
```

---

<div align="center">

## 🎊 デプロイ完了おめでとうございます！

あなたは今、**AI駆動開発者**として立派な成果物を世界に公開しました。

**Xでシェアしましょう！**

```
🚀 非エンジニアがCursor×Geminiで病院向けダッシュボードを開発＆公開しました！

✨ Streamlit + Plotly
📊 購入推移・削減コスト可視化
📄 PDF出力機能

👉 https://あなたのアプリ.streamlit.app

#AI駆動開発 #Streamlit #Cursor #ノーコード
```

</div>

