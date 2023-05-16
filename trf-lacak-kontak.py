from extraction import getDataLacakKontak
import pandas as pd
import numpy as np


df = getDataLacakKontak()

kontak_erat = df[df['pdp_name2'] == '']
kontak_erat = kontak_erat.drop(
    labels=['pdp_name2', 'nik_npm', 'sex', 'date_of_birth', 'date_of_interview'], axis=1)
kontak_erat.head()

index_case = df[df['pdp_name2'] != '']
index_case = index_case[['record_id', 'pdp_name2',
                         'nik_npm', 'sex', 'date_of_birth', 'date_of_interview']]

lacak_kontak = pd.merge(index_case, kontak_erat, on='record_id', how='outer')

lacak_kontak.to_excel(
    'dataset-dashboard/dataset-lacakkontak.xlsx', index=False)
