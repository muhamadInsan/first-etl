from googleapiclient.discovery import build
from google.oauth2 import service_account
from datetime import timedelta
from extraction import getDataTreatment
import re
import pandas as pd
import numpy as np


df = getDataTreatment()
asrama_pupr = df['pupr']
asrama_wilasa8 = df['wilasa8']

# # create header asrama pupr
asrama_pupr.columns = asrama_pupr.iloc[0]
asrama_pupr.columns = asrama_pupr.iloc[0].combine_first(asrama_pupr.iloc[1])
asrama_pupr = asrama_pupr[['NPM/NIP/NIK', 'NAMA', 'Nakes yang manangani', 'Kondisi harian (hari isoman)', '2',
                           '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']]
asrama_pupr = asrama_pupr.rename(columns={'NPM/NIP/NIK': 'nik', 'NAMA': 'nama',
                                 'Nakes yang manangani': 'nm_nakes', 'Kondisi harian (hari isoman)': '1'})
treatment_pupr = asrama_pupr.drop(labels=[0, 1], axis=0)

# create header asrama wilasa8
asrama_wilasa8.columns = asrama_wilasa8.iloc[3]
asrama_wilasa8.columns = asrama_wilasa8.iloc[3].combine_first(
    asrama_wilasa8.iloc[4])
asrama_wilasa8 = asrama_wilasa8[['NPM/NIP/NIK', 'NAMA', 'Nakes yang menangani', 'Kondisi', '2', '3', '4', '5',
                                 '6', '7', '8', '9', '10', '11', '12', '13']]
asrama_wilasa8 = asrama_wilasa8.rename(columns={'NPM/NIP/NIK': 'nik',
                                                'NAMA': 'nama', 'Nakes yang menangani': 'nm_nakes', 'Kondisi': '1'})
treatment_wilasa8 = asrama_wilasa8.drop(labels=[0, 1, 2, 3, 4], axis=0)

drop_pupr = treatment_pupr[treatment_pupr.nik.isna()]
treatment_pupr = treatment_pupr.drop(labels=drop_pupr.index, axis=0)
drop_wilasa8 = treatment_wilasa8[treatment_wilasa8.nik.isna()]
treatment_wilasa8 = treatment_wilasa8.drop(labels=drop_wilasa8.index, axis=0)

treatment = pd.concat([treatment_pupr, treatment_wilasa8])

treatment.to_excel('dataset-dashboard/dataset-treatment.xlsx', index=False)
