import streamlit as st
import pandas as pd
from typing import Any
from module.survey_weighting_R.utils_module.utils import load, demography, sorter
from module.utils.ui_components import ui_divider
from module.survey_weighting_R.weighting_module.weighting import calc_weight

def upload_file()->Any:
    '''
    Streamlit component for the user to upload the file.

    Args:
        - None

    Return:
        - df: streamlit dataframe, Uploadedfile sub-class of BytesIO. 
    '''
    st.subheader("Upload cleaned survey responses (csv/xlsx)")
    df = st.file_uploader(
        "Please ensure the data are cleaned prior to uploading to be weighted."
        )
    return df

def read_file(df:Any)->tuple[pd.DataFrame,str]:
    '''
    Component to read file from streamlit dataframe.

    Args:
        - df: streamlit dataframe, Uploadedfile sub-class of BytesIO. 

    Return:
        - read_df: pandas dataframe
        - df_name: Name of the uploaded file
    '''
    df_name = df.name
    read_df = load(df)
    return read_df, df_name

def demography_selection(df:pd.DataFrame)->list[str]:
    '''
    Component for user to select `demography` column from the dataframe.

    Args:
        - df: pandas dataframe 

    Return:
        - demos: List of name of the selected demography columns.
    '''
    demos = st.multiselect(
        "Choose the demograhic(s) you want to build the crosstabs across",
        list(df.columns) + demography(df),
        demography(df)
        )
    return demos

def get_dist_value(df:pd.DataFrame, sample_list:list)->list[pd.DataFrame]:
    '''
    Component for user to input the distribution value for unique value 
    of `demography` column in sample_list manually.

    Args:
        - df: pandas dataframe
        - sample_list: List of name of the selected demography columns.

    Return:
        - pop_list: List of pandas dataframe
    '''
    pop_dict = {}
    for demo in sample_list:
        temp_df = pd.DataFrame(columns=[demo, 'freq'])
        sorted_list = sorter(demo, df=df)
        for x in sorted_list:
            unique_value = x
            value = st.number_input(
                f"{x} distribution for {demo}:", 
                max_value=1.0
                )
            new_value = len(df) * value
            new_dist = {
                demo: unique_value, 
                'freq': new_value
                }
            temp_df = pd.concat(
                [temp_df, pd.DataFrame(new_dist, index=[0])], 
                ignore_index=True
                )
        pop_dict[f"{demo}_dist"] = temp_df
    pop_list = list(pop_dict.values())
    return pop_list

def input_lower_limit():
    lower_limit = st.number_input(
        f"Lower limit for the trimmed weights:",
        min_value=0.3,
        value=0.3
    )
    return lower_limit

def input_upper_limit():
    upper_limit = st.number_input(
        f"Upper limit for the trimmed weights:",
        value=3
    )
    return upper_limit

def init_survey_weighting():
    '''
    Composite function to run the front-end of the crosstabs streamlit based on logic. 

    Args:
        - None

    Return:
        - None
    '''
    df = upload_file()
    if df:
        df, df_name = read_file(df=df)
        sample_list = demography_selection(df=df)
        ui_divider()
        if len(sample_list) > 0:
            pop_list = get_dist_value(df=df, sample_list=sample_list)
            ui_divider()
            if pop_list:
                lower_limit = input_lower_limit()
                if lower_limit:
                    upper_limit = input_upper_limit()
                    button = st.button("Calculate Weights")
                    if button:
                        df_weighted = calc_weight(
                            df=df,
                            sample_list=sample_list,
                            pop_list=pop_list,
                            lower_limit=lower_limit,
                            upper_limit=upper_limit
                        )
                        st.dataframe(df_weighted)
                        # display summary untrimmed
                        # display summary trimmed
                        df_name = df_name[:df_name.find('.')]
                        st.balloons()
                        st.header('Weighted survey ready for download!')
                        st.download_button(
                            label='📥 Download', 
                            data=df_weighted, 
                            file_name= df_name + '-weighted.xlsx'
                            )
        