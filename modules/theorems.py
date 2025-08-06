import streamlit as st
from modules import proof_validator

def prove_theorem():
    st.header("Theorem Prover")
    st.markdown("> **Theorem:** Two distinct lines cannot have more than one point in common.")

    proof_text = st.text_area("🧠 Your Proof Steps", height=200)
    if st.button("Submit Proof"):
        feedback = proof_validator.validate_proof(proof_text)
        st.markdown(feedback)

# import streamlit as st

# def prove_theorem():
#     st.header("Theorem Prover")
#     st.markdown("Try proving this theorem using Euclid's axioms:")
#     st.markdown("> **Theorem:** Two distinct lines cannot have more than one point in common.")
    
#     st.text_area("🧠 Your Proof Steps", height=200)
#     st.button("Submit Proof")

