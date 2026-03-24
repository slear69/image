import streamlit as st
# Заглавие
st.title("Галерия от любими животни")
# Списък със животни
if "animals" not in st.session_state:
  st.session_state.animals = []
# Добавяне
st.header("Добави ново животно")
name = st.text_input("Име на животното")
description = st.text_area ("Описание")
image_url = st.text_input("URL на картинка")
if st.button("Добави"):
  if name and description and image_url:
    st.session_state.animals.append({
"име": пате, "описание": description, "картинка": image_url
})
    st.success(f"{name} е добавено!")
else:
  st.warning("Попълнете всички полета!")
