from extraction import getDataEmg
import pandas as pd


df = getDataEmg()

dataset = {}
for item in df['valueRanges']:
    #     print(item['range'])
    dataset[item['range']] = item['values']


call_center = pd.DataFrame(dataset['Keluhan_CallCenter!A1:Z1004'])
call_center.columns = call_center.iloc[0]
call_center.drop(labels=0, axis=0, inplace=True)

list_drop = call_center[call_center['Jenis Keluhan'].isna()]
call_center.drop(labels=list_drop.index, axis=0, inplace=True)
call_center

ambulance = pd.DataFrame(dataset['Ambulance!A1:AA1000'])
ambulance.columns = ambulance.iloc[0]
ambulance.drop(labels=0, axis=0, inplace=True)

o2 = pd.DataFrame(dataset['Oksigen!A1:Z1000'])
o2.columns = o2.iloc[0]
o2.drop(labels=0, axis=0, inplace=True)

with pd.ExcelWriter('dataset-dashboard/dataset-emergency.xlsx') as writer:
    call_center.to_excel(writer, sheet_name='Call Center', index=False)
    ambulance.to_excel(writer, sheet_name='Ambulance', index=False)
    o2.to_excel(writer, sheet_name='Oksigen', index=False)
