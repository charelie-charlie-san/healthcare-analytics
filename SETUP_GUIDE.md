# 🚀 今日中にWeb公開！完全ガイド

## ⚠️ 最重要：秘密の守り方

### APIキーは絶対に公開しない！

このプロジェクトでは現在APIキーは使っていないようですが、今後のために覚えておきましょう：

1. **絶対にGitHubに上げてはいけないもの**
   - `.env` ファイル（APIキーが書かれたファイル）
   - `config.py`（パスワードやトークンが書かれたファイル）
   - `secrets.toml`（Streamlitの秘密情報）

2. **守り方**
   - `.gitignore` というファイルで除外設定をする（次のステップで作成します）

---

## 📝 ターミナルコマンド（方法A/Bが使えない場合のみ）

### Git初期設定（一度だけ実行）

```bash
# あなたの名前を登録
git config --global user.name "にくまる"

# GitHubのメールアドレスを登録
git config --global user.email "your-github-email@example.com"
```

### GitHub認証（Personal Access Token方式）

1. GitHubにログイン
2. 右上のプロフィール画像 → **Settings**
3. 左メニュー一番下の **Developer settings**
4. **Personal access tokens** → **Tokens (classic)**
5. **Generate new token (classic)**
6. 設定：
   - Note: `Cursor from Mac`
   - Expiration: `90 days`（3ヶ月）
   - Scope: ✅ `repo` にチェック
7. **Generate token** → 生成されたトークンをコピー（二度と表示されないので注意！）
8. 安全な場所にメモしておく（パスワードマネージャー推奨）

このトークンは、後でGitHubにPushする時にパスワード代わりに使います。

---

## 🔐 SSH方式（より安全・上級者向け）

ターミナルで以下を実行：

```bash
# SSH鍵を生成
ssh-keygen -t ed25519 -C "your-github-email@example.com"

# Enterを3回押す（パスフレーズは空でOK）

# 公開鍵の内容を表示
cat ~/.ssh/id_ed25519.pub
```

表示された文字列（`ssh-ed25519 AAAA...`で始まる長い文字列）をコピーして：

1. GitHub → Settings → SSH and GPG keys
2. **New SSH key**
3. Title: `Cursor Mac`
4. Key: さっきコピーした文字列を貼り付け
5. **Add SSH key**

これで完了！次回からパスワード不要でPushできます。

