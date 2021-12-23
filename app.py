import streamlit as st
st.title('Alan calculator')
num = st.slider('choose your number' , 1 , 100)
st.write('squre of ' , num , 'is = ' , num**2)
num2 = st.slider('choose any number to find out sruare root ' , 1 , 100)
st.write('squre root of ' , num2 , 'is = ' , num2**0.5 )
@st.cache()
def average(a ,b ,c):
	return (a+b+c)/3
a = st.slider('choose the value of a ')
b = st.slider('choose the value of b ')
c = st.slider('choose the value of c ')
if st.button('average '):
	average = average(a ,b ,c)
	st.write('average of three = ' , average)
