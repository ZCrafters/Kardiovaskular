import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import warnings

from web_functions import train_model

def app(kentang, X, y):
    warnings.filterwarnings("ignore")
    st.title("Visualise Cardiovaskular")

    if st.checkbox("Correlation Heatmap"):
        st.subheader("Correlation Heatmap")

        corr_matrix = kentang.corr()
        fig = plt.figure(figsize=(12, 8))
        ax = sns.heatmap(corr_matrix, annot=True, cmap='mako')
        plt.title('Correlation Matrix')

        # Fixing the potential issue with ylim
        bottom, top = ax.get_ylim()
        ax.set_ylim(bottom + 0.5, top - 0.5)

        st.pyplot(fig)

    # Define a custom color palette
    custom_palette = sns.color_palette(["#E74C3C", "#76D7C4"])  # Blue and mint colors

    # Single selection option
    option = st.selectbox("Select a feature to visualize with Cardio", 
                          ["Age with Cardio", "Gender with Cardio", "Cholesterol with Cardio", 
                           "Glucose with Cardio", "Smoking with Cardio", "Alcohol with Cardio", 
                           "Physical Activity with Cardio"])

    if option == "Age with Cardio":
        st.subheader("Bar Plot: Age with Cardio")
        fig2 = plt.figure(figsize=(12, 6))
        ax2 = sns.countplot(x='age', hue='cardio', data=kentang, palette=custom_palette)
        plt.title('Age')
        bottom, top = ax2.get_ylim()
        ax2.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig2)
    
    elif option == "Gender with Cardio":
        st.subheader("Bar Plot: Gender with Cardio")
        fig2 = plt.figure(figsize=(12, 6))
        ax2 = sns.countplot(x='gender', hue='cardio', data=kentang, palette=custom_palette)
        plt.title('Gender')
        bottom, top = ax2.get_ylim()
        ax2.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig2)

    elif option == "Cholesterol with Cardio":
        st.subheader("Bar Plot: Cholesterol with Cardio")
        fig2 = plt.figure(figsize=(12, 6))
        ax2 = sns.countplot(x='cholesterol', hue='cardio', data=kentang, palette=custom_palette)
        plt.title('Cholesterol')
        bottom, top = ax2.get_ylim()
        ax2.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig2)

    elif option == "Glucose with Cardio":
        st.subheader("Bar Plot: Glucose with Cardio")
        fig2 = plt.figure(figsize=(12, 6))
        ax2 = sns.countplot(x='gluc', hue='cardio', data=kentang, palette=custom_palette)
        plt.title('Glucose')
        bottom, top = ax2.get_ylim()
        ax2.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig2)

    elif option == "Smoking with Cardio":
        st.subheader("Bar Plot: Smoking with Cardio")
        fig2 = plt.figure(figsize=(12, 6))
        ax2 = sns.countplot(x='smoke', hue='cardio', data=kentang, palette=custom_palette)
        plt.title('Smoking')
        bottom, top = ax2.get_ylim()
        ax2.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig2)

    elif option == "Alcohol with Cardio":
        st.subheader("Bar Plot: Alcohol with Cardio")
        fig2 = plt.figure(figsize=(12, 6))
        ax2 = sns.countplot(x='alco', hue='cardio', data=kentang, palette=custom_palette)
        plt.title('Alcohol')
        bottom, top = ax2.get_ylim()
        ax2.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig2)

    elif option == "Physical Activity with Cardio":
        st.subheader("Bar Plot: Physical Activity with Cardio")
        fig2 = plt.figure(figsize=(12, 6))
        ax2 = sns.countplot(x='active', hue='cardio', data=kentang, palette=custom_palette)
        plt.title('Physical Activity')
        bottom, top = ax2.get_ylim()
        ax2.set_ylim(bottom + 0.5, top - 0.5)
        st.pyplot(fig2)
