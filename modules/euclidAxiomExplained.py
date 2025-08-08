import streamlit as st

def display_axioms_explanation():
    st.write(
        """
        These axioms are the bedrock of classical geometry, forming the logical rules 
        that underpin geometric proofs. This page is designed to help users explore, 
        visualize, and experiment with these principles interactively.
        """
    )

    euclid_axioms = [
        {
            "title": "Axiom 1",
            "description": (
                "Things which are equal to the same thing are equal to one another. "
                "This is the transitive property of equality. "
                "Example: If A = C and B = C, then A = B. "
                "In geometry, this helps link different elements through a common reference."
            )
        },
        {
            "title": "Axiom 2",
            "description": (
                "If equals are added to equals, the wholes are equal. "
                "This reflects the additive property of equality. "
                "Example: If A = B and C = D, then A + C = B + D. "
                "Useful in constructing larger shapes from equal parts."
            )
        },
        {
            "title": "Axiom 3",
            "description": (
                "If equals are subtracted from equals, the remainders are equal. "
                "This is the subtractive counterpart to Axiom 2. "
                "Example: If A = B and C = D, then A − C = B − D. "
                "Often used in proofs involving segment or angle subtraction."
            )
        },
        {
            "title": "Axiom 4",
            "description": (
                "Things which coincide with one another are equal to one another. "
                "This emphasizes geometric congruence. "
                "If two shapes or lines perfectly overlap, they are considered equal. "
                "Crucial for proving congruence of figures."
            )
        },
        {
            "title": "Axiom 5",
            "description": (
                "The whole is greater than the part. A basic principle of hierarchical comparison. "
                "Example: A triangle is greater than any one of its sides. "
                "Helps establish inequalities in geometric reasoning."
            )
        }
    ]

    for i, axiom in enumerate(euclid_axioms, 1):
        st.markdown(f"### 🧩 Explanation {i}: {axiom['title']}")
        st.markdown(axiom["description"])

    st.markdown("🧠 **How the Page Enhances Understanding**")
    st.write(
        """
        The surrounding page offers interactive tools to explore these axioms visually, 
        test geometric relationships, and build intuition through experimentation.
        """
    )
