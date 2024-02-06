import streamlit as st
import datetime
import pytz
import time

# Helper functions
def display_time(timezone):
    now = datetime.datetime.now(pytz.timezone(timezone))
    return now.strftime('%Y-%m-%d %H:%M:%S')

def get_unix_timestamp():
    return int(time.time())

def convert_unix_to_human(unix_timestamp):
    return datetime.datetime.fromtimestamp(int(unix_timestamp)).strftime('%Y-%m-%d %H:%M:%S')

# App layout and navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["World Clock", "Convert UNIX Timestamp"])

if page == "World Clock":
    st.title('World Clock')

    timezones = {
        'Shanghai': 'Asia/Shanghai',
        'Seattle': 'America/Los_Angeles',
        'Paris': 'Europe/Paris',
        'Tokyo': 'Asia/Tokyo'
    }

    selected_locations = st.multiselect('Select locations:', options=list(timezones.keys()), default=['Shanghai'])

    unix_timestamp_display = st.empty()

    time_displays = {location: st.empty() for location in selected_locations}

    while True:
        unix_timestamp = get_unix_timestamp()
        unix_timestamp_display.write("Current UNIX Timestamp: " + str(unix_timestamp))
        for location in selected_locations:
            current_time = display_time(timezones[location])
            time_displays[location].header(f"{location}: {current_time}")
        time.sleep(1)

elif page == "Convert UNIX Timestamp":
    st.title('Convert UNIX Timestamp to Human-Readable Time')

    unix_timestamp_input = st.number_input("Enter UNIX Timestamp:", min_value=0, format="%d")
    
    if unix_timestamp_input:
        human_time = convert_unix_to_human(unix_timestamp_input)
        st.write(f"Human-readable time: {human_time}")
    