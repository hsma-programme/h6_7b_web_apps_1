import streamlit as st

st.title("Budget calculator")

name = st.text_input("What is your name?")

take_home = st.number_input("What is your monthly take home pay (£)", step=10, min_value= 0)
if take_home>10000:
    st.write(f"Are you sure this is correct? Your take home pay is £{take_home}!")
    st.image("https://unsplash.com/photos/1zO4O3Z0UJA/download?ixid=M3wxMjA3fDB8MXxzZWFyY2h8Mnx8cmljaHxlbnwwfHx8fDE3MjcxMjg4NzN8MA&force=true")

housing = st.number_input("What are your monthly housing costs (£)", step=10, min_value= 0)

food = st.number_input("What are your monthly food costs (£)", step=10, min_value= 0)

utility = st.number_input("What are your monthly utility costs (£)", step=10, min_value= 0)

import pandas as pd

df = pd.DataFrame(
    [
        {"Cost type": "Housing", "value": housing},
         {"Cost type": "Food", "value": food},
          {"Cost type": "Utilities", "value": utility},
    ]
)
df["Percentage of take home"]= (df["value"]/take_home)*100

st.write(f"Hello {name}!")
st.write("Here is the breakdown of your costs:")

st.dataframe(df, use_container_width=True)
left = take_home - housing- food   - utility

st.write(f"After all costs, you have £{left} left")