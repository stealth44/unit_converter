import streamlit as st
import time

from PIL import Image
image=Image.open('unit.png')

st.image(image,width=700)

st.title('Welcome to my unit converter')


with st.expander("Read More....."):
     st.write("""
       This is a web app that aims to make
       conversion of units to other units 
       very easy and fast!
     """)

number = st.number_input('Insert a number')



option1 = st.selectbox(
     'FROM:  select unit',
     ('foot', 'yard', 'inch', 'metre','kilometre', 'centimetre', 'millimetre', 'gram', 'kilogram', 'milligram', 'metric ton', 'litre', 'centilitre', 'millilitre'))


option2 = st.selectbox(
     'TO:  select unit',
     ('foot', 'yard', 'inch', 'metre','kilometre','centimetre', 'millimetre', 'gram', 'kilogram', 'milligram', 'metric ton',  'litre', 'centilitre', 'millilitre'))


if option1 == 'inch' and option2 == 'centimetre':
    result =number*2.54
elif option1 =='centimetre' and option2 =='inch':
    result=number/2.54
elif option1 =='millimetre' and option2 =='inch':
    result=number/25.4 
elif option1 =='inch' and option2 =='millimetre':
    result=number*25.4 
elif option1 =='inch' and option2 =='metre':
    result=number/39.3700787 
elif option1 =='metre' and option2 =='inch':
    result=number*39.3700787 
elif option1 =='inch' and option2 =='kilometre':
    result=number/39370.0787
elif option1 =='foot' and option2 =='yard':
    result=round(number/3)
elif option1 =='yard' and option2 =='foot':
    result=number*3
elif option1 =='yard' and option2 =='metre':
    result=number/1.0936133
elif option1 =='metre' and option2 =='yard':
    result=number*1.0936133
elif option1 =='yard' and option2 =='centimetre':
    result=number/91.44
elif option1 =='yard' and option2 =='millimetre':
    result=number*914.4
elif option1 =='millitre' and option2 =='yard':
    result=number/914.4
elif option1 =='yard' and option2 =='centimetre':
    result=number*91.44
elif option1 =='yard' and option2 =='kilometre':
    result=number/1093.6133
elif option1 =='kilometre' and option2 =='yard':
    result=number*1093.6133
elif option1 =='foot' and option2 =='metre':
    result=number/3.2808399
elif option1 =='metre' and option2 =='foot':
    result=number*3.2808399
elif option1 =='foot' and option2 =='inch':
    result=number*12
elif option1 =='foot' and option2 =='kilometre':
    result=number/3280.8399
elif option1 =='kilometre' and option2 =='foot':
    result=number*3280.8399 
elif option1 =='millimetre' and option2 =='foot':
    result=number/304.8
elif option1 =='foot' and option2 =='millimetre':
    result=number*304.8 
elif option1 =='centimetre' and option2 =='foot':
    result=number/30.48
elif option1 =='foot' and option2 =='centimetre':
    result=number*30.48
elif option1 =='inch' and option2 =='foot':
    result=number/12 
elif option1 =='centimetre' and option2 =='metre':
    result=number/100
elif option1 =='metre' and option2 =='centimetre':
    result=number*100
elif option1 =='millimetre' and option2 =='metre':
    result=number/1000
elif option1 =='metre' and option2 =='millimetre':
    result=number*1000
elif option1 =='kilometre' and option2 =='metre':
    result=number*1000
elif option1 =='metre' and option2 =='kilometre':
    result=number*1000
elif option1 =='centimetre' and option2 =='millimetre':
    result=number*10
elif option1 =='millimetre' and option2 =='centimetre':
    result=number/10
elif option1 =='kiloemetre' and option2 =='millimetre':
    result=number*1000000
elif option1 =='millimetre' and option2 =='kilometre':
    result=number/1000000
elif option1 =='kilometre' and option2 =='centimetre':
    result=number*100000
elif option1 =='centimetre' and option2 =='kilometre':
    result=number/100000
elif option1 =='gram' and option2 =='kilogram':
    result=number/1000    
elif option1 =='kilogram' and option2 =='gram':
    result=number*1000
elif option1 =='gram' and option2 =='milligram':
    result=number*1000 
elif option1 =='milligram' and option2 =='gram':
    result=number/1000 
elif option1 =='kilogram' and option2 =='milligram':
    result=number*1000000
elif option1 =='milligram' and option2 =='kilogram':
    result=number/1000000
elif option1 =='metric ton' and option2 =='kilogram':
    result=number*1000
elif option1 =='kilogram' and option2 =='metric ton':
    result=number/1000
elif option1 =='gram' and option2 =='metric ton':
    result=number/1000000
elif option1 =='metric ton' and option2 =='gram':
    result=number*1000000    
elif option1 =='milligram' and option2 =='metric ton':
    result=number/1.0000E+9
elif option1 =='metric ton' and option2 =='milligram':
    result=number*1.0000E+9
elif option1 =='metric ton' and option2 =='centigram':
    result=number*100000000
elif option1 =='centigram' and option2 =='metric ton':
    result=number/100000000    
    

     
    
    
    
    
    
if st.button('Calculate',):
    with st.spinner('Wait for it...'):
        time.sleep(1)
    st.success(result)









hide_streamlit= """
            <style>
            #MainMenu :{visibility:hidden;}
            footer: {visibility:hidden;}
            </style>
            """
st.markdown(hide_streamlit,unsafe_allow_html=True)