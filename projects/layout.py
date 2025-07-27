import streamlit as st
import pyttsx3
st.write("Streamlit version:", st.__version__)

st.markdown("""
<h1 style='
    font-size: 60px;
    font-family: fantasy;
    font-weight: bold;
    color: 	#DC143C; /* Crimson red*/                 
    text-align: center;
'>
    Hall of Fame
</h1>""", unsafe_allow_html=True)

st.markdown("""
<h4 style='
    font-size: 40px;
    font-style: italic;
    font-weight: bold;
    color: #2E8B57; /* Goldenrod */          
    text-align: center;
'>
    Vote Now Let the Battle of Stars Begin!
</h4>
""", unsafe_allow_html=True)

name=st.text_input("Enter your name")


col1,col2,col3,col4=st.columns(4)
with col1:
    st.image("https://i.pinimg.com/736x/8d/03/e6/8d03e67e23e6d302f5bfaa4d9ec64ab1.jpg",width=200)
    st.write('''Hrithik Roshan''')
    vote1=st.button("Vote Hrithik")
with col2:
    st.image("https://i.pinimg.com/736x/00/6c/ad/006cad8d9ca00939ce22347a9220eb22.jpg",width=200)
    st.write("Prabhas")
    vote2=st.button("Vote Prabhas")

with col3:
    st.image("https://i.pinimg.com/736x/75/1e/a0/751ea0a12c046635e978464eae11f184.jpg",width=200)
    st.write("Rajni kanth")
    vote3=st.button("Vote Rajnikanth")   

with col4:
    st.image("https://i.pinimg.com/736x/a8/5a/f5/a85af5c0ef5d326a7fd2d5b2c3fb960d.jpg",width=200)       
    st.write("Mahesh Babu")
    vote4=st.button("Vote Mahesh Babu")

if vote1:
     st.success(f"Thanks for voting Hrithik roshan {name}")
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully")

elif vote2:
     st.success(f"Thanks for voting Prabhas {name}")
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully")

elif vote3:
     st.success(f"Thanks for voting Rajinikanth {name}")
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully")

elif vote4:
     st.success(f"Thanks for voting Mahesh Babu {name}")
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully")
  

         
col5,col6,col7,col8=st.columns(4)

with col5:
    st.image("https://i.pinimg.com/1200x/74/ab/e0/74abe04d9a47ec4c78cb189525a00d79.jpg",width=200)
    st.write("Allu Arjun")
    vote5=st.button("Vote Allu Arjun")

with col6:
    st.image("https://i.pinimg.com/736x/ff/28/df/ff28df95960e06087fe84c7708762cee.jpg",width=200)
    st.write("Ranbir Kapoor")
    vote6=st.button("Vote Ranbir kapoor")

with col7:
    st.image("https://i.pinimg.com/736x/e2/82/20/e282200749f5092300c226acba942a35.jpg",width=200)
    st.write("Shah Rukh Khan")
    vote7=st.button("Vote SRK")

with col8:
    st.image("https://i.pinimg.com/1200x/6d/50/c4/6d50c4a8fdf1bcad8d271bc4d8421110.jpg",width=200)
    st.write("Chiranjeevi")
    vote8=st.button("Vote Chiranjeevi")


if vote5:
     st.success(f"Thanks for Allu Arjun {name}")
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully")

elif vote6:
     st.success(f"Thanks for voting Ranbir Kapoor{name}")
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully")

elif vote7:
     st.success(f"Thanks for voting Shah Rukh Khan{name}")
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully")

elif vote8:
     st.success(f"Thanks for voting Chiranjeevi {name}") 
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully") 



col9,col10,col11,col12=st.columns(4)

with col9:
     st.image("https://i.pinimg.com/1200x/d8/8f/79/d88f79606a3466f9122c5ac71e28fe19.jpg",width=200)
     st.write("NTR")
     vote9=st.button("Vote NTR")

with col10:
     st.image("https://i.pinimg.com/1200x/f1/34/7e/f1347e42e393a3f1bf46f050e08c513f.jpg",width=200)
     st.write("Yash")
     vote10=st.button("Vote Yash")

with col11:
     st.image("https://i.pinimg.com/736x/eb/53/d5/eb53d500375467c65a8f31a22a0e067c.jpg",width=200)
     st.write("Vijay Antony")
     vote11=st.button("Vote Vijay")

with col12:
     st.image("https://i.pinimg.com/736x/b4/b2/15/b4b21556678d4b25a5b9c11794bd068d.jpg",width=200)
     st.write("Salman Khan")
     vote12=st.button("Vote Salman Khan")

if vote9:
     st.success(f"Thanks for NTR {name}")
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully")

elif vote10:
     st.success(f"Thanks for voting Yash{name}")
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully")

elif vote11:
     st.success(f"Thanks for voting Vijay aka Thalapathy{name}")
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully")

elif vote12:
     st.success(f"Thanks for voting Salman Khan{name}") 
     st.balloons()
     pyttsx3.speak("Your vote has been casted succesfully") 






    


    
         
            


        

        


