import os
import glob
import numpy as np
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from snowflake.snowpark.session import Session
import streamlit as st

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
conn = Session.builder.configs(CONNECTION_PARAMETERS).create()


def verify_code(verification_code):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM EMP WHERE code = '{verification_code}' AND attended = FALSE")
    attendee_data = cursor.fetchone()
    if attendee_data:
        cursor.execute(f"UPDATE EMP SET attended = TRUE WHERE code = '{verification_code}'")
        conn.commit()
        return True
    else:
        return False
st.title('Event Attendance Verification')
verification_code = st.text_input('Enter Verification Code:')
if st.button('Verify'):
    if verification_code:
        if verify_code(verification_code):
            st.success('Code verified successfully! Attendance count increased.')
        else:
            st.error('Invalid code or code already used.')
# Display attendance count
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM attendees WHERE attended = TRUE")
attendance_count = cursor.fetchone()[0]
st.write(f'Total Attended: {attendance_count}')
