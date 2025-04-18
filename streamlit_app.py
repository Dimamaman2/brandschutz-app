import streamlit as st

st.title("Brandschutz Materialchecker")

# Выбор класса материала
material = st.selectbox("Выбери класс материала:", ["A1", "A2", "B", "B2", "E"])

# Выбор области применения
bereich = st.selectbox("Где ты хочешь использовать материал?", ["Wand", "Decke", "Boden", "Fassade"])

# Простой вывод решения
if material == "A1":
    st.success("Материал можно использовать без ограничений.")
elif material == "B2" and bereich in ["Wand", "Decke"]:
    st.error("Использование запрещено без дополнительной защиты.")
elif material == "B2" and bereich == "Boden":
    st.warning("Разрешено только в цоколе с защитными мерами.")
else:
    st.info("Требуется дополнительная проверка в соответствии с VKF-Richtlinie.")