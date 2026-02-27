import streamlit as st

st.set_page_config(page_title="Guida Aver Cura GCA", layout="wide")

# Menu Laterale
st.sidebar.title("Navigazione Guide")
fase = st.sidebar.radio("Scegli un'area:", ["Home", "1. OSSERVARE", "2. STIMOLARE", "Quick Links"])

if fase == "Home":
    st.title("Benvenuti nella Guida Interattiva GCA")
    st.write("Uno strumento di supporto basato sui volumi 'Aver Cura'.")
    st.image("https://via.placeholder.com/800x400.png?text=Benvenuti+Caregiver") # Qui potrai mettere un'immagine vera

elif fase == "1. OSSERVARE":
    st.header("Area 01: Osservare i segni")
    st.subheader("Checklist Giornaliera")
    st.checkbox("Apre gli occhi spontaneamente?")
    st.checkbox("Segue con lo sguardo un oggetto?")
    st.info("Suggerimento dal Vol. 1: Annota questi segni nel Diario di Bordo.")

elif fase == "2. STIMOLARE":
    st.header("Area 02: Stimolare il recupero")
    st.subheader("La Scala LCF")
    st.write("Identifica il livello di risposta per agire correttamente.")
    # Esempio di interattività
    lcf = st.slider("Seleziona il livello LCF (1-8)", 1, 8, 1)
    st.write(f"Al livello {lcf}, il consiglio è: riduci i rumori e parla con calma.")

elif fase == "Quick Links":
    st.header("Azioni Rapide")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Emergenza: Crisi Epilettica"):
            st.error("Cosa fare: Metti la persona su un fianco. Non forzare la bocca.")
    with col2:
        if st.button("Preparare la Stanza"):
            st.success("Cosa fare: Luce naturale, foto di famiglia, silenzio.")
