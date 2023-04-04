import pandas as pd
import streamlit as st
import StationPerformance as stp
import calculations

#station performance

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Station Performance", "Calculations", "Deslugging operator inputs","Flowrates","Lime feed","Lime dose","Jar Test","Desluging info"])


with tab1:

    stp.get_St_Performance()


with tab2:
    calculations.get_calculations()    

with tab3:
   #sp2 = pd.read_excel('data/ExelModel.xlsm',sheet_name=2)
   #st.dataframe(sp2)
   stp.say_hello()

#flowrates
with tab4:
   st.write('Flow rates to measure and record')
   sp3 = pd.read_excel('data/ExelModel.xlsm',sheet_name=3,skiprows=2,usecols=['Stream','Flow (l/s)','Flow (l/s).1','Flow (l/s).2','Avg (l/h)'])
   sp3['Avg (l/h)'] = sp3['Flow (l/s)']*3600/3 + sp3['Flow (l/s).1']*3600/3 + sp3['Flow (l/s).2']*3600/3
   sp3 = sp3.fillna(' ').astype(str)
   st.dataframe(sp3)
   

with tab5:
   st.write('Calibrate silo feed using bucket (packet test). Set feed opening to a certain percentage')
   sp4 = pd.read_excel('data/ExelModel.xlsm',sheet_name=4,skiprows=2)
   st.dataframe(sp4)
   

with tab6:
   sp5 = pd.read_excel('data/ExelModel.xlsm',sheet_name=5,skiprows=1).astype(str)
   st.dataframe(sp5)
   

with tab7:
   sp6 = pd.read_excel('data/ExelModel.xlsm',sheet_name=6).dropna(thresh=3)
   st.dataframe(sp6.astype(str))
  

with tab8:
   #sp7 = pd.read_excel('data/ExelModel.xlsm',sheet_name=7)
   #st.dataframe(sp7)
   st.write('hello')