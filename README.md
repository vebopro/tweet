# Twitter 感情分析アプリ

指定したTwitterアカウントの最新ツイートを取得し、ポジティブ・ネガティブの割合を可視化するアプリです。

## 🔧 使用方法

1. 必要ライブラリをインストール:

```
pip install -r requirements.txt
```

2. アプリを起動:

```
streamlit run streamlit_app.py
```

3. ブラウザで `http://localhost:8501` にアクセス

## ✅ 使用技術
- Streamlit
- Hugging Face Transformers（日本語感情分析モデル）
- snscrape（ツイート取得）

## 💡 注意
- Twitterアカウントは公開されている必要があります。
- `snscrape` は非公式のスクレイピングライブラリです。
