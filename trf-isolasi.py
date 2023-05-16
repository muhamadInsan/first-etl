from extraction import getDataIsolasi
from datetime import timedelta
import pandas as pd
import numpy as np

###################################ASRAMA ISOLASI###############################################################

isolasi = getDataIsolasi()
# data asrama purppy
asrama_pupr = isolasi['pupr']
# data asrama wilasa 8
asrama_wilasa8 = isolasi['wilasa8']


# create header asrama pupr
asrama_pupr.columns = asrama_pupr.iloc[0]
asrama_wilasa8.columns = asrama_wilasa8.iloc[3]
# create header asrama wilasa8
asrama_pupr.drop(labels=[0, 1], axis=0, inplace=True)
asrama_wilasa8.drop(labels=[0, 1, 2, 3, 4], axis=0, inplace=True)
# add status asrama, concate data sarama pupr & wilasa 8
asrama_pupr['asrama'] = 'PUPR'
asrama_wilasa8['asrama'] = 'WILASA8'
asrama_isolasi = pd.concat([asrama_pupr, asrama_wilasa8])

# drop row missing data
drop = asrama_isolasi[asrama_isolasi.NAMA.isna()]
asrama_isolasi = asrama_isolasi.drop(labels=drop.index, axis=0)

# simplify column name
asrama_isolasi.rename(columns={"Nomor WhatsApp": "whatsapp",
                               "TANGGAL CHECK IN": "checkin",
                               "TANGGAL CHECK OUT": "checkout",
                               "FAKULTAS/UNIT KERJA": "unit kerja",
                               "JAM CHECK IN": "jam checkin",
                               "JAM CHECK OUT": "jam checkout",
                               "Tanggal mulai sakit (ONSET) (Untuk yg bergejala)\n": "mulai sakit",
                               "Antigen = 1\nPCR = 2": "jenis test",
                               "Estimasi Check Out 10 hari setelah Test (jika tidak bergejala sejak awal)": "estimasi checkout 10",
                               "Estimasi Check Out 13 hari setelah ONSET (jika bergejala dan hari ke 10 hilang gejalanya)": "estimasi checkout 13",
                               "BOR per bulan (%) sudah termasuk jeda bersihkan kamar": "BOR /bulan",
                               "BOR per 1/2 bulan (%) sudah termasuk jeda bersihkan kamar": "BOR 1/2 bulan"}, inplace=True)

asrama_isolasi = asrama_isolasi[['NO',
                                 'NAMA',
                                 'whatsapp',
                                 'NPM/NIP/NIK',
                                 'unit kerja',
                                 'checkin',
                                 'checkout',
                                 'jam checkin',
                                 'jam checkout',
                                 'mulai sakit',
                                 'Tanggal test',
                                 'jenis test',
                                 'Keterangan',
                                 'asrama']].replace('-', '')

# replace month to standar date
bulan = {'Januari': '01', 'Februari': '02', 'Maret': '03', 'April': '04', 'Mei': '05', 'Juni': '06',
         'Juli': '07', 'Agustus': '08', 'September': '09', 'Oktober': '10', 'November': '11', 'Desember': '12'}

for checkin in asrama_isolasi.checkin:
    for bln in bulan.items():
        asrama_isolasi['checkin'] = asrama_isolasi.checkin.str.replace(
            bln[0], '/'+bln[1]+'/')

for checkin in asrama_isolasi.checkout:
    for bln in bulan.items():
        asrama_isolasi['checkout'] = asrama_isolasi.checkout.str.replace(
            bln[0], '/'+bln[1]+'/')

for checkin in asrama_isolasi['Tanggal test']:
    for bln in bulan.items():
        asrama_isolasi['Tanggal test'] = asrama_isolasi['Tanggal test'].str.replace(
            bln[0], '/'+bln[1]+'/')

# replace tanda pemisah tanggal
asrama_isolasi.checkout = asrama_isolasi['checkout'].str.replace('-', '/')
asrama_isolasi.checkin = asrama_isolasi['checkin'].str.replace('-', '/')

# create date format standart for checkin
asrama_isolasi[['day', 'month', 'year']
               ] = asrama_isolasi["checkin"].str.split("/", expand=True)
asrama_isolasi.checkin = pd.to_datetime(
    asrama_isolasi[['day', 'month', 'year']], format='%d%m%Y')
asrama_isolasi.drop(
    columns=asrama_isolasi[['day', 'month', 'year']], inplace=True)

# create date format standart for checkout
asrama_isolasi[['day', 'month', 'year']
               ] = asrama_isolasi["checkout"].str.split("/", expand=True)
asrama_isolasi.checkout = pd.to_datetime(
    asrama_isolasi[['day', 'month', 'year']], format='%d%m%Y')
asrama_isolasi.drop(
    columns=asrama_isolasi[['day', 'month', 'year']], inplace=True)

# Create new column calculation
asrama_isolasi['estimasi checkout 10'] = asrama_isolasi['checkin'] + \
    timedelta(days=10)
asrama_isolasi['estimasi checkout 13'] = asrama_isolasi['checkin'] + \
    timedelta(days=13)
asrama_isolasi['lama isolasi'] = asrama_isolasi.checkout - \
    asrama_isolasi.checkin
asrama_isolasi['BOR (%)'] = np.round(
    asrama_isolasi['lama isolasi'].dt.days/(50*31)*100, decimals=3)

asrama_isolasi['jenis test'].replace(
    {'1': 'Antigen', '2': 'PCR'}, inplace=True)

# Save Data isolasi
# asrama_isolasi.to_excel('dataset-dashboard/data-isolasi.xlsx', index=False)

# HITUNG BOR
io = asrama_isolasi[['asrama', 'checkin', 'checkout']].dropna()
io = io.reset_index().drop(labels='index', axis=1)

# BOR asrama PUPR
io_pupr = io[io['asrama'] == 'PUPR']

pupr = {}
_pupr = {}


def lokasi_pupr():
    for date in io_pupr.index:
        pupr[date] = pd.date_range(
            start=io_pupr.checkin[date], end=io_pupr.checkout[date])
    for k in pupr:
        _pupr[k] = pd.DataFrame(pupr[k])

    final_pupr = pd.concat(_pupr).reset_index().drop(
        labels='level_0', axis=1).rename(columns={0: 'hari_perawatan'})
    final_pupr = final_pupr[(final_pupr['hari_perawatan'] >= '2021-05-30')
                            & (final_pupr['hari_perawatan'] <= '2021-12-30')]
    final_pupr = final_pupr['hari_perawatan'].value_counts(
        sort=False).reset_index()

    return final_pupr


def hari_rawat_pupr(tgl_mulai, tgl_selesai):
    return lokasi_pupr()[(lokasi_pupr()['index'] >= tgl_mulai) & (lokasi_pupr()['index'] <= tgl_selesai)].hari_perawatan.sum()


jml_tt_pupr = 78

data_pupr = {'Periode (Asrama PURP)': ['01 - 15 Juni', '16 - 30 Juni', '01 - 15 Juli', '16 - 31 Juli', '01 - 15 Agustus'],
             'Hari Periwatan': [hari_rawat_pupr('2021-06-01', '2021-06-15'),
                                hari_rawat_pupr('2021-06-16', '2021-06-30'),
                                hari_rawat_pupr('2021-07-01', '2021-07-15'),
                                hari_rawat_pupr('2021-07-16', '2021-07-31'),
                                hari_rawat_pupr('2021-08-01', '2021-08-15')],
             'BOR(%)': [(hari_rawat_pupr('2021-06-01', '2021-06-15')/(jml_tt_pupr*15))*100,
                        (hari_rawat_pupr('2021-06-16', '2021-06-30') /
                         (jml_tt_pupr*15))*100,
                        (hari_rawat_pupr('2021-07-01', '2021-07-15') /
                         (jml_tt_pupr*15))*100,
                        (hari_rawat_pupr('2021-07-16', '2021-07-31') /
                         (jml_tt_pupr*15))*100,
                        (hari_rawat_pupr('2021-08-01', '2021-08-15')/(jml_tt_pupr*15))*100, ]}

bor_pupr = pd.DataFrame(data_pupr)

# BOR Asrama Wilasa 8
io_wilasa8 = io[io['asrama'] == 'WILASA8']

wilasa8 = {}
_wilasa8 = {}


def lokasi_wilasa8():
    for date in io_wilasa8.index:
        wilasa8[date] = pd.date_range(
            start=io_wilasa8.checkin[date], end=io_wilasa8.checkout[date])
    for k in wilasa8:
        _wilasa8[k] = pd.DataFrame(wilasa8[k])

    final_wilasa8 = pd.concat(_wilasa8).reset_index().drop(
        labels='level_0', axis=1).rename(columns={0: 'hari_perawatan'})
    final_wilasa8 = final_wilasa8[(final_wilasa8['hari_perawatan'] >=
                                   '2021-05-30') & (final_wilasa8['hari_perawatan'] <= '2021-12-30')]
    final_wilasa8 = final_wilasa8['hari_perawatan'].value_counts(
        sort=False).reset_index()

    return final_wilasa8


def hari_rawat_wilasa8(tgl_mulai, tgl_selesai):
    return lokasi_wilasa8()[(lokasi_wilasa8()['index'] >= tgl_mulai) & (lokasi_wilasa8()['index'] <= tgl_selesai)].hari_perawatan.sum()


jml_tt_wilasa8 = 66
data_wilasa8 = {'Periode (Asrama Wilasa8)': ['01 - 15 Juni', '16 - 30 Juni', '01 - 15 Juli', '16 - 31 Juli', '01 - 15 Agustus'],
                'Hari Periwatan': [hari_rawat_wilasa8('2021-06-01', '2021-06-15'),
                                   hari_rawat_wilasa8(
                                       '2021-06-16', '2021-06-30'),
                                   hari_rawat_wilasa8(
                                       '2021-07-01', '2021-07-15'),
                                   hari_rawat_wilasa8(
                                       '2021-07-16', '2021-07-31'),
                                   hari_rawat_wilasa8('2021-08-01', '2021-08-15')],
                'BOR(%)': [(hari_rawat_wilasa8('2021-06-01', '2021-06-15')/(jml_tt_wilasa8*15))*100,
                           (hari_rawat_wilasa8('2021-06-16', '2021-06-30') /
                            (jml_tt_wilasa8*15))*100,
                           (hari_rawat_wilasa8('2021-07-01', '2021-07-15') /
                            (jml_tt_wilasa8*15))*100,
                           (hari_rawat_wilasa8('2021-07-16', '2021-07-31') /
                            (jml_tt_wilasa8*15))*100,
                           (hari_rawat_wilasa8('2021-08-01', '2021-08-15')/(jml_tt_wilasa8*15))*100, ]}

bor_wilasa8 = pd.DataFrame(data_wilasa8)

with pd.ExcelWriter('dataset-dashboard/data-isolasi.xlsx') as writer:
    asrama_isolasi.to_excel(writer, sheet_name='Isolasi', index=False)
    bor_pupr.to_excel(writer, sheet_name='Bor PUPR', index=False)
    bor_wilasa8.to_excel(writer, sheet_name='Bor WILASA8', index=False)
