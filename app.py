import streamlit as st

# Define subject keyword banks
keyword_banks = {
    "Math": ["sum", "multiply", "subtract", "angle", "geometry", "equation"],
    "Money Matters": ["minimum wage", "economy", "profit", "rent", "income", "tax"]
}

simile_prompts = [
    "I'm as [adjective] as [noun]...",
    "Like a [noun], I [verb] through...",
    "I move like [name or object], unstoppable and bold...",
    "My thoughts hit hard like [metaphor]..."
]

st.title("🎤 Lyric Writing Studio")

# Subject selection
subject = st.selectbox("Choose your subject:", list(keyword_banks.keys()))

# Display keyword bank
st.subheader("🧠 Keyword Bank")
st.markdown(" ".join(f"`{word}`" for word in keyword_banks[subject]))

# Simile & metaphor prompts
st.subheader("💡 Simile & Metaphor Prompts")
for prompt in simile_prompts:
    st.markdown(f"- {prompt}")

# Dynamic verse input
st.subheader("✍️ Write Your Verses")
if "verses" not in st.session_state:
    st.session_state.verses = [""]

for i, verse in enumerate(st.session_state.verses):
    st.session_state.verses[i] = st.text_area(f"Verse {i + 1}", value=verse, key=f"verse_{i}")

if st.button("➕ Add Another Verse"):
    st.session_state.verses.append("")

# Save button
if st.button("💾 Save My Rhymes"):
    st.success("✅ Rhymes saved (functionality coming soon)")
