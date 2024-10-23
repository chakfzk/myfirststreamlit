# import streamlit as st
# st.set_page_config(page_title="연습용페이지(김영준)", page_icon="😁")

# st.title("과학 퀴즈")

# #객관식
# option=st.radio("선생님의 이름은 무엇일까요?", ["김","영","준","김영준","김준영"])
# if option=='김영준':
#     st.success("정답!!")
# elif option=="김"
#     st.write("아닌데...")

# else:
#     st.error("실패!!")


# #드롭박스
# option=st.selectbox("선생님의 이름은 무엇일까요?", ["김","영","준","김영준","김준영"])

# #드롭박스, 중복
# option=st.multiselect("선생님의 이름은 무엇일까요?", ["김","영","준","김영준","김준영"])

# agree = st.checkbox("동의하시나요?")

# if agree:
#     st.info("잘했어요!")
# else:
#     st.error("⏫체크해주세요!")

# name= st.text_input("이름을 입력해주세요.")

# if name:
#     st.warning(f"{name}님이군요😎")


import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="연습용페이지(김영준)",
    page_icon="😁",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 타이틀 및 설명
st.title("과학 퀴즈")
st.subheader("김영준 선생님의 퀴즈 페이지에 오신 것을 환영합니다!")
st.markdown("---")  # 구분선

# 객관식 퀴즈
st.header("퀴즈 1: 객관식 문제")
option = st.radio("선생님의 이름은 무엇일까요?", ["김", "영", "준", "김영준", "김준영"])

if option == '김영준':
    st.success("정답!! 🎉")
elif option == "김":
    st.warning("힌트: 이름은 두 글자 이상이랍니다.")
else:
    st.error("실패!! 다시 시도해보세요.")

st.markdown("---")

# 드롭다운 선택
st.header("퀴즈 2: 드롭다운 문제")
dropdown_option = st.selectbox("선생님의 이름은 무엇일까요?", ["김", "영", "준", "김영준", "김준영"])

if dropdown_option == '김영준':
    st.success("정답!!")
else:
    st.error("다시 시도해보세요.")

st.markdown("---")

# 멀티셀렉트
st.header("퀴즈 3: 멀티셀렉트 문제")
multi_option = st.multiselect("선생님의 이름에 포함된 글자를 모두 선택하세요.", ["김", "영", "준", "김영준", "김준영"])

if set(multi_option) == {"김", "영", "준"}:
    st.success("정답!! 김영준 선생님의 이름은 '김', '영', '준'으로 이루어져 있습니다.")
else:
    st.error("실패!! 다시 시도해보세요.")

st.markdown("---")

# 체크박스
st.header("추가 동의")
agree = st.checkbox("동의하시나요?")

if agree:
    st.info("잘했어요! 😊")
else:
    st.error("체크해주세요! ⏫")

st.markdown("---")

# 이름 입력
st.header("사용자 이름 입력")
name = st.text_input("이름을 입력해주세요.")

if name:
    st.success(f"{name}님, 환영합니다! 😎")

st.markdown("---")

# 사이드바
st.sidebar.title("추가 기능")
st.sidebar.write("이 페이지는 연습용 퀴즈 페이지입니다.")
st.sidebar.button("퀴즈 리셋", on_click=lambda: st.experimental_rerun())
