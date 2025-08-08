import streamlit as st

st.header("📐 Euclid's Axioms - Explained")

def display_axioms_explanation():
    st.write("These axioms are the bedrock of classical geometry, forming the logical rules that underpin geometric proofs. The page you're viewing is designed to help users explore, visualize, and experiment with these principles interactively.")
    euclidAxiomExplained = [
        "Axiom 1: Things which are equal to the same thing are equal to one another.This is the transitive property of equality. Example: If A = C and B = C, then A = B. In geometry, this helps link different elements through a common reference.",
        "Axiom 2: If equals are added to equals, the wholes are equal. This reflects the additive property of equality. Example: If A = B and C = D, then A + C = B + D. Useful in constructing larger shapes from equal parts. Example: If A = B and C = D, then A − C = B − D. Often used in proofs involving segment or angle subtraction.",
        "Axiom 3: If equals are subtracted from equals, the remainders are equal. This is the subtractive counterpart to",
        "Axiom 4: Things which coincide with one another are equal to one another. This emphasizes geometric congruence. If two shapes or lines perfectly overlap, they are considered equal. Crucial for proving congruence of figures.",
        "Axiom 5: The whole is greater than the part. A basic principle of hierarchical comparison. Example: A triangle is greater than any one of its sides. Helps establish inequalities in geometric reasoning. 🧠 How the Page Enhances Understanding. The surrounding page offers tools like:"
    ]
    
    for j, explanation in enumerate(euclidAxiomExplained, 1):
        st.markdown(f"**Explanation {j}:** {explanation}")
   