# ブログネタだし君

ブログネタだし君はブログのタイトルと本文を生成してくれるWebアプリです。  "プロンプト"と呼ばれるお題と例示を与えると、その情報から何を答えるべきかを理解して、回答してくれます。　　

紹介blog: https://zerebom.hatenablog.com/entry/2021/12/07/082607

## Installation

1. [OpenAI API](https://openai.com/api/)にユーザ登録する
2. API keyを取得する
3. API keyを環境変数にセットする
4. このレポジトリをDLしてローカルホストで立ち上げる

```bash
git clone git@github.com:zerebom/blog-generator-app.git
cd blog-generator-app
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py

```

## Demo
https://user-images.githubusercontent.com/38466611/144997939-4876bdbe-af19-46db-b1c7-0f09b9441693.mov

