from module.crossart_generator.chart_module.chart import load_chart
from module.crossart_generator.component_module.viz import draw_chart
import streamlit as st
import pandas as pd
from typing import Any

def issue_warning()->Any:
    '''
    Streamlit component to warn user regarding the type of uploaded file. 

    Args:
        - None

    Return:
        - streamlit subheader display.
    '''
    st.subheader(
        "Upload Crosstab result in .xlsx format only"
    )

def upload_crosstabs()->pd.DataFrame:
    '''
    Streamlit component for the user to upload file that contains crosstabs table.

    Args:
        - None

    Return:
        - df_charts: streamlit dataframe, Uploadedfile sub-class of BytesIO. 
    '''
    st.warning(
        "Please ensure the file contains the **CROSSTAB TABLE**:heavy_exclamation_mark::heavy_exclamation_mark: prior to uploading.", 
        icon="❗"
        )
    df_charts = st.file_uploader("Upload the file here:")
    return df_charts

def error_warning()->st.error:
    '''
    Streamlit component to display error to user when the uploaded file did not contain crosstabs table. 

    Args:
        - None

    Return:
        - streamlit error display.
    '''
    st.error(
        "The file should contain the crosstabs table!", 
        icon="🚨"
        )

def init_chart_gen():
    '''
    Composite function to run the front-end of the chart generator streamlit based on logic. 

    Args:
        - None

    Return:
        - None
    '''
    issue_warning()
    try:
        df_charts = upload_crosstabs()
        if df_charts:
            dfs, sheet_names, df_chartsname = load_chart(df_charts=df_charts, filename=True)
            df_charts = draw_chart(dfs=dfs, sheet_names=sheet_names)
            df_chartsname = df_chartsname[:df_chartsname.find('.')]
            st.balloons()
            st.header("Charts ready for download!")
            st.download_button(
                label='📥 Download', 
                data=df_charts, 
                file_name= df_chartsname + '-charts.xlsx'
                )
    except:
        error_warning()