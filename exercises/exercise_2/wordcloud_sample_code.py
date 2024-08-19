# Import libraries (wordcloud will need to be installed)
from wordcloud import WordCloud, STOPWORDS
import string
import matplotlib.pyplot as plt

# Read text in for which we want to generate word cloud
# The read() method of the file object simply reads in the contents of the file
# as one, single continuous string of text.
with open("bttf_reviews.txt", "r") as f:
    full_text = f.read()

# STOPWORDS has a list of common stopwords (words such as "the", "and",
# "because", "isn't" etc that we're probably not interested in here).  We'll
# take a copy of STOPWORDS (which we'll call stopwords) in case we want to
# add our own etc.  We won't here, but we need them to remain as a set.
# Note - we're just setting up the set of stopwords here, we're not removing
# them from our text yet.  If we want to look at the stopwords, just type
# stopwords in the console after we've run this line of code.
stopwords = set(STOPWORDS)

# Tokenize the text (split into individual words (with punctuation attached) and
# put them in a list - we can see this if we look at the tokens list after we
# run this)
tokens = full_text.split()

# Set up a translation table that maps punctuation characters (stored in
# string.punctuation) to 'None'.  (We can see the list of punctuation characters
# stored in string if we type string.punctuation in the console).  This allows
# us to get rid of punctuation characters (which you'll have seen were still in
# the tokens).  The maketrans() method of a string object takes up to three
# inputs (arguments).  If we supply three, then the characters passed in the
# third argument are mapped to 'None' - ie it gets rid of them.  So we pass
# three inputs here - the first two we just pass empty strings (so it doesn't do
# any translation with them), and then we pass string.punctuation (which
# contains a list of punctuation characters) as the third input.  It will then
# set up a translation table that we can use to remove punctuation from text.
punctuation_mapping_table = str.maketrans('', '', string.punctuation)

# The translate() function maps one set of characters to another.  Here, we
# use that to translate tokens with punctuation to ones without punctuation
# by using the mapping table we specified above.  We use a list comprehension
# here to give us a list of tokens that have had the translation applied from
# the list of tokens that haven't.  After we run this bit of code, we can look
# at the tokens_stripped_of_punctuation.
tokens_stripped_of_punctuation = [token.translate(punctuation_mapping_table)
                                  for token in tokens]

# Convert all tokens to lowercase (so we don't count capitalised words
# differently).  We can use the lower() method of a string object (each token is
# a string) to make the string lowercase.  Again we use a list comprehension
# here.  We can then look at lower_tokens to see all our tokens are now lower
# case.
lower_tokens = [token.lower() for token in tokens_stripped_of_punctuation]

###NEW
# Let's remove the words "movie", "film", "back", "future".
# First, we'll set up a list of the words we want to remove (remember, all our
# tokens are lower case and have no punctuation, so our words to remove should
# be the same)
words_to_remove = ["movie", "film", "back", "future", "one"]

# Now let's generate a new list of tokens that have these words removed, by
# forming it only from tokens that are not in our list of words to remove above
refined_tokens = [token for token in lower_tokens if token
                  not in words_to_remove]

# Now let's join the refined tokens back up
joined_string = (" ").join(refined_tokens)

# Generate a wordcloud - specify the size, background colour, and the minimum
# font size.  We also specify the set of stopwords we want excluded that we
# set up earlier.  Specify that the word cloud should be generated on our text
# string by passing that string into the generate method of WordCloud.
# Note that the minimum font size specified will exclude words that would
# appear smaller than this (as they are too uncommon).  So reducing minimum
# font size acts as a proxy filter where more uncommon words are allowed in to
# the cloud.
wordcloud = WordCloud(width=1800,
                      height=1800,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=20).generate(joined_string)

# Now we plot (and save) the wordcloud using some matplotlib instructions.

# We set the size of the figure
plt.figure(figsize=(30,40))

# Turn off axes
plt.axis("off")

# Then use imshow to plot an image (here, our wordcloud)
plt.imshow(wordcloud)

# Then save the image as a png
plt.savefig("wordcloud.png")
