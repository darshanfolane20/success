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
    "user"="darshan8",
    "password"="Darsh@1234",
    "account"="go52266.ap-south-1",
    "warehouse"="COMPUTE_WH",
    "database"="NEXUS",
    "schema"="history_makers", 
}


# create session
session = Session.builder.configs(CONNECTION_PARAMETERS).create()

