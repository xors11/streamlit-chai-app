import streamlit as st
import pandas as pd
st.markdown("""
<h1 style='
    font-size: 60px;
    font-style: italic;
    font-weight: bold;
    color: #DAA520; /* Goldenrod */          
    text-align: center;
'>
    BMI Calculator
</h1>
""", unsafe_allow_html=True)
#Background color
st.markdown("""
<h4 style='
    font-size: 20px;
    font-family: monospace;
    font-weight: bold;
    color: #2F4F4F; /* Dark Slate Gray */
    text-align: center;
'>
    Track your fitness - Know your BMI
</h4>
""", unsafe_allow_html=True)

name=st.text_input("Enter your name")
age=st.number_input("Enter your age",min_value=1,max_value=1000,step=1)
height=st.number_input("Enter your height in cm",min_value=50,max_value=300,step=1)
weight=st.number_input("Enter your weight in kg",min_value=10,max_value=300,step=1)
if st.button("Calculate your BMI"):
    if height > 0 and weight > 0:
        height = height / 100
        bmi = weight / (height ** 2)
        st.success(f"Hey {name}, Your BMI: {bmi:.2f}")

    if bmi<18.5:
     st.warning("Underweight")
     st.image("https://i.pinimg.com/1200x/77/46/93/77469372d584fc4ab892ee0df5da12c9.jpg",width=200)

    elif 18.5<=bmi<24.9:
     st.info("Normal weight")
     st.image("https://i.pinimg.com/736x/6f/e6/cb/6fe6cba1279d4030ef532ca31d9f24e2.jpg",width=200)

    elif 25.0<=bmi<29.9:
     st.warning("Overweight")
     st.image("https://i.pinimg.com/1200x/77/46/93/77469372d584fc4ab892ee0df5da12c9.jpg",width=200)

    elif 30.0<=bmi<34.9:
     st.info("Obesity class | (Mild)")
     st.image("https://tse4.mm.bing.net/th/id/OIP.VcF0Y8BPvh5pcxdH8WKfmgHaHr?pid=Api&P=0&h=220",width=200)

    elif 35.0<=bmi<39.9:
     st.warning("Obesity class || (Severe)")
     st.image("https://i.pinimg.com/1200x/77/46/93/77469372d584fc4ab892ee0df5da12c9.jpg",width=200)

    elif bmi>=40:
     st.warning("Obesity class ||| (Extreme\High Risk)")
     st.image("https://i.pinimg.com/1200x/77/46/93/77469372d584fc4ab892ee0df5da12c9.jpg",width=200)

    else:
     st.error("Please enter a valid height.")

     if weight<=0:
      st.error("Please enter a valid weight.")

file=st.file_uploader("Upload your file",type=["csv"])
if file:
    df=pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df)


