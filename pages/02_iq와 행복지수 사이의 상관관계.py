import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 설정
st.set_page_config(page_title="IQ와 행복지수의 상관관계 (대규모)", layout="wide")
st.title("🧠 IQ와 😊 행복지수의 상관관계")
st.write("500명의 가상 데이터를 통해 IQ와 행복지수 간의 관계를 시각화합니다.")

# 가상 데이터 생성
np.random.seed(42)
n = 500
iqs = np.clip(np.random.normal(loc=105, scale=15, size=n), 85, 160)  # IQ 정규분포
noise = np.random.normal(0, 0.6, size=n)
happiness = np.clip(0.03 * iqs + 4 + noise, 0, 10)  # IQ와 약한 양의 상관관계 포함

df = pd.DataFrame({
    "사람번호": [f"사람{i+1}" for i in range(n)],
    "IQ": iqs,
    "행복지수": happiness
})

# 상관계수 계산
correlation = df["IQ"].corr(df["행복지수"])

# 산점도 시각화
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(df["IQ"], df["행복지수"], alpha=0.6, s=15, color="cornflowerblue", edgecolors="k", linewidths=0.3)
ax.set_xlabel("IQ")
ax.set_ylabel("행복지수 (0 ~ 10)")
ax.set_title("IQ vs 행복지수 (500명 가상 데이터)")
ax.set_xlim(80, 165)
ax.set_ylim(0, 10)

# 회귀선 추가 (선형 추세선)
m, b = np.polyfit(df["IQ"], df["행복지수"], 1)
ax.plot(df["IQ"], m * df["IQ"] + b, color="red", linewidth=2, label="추세선")
ax.legend()

# Streamlit 출력
st.pyplot(fig)
st.markdown(f"📈 **상관계수 (Pearson r)**: `{correlation:.2f}`")

# 해석
if correlation > 0.5:
    st.success("꽤 강한 양의 상관관계가 보입니다!")
elif correlation > 0.2:
    st.info("약한 양의 상관관계가 있습니다.")
else:
    st.warning("상관관계가 거의 없거나 미미합니다.")
