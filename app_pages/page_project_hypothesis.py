import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect mildew infected leaves have clear marks/signs, "
        f"typically in the middle of the leaf, that can be used to differentiate between infected and healthy leaves. \n\n"
        f"* Our Image Montage, shows that typically an infected leaf has a stringy white growth across the leafs surface. "
        f"Average Image, Variability Image and Difference between Averages studies didn't reveal "
        f"any clear pattern to differentiate one to another."
    )
