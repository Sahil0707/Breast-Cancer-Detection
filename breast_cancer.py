import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved model
breast_model = pickle.load(open('Breast_Cancer.sav', 'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Breast Cancer Prediction', 
                           ['Breast Cancer Prediction'], 
                           icons=['person'], 
                           default_index=0)

# Breast Cancer Prediction Page
if selected == "Breast Cancer Prediction":
    st.title("Breast Cancer Prediction Using ML")

    # Getting input data from the user
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Mean_Radius = st.text_input('Mean Radius')
    with col2:
        Mean_Texture = st.text_input('Mean Texture')
    with col3:
        Mean_Perimeter = st.text_input('Mean Perimeter')
    with col4:
        Mean_Area = st.text_input('Mean Area')
    with col5:
        Mean_Smoothness = st.text_input('Mean Smoothness')

    with col1:
        Mean_Compactness = st.text_input('Mean Compactness')
    with col2:
        Mean_Concavity = st.text_input('Mean Concavity')
    with col3:
        Mean_Concave_Points = st.text_input('Mean Concave Points')
    with col4:
        Mean_Symmetry = st.text_input('Mean Symmetry')
    with col5:
        Mean_Fractal_Dimension = st.text_input('Mean Fractal Dimension')

    with col1:
        Radius_Error = st.text_input('Radius Error')
    with col2:
        Texture_Error = st.text_input('Texture Error')
    with col3:
        Perimeter_Error = st.text_input('Perimeter Error')
    with col4:
        Area_Error = st.text_input('Area Error')
    with col5:
        Smoothness_Error = st.text_input('Smoothness Error')

    with col1:
        Compactness_Error = st.text_input('Compactness Error')
    with col2:
        Concavity_Error = st.text_input('Concavity Error')
    with col3:
        Concave_Point_Error = st.text_input('Concave Point Error')
    with col4:
        Symmetry_Error = st.text_input('Symmetry Error')
    with col5:
        Fractal_Dimension_Error = st.text_input('Fractal Dimension Error')

    with col1:
        Worst_Radius = st.text_input('Worst Radius')
    with col2:
        Worst_Texture = st.text_input('Worst Texture')
    with col3:
        Worst_Perimeter = st.text_input('Worst Perimeter')
    with col4:
        Worst_Area = st.text_input('Worst Area')
    with col5:
        Worst_Smoothness = st.text_input('Worst Smoothness')

    with col1:
        Worst_Compactness = st.text_input('Worst Compactness')
    with col2:
        Worst_Concavity = st.text_input('Worst Concavity')
    with col3:
        Worst_Concave_Points = st.text_input('Worst Concave Points')
    with col4:
        Worst_Symmetry = st.text_input('Worst Symmetry')
    with col5:
        Worst_Fractal_Dimension = st.text_input('Worst Fractal Dimension')

    # Convert input to float and handle empty fields
    try:
        features = [float(x) if x else 0 for x in [
            Mean_Radius, Mean_Texture, Mean_Perimeter, Mean_Area, Mean_Smoothness,
            Mean_Compactness, Mean_Concavity, Mean_Concave_Points, Mean_Fractal_Dimension,
            Radius_Error, Texture_Error, Perimeter_Error, Area_Error, Smoothness_Error,
            Compactness_Error, Concavity_Error, Concave_Point_Error, Symmetry_Error,
            Fractal_Dimension_Error, Worst_Radius, Worst_Texture, Worst_Perimeter,
            Worst_Area, Worst_Smoothness, Worst_Compactness, Worst_Concavity,
            Worst_Concave_Points, Worst_Symmetry, Worst_Fractal_Dimension
        ]]
    except ValueError:
        st.warning("Please enter valid numeric values.")

    # Code for Breast Cancer Prediction
    breast_cancer_diagnosis = ""

    if st.button('Breast Cancer Test Result'):
        prediction = breast_model.predict([features])

        if prediction[0] == 1:
            breast_cancer_diagnosis = "The person has Breast Cancer."
        else:
            breast_cancer_diagnosis = "The person is Cancer-Free."

        st.success(breast_cancer_diagnosis)

            """The Person is Cancer Free"""

    st.success(breast_cancer_diagnosis)
