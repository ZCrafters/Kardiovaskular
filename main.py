import streamlit as st 
from Tabs import about, home, data, predict, visualise
from Tabs.web_functions import load_data

st.set_page_config(
    page_title='Kardiovaskular Disease Prediction',
    page_icon='heart',
    layout='wide',
    initial_sidebar_state='auto'
)

Tabs = {
    "About": about,
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    "Visualisation": visualise
}

st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", list(Tabs.keys()))

kentang, X_pred, X_vis, y = load_data()

if page == "Prediction":
    Tabs[page].app(kentang, X_pred, y)
elif page == "Visualisation":
    Tabs[page].app(kentang, X_vis, y)
elif page == "Data Info":
    Tabs[page].app(kentang)
else:
    Tabs[page].app()
