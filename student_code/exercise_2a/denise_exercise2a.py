import streamlit as st

st.title("Denise: Streamlit testing")

tab1, tab2 = st.tabs(["Expenses", "Summary"])

with tab1:

    st.text("Please complete the fields below, then click on the summary tab to view your results")

    user_name= st.text_input("Please enter your full name")

    if user_name == "":
        st.error("You havent entered your name", icon = "❌")

    salary= st.number_input("Please enter your monthly take home salary",
                            value= 500
                            , min_value = 1
                            , max_value = 100000)

    if salary == "":
        st.error("You havent entered your salary", icon = "❌")
    else:
        st.success(f"Your monthly take home salary is £{salary:.2f}")

    housing_cost = st.number_input("What's your monthly housing cost (rent/mortgage)?")

    if housing_cost == "":
        st.error("You havent entered your monthly housing cost", icon = "❌")
    else:
        st.success(f"Your monthly housing cost is £{housing_cost:.2f}")

    food_cost = st.number_input("How much do you spend on food per month?")

    if food_cost == "":
        st.error("You havent entered your food cost", icon = "❌")
    else:
        st.success(f"Your monthly food cost is £{food_cost:.2f}")

    utility_cost = st.number_input("How much do you spend on utilities per month?")

    if utility_cost == "":
        st.error("You havent entered your monthly utility cost", icon = "❌")
    else:
        st.success(f"Your monthly utiliyy cost is £{utility_cost:.2f}")


with tab2:
    st.text(f"Hello {user_name}")

    # Calculate the percentage of take home that housing costs represent
    housing_perc = housing_cost/salary

    st.text(f"The percentage of your take home salary spent on housing is {housing_perc*100:.2f}%")

    if housing_cost > 0.5:
        st.warning("Housing costs exceed 50%", icon ="⚠️")
    elif housing_perc > 0.33:
        st.warning("Housing costs exceed 50%", icon ="⚠️")
    else:
        st.success("Housing costs are less than 33%", icon = "✅")

    # Calculate remaining money after housing, food and utility costs
    remaining = salary - housing_cost - food_cost - utility_cost

    st.text(f"Your monthly salary left over after housing, food and utility costs is £{remaining}")

    if remaining > 10:
       st.success("Treat yourself!",icon="💰")

    st.image("https://raw.githubusercontent.com/hsma-programme/h6_7b_web_apps_1/refs/heads/main/student_code/exercise_2a/denise.png")
