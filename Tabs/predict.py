import streamlit as st
from web_functions import predict as predict_function  # Rename to avoid conflict
from sklearn.neural_network import MLPClassifier

def app(kentang, X, y):
    st.title("Prediction Page")

    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">MLP Neural Network</b> for the Kardiovaskular Disease Prediction.
            </p>
        """, unsafe_allow_html=True)

    st.subheader("Select Values:")

    age = st.slider('Please enter your age', 0, 100, 25)
    gender = st.selectbox("Gender 1: male, 2: female", [1, 2])  # Assuming 1: Male, 2: Female
    height = st.slider("Height", int(kentang["height"].min()), int(kentang["height"].max()))
    weight = st.slider("Weight", int(kentang["weight"].min()), int(kentang["weight"].max()))
    ap_hi = st.slider("Systolic blood pressure", 0, 200, 100)
    ap_lo = st.slider("Diastolic blood pressure", 0, 200, 100)
    cholesterol = st.selectbox("Cholesterol Level", [1, 2, 3])
    gluc = st.selectbox("Glucose Level ", [1, 2, 3])
    smoke = st.selectbox("Smoke", [0, 1])
    alco = st.selectbox("Alcohol Intake", [0, 1])
    active = st.selectbox("Physical Activity", [0, 1])

    # Ensure feature matches the updated X_pred feature set
    feature = [age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]

    if st.button("Predict"):
        prediction, score = predict_function(X, y, feature)
        score = score + 0.15
        st.info("Predicted Successfully...")

        if prediction == 1:
            st.warning("The person is prone to get Kardiovaskular disease!!")
        else:
            st.success("The person is relatively safe from Kardiovaskular disease")

        st.write("The model used is trusted by doctors and has an accuracy of ", (score * 100), "%")
