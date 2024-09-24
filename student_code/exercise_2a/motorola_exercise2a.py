import streamlit as st
my_users_name = st.text_input("FIRST AND FOREMOST - please enter your name")

if my_users_name=="":
    st.title("Hello (yet to be defined) User!")
else:
    st.title(f"Hello {my_users_name}!")




st.subheader("This is a calculator for calculating your monthly expenses.")


salary = st.number_input(label="What is your salary" + (f", {my_users_name}" if my_users_name else ""),
                       placeholder="£",
                       value=0,
                       step=10,
                       min_value=0
                       )

if salary ==0:
    st.warning("Please enter a salary value (£)!!!")
else:
    st.success(f"Thanks {my_users_name}. Your monthly income is £{salary}. Noice.")

housing_costs = st.number_input(label="What is your monthly take home income (rent/mortgage)" + (f", {my_users_name}" if my_users_name else ""),
                       placeholder="£",
                       value=0,
                       step=10,
                       min_value=0
                       )

if housing_costs ==0:
    st.warning("Please enter a housing cost value (£)!!!")
else:
    st.success(f"Thanks {my_users_name}. Your housing cost (rent/mortgage) is £{housing_costs}. Wowsers.")


food_costs = st.number_input(label="What is your monthly food spend" + (f", {my_users_name}" if my_users_name else ""),
                       placeholder="£",
                       value=0,
                       step=10,
                       min_value=0
                       )

if food_costs ==0:
    st.warning("Please enter a food cost value (£)!!!")
else:
    st.success(f"Thanks {my_users_name}. Your food spend is £{food_costs}. Delish")


utility_costs = st.number_input(label="What is your monthly utility spend" + (f", {my_users_name}" if my_users_name else ""),
                       placeholder="£",
                       value=0,
                       step=10,
                       min_value=0
                       )

if utility_costs ==0:
    st.warning("Please enter a utility cost value (£)!!!")
else:
    st.success(f"Thanks {my_users_name}. Your utility spend is £{utility_costs}. Exceptional")



if salary==0 | housing_costs ==0 | food_costs ==0 | utility_costs==0:
    st.warning("Must enter all values for calculation")
else:
   remaining = salary - housing_costs - food_costs - utility_costs
   housing_perc = housing_costs / salary
#    st.success(f"Your remaining money after housing, food and utility costs is £{remaining}.",
#    f"Your monthly amount after housing, food and utility costs is",
#    f"£{remaining}.  Your housing costs represent {housing_perc*100:.2f}%",
#    f"of your monthly take home.")
   st.write(f"Ok,{my_users_name}... let's break it down! Your remaining money after housing, food and utility costs is £{remaining}.",
   f"Your monthly amount after housing, food and utility costs is",
   f"£{remaining}.  Your housing costs represent {housing_perc*100:.2f}%",
   f"of your monthly take home.")
