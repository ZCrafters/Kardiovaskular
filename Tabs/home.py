import streamlit as st

def app():

    st.title("Prediksi Penyakit Kardiovaskular")

    st.image("images/home.jpg")

    st.markdown(
        """<p style="font-size:20px;">
            Penyakit kardiovaskular (CVD) merupakan salah satu penyebab utama kematian di seluruh dunia. Faktor risiko penyakit kardiovaskular dapat mencakup berbagai aspek seperti gaya hidup, faktor genetik, kondisi medis yang ada, dan faktor lingkungan. Mengidentifikasi dan memahami faktor-faktor risiko ini sangat penting untuk pencegahan, pengelolaan, dan perawatan penyakit kardiovaskular.
            Penyakit kardiovaskular ini seringkali sulit untuk dideteksi karena dipengaruhi oleh banyak faktor risiko yang kompleks, seperti tekanan darah tinggi, ketidakseimbangan kadar kolesterol, pola denyut nadi yang tidak normal, serta gaya hidup seperti konsumsi alkohol dan merokok berlebihan. Oleh karena itu, penting untuk membuat keputusan yang tepat dan memberikan pengobatan yang optimal dalam menangani risiko penyakit jantung ini.
        </p>
        """, unsafe_allow_html=True)

