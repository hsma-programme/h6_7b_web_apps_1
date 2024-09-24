import streamlit as st

form = st.form("my_form")
form.title("Finance calculator")

name = form.text_input("Please enter your name:", value="User")

monthly_pay = form.number_input(f"Monthly take home pay:",step=1,min_value=1)

housing = form.number_input(f"Housing cost:",step=1,min_value=0)

food = form.number_input(f"Food cost:",step=1,min_value=0)

utility = form.number_input(f"Utility cost:",step=1,min_value=0)

calc_btn = form.form_submit_button("Calculate")

if calc_btn:
    st.write(f"Hello {name}!\nWelcome to the finance calculator!")

    if housing+food+utility>monthly_pay:
        st.error(f"{name}, you are spending more than your monthly income!")
    elif housing+food+utility==monthly_pay:
        st.warning((f"{name}, you did not save anything!"))
    else:
        st.success(f"{name}, you saved {monthly_pay-(housing+food+utility)}£!")

    housing_per = (housing/monthly_pay)*100
    food_per = (food/monthly_pay)*100
    utility_per = (utility/monthly_pay)*100

    if housing_per>=50:
        st.error(f"{name}, you are spending {housing_per}% of your monthly income on housing")
    elif housing_per>=33.3:
        st.warning(f"{name}, you are spending {housing_per}% of your monthly income on housing")
    else:
        st.info(f"{name}, you are spending {housing_per}% of your monthly income on housing")


    if food_per>=50:
        st.error(f"{name}, you are spending {food_per}% of your monthly income on food")
    elif food_per>=33.5:
        st.warning(f"{name}, you are spending {food_per}% of your monthly income on food")
    else:
        st.info(f"{name}, you are spending {food_per}% of your monthly income on food")


    if utility_per>=50:
        st.error(f"{name}, you are spending {utility_per}% of your monthly income on utility")
    elif utility_per>=33.3:
        st.warning(f"{name}, you are spending {utility_per}% of your monthly income on utility")
    else:
        st.info(f"{name}, you are spending {utility_per}% of your monthly income on utility")