#%%
import pandas as pd

def remove_nan_columns(df):
    '''removes any columns where every value is null/NaN'''
    missing_columns = [col for col in df.columns if df[col].isnull().all()]
    reduced_df = test_df.drop(axis=1, columns=missing_columns)
    return reduced_df

def replace_nan_elements(df):
    '''replaces any elenents == NULL or NAN with 0'''

def load_all_dataframes():
    years_list=list(range(1987, 1996+1))
    years_list.remove(1988)
    path='data-analytics-files/'
    year_dataframes={}
    for year in years_list:
        filepath=path+str(year)+'.csv'
        year_dataframes[str(year)]=remove_nan_columns(pd.read_csv(filepath))

if __name__ == '__main__':
    load_all_dataframes()








# %%

# %%
