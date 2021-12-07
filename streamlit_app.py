import os

import numpy as np
import openai
import pandas as pd
import streamlit as st

openai.api_key = os.getenv("OPENAI_API_KEY")

with open("./input/main_body_prompt.txt", mode="r") as f:
    default_main_body_prompt = f.read()

with open("./input/title_prompt.txt", mode="r") as f:
    default_title_prompt = f.read()

default_params_dic = {
    "タイトル": {
        "prompt": default_title_prompt,
        "temperature": [0.0, 1.0, 0.3],
        "max_tokens": [16, 128, 96],
        "top_p": [0.0, 1.0, 1.0],
        "frequency_penalty": [0.0, 2.0, 0.5],
        "presence_penalty": [0.0, 2.0, 0.0],
    },
    "本文": {
        "prompt": default_main_body_prompt,
        "temperature": [0.0, 1.0, 0.3],
        "max_tokens": [16, 512, 256],
        "top_p": [0.0, 1.0, 1.0],
        "frequency_penalty": [0.0, 2.0, 0.5],
        "presence_penalty": [0.0, 2.0, 0.0],
    },
}

st.title("ブログネタだし君", anchor=None)

right_col, left_col = st.columns([2, 1])
with right_col:
    task_type = st.radio(
        "生成したいコンテンツの種類を選択してください",
        ["タイトル", "本文"],
        index=0,
        on_change=None,
    )

    prompt = st.text_area(
        "プロンプトを入力してください",
        key="prompt",
        value=default_params_dic[task_type]["prompt"],
        height=300,
    )

with left_col:
    param_val_dic = {}
    for param in [
        "temperature",
        "max_tokens",
        "top_p",
        "frequency_penalty",
        "presence_penalty",
    ]:
        param_val_dic[param] = st.slider(param, *default_params_dic[task_type][param])

    clicked = st.button("アイディアを授かる")

if clicked:
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt=prompt,
        **param_val_dic,
    )

    st.header(f"ブログネタだし君が生成した{task_type}は↓")
    st.code(response["choices"][0]["text"], language="txt")
