import streamlit as st
import os
import seaborn as sns
import numpy as np
import pandas as pd
import random
import itertools
import matplotlib.pyplot as plt
from matplotlib.image import imread


def leaves_visualiser_body():

    st.write(
        f"### Leaf Image Variability\n\n"
        f"Exploratory Data Analysis and visual display of the average "
        f"variability of healthy and infected leaf images."
    )

    st.success(
        f"To determine if there are differences between infected and healthy "
        f"leaves, and prepare images for machine learning, "
        f"Exploratory Data Analysis was carried out.\n\n"
        f"Images from both healthy and infected leaves were assessed for "
        f"average variability between labels and are displayed below.\n\n"
    )

    version = 'v1'
    if st.checkbox(
        "Difference between average and variability image"
    ):

        avg_powdery_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_uninfected = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.error(
            f"There are visible differences between infected and healthy "
            f"images.\n\n"
            f"Infected leaves generate average images which are lighter in "
            f"appearance in the centre.\n\n"
            f"Infected leaves show a cloudier appearance in the centre in "
            f"variability displays, indicating greater variability than the "
            f"dark centres of the healthy images "
        )

        st.image(
            avg_powdery_mildew,
            caption='Affected leaf - Average and Variability')
        st.image(
            avg_uninfected,
            caption='healthy leaf - Average and Variability')
        st.write("---")

    if st.checkbox("Differences between average infected and "
                   "average healthy leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.error(
            f"Combining average images from healthy and infected leaf images "
            f"didn't show any noticeable patterns."
        )

        st.image(diff_between_avgs,
                 caption='Difference between average images')
