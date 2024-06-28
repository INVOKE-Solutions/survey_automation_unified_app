import pandas as pd
import re
from typing import Dict
import json

def load(df:pd.DataFrame)->pd.DataFrame:
    '''
    A function to read and load the streamlit dataframe into pandas dataframe.

    Args:
        - df: Whole dataframe [streamlit dataframe]

    Return:
        - df: a pandas dataframe
    '''
    df_name = df.name

    # check file type and read them accordingly
    if df_name[-3:] == 'csv':
        df = pd.read_csv(df, na_filter=False)
    else:
        df = pd.read_excel(df, na_filter=False)
    
    return df

def demography(df:pd.DataFrame)->list:
    '''
    A function to autoselect the demography columns. 

    Args:
        - df: Whole dataframe [pandas dataframe]

    Return:
        - default_demo: listof the column that contains string like 'age', 'gender', 'eth', 'income', 'urban'.
    '''
    default_demo = ['age', 'gender', 'eth', 'income', 'urban']
    data_list = list(df.columns)
    pattern = re.compile('|'.join(default_demo), re.IGNORECASE)
    default_demo = [item for item in data_list if pattern.search(item) and len(item.split()) <= 2]

    return default_demo

def sorter(demo:str, df:pd.DataFrame)->list[str]:
    '''
    A function to sort the list of the unique value in the demographic column.

    Args:
        - demo: Column name of the demography you're building the table on [str]
        - df: Whole dataframe [pandas dataframe]

    Return:
        - sorted list of unique values from specific column in the dataframe
    '''
    if re.search(r'age', demo, re.IGNORECASE):
        return sorted(list(df[demo].unique()))

    elif re.search(r'gender', demo, re.IGNORECASE):
        return sorted(list(df[demo].unique()),
                      key=lambda x: (re.match(r'^M|^L', x, re.IGNORECASE) is None,
                                     re.match(r'^F|^P', x, re.IGNORECASE) is None))

    elif re.search(r'eth', demo, re.IGNORECASE):
        return sorted(list(df[demo].unique()),
                      key=lambda x: (0 if re.match(r'^M', x, re.IGNORECASE) else
                                     1 if re.match(r'^C', x, re.IGNORECASE) else
                                     2 if re.match(r'^I', x, re.IGNORECASE) else
                                     3 if re.match(r'^B', x, re.IGNORECASE) else
                                     4 if re.match(r'^O|^L', x, re.IGNORECASE) else 5))

    elif re.search(r'income', demo, re.IGNORECASE):
        return sorted(list(df[demo].unique()))

    elif re.search(r'urban', demo, re.IGNORECASE):
        return sorted(list(df[demo].unique()),
                      key=lambda x: (0 if re.match(r'^U|^B', x) else
                                     1 if re.match(r'^S', x) else
                                     2 if re.match(r'^R|^L', x) else 3))

def convert_list_to_dict(pop_list:list[pd.DataFrame])->Dict:
    '''
    A function to transform list of pandas data frame into dictionary to pass to endpoint.

    Args:
        - pop_list: List of pandas dataframe

    Return:
        - pop_dict: Dictionary of list of pandas data frame
    '''
    pop_dict = {}
    for df in pop_list:
        df_name = df.columns[0]
        df_records = df.to_dict(orient="records")
        pop_dict[df_name] = df_records

    return pop_dict

def convert_df_to_json(df: pd.DataFrame)->str:
    """
    A function to convert a pandas Data Frame to JSON string format.

    Args:
        df: Survey data in pandas Data Frame

    Returns:
        final_json: JSON string
    """
    json_data = df.to_json(orient='records')
    json_object = {"data": json.loads(json_data)}
    final_json = json.dumps(json_object, indent=2)
    return final_json

def convert_dict_to_json(input_dict: Dict)->str:
    '''
    A function to convert dictionary to JSON string format.

    Args:
        input_dict: Dictionary data

    Returns:
        json_string: JSON string
    '''
    json_string = json.dumps(input_dict, indent=2)
    return json_string

def json_to_df(response:list[Dict]):
    '''
    A function to convert JSON response into pandas Data Frame.

    Args:
        response: JSON response

    Returns:
        df: pandas Data Frame
    '''
    df = pd.read_json(response)
    return df