import streamlit as st
import pandas as pd
import requests
from module.survey_weighting_R.utils_module.utils import (
    convert_list_to_dict, 
    convert_df_to_json,
    convert_dict_to_json
    )

url = st.secrets["survey_weighting"]["ENDPOINT"]

def calc_weight(
        df:pd.DataFrame, 
        sample_list:list[str], 
        pop_list:list[pd.DataFrame], 
        lower_limit:int, 
        upper_limit:int):
    '''
    Backend function to calculate the weight of cleaned survey responses.
    This script serves as the top script for the back-end of the survey weighting R.

    Args:
        - df: pandas DataFrame 
        - sample_list: List of name of the selected demography columns. 
        - pop_list: List of pandas DataFrame. 
        - lower_limit: lower limit for the trimmed_weight column.
        - upper_limit: upper limit for the trimmed_weight column.

    Return:
        - response.json: TBD
    '''
    survey_data = convert_df_to_json(df=df)
    pop_dict = convert_list_to_dict(pop_list=pop_list)
    sample_dict = {
        "sample_list": sample_list
        }
    sample_list_json = convert_dict_to_json(sample_dict)
    limit_dict = {
        "lower_limit": lower_limit,
        "upper_limit": upper_limit
    }
    limit = convert_dict_to_json(limit_dict)
    response = requests.post(
        url=url,
        json={
            "survey_file": survey_data,
            "sample_list_json": sample_list_json,
            "pop_list_json": pop_dict,
            "limit": limit
        }
    )

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response}"
