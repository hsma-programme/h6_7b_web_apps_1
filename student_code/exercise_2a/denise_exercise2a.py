import streamlit as st

st.title("Denise Streamlit App")

# Enter name
name = st.text_input("Enter name")

if name == "":
       st.warning("Enter valid name")
else:
       st.text(f"Your name is {name}")

# Enter costs
monthly_take_home = int(st.number_input(
       "What's your monthly take home income?",
       value = 10,
       min_value=0,
       max_value=20
       ))

housing_costs = int(st.number_input("What's your monthly housing cost (rent/mortgage)?", value = 5))

food_costs = int(st.number_input("How much do you spend on food per month?", value = 1))

utility_costs = int(st.number_input("How much do you spend on utilities per month?", value = 1))

st.text(f"Your take home salary is {monthly_take_home}")
st.text(f"Your housing costs are {housing_costs}")
st.text(f"Your food costs are {food_costs}")
st.text(f"Your utility costs are {utility_costs}")

# Calculations

housing_perc = housing_costs / monthly_take_home

st.text(f"Percentage of take home spent on housing are {housing_perc*100:.2f}%")

remaining = monthly_take_home - housing_costs - food_costs - utility_costs

st.text(f"Your monthly amount after housing, food and utility costs is £{remaining}.")

if housing_perc > 0.5:
       st.error("Housing exceeds 50%")
elif housing_perc > 0.33:
       st.warning("Housing exceeds 33%")
else:
       st.success("Housing <= 33%")

if monthly_take_home > 10:
       st.success("Spend!")

st.image("denise.png")