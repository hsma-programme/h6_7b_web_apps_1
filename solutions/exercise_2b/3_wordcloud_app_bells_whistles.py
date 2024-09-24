import streamlit as st

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import string
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance
import io
from io import StringIO
import PIL.ImageOps

# rembg is not included in the main hsma_webdev file as it's quite large
# and has various additional requirements
# You would need to run
# !pip install rembg
# to run this version of the file
from rembg import remove

st.set_page_config(layout="wide")

st.title("HSMA Wordcloud Generator")

with open("bttf_reviews.txt", "r") as f:
    sample_text = f.read()

def make_wordcloud(text_input, mask_image=None, use_image_colours=False, **kwargs):
    stopwords = set(STOPWORDS)
    tokens = text_input.split()
    punctuation_mapping_table = str.maketrans('', '', string.punctuation)
    tokens_stripped_of_punctuation = [token.translate(punctuation_mapping_table)
                                  for token in tokens]
    lower_tokens = [token.lower() for token in tokens_stripped_of_punctuation]

    joined_string = (" ").join(lower_tokens)

    plt.figure(figsize=(30,40))
    # Then use imshow to plot an image (here, our wordcloud)

    # The easiest way to do this today is to save the image and reload it
    # This works during local testing but would also work if we deployed this

    if mask_image is not None:

        # mask_image_opened = Image.open(mask_image)

        with st.expander("Click Here to see the Image processing options"):
            process_it = st.checkbox("Process Image", value=True)

            imagefile = io.BytesIO(mask_image.read())

            im = Image.open(imagefile)

            if process_it:

                threshold = st.slider("Choose a threshold", 1, 100, value=80, step=1)
                contrast_factor = st.slider("Contrast Enhancement Strength", 0.0, 2.0, value=1.0, step=0.05)
                invert = st.checkbox("Invert Output Image?")
                remove_background = st.checkbox("Remove Background")

                enhancer = ImageEnhance.Contrast(im)
                img_edited = enhancer.enhance(contrast_factor)

                img_edited = img_edited.convert("L").point(
                    lambda x: 255 if x > threshold else 0
                )

                if invert:
                    img_edited = PIL.ImageOps.invert(img_edited)

                if remove_background:
                    img_edited = remove(img_edited, bgcolor=[255,255,255,255])

                st.write("Original Image")
                st.image(mask_image, width=150)

                st.write("Edited Image")
                st.image(img_edited, width=150)
            else:
                img_edited = im

        mask_array = np.array(img_edited)


        wordcloud = WordCloud(width=mask_array.shape[1],
                    height=mask_array.shape[0],
                    stopwords=stopwords,
                    mask=mask_array,
                    margin=1,
                    **kwargs).generate(joined_string)

        if use_image_colours:
            # mask_colours = mask_array[::3, ::3]
            image_colors = ImageColorGenerator(mask_array, default_color=(255,255,255))
            wordcloud = wordcloud.recolor(color_func=image_colors)

        plt.imshow(wordcloud, interpolation='bilinear')

    else:
        wordcloud = WordCloud(width=1800,
                    height=1800,
                    stopwords=stopwords,
                    margin=1,
                    **kwargs).generate(joined_string)
        plt.imshow(wordcloud)

    # Turn off axes
    plt.axis("off")

    plt.savefig("wordcloud.png")

uploaded_text = st.file_uploader("Upload a text file here", ["txt"])
# Convert uploaded text to a string and display
if uploaded_text is not None:
    # see docs
    # https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader
    stringio = StringIO(uploaded_text.getvalue().decode("utf-8"))
    uploaded_text = stringio.read()

entered_text = st.text_area(label="Or enter your text here", value=sample_text,
                         height=300)

st.info("Uploaded file will be prioritised over entered text if both are present!")

if uploaded_text is None:
    your_text = entered_text
else:
    your_text = uploaded_text

background_colour_selected = st.selectbox("Choose a background colour", ["white", "black", "pink"])

minimum_font_size = st.number_input("Select the Minimum Font Size", 5, 25, 15)

mask_image = st.file_uploader(label="Optional: Upload an image to use as a mask", type=["png", "jpg", "jpeg"])

st.info(
    """
    White in images will be counted as an area where the words in the image cannot be drawn.

    If your image mask isn't working, check whether the white elements are pure white or not!
    """
)

if mask_image is not None:
    use_image_colours = st.checkbox("Use Image Colours?")
    contour_width = st.number_input("Select the Contour Width", 0, 5, 0)
else:
    use_image_colours = False
    contour_width = 0

if not use_image_colours:
    colourmaps =  ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r',
    'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Grays', 'Greens',
    'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r',
    'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu',
    'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r',
    'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn',
    'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r',
    'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r',
    'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r',
    'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis',
    'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix',
    'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r',
    'gist_grey', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow',
    'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gist_yerg',
    'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'grey', 'hot', 'hot_r',
    'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral',
    'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism',
    'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer',
    'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r',
    'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted',
    'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

    colourmap_selected = st.selectbox("Choose a colourmap", colourmaps)
else:
    colourmap_selected = "plasma"

if your_text is not None:
    make_wordcloud(text_input=your_text, mask_image=mask_image,
                   use_image_colours=use_image_colours,
                   background_color = background_colour_selected,
                   colormap = colourmap_selected,
                   min_font_size=minimum_font_size,
                   contour_width=contour_width
                   )

    st.image("wordcloud.png", use_column_width=True)

    with open("wordcloud.png", "rb") as file:
        btn = st.download_button(
            label="Click Here to Download Your Word Cloud!",
            data=file,
            file_name="my_wordcloud.png",
            mime="image/png",
        )
