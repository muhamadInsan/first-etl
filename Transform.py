from extraction import getDataVaksinasiRedcap, getDataIsolasi
from datetime import timedelta
import pandas as pd
import numpy as np


# input 2 parameter yaitu tanggal di mulai dan tanggal selesai (mulai_tgl, selesai_tgl)
maret = getDataVaksinasiRedcap('2021-03-25', '2021-03-26')
april = getDataVaksinasiRedcap('2021-04-19', '2021-04-22')
mei = getDataVaksinasiRedcap('2021-05-20', '2021-05-31')
juni = getDataVaksinasiRedcap('2021-06-02', '2021-06-03')
juli_masal = getDataVaksinasiRedcap('2021-07-24', '2021-07-25')
agst_masal1 = getDataVaksinasiRedcap('2021-08-07', '2021-08-08')
agst_masal2 = getDataVaksinasiRedcap('2021-08-14', '2021-08-15')
agst_masal3 = getDataVaksinasiRedcap('2021-08-21', '2021-08-22')
agst_masal4 = getDataVaksinasiRedcap('2021-08-28', '2021-08-29')
sept_masal1 = getDataVaksinasiRedcap('2021-09-04', '2021-09-05')
sept_masal2 = getDataVaksinasiRedcap('2021-09-11', '2021-09-12')

reg_juli = getDataVaksinasiRedcap('2021-07-05', '2021-07-30')
reg_agst = getDataVaksinasiRedcap('2021-08-02', '2021-08-31')
reg_sept = getDataVaksinasiRedcap('2021-09-01', '2021-09-10')

drop = reg_juli[(reg_juli['tgl_vaksin'] == '2021-07-15') &
                (reg_juli['lok_faskes'] == 'Dipatiukur - Klinik Pratama Akademik Padjadjaran Unpad')]
reg_juli = reg_juli.drop(labels=drop.index, axis=0)

drop_masal = reg_agst[(reg_agst['tgl_vaksin'] == '2021-08-07') |
                      (reg_agst['tgl_vaksin'] == '2021-08-08') |
                      (reg_agst['tgl_vaksin'] == '2021-08-14') |
                      (reg_agst['tgl_vaksin'] == '2021-08-15') |
                      (reg_agst['tgl_vaksin'] == '2021-08-21') |
                      (reg_agst['tgl_vaksin'] == '2021-08-22') |
                      (reg_agst['tgl_vaksin'] == '2021-08-28') |
                      (reg_agst['tgl_vaksin'] == '2021-08-29')]

reg_agst = reg_agst.drop(labels=drop_masal.index, axis=0)

masal_sept = reg_sept[(reg_sept['tgl_vaksin'] == '2021-09-04') |
                      (reg_sept['tgl_vaksin'] == '2021-09-05') |
                      (reg_sept['tgl_vaksin'] == '2021-09-11') |
                      (reg_sept['tgl_vaksin'] == '2021-09-12')]

reg_sept = reg_sept.drop(labels=masal_sept.index, axis=0)

maret['tipe'] = 'Masal'
april['tipe'] = 'Masal'
mei['tipe'] = 'Reguler'
juni['tipe'] = 'Reguler'
juli_masal['tipe'] = 'Masal'
agst_masal1['tipe'] = 'Masal'
agst_masal2['tipe'] = 'Masal'
agst_masal3['tipe'] = 'Masal'
agst_masal4['tipe'] = 'Masal'
sept_masal1['tipe'] = 'Masal'
sept_masal2['tipe'] = 'Masal'
reg_juli['tipe'] = 'Masal'
reg_agst['tipe'] = 'Masal'
reg_sept['tipe'] = 'Masal'

df = pd.concat([maret,
                april,
                mei,
                juni,
                juli_masal,
                agst_masal1,
                agst_masal2,
                agst_masal3,
                agst_masal4,
                sept_masal1,
                sept_masal2,
                reg_juli,
                reg_agst,
                reg_sept])

# Transform tanggal vakasin
df['day'] = df.tgl_vaksin.str.slice(8, 10)
df['month'] = df.tgl_vaksin.str.slice(5, 7)
df['year'] = df.tgl_vaksin.str.slice(0, 4)
df['tgl_vaksin'] = pd.to_datetime(
    df[['day', 'month', 'year']], format='%d/%m/%Y')
df.drop(columns=df[['day', 'month', 'year']], inplace=True)

# Transform tanggal lahir
df['day'] = df.tgl_lahir.str.slice(8, 10)
df['month'] = df.tgl_lahir.str.slice(5, 7)
df['year'] = df.tgl_lahir.str.slice(0, 4)
df['tgl_lahir'] = pd.to_datetime(
    df[['day', 'month', 'year']], format='%d/%m/%Y')
df.drop(columns=df[['day', 'month', 'year']], inplace=True)

# Transform tanggal screening
df['day'] = df.tgl_screening.str.slice(8, 10)
df['month'] = df.tgl_screening.str.slice(5, 7)
df['year'] = df.tgl_screening.str.slice(0, 4)
df['tgl_screening'] = pd.to_datetime(
    df[['day', 'month', 'year']], format='%d/%m/%Y')
df.drop(columns=df[['day', 'month', 'year']], inplace=True)

# drop data yg tidak memiliki no tiket, nama petugas entri dan no serial vakasin
data_drop = df.loc[(df['no_tiket'] == '') & (
    df['nama'] == '') & (df['nik'] == '')]
df.drop(labels=data_drop.index, axis=0, inplace=True)

vaksinasi = df[['nm_petugas', 'no_tiket', 'nik', 'nama', 'nip', 'jk',
                'pekerjaan', 'tgl_lahir', 'umur', 'kel_umur', 'alamat', 'tlp', 'bpjs',
                'tgl_screening', 'vaksin', 'dosis', 'tgl_vaksin', 'no_batch',
                'no_serial', 'observasi', 'keluhan', 'keterangan', 'lok_faskes', 'suhu', 'sistole', 'diastole',
                'tanya_1a', 'tanya_1b', 'tanya_3', 'tanya_4', 'tanya_5', 'tanya_6',
                'tanya_2', 'tanya_lansia_1', 'tanya_lansia_2', 'tanya_lansia_3',
                'tanya_lansia_4', 'suhu_bumil', 'sistole_bumil', 'diastole_bumil', 'usia_hamil',
                'tanya_bumil1', 'tanya_bumil2', 'tanya_bumil3', 'tanya_bumil4',
                'tanya_bumil5', 'tanya_bumil6', 'tanya_bumil7', 'tanya_bumil8',
                'kartu_kendali_khusus_ibu_hamil_complete', 'suhu_anak', 'sistole_anak',
                'diastole_anak', 'tanya_anak1', 'tanya_anak2', 'tanya_anak3',
                'tanya_anak4', 'tanya_anak5', 'tanya_anak6', 'tanya_anak7',
                'tanya_anak8', 'tanya_anak9', 'tipe']].reset_index()

vaksinasi.drop(labels='index', axis=1, inplace=True)

# Set vaksin name with CoronaVac
vaksinasi.vaksin = 'CoronaVac'
# delete white space
vaksinasi[['nik', 'no_tiket', 'nip', 'tlp']] = vaksinasi[[
    'nik', 'no_tiket', 'nip', 'tlp']].replace(' ', '')
vaksinasi.nama = vaksinasi.nama.str.upper().str.strip()

vaksinasi.pekerjaan.replace({'A': 'Dosen', 'B': 'Tenaga Kependidikan',
                            'C': 'Mahasiswa', 'D': 'Tenaga Kontrak', 'E': 'Lainnya'}, inplace=True)
vaksinasi.keterangan.replace(
    {'2': 'Lanjut', '1': 'Tunda', '0': 'Tidak diberikan'}, inplace=True)

vaksinasi.bpjs.replace(
    {'1': 'BPJS PBI', '2': 'BPJS Non PBI', '3': 'Non Anggota'}, inplace=True)

vaksinasi.kel_umur.replace(
    {'1': '12-17', '2': '18-30', '3': '31-45', '4': '46-59', '5': '>60'}, inplace=True)

# mapping kelompok umur


def kel_umur(x):
    if (x > '0') & (x < '12'):
        return('belum cukup umur')
    elif (x >= '12') & (x <= '17'):
        return('12-17')
    elif (x >= '18') & (x <= '30'):
        return('18-30')
    elif (x >= '31') & (x <= '45'):
        return('31-45')
    elif (x >= '46') & (x <= '59'):
        return('46-59')
    if x >= '60':
        return('>60')


vaksinasi.kel_umur = vaksinasi['umur'].map(kel_umur)

col_convert_float = ['suhu', 'suhu_anak', 'suhu_bumil', 'sistole', 'diastole',
                     'sistole_anak',
                     'diastole_anak',
                     'sistole_bumil',
                     'diastole_bumil']

for col in col_convert_float:
    vaksinasi[col] = pd.to_numeric(vaksinasi[col], errors='coerce')


# Save Data vaksinasi
vaksinasi.to_excel('dataset-dashboard/data-vaksinasi.xlsx', index=False)
