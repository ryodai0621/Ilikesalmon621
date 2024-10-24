import streamlit as st
import math

st.title("重力加速度計算アプリ")

st.write("このアプリは、単振り子の長さと周期から重力加速度を計算します。")

## 入力セクション
st.header("入力")

time = st.slider("周期（秒）", min_value=0.1, step=0.001, value=3.0)
long = st.slider("単振り子の長さ（メートル）", min_value=0.1, step=0.001, value=10.0)

## 計算セクション
if st.button("計算"):
    try:
        gravity = (4*3.14159265358979323846264338 * long) / (time ** 2)
        st.success(f"計算された重力加速度: {gravity:.2f} m/s²")
        
        ## 理論値との比較
        theoretical_g = 9.8
        error = abs(gravity - theoretical_g) / theoretical_g * 100
        
        st.write(f"理論値（9.8 m/s²）との誤差: {error:.2f}%")
        
        ## 考察
        st.header("考察")
        if error < 5:
            st.write("計算結果は理論値に非常に近いです。測定が正確に行われたと考えられます。")
        elif error < 10:
            st.write("計算結果は理論値とやや異なります。測定誤差や空気抵抗の影響が考えられます。")
        else:
            st.write("計算結果は理論値と大きく異なります。測定方法を見直すか、他の要因（風や摩擦など）を考慮する必要があるかもしれません。")

    except ZeroDivisionError:
        st.error("エラー: 落下時間は0にできません。")
    except Exception as e:
        st.error(f"エラーが発生しました: {e}")

## 注意事項
st.header("注意事項")
st.write("- このアプリケーションは、空気抵抗を無視した理想的な状況を想定しています。")
st.write("- 実際の測定では、様々な要因により誤差が生じる可能性があります。")
st.write("- 正確な結果を得るためには、複数回の測定を行い、平均値を使用することをお勧めします。")


