import streamlit as st

c1,c2=st.columns(2)
fnum=c1.number_input("first Value",min_value=0,value=0)
snum=c2.number_input("second vaqlue",min_value=0,value=0)

options = ["Add","sub","mul","div"]
choice=st.radio("select an operation",options,horizontal=True)
btn=st.button("calculate")
if btn:
   if choice==options[0]:
    result=fnum+snum
   elif choice==options[1]:
    result=fnum-snum
   elif choice==options[2]:
    result=fnum*snum
   else:
      result=fnum/snum
   st.success(f'{result:.2f}')




