import streamlit  as st 

#streamlite ui
st.title("Power Calculator")
st.write("Enter the no to calculate its square , cube , and fifth power.")

#get user input
n = st.number_input("enter the int",value =1,step=1)

# calculate results 
square = n**2
cube = n**3
fifth_power = n**5

#display results
st.write(f"the square of the {n} is :{square}")
st.write(f"the cube of the {n} is :{cube}")
st.write(f"the fifth power of the {n} is :{fifth_power}")