import streamlit as st

st.title("👋🏻 연수 실습 페이지")
st.subheader("이 페이지는 영준쌤이 만들었습니다.")
st.info("10월 23일 수요일에 연수를 들으며 만들고 있습니다. 혼자 열심히 해보다가 놓치지 않아보려고 합니다. giphy에서 gif파일을 가져왔고, video를 이용해서 유튜브를 임베딩하고 있습니다.")
st.link_button("영준쌤의 과학", "https://www.notion.so/yngjn0/92e1ac1c012040989ac07efae302c53b")

st.success("초록색 창")
st.error("빨간색 창")
st.info("파란색 창")
st.warning("노란색 창") # ctrl+/ : 주석처리
st.image("https://media.giphy.com/media/lGHFhGuIUX6tW/giphy.gif?cid=ecf05e47nxamoc2hpphvhgqo4tcqqy8hbcvzhntmc7jbs9y0&ep=v1_gifs_search&rid=giphy.gif&ct=g","funny free kick") 
st.video("https://youtu.be/xdJ3RP92UlU?si=KOPc4H6QA8MjzJT3")
st.image("data/예비군 교육훈련 소집통지서(김영준).jpg")