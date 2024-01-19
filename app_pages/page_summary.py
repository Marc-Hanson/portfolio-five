import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew of sweet and sour cherry is caused by Podosphaera Clandestina,"
        f" an obligate biotrophic fungus. \n"
        f"* Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected,"
        f" rendering them unmarketable due to the covering of white fungal growth on the cherry surface.\n"
        f"* Season long disease control of both leaves and fruit is critical to"
        f" minimize overall disease pressure in the orchard and consequently to protect"
        f" developing fruit from accumulating spores on their surfaces.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 4208 leaves, split exactly in half with 2104 healthy leaves "
        f"and 2104 infected leaves. These photos are taken with a neutral background.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Marc-Hanson/portfolio-five/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate"
        f" a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
    )
