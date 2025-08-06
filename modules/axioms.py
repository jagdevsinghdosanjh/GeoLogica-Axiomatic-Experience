import streamlit as st
import json

def display_axioms():
    st.header("Euclid's Axioms")
    axioms = [
        "Things which are equal to the same thing are equal to one another.",
        "If equals are added to equals, the wholes are equal.",
        "If equals are subtracted from equals, the remainders are equal.",
        "Things which coincide with one another are equal to one another.",
        "The whole is greater than the part."
    ]
    for i, axiom in enumerate(axioms, 1):
        st.markdown(f"**Axiom {i}:** {axiom}")
