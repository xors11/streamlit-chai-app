import streamlit as st
st.title("The Chai")
st.write("In your favourite way")
chai=st.selectbox("Select your chai",["Masala chai","keasri chai","lemon chai","Badam chai","Ginger chai","Tulasi chai","Heaven chai"])
st.write(f"You have selected {chai}")
st.radio("Requirments",["More milk","Honey","Cream","Caramel"])
st.checkbox("Extra sugar packets")
qty=st.checkbox("Biscuit")
if qty:
    st.number_input("How many biscuits",min_value=1,max_value=5,step=1)
level=st.slider("strongness level",0,5,1)
st.write(f"Selected level: {level}")
name=st.text_input("Enter your name")
if st.button("Prepare"):
    st.success(f"Hello {name}!!! Your chai is being prepared")
