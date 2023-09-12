import streamlit as st


def summary_body():

    st.write(
        f"The 'Mildew Detector' is a machine learning project designed "
        f"to predict if a host tree is infected with Powdery Mildew "
        f"disease.\n\n"
        f"The project uses an image of a leaf from the tree to determine the "
        f"probability of whether the tree is infected or healthy."
    )

    st.success(
        f"### The Disease\n\n"
        f"Powdery Mildew is a disease is caused by Podosphaera clandestina, "
        f"one of the common species of the powdery mildew group of fungi.\n\n"
        f"The disease affects cherry trees, damages and stunts new growth "
        f"and can affect crop return in commercial settings.\n\n"
        f"The same fungus reportedly causes powdery mildew in peaches, "
        f"apricots, apples and pears.\n\n"

        f"### Symptoms and Signs\n\n"
        f"Powdery mildew is marked by superficial, white, weblike growth on "
        f"leaves, shoots, or fruit.\n\n"
        f"At first, infected leaves curl upward and by mid-season, the whitish "
        f"fungus can be seen growing over the leaves and shoots, sometimes in "
        f"patches and other times covering most of the new growth.\n\n"

        f"### Disease Life Cycle\n\n"
        f"The Podosphaera clandestina fungus overwinters in buds on twigs and "
        f"as chasmothecia, "
        f"which are spore-containing structures, on the bark of twigs and "
        f"branches. Secondary spores produced in spring spread the fungus to "
        f"new growth."
    )
    st.write("---")

    st.warning(
        f"### Business Requirements\n\n"
        f"The project satisfies two business requirements:\n\n"
        f"1 - A study to visually differentiate a healthy from an infected "
        "leaf.\n\n"
        f"2 - An accurate prediction whether a given leaf is infected by "
        "powdery mildew or not."
    )
    st.write("---")

    st.info(
        f"### Project Dataset\n\n"
        f"The available dataset contains images of 2104 healthy leaves and "
        f"2104 infected leaves."
    )
    st.write("---")


"""
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
"""
