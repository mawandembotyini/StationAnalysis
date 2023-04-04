import pandas as pd
import streamlit as st

#station performance
def say_hello():
    st.write('hello from another module')
def block_updater(sp,row,column,value):
    sp.loc[row,[column]] = float(value)
    sp.to_excel('data/ExelModel1.xlsm',index=False)

def get_St_Performance():
     sp = pd.read_excel('data/ExelModel1.xlsm')
     
     sp['2P-M'] = sp['P-alkalinity']*2 - sp['M-alkalinity']
     #sp['Lime Dosage'] = 'Underdose' if sp['2P-M'] < 0
     sp1 = sp.copy()
     sp2 = sp1.fillna(' ').astype(str)
     col1,col2 = st.columns([4,1])
     with col1:
         st.dataframe(sp2)
    
     with col2:
         st.write('Update')
         column = st.selectbox(label='column',options= sp1.columns)
         row = st.number_input(label='row',min_value=0, max_value=len(sp1), value=0)
         value = st.text_input(label='new value',value=str(sp[column].values[row]))
         st.button('update',on_click=block_updater,args=[sp,row,column,value])

