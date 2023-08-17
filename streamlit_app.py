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
    "account": st.secrets['connection.snowpark']['account'], 
   "user": st.secrets['connection.snowpark']['user'],
   "password": st.secrets['connection.snowpark']['password'],
    "database": st.secrets['connection.snowpark']['database'],
   "schema": st.secrets['connection.snowpark']['schema'],
   "warehouse": st.secrets['connection.snowpark']['warehouse'], 
}


# create session
session = Session.builder.configs(CONNECTION_PARAMETERS).create()

