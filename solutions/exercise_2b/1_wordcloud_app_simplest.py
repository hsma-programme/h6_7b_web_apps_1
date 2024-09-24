import streamlit as st

from wordcloud import WordCloud, STOPWORDS
import string
import matplotlib.pyplot as plt

# Pasted in the exact make_wordcloud function from the provided sample code
def make_wordcloud(text_input, filename="wordcloud.png"):
    stopwords = set(STOPWORDS)
    tokens = text_input.split()
    punctuation_mapping_table = str.maketrans('', '', string.punctuation)
    tokens_stripped_of_punctuation = [token.translate(punctuation_mapping_table)
                                  for token in tokens]
    lower_tokens = [token.lower() for token in tokens_stripped_of_punctuation]

    joined_string = (" ").join(lower_tokens)

    wordcloud = WordCloud(width=1800,
                      height=1800,
                      stopwords=stopwords,
                      min_font_size=20).generate(joined_string)

    plt.figure(figsize=(30,40))
    # Turn off axes
    plt.axis("off")
    # Display (essential to actually get the wordcloud in the image)
    plt.imshow(wordcloud)
    # Save the wordcloud to a file
    plt.savefig(filename)

# Get some user input
your_text = st.text_area(label="Enter your text here")

# Take the text the user has inputted and pass it into the wordcloud function
make_wordcloud(text_input=your_text)

# Display the image we created
st.image("wordcloud.png")
