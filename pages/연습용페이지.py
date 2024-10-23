import streamlit as st
st.set_page_config(page_title="연습용페이지(김영준)", page_icon="😁")

st.title("과학 퀴즈")

#객관식
option=st.radio("선생님의 이름은 무엇일까요?", ["김","영","준","김영준","김준영"])
if option=='김영준':
    st.success("정답!!")

else:
    st.error("실패!!")


#드롭박스
option=st.selectbox("선생님의 이름은 무엇일까요?", ["김","영","준","김영준","김준영"])

#드롭박스, 중복
option=st.multiselect("선생님의 이름은 무엇일까요?", ["김","영","준","김영준","김준영"])

agree = st.checkbox("동의하시나요?")

if agree:
    st.info("잘했어요!")
else:
    st.error("⏫체크해주세요!")

name= st.text_input("이름을 입력해주세요.")

if name:
    st.warning(f"{name}님이군요😎")
