import pandas as pd
import numpy as np
from PIL import Image
import streamlit as st
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)
from src.data_management import download_dataframe_as_csv


def mildew_detector_body():

    st.write("Mildew Detector")
    st.write("---")

    st.info(
        f"Upload pictures of cherry leaves to discover whether it's affected "
        f"by powdery mildew or not and download a report of the examined "
        f"leaves."
    )

    st.write(
        f"You can download a set of infected and healthy leaves for live "
        f"prediction from [here] "
        f"(https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).")

    st.write("---")

    st.write(
        f"**Upload a clear picture of a cherry leaf.** "
        f"**You may select more than one.**"
    )
    images_buffer = st.file_uploader(
        ' ', type='jpg', accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry leaf Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil,
                caption=f"Image Size: {img_array.shape[1]}px width x "
                        f"{img_array.shape[0]}px height"
            )

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append(
                {
                    "Name": image.name,
                    'Result': pred_class
                }, ignore_index=True
            )

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(
                df_report), unsafe_allow_html=True)
