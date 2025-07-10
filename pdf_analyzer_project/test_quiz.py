import streamlit as st

st.title("🧠 Teszt Quiz Alkalmazás")

st.write("Ez egy egyszerű teszt alkalmazás.")

# Sidebar teszt
st.sidebar.header("Beállítások")
test_option = st.sidebar.selectbox("Válassz opciót:", ["Opció 1", "Opció 2", "Opció 3"])
test_slider = st.sidebar.slider("Kérdések száma", 1, 10, 5)

st.write(f"Kiválasztott opció: {test_option}")
st.write(f"Kérdések száma: {test_slider}")

# Gomb teszt
if st.button("🚀 Teszt Gomb"):
    st.success("A gomb működik!")

# Kérdés teszt
st.subheader("Teszt kérdés:")
question = "Mi Magyarország fővárosa?"
st.write(f"**{question}**")

col1, col2 = st.columns(2)
with col1:
    if st.button("A) Budapest"):
        st.success("✅ Helyes válasz!")
with col2:
    if st.button("B) Debrecen"):
        st.error("❌ Helytelen válasz!")

st.write("---")
st.write("Ha ezt látod, akkor a Streamlit működik!") 