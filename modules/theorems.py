import streamlit as st
from modules import proof_validator, logger

def prove_theorem():
    st.header("Theorem Prover")
    st.markdown("> **Theorem:** Two distinct lines cannot have more than one point in common.")

    proof_text = st.text_area("🧠 Your Proof Steps", height=200)
    if st.button("Submit Proof"):
        feedback = proof_validator.validate_proof(proof_text)
        st.markdown(feedback)

        # Extract matched axioms from feedback
        matched = [line.split("- ")[1] for line in feedback.splitlines() if line.startswith("- ")]
        logger.log_attempt(proof_text, matched)
