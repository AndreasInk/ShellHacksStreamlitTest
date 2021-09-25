import streamlit as st
import time
from playsound import playsound
import datetime
from datetime import datetime as dt
def playAudio():
    time_change = datetime.timedelta(minutes=45)
    next = dt.now()  + time_change


    next_time = next.strftime("%H:%M:%S")

    while True:
        now = dt.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time == next_time:
            st.text("HERE")
            playsound('001.mp3')
            time.sleep(2700)