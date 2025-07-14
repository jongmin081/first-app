import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="IQ와 행복지수의 상관관계 (개인)", layout="centered")

st.title("🧠 개인 IQ와 😊 행복지수의 상관관계")
st.write("IQ가 높을수록 더 행복할까요? 20명의 가상 데이터를 통해 살펴봅시다.")

# 가상의 사람 데이터 생성 (고정된 시드로 랜덤)
random.seed(42)
names = [f"사람{i+1}" for i in range(20)]
iqs = [random.randint(85, 155) for _ in range(20)]
happiness = [round(random.uniform(4.5, 8.5) + 0.015 * (iq - 100), 2) for iq in iqs]  # 약한 양의 상관관계 포함

df = pd.DataFrame({
    "이름": names,
    "IQ": iqs,
    "행복지수": happiness
})

# 상관계수 계산
correlation = df["IQ"].corr(df["행복지수"])

# 산점도 시각화
fig, ax = plt.subplots()
ax.scatter(df["IQ"], df["행복지수"], color="skyblue", edgecolors="black")

# 이름 레이블 추가
for i, row in df.iterrows():
    ax.text(row["IQ"] + 0.3, row["행복지수"], row["이름"], fontsize=8)

ax.set_title("IQ vs 행복지수 (개인별)")
ax.set_xlabel("IQ")
ax.set_ylabel("행복지수 (0 ~ 10)")
ax.set_xlim(80, 160)
ax.set_ylim(4, 10)

st.pyplot(fig)

# 상관계수 출력
st.markdown(f"📈 **상관계수**: `{correlation:.2f}`")
if correlation > 0.5:
    st.success("꽤 강한 양의 상관관계가 보입니다!")
elif correlation > 0.2:
    st.info("약한 양의 상관관계가 있습니다.")
else:
    st.warning("상관관계가 거의 없거나 미미합니다.")
