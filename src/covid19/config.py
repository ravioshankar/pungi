from pathlib import Path
import numpy
import pandas as pd
data_dir_raw = Path('../data/covid_19_India')
age_group_details = pd.read_csv(data_dir_raw/'AgeGroupDetails.csv')
covid_19_data = pd.read_csv(data_dir_raw/'covid_19_data.csv')