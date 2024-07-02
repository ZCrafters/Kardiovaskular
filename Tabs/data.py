import streamlit as st

def app(kentang):
    st.title("Data Info Page")

    st.subheader("View Data")
    with st.expander("View data"):
        st.dataframe(kentang)

    st.subheader("Columns Description:")

    if st.checkbox("View Summary"):
        st.dataframe(kentang.describe())

    col_name, col_dtype, col_data = st.columns(3)

    with col_name:
        if st.checkbox("Column Names"):
            st.dataframe(kentang.columns)

    with col_dtype:
        if st.checkbox("Columns data types"):
            dtypes = kentang.dtypes.apply(lambda x: x.name)
            st.dataframe(dtypes)

    with col_data:
        if st.checkbox("Columns Data"):
            col = st.selectbox("Column Name", list(kentang.columns))
            st.dataframe(kentang[col])

    st.markdown("""
        <p style="font-size:24px">
            <a href="https://www.kaggle.com/datasets/thedevastator/exploring-risk-factors-for-cardiovascular-diseas/data" target=_blank style="text-decoration:none;">
                Get Dataset
            </a>
        </p>
    """, unsafe_allow_html=True)
