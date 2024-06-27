import streamlit as st
import pandas as pd
import requests
from module.survey_weighting_R.utils_module.utils import convert_list_to_dict, convert_df_to_json

url = st.secrets["survey_weighting"]["ENDPOINT"]

def calc_weight(
        df:pd.DataFrame, 
        sample_list:list[str], 
        pop_list:list[pd.DataFrame], 
        lower_limit:int, 
        upper_limit:int):
    '''
    
    '''
    survey_data = convert_df_to_json(df=df)
    pop_dict = convert_list_to_dict(pop_list=pop_list)
    query_params = {
        "sample_list_json": ",".join(sample_list),
        "lower_limit": lower_limit,
        "upper_limit": upper_limit
    }
    # response = requests.post(
    #     url=url,
    #     params=query_params,
    #     json={
    #         "survey_file": survey_data,
    #         "pop_list_json": pop_dict
    #     }
    # )
    response  = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response}"
