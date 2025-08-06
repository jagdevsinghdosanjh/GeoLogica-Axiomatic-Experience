import streamlit as st

# Define keywords from Euclid's axioms
AXIOM_KEYWORDS = {
    "Axiom 1": ["equal to the same", "equal to one another"],
    "Axiom 2": ["added to equals", "wholes are equal"],
    "Axiom 3": ["subtracted from equals", "remainders are equal"],
    "Axiom 4": ["coincide", "equal to one another"],
    "Axiom 5": ["whole is greater", "part"]
}
st.write("Hey! Are you able to prove that You understand the Euclid's Geometery...")
def validate_proof(proof_text):
    if not proof_text.strip():
        return "❌ No proof submitted. Please write your reasoning."

    matched_axioms = []
    for axiom, keywords in AXIOM_KEYWORDS.items():
        for keyword in keywords:
            if keyword.lower() in proof_text.lower():
                matched_axioms.append(axiom)
                break

    if matched_axioms:
        feedback = "✅ Your proof references the following axioms:\n"
        for axiom in matched_axioms:
            feedback += f"- {axiom}\n"
        if len(matched_axioms) >= 2:
            feedback += "\n🧠 Good job! Try refining your logic further."
        else:
            feedback += "\n📌 Try to incorporate more axioms for a stronger proof."
    else:
        feedback = "⚠️ No recognizable axioms found. Revisit Euclid's principles and try again."

    return feedback
