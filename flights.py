#%%
import pandas as pd

years_list=list(range(1987, 1996+1))
years_list.remove(1988)
path='data-analytics-files/'
year_dataframes={}
for year in years_list:
    filepath=path+str(year)+'.csv'
    year_dataframes[str(year)]=pd.read_csv(filepath)
# %%
test_df=year_dataframes['1987']
test_df.info()
test_df['TailNum']
# %%

# %%
