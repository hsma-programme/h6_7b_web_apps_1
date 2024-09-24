import streamlit as st


st.title('Simple Calculator App')

st.write('Wage Calculater')

name = st.text_input('Please input your name')
wage = st.slider('Please input your wage', min_value = 0, max_value = 10000, value = 1000)
housing = st.number_input('please input housing cost', min_value = 0, value = 1000)
food = st.number_input('please input food costs', min_value = 0)
utility = st.number_input('please input utility costs', min_value = 0)

if name == "":
    st.warning('Please enter your name')
else:
    st.success(f"Hello {name}")

max_housing_spend = wage * 0.5
max_food_spend = wage * 0.1
max_utility_spend = wage * 0.1

if wage == 0:
    st.error('Please enter your wage')
else:
    housing_spend = housing / wage
    if housing_spend > max_housing_spend:
        st.warning(f'Percentage of wage spent on housing is {housing_spend:.1%}')
    else: 
        st.success(f'Percentage of wage spent on housing is {housing_spend:.1%}')

    leftover_wage = wage - (housing + food + utility)
    leftover_wage_text = f"Leftover wage is £{leftover_wage}"
    if leftover_wage < 0:
        st.error("Your costs are higher than your wage.")
    elif leftover_wage > 5000:
        st.success(leftover_wage_text)
        st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Fphoto-rich-happy-entrepreneur-guy-s-business-suit-de-photo-rich-happy-entrepreneur-guy-s-business-suit-115310958.jpg&f=1&nofb=1&ipt=bd374a4458907e8ac8e7fe9729178ac838e9ad33b6182962972068216e7b8887&ipo=images")
    else:
        st.warning(leftover_wage_text)
        st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fthumbs.dreamstime.com%2Fb%2Fpoor-businessman-holding-sign-asking-job-homeless-new-41033230.jpg&f=1&nofb=1&ipt=7195f4f3cd952e5679711c97a3da80f9b7c11edff6ff6b75204273a724d39dde&ipo=images")

st.write(f'Recommended maximum housing spend is £{max_housing_spend:.0f}')
st.write(f'Recommended maximum food spend is £{max_food_spend:.0f}')
st.write(f'Recommended maximum utility spend is £{max_utility_spend:.0f}')