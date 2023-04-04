import streamlit as st
import pandas as pd

def get_calculations():
   col1,col2 = st.columns([2,3])
   with col1:
     tb1,tb2,tb3,tb4 = st.tabs(['clarifier Dimentions','cooling water su[[ly','Conglant aid','Lime Dosing'])
     with tb1:
         diameter = st.text_input(label='Diameter (m)',value='18.5')
         height = st.text_input(label='Height (m)',value='5.3')
         area = st.text_input(label='Area (m^2)',value='269')
         volume = st.text_input(label='Volume (m^3)',value='1420')
         st.write(' ')
    

     with tb2:
         main_feed_flow = st.text_input(label='Main feed flow (I/s)',value='250')
         feed_per_classifier = float(main_feed_flow)*3600/2000
         st.write('main feed per clarifier (m3/h): {}'.format(feed_per_classifier))
         flow_through_velocity = feed_per_classifier/4
         st.write('Flow trough velocity (m/h): {}'.format(float(flow_through_velocity)))
         Retention_in_classifier = float(volume)/feed_per_classifier
         st.write('Retention in classifier (h): {}'.format(float(Retention_in_classifier)))
     with tb3:
         #Coagulant Aid
         st.write('coag type: RHEOFLOC 5414')
         st.write('Chemical name: Poly( Hydroxyalkylene dimethylammonium chloride')
         concentation_50 = 500000
         st.write('concentration 50% (ppm): {}'.format(concentation_50))
         pump_dosing = 0.2
         st.write('pump dosing (%): {}'.format(pump_dosing*100))
         feed_flow = 9.9
         st.write('feed flow (I/h): {}'.format(feed_flow))
         coag_dosage = 5.5
         st.write('coag dosage (ppm): {}'.format(coag_dosage))
     with tb4:
         #Lime dosing
         st.write('lime type: Heydrated lime')
         concentration = float(st.text_input(label = 'Concentration % (Ca(OH)2)',value='70'))
         rotary_feed_opening = float(st.text_input(label='Rotary feed opening % (100%=400kg/h)',value = '86'))
         feed_Ca_OH2 = float(st.text_input(label = 'feed Ca(OH)2 (kg/h)',value='242'))
         motive_water_feed = float(st.text_input(label='Motive water feed (I/h)',value='34104'))
         slury_concentration = float(feed_Ca_OH2)*100/float(motive_water_feed)
         st.write('slury concentration (g/l): {}'.format(slury_concentration))
         concentration_in_ppm = float(slury_concentration)*1000
         st.write('concentration in ppm (mg/l): {}'.format(concentration_in_ppm))
         dilution_water_supply = float(st.text_input(label = 'Dilution water supply (I/h)',value='39600'))
         concentration_in_mixer = concentration_in_ppm*(motive_water_feed/2)/dilution_water_supply
         st.write('Concentration in mixer (mg/l): {}'.format(concentration_in_mixer))
         concentration_per_classifier = (dilution_water_supply+motive_water_feed)*concentration_in_mixer/(feed_per_classifier*1000)
         st.write('concentration per classifier (ppm): {}'.format(concentration_per_classifier))
         based_on_measured_flow = 25.89
         st.write('Based on measured flow (ppm):'.format(based_on_measured_flow))

   with col2:
         import cv2
         img = cv2.imread('data/image.png')
         st.image(img,caption = 'flow diagram')