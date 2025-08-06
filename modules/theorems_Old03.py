# theorems.py

import streamlit as st
from modules.logger import log_attempt

# Sample Euclidean axioms for matching
EUCLID_AXIOMS = [
    "A straight line segment can be drawn joining any two points",
    "Any straight line segment can be extended indefinitely",
    "A circle can be drawn with any center and radius",
    "All right angles are equal",
    "If a line intersects two lines such that the sum of interior angles on the same side is less than two right angles, the lines meet on that side"
]

def match_axioms(user_text):
    matched = []
    for axiom in EUCLID_AXIOMS:
        if axiom.lower() in user_text.lower():
            matched.append(axiom)
    return matched

def prove_theorem():
    st.title("🔍 Euclidean Theorem Checker")

    user_text = st.text_area("Enter your proof attempt:", height=200)

    if st.button("Check Proof"):
        matched = match_axioms(user_text)
        log_attempt(user_text, matched)

        if matched:
            st.success(f"✅ Matched {len(matched)} axiom(s):")
            for axiom in matched:
                st.markdown(f"- {axiom}")
        else:
            st.warning("⚠️ No recognizable axioms found. Try rephrasing or reviewing Euclid's principles.")
            with st.expander("📜 View Euclid's Axioms"):
                for axiom in EUCLID_AXIOMS:
                    st.markdown(f"- {axiom}")
            st.info("💡 Tip: Use precise geometric language or refer to known postulates.")

