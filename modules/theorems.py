# theorems.py
import streamlit as st
from difflib import SequenceMatcher
from modules.logger import log_attempt

# Euclid's axioms
EUCLID_AXIOMS = [
    "A straight line segment can be drawn joining any two points",
    "Any straight line segment can be extended indefinitely",
    "A circle can be drawn with any center and radius",
    "All right angles are equal",
    "If a line intersects two lines such that the sum of interior angles on the same side is less than two right angles, the lines meet on that side"
]

# Fuzzy matching threshold
FUZZY_THRESHOLD = 0.6

def match_axioms(user_text):
    matched = []
    for axiom in EUCLID_AXIOMS:
        ratio = SequenceMatcher(None, axiom.lower(), user_text.lower()).ratio()
        if ratio >= FUZZY_THRESHOLD:
            matched.append((axiom, round(ratio, 2)))
    return matched

def prove_theorem():
    st.title("🔍 Euclidean Theorem Checker")
    st.markdown("Try proving this theorem using Euclid's axioms:")
    st.markdown("> **Theorem:** Two distinct lines cannot have more than one point in common.")
    user_text = st.text_area("Enter your proof attempt:", height=200)

    if st.button("Check Proof"):
        matched = match_axioms(user_text)
        log_attempt(user_text, [m[0] for m in matched])

        if matched:
            st.success(f"✅ Matched {len(matched)} axiom(s) with fuzzy logic:")
            for axiom, score in matched:
                st.markdown(f"- **{axiom}** _(match score: {score})_")
        else:
            st.warning("⚠️ No recognizable axioms found. Try rephrasing or reviewing Euclid's principles.")
            with st.expander("📜 View Euclid's Axioms"):
                for axiom in EUCLID_AXIOMS:
                    st.markdown(f"- {axiom}")
            st.info("💡 Tip: Use geometric terms like 'line', 'circle', 'angle', and refer to known postulates.")

