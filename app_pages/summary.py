import streamlit as st


def summary_body():

    st.write(
        f"## Project Summary\n\n"
        f"The 'Mildew Detector' is a machine learning project designed "
        f"to predict if a host tree is infected with Powdery Mildew "
        f"disease.\n\n"
        f"The project uses an image of a leaf from the tree to determine the "
        f"probability of whether the tree is infected or healthy."
    )

    st.write("---")

    st.success(
        f"### The Disease\n\n"
        f"Powdery Mildew is a disease is caused by *Podosphaera clandestina*, "
        f"one of the common species of the powdery mildew group of fungi.\n\n"
        f"The disease affects cherry trees, damages and stunts new growth "
        f"and can affect crop return in commercial settings.\n\n"
        f"The same fungus reportedly causes powdery mildew in peaches, "
        f"apricots, apples and pears.\n\n"

        f"### Symptoms and Signs\n\n"
        f"Powdery mildew is marked by superficial, white, weblike growth on "
        f"leaves, shoots, or fruit.\n\n"
        f"At first, infected leaves curl upward and by mid-season, "
        f"the whitish "
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

    st.success(
        f"### Project Dataset\n\n"
        f"The available dataset contains images of 2104 healthy leaves and "
        f"2104 infected leaves."
    )

    st.write("---")
