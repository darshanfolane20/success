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
   "account": st.secrets['go52266.ap-south-1'], 
   "user": st.secrets['darshan8'],
   "password": st.secrets['Darsh@1234'],
    "database": st.secrets['NEXUS'],
   "schema": st.secrets['HISTORY_MAKERS'],
   "warehouse": st.secrets['COMPUTE_WH'], 
}

# create session
session = Session.builder.configs(CONNECTION_PARAMETERS).create()

