import streamlit as st
from modules import axioms,euclidAxiomExplained, theorems, visuals

st.set_page_config(page_title="Euclid Unfolded", layout="wide")

st.title("📐 Euclid Unfolded: Geometry Reimagined")
st.markdown("Explore axioms, prove theorems, and visualize classical geometry interactively.")

tab1, tab2, tab3,tab4 = st.tabs(["Axiom Explorer","Euclid's Axioms Explained", "Theorem Prover", "Visual Playground"])

with tab1:
    axioms.display_axioms()
    
with tab2:
    euclidAxiomExplained.display_axioms_explanation()
    
with tab3:
    theorems.prove_theorem()

with tab4:
    visuals.show_visuals()
