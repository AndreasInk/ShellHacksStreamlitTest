import streamlit as st
import time
from playsound import playsound
from datetime import datetime
# for playing note.wav file




next = datetime.now() ##+ 2700


next_time = next.strftime("%H:%M:%S")

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == next_time:
        st.text("HERE")
        playsound('001.mp3')
        time.sleep(2700)