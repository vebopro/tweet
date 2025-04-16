import streamlit as st
import snscrape.modules.twitter as sntwitter
from transformers import pipeline
import pandas as pd

# 感情分析モデルの読み込み
model = pipeline("sentiment-analysis", model="daigo/bert-base-japanese-sentiment")

st.title("X（Twitter）感情分析アプリ")
username = st.text_input("分析したいTwitterアカウントID（@は不要）", "")
limit = st.slider("取得するツイート数", 10, 100, 50)
analyze = st.button("感情分析する")

if analyze and username:
    with st.spinner("ツイート取得中..."):
        tweets = []
        for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
            if i >= limit:
                break
            tweets.append(tweet.content)

    if tweets:
        st.success(f"{len(tweets)} 件のツイートを取得しました！分析中...")

        results = model(tweets)
        df = pd.DataFrame(results)
        pos_rate = (df['label'] == 'ポジティブ').sum() / len(df) * 100
        neg_rate = (df['label'] == 'ネガティブ').sum() / len(df) * 100

        st.metric("ポジティブ率", f"{pos_rate:.1f}%")
        st.metric("ネガティブ率", f"{neg_rate:.1f}%")
    else:
        st.error("ツイートが取得できませんでした。非公開アカウントかも？")
