import streamlit as st

st.title("Remaining Income Calculator")

user_name = st.text_input("Please Enter Your Name")

# Get inputs from user, cast as integers and store in variables
monthly_take_home = st.number_input("What's your monthly take home income?")
housing_costs = st.number_input("What's your monthly housing cost (rent/mortgage)?")
food_costs = st.number_input("How much do you spend on food per month?")
utility_costs = st.number_input("How much do you spend on utilities per month?")

# Calculate remaining money after housing, food and utility costs
remaining = monthly_take_home - housing_costs - food_costs - utility_costs

if len(user_name) > 1:
    st.write(f"Hello {user_name}!")

if monthly_take_home > 0.0:
    # Calculate the percentage of take home that housing costs represent
    housing_perc = housing_costs / monthly_take_home

    # Print the message to the user
    st.write(f"Your monthly amount after housing, food and utility costs is £{remaining:.2f}.")

    st.write(f"Your housing costs represent {housing_perc*100:.1f}% of your monthly take home.")

    if housing_perc > 0.5:
        st.error("Your Housing Costs are much higher than the recommended maximum for your income.")
    elif housing_perc > 0.33:
        st.warning("Your Housing Costs are slightly higher than the recommended maximum for your income.")
    else:
        st.success("Your housing costs are within the recommended limits for your income.")

else:
    st.write("Please enter your details")
