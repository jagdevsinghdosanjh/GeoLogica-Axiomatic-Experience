import streamlit as st
import spacy
from modules import proof_validator

with st.spinner("Analyzing your proof using Euclid's logic..."):
    proof_text = st.text_area("Enter your geometric proof:")
    feedback = proof_validator.validate_proof(proof_text)
    st.markdown(feedback)
    
nlp = spacy.load("en_core_web_sm")

AXIOM_PATTERNS = {
    "Axiom 1": ["equal", "same thing"],
    "Axiom 2": ["add", "equals", "whole"],
    "Axiom 3": ["subtract", "equals", "remainder"],
    "Axiom 4": ["coincide", "equal"],
    "Axiom 5": ["whole", "greater", "part"]
}

def validate_proof(proof_text):
    if not proof_text.strip():
        return "❌ No proof submitted. Please write your reasoning."

    doc = nlp(proof_text.lower())
    matched_axioms = []

    for axiom, keywords in AXIOM_PATTERNS.items():
        if any(token.text in keywords for token in doc):
            matched_axioms.append(axiom)

    if matched_axioms:
        feedback = "✅ Your proof references the following axioms:\n"
        for axiom in matched_axioms:
            feedback += f"- {axiom}\n"
        feedback += "\n🧠 Great! Try refining your logic or adding diagrams."
    else:
        feedback = "⚠️ No recognizable axioms found. Try rephrasing or reviewing Euclid's principles."

    return feedback
