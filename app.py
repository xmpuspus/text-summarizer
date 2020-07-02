import streamlit as st
from gensim.summarization import summarize


# Header
### Set Title
st.title("Text Summarizer")
st.markdown("""Summarize a long paragraph based on [this reference](https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf).""")

# Ratio of words as summary output
ratio = st.sidebar.slider("Summary Ratio: ", 0., 1., 0.2, 0.01)

# Text input
text = st.text_area("Input long paragraph", """Thomas A. Anderson is a man living two lives. By day he is an average computer programmer and by night a hacker known as Neo. Neo has always questioned his reality, but the truth is far beyond his imagination. Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government. Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix. As a rebel against the machines, Neo must return to the Matrix and confront the agents: super-powerful computer programs devoted to snuffing out Neo and the entire human rebellion.""", height=250)

# Word count
# word_count = st.sidebar.number_input("Summary Word Count", 0, len(text.split(" ")))

# Summarize
summary = summarize(text, ratio=ratio)

if not summary:
    st.write("Input a longer paragraph.")
else:
    st.write(summary)

