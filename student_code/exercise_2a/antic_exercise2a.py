import streamlit as st



# It should have a title.
st.title('Welcome to our Expenses App')


# It should ask the user for 
# their name 

username = st.text_input(label='username')

# their monthly take home pay

take_home = st.number_input(label='Monthly Pay')

# their housing costs

housing_cost = st.number_input(label='Housing Costs')

# their food costs

food_cost = st.number_input(label='Food Costs')
# their utility costs 

utility_cost = st.number_input(label='Utility Costs')

# Display name
if len(username) == 0:
    st.warning('Please enter username')
else:
    st.write(f'Hello {username} welcome to the Expenses App!')

# Display the percentage of their monthly take home pay that is spent on housing




if housing_cost == 0:
    st.warning('Please enter housing cost')
else:
    percentage_housing = housing_cost / take_home
    st.write(f"Your percentage of monthly take home spent on housing is {percentage_housing :.1%}")

if utility_cost == 0:
    st.write('Please enter costs')
else:
    remaining_money = take_home - housing_cost - food_cost - utility_cost
    if remaining_money > 0:
        st.balloons()
        st.write(f"Your remaining money is {remaining_money}")
        st.markdown("![Alt Text](https://media1.tenor.com/m/YlBfgZ3_INcAAAAd/cat-kitty.gif)")
    else:
        st.warning(f"Your remaining money is {remaining_money}")
        st.markdown("![Alt Text](https://media1.tenor.com/m/Lx4kuvnOA3sAAAAd/no-money-broke.gif)")
        

# Display the amount of money they have left after all costs are accounted for


# (for now, don’t worry if it displays an error until the user has entered all of the information!)
