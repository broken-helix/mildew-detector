import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation


def ml_performance_body():
    st.write("## Machine Learning Performance")
    st.write("---")

    # Set model version
    version = 'v1'

    st.write("## Train, Validation and Test Set: Labels Frequencies")

    # Load label distribution bar chart
    labels_distribution = plt.imread(
        f"outputs/{version}/labels_distribution.png")
    # Display label distribution bar chart
    st.image(labels_distribution,
             caption='Labels Distribution on Train, Validation and Test Sets')

    st.write("---")

    # Load label distribution pie chart
    labels_distribution = plt.imread(
        f"outputs/{version}/sets_distribution_pie.png")
    # Display label distribution pie chart
    st.image(labels_distribution, caption='Sets distribution')

    st.write("---")

    st.write("## Model History")

    # Load model training and validation accuracy png
    model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
    # Display model training and validation accuracy plot
    st.image(model_acc, caption='Model Training Accuracy')
    # Load model training and validation loss png
    model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
    # Display model training and validation loss plot
    st.image(model_loss, caption='Model Training Losses')

    st.write("---")

    st.write("## Confusion Matrix")

    # Load confusion matrix
    model_cm = plt.imread(f"outputs/{version}/confusion_matrix.png")
    # Display confusion matrix
    st.image(model_cm, caption='Confusion Matrix')

    st.write("---")

    st.write("## Generalised Performance on Test Set")

    # Display evaluation.pkl in dataframe
    st.dataframe(pd.DataFrame(load_test_evaluation(version),
                              index=['Loss', 'Accuracy']))

    st.write("---")
