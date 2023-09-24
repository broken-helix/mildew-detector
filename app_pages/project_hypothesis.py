import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def project_hypothesis_body():

    version = 'v3'

    st.write("## Project Hypotheses")
    st.write("---")

    st.success(
        f"### Hypothesis 1\n\n"
        f"***There is a visual difference in appearance between infected and "
        f"healthy cherry tree leaves.***\n\n"
    )

    st.warning(
        f"Average infected leaf images show a cloudy appearance in the image "
        f"centre and have a uniform appearance in average variability images."
    )
    # Load average and variability images
    avg_powdery_mildew = plt.imread(
        f"outputs/v1/avg_var_powdery_mildew.png"
    )
    avg_uninfected = plt.imread(
        f"outputs/v1/avg_var_healthy.png"
    )

    # Display infected average and variability images
    st.image(
        avg_powdery_mildew,
        caption='Infected Leaves - Average and Variability'
    )

    st.warning(
        f"Average healthy leaf images display a clear patch in the image "
        f"centre and a dark centre in average variability images."
    )

    # Display healthy average and variability images
    st.image(
        avg_uninfected,
        caption='Healthy Leaves - Average and Variability'
    )

    st.warning(
        f"There are visible differences between average infected and healthy "
        f"images."
    )

    st.write("---")

    st.success(
        f"### Hypothesis 2\n\n"
        f"***It is possible to predict, with at least 97% accuracy, if an image of a cherry tree leaf is infected with powdery mildew.***\n\n"
    )

    # Display evaluation.pkl in dataframe
    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(
        version), index=['Loss', 'Accuracy']))

    st.warning(
        f"The model used for the prediction task has an accuracy of >97%."
    )

    st.write("---")
