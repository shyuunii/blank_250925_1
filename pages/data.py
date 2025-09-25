import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
# 한글 폰트 설정
font_path = './fonts/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())
plt.rcParams['axes.unicode_minus'] = False

import streamlit as st
import pandas as pd
import numpy as np

st.title('간단한 데이터 시각화')


# 샘플 데이터 생성
df = pd.DataFrame({
	'날짜': pd.date_range('2023-01-01', periods=20),
	'값1': np.random.randn(20).cumsum(),
	'값2': np.random.rand(20) * 100
})

st.subheader('데이터 미리보기')
st.dataframe(df)


# 라인 차트 (matplotlib 사용, 한글 폰트 적용)
st.subheader('라인 차트')
fig, ax = plt.subplots()
df.set_index('날짜')[['값1', '값2']].plot(ax=ax)
ax.set_title('값1과 값2의 변화', fontproperties=fontprop)
ax.set_ylabel('값', fontproperties=fontprop)
ax.set_xlabel('날짜', fontproperties=fontprop)
st.pyplot(fig)

# 바 차트 (matplotlib 사용, 한글 폰트 적용)
st.subheader('바 차트')
fig2, ax2 = plt.subplots()
df.set_index('날짜')['값2'].plot(kind='bar', ax=ax2)
ax2.set_title('값2의 바 차트', fontproperties=fontprop)
ax2.set_ylabel('값2', fontproperties=fontprop)
ax2.set_xlabel('날짜', fontproperties=fontprop)
st.pyplot(fig2)
