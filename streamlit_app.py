import os
import glob
import numpy as np
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from snowflake.snowpark.session import Session
import streamlit as st
import pandas as pd

# snowpark connection
CONNECTION_PARAMETERS = {
    "account": st.secrets['account'], 
   "user": st.secrets['user'],
   "password": st.secrets['password'],
    "database": st.secrets['database'],
   "schema": st.secrets['schema'],
   "warehouse": st.secrets['warehouse'], 
}


# create session
session = Session.builder.configs(CONNECTION_PARAMETERS).create()


# Verify the code and mark attendance
def verify_and_mark_attendance(verification_code, attendee_id):
    attendees = session.read.table("EMP")
    filtered_attendee = attendees.filter(attendees["code"] == verification_code).filter(attendees["attendee_id"] == attendee_id).filter(attendees["attended"] == False)
    if not filtered_attendee.collect().empty():
        attendees.write \
            .overwrite() \
            .filter(attendees["code"] == verification_code) \
            .filter(attendees["EMP_ID"] == attendee_id) \
            .set("attended", True)
        return True
    else:
        return False
# Streamlit app
st.title('Event Attendance Verification')
attendee_id = st.text_input('Enter Your Attendee ID:')
verification_code = st.text_input('Enter Verification Code:')
if st.button('Verify'):
    if attendee_id and verification_code:
        if verify_and_mark_attendance(verification_code, int(EMP_ID)):
            st.success('Code verified successfully! You are marked as attended.')
        else:
            st.error('Invalid code or code already used.')
# Note: For security, you should also display the attendee's name for confirmation.
# Display attendance count
attendees = session.read.table("EMP")
attendance_count = attendees.filter(attendees["attended"] == True).count()
st.write(f'Total Attended: {attendance_count}')

