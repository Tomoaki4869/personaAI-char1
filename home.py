import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AIペルソナ</title>
</head>
<body>
<div class="header">
    <div class="title">
        <h2>AIペルソナ</h2>
    </div>

    <div class="link">
        <a href="https://personaai-gdm.streamlit.app/" target="_blank">妊娠糖尿病</a><a>　いのち 花子 さん</a><br>
        <a>https://personaai-gdm.streamlit.app/</a><br><br>
        <a href="https://personaai-t1d.streamlit.app/" target="_blank">1型糖尿病</a><a>　川上 想太朗 さん</a><br>
        <a>https://personaai-t1d.streamlit.app/</a><br><br>
        <a href="https://personaai-t2d.streamlit.app/" target="_blank">2型糖尿病</a><a>高橋 健一 さん</a><br>
        <a>https://personaai-t2d.streamlit.app/</a><br><br>
        <a href="https://personaai-pret2d.streamlit.app/" target="_blank">2型糖尿病 予備軍</a><a>　田中 健一 さん</a><br>
        <a>https://personaai-pret2d.streamlit.app/</a><br><br>
    </div>
</body>
</html>
"""

# StreamlitでHTMLを埋め込み
components.html(html_code, height=1200, scrolling=True)








