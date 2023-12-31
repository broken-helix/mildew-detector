import streamlit as st
import os
import seaborn as sns
import random
import itertools
import matplotlib.pyplot as plt
from matplotlib.image import imread


def leaves_visualiser_body():

    st.write(
        "## Leaves Visualiser\n\n"
        "Exploratory data analysis and visual display of the average "
        "variability of healthy and infected leaf images."
    )

    st.error(
        "This page handles Business Requirement 1."
    )

    st.write("---")

    st.success(
        "To determine if there are differences between infected and healthy "
        "leaves, and prepare images for machine learning, "
        "Exploratory Data Analysis was carried out.\n\n"
        "Images from both healthy and infected leaves were assessed for "
        "average variability between labels and are displayed below.\n\n"
    )

    st.write("---")

    version = 'v1'
    if st.checkbox(
            "Difference between average and variability image"):
        avg_powdery_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_uninfected = plt.imread(f"outputs/{version}/avg_var_healthy.png")

        st.warning(
            "There are visible differences between infected and healthy "
            "images.\n\n"
            "Infected leaves generate average images which are lighter in "
            "appearance in the centre.\n\n"
            "Infected leaves show a cloudier appearance in the centre in "
            "variability displays, indicating greater variability than the "
            "dark centres of the healthy images "
        )

        st.image(
            avg_powdery_mildew,
            caption='Affected leaf - Average and Variability')
        st.image(
            avg_uninfected,
            caption='healthy leaf - Average and Variability')
        st.write("---")

    st.write("---")

    if st.checkbox("Differences between average infected and "
                   "average healthy leaves"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")

        st.warning(
            "Combining average images from healthy and infected leaf images "
            "didn't show any noticeable patterns."
        )

        st.image(diff_between_avgs,
                 caption='Difference between average images')

    st.write("---")

    if st.checkbox("Image Montage"):
        st.warning("To refresh the montage, "
                   "click on the 'Create Montage' button")
        my_data_dir = 'inputs/mildew-dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label", options=labels, index=0)
        if st.button("Create Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))

    st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("white")
    labels = os.listdir(dir_path)

    # subset the class you are interested to display
    if label_to_display in labels:

        # checks if your montage space is greater than subset size
        # how many images in that folder
        images_list = os.listdir(dir_path+'/' + label_to_display)
        if nrows * ncols < len(images_list):
            img_idx = random.sample(images_list, nrows * ncols)
        else:
            print(
                f"Decrease nrows or ncols to create your montage. \n"
                f"There are {len(images_list)} in your subset. "
                f"You requested a montage with {nrows * ncols} spaces")
            return

        # create list of axes indices based on nrows and ncols
        list_rows = range(0, nrows)
        list_cols = range(0, ncols)
        plot_idx = list(itertools.product(list_rows, list_cols))

        # create a Figure and display images
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
        for x in range(0, nrows*ncols):
            img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
            img_shape = img.shape
            axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
            axes[plot_idx[x][0], plot_idx[x][1]].set_title(
                f"Width {img_shape[1]}px x Height {img_shape[0]}px")
            axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
            axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
        plt.tight_layout()

        st.pyplot(fig=fig)
        # plt.show()

    else:
        print("The label you selected doesn't exist.")
        print(f"The existing options are: {labels}")

    st.write("---")
