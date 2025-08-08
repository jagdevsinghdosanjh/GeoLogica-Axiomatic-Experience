import streamlit as st
from modules.theorems import get_theorems
from modules.axioms import get_axioms

def interactive_proof_builder():
    st.subheader("🧩 Interactive Proof Builder")

    selected_theorem = st.selectbox("Select a theorem to prove", get_theorems())
    st.markdown(f"**Selected Theorem:** {selected_theorem}")

    steps = []
    for i in range(1, 6):  # Max 5 steps
        st.markdown(f"### Step {i}")
        axiom = st.selectbox(f"Choose an axiom for Step {i}", get_axioms(), key=f"axiom_{i}")
        object_type = st.selectbox(f"Select geometric object", ["Point", "Line", "Angle", "Triangle"], key=f"obj_{i}")
        transformation = st.text_input(f"Describe transformation or logic", key=f"trans_{i}")
        steps.append((axiom, object_type, transformation))

    if st.button("Submit Proof"):
        st.success("Proof submitted! You can now validate it.")
        return steps
