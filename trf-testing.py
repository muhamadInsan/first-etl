from extraction import DataTesting, getDataVaksinasiRedcap
import pandas as pd


# get data testing and fill the param with sheet name on gsheet
df = DataTesting(['Terima Sampel Juli 2021', 'Hasil Juli 2021',
                  'Terima Sampel Agustus 2021', 'Hasil Agustus 2021',
                  'Terima Sampel September 2021', 'Hasil September 2021'])

dataset = {}
for item in df['valueRanges']:
    #     print(item['range'])
    dataset[item['range']] = item['values']

# create dataset from every sheet and drop missing rows
sample_juli = pd.DataFrame(dataset["'Terima Sampel Juli 2021'!A1:S1009"],
                           columns=dataset["'Terima Sampel Juli 2021'!A1:S1009"][0]
                           ).dropna(thresh=4).drop(labels=[0])

hasil_juli = pd.DataFrame(dataset["'Hasil Juli 2021'!A1:Q1010"],
                          columns=dataset["'Hasil Juli 2021'!A1:Q1010"][0]
                          ).dropna(thresh=4).drop(labels=[0])

sample_agst = pd.DataFrame(dataset["'Terima Sampel Agustus 2021'!A1:S1001"],
                           columns=dataset["'Terima Sampel Agustus 2021'!A1:S1001"][0]
                           ).dropna(thresh=4).drop(labels=[0])

hasil_agst = pd.DataFrame(dataset["'Hasil Agustus 2021'!A1:S1001"],
                          columns=dataset["'Hasil Agustus 2021'!A1:S1001"][0]
                          ).dropna(thresh=4).drop(labels=[0])

sample_sept = pd.DataFrame(dataset["'Terima Sampel September 2021'!A1:Z1000"],
                           columns=dataset["'Terima Sampel September 2021'!A1:Z1000"][0]
                           ).dropna(thresh=4).drop(labels=[0])

hasil_sept = pd.DataFrame(dataset["'Hasil September 2021'!A1:S1001"],
                          columns=dataset["'Hasil September 2021'!A1:S1001"][0]
                          ).dropna(thresh=4).drop(labels=[0])

# merge sheet sampel and sheet hasil
pcr_juli = sample_juli.merge(hasil_juli, on='No Lab', how='inner').drop(
    labels=['Nama Lengkap_y', 'Swab ke', 'Form', 'No.', 'Skrining / Tracing'], axis=1)
pcr_agst = sample_agst.merge(hasil_agst, on='No Lab', how='inner').drop(
    labels=['Nama Lengkap_y', 'Swab ke', 'Form', 'NO_y', 'Skrining / Tracing'], axis=1)
pcr_sept = pd.merge(sample_sept, hasil_sept, how="left", on="No Lab").drop(
    labels=['Nama Lengkap_y', 'NO_y', 'Form', 'Swab ke', 'Skrining / Tracing'], axis=1)

# rename columns
pcr_juli.columns = ['no', 'no_lab', 'nama', 'jk', 'nik',
                    'tgl_lahir', 'no_telp', 'jenis_spesimen', 'tgl_swab', 'alamat',
                    'unit_kerja', 'tgl_terima_sampel', 'tgl_periksa',
                    'tgl_hasil', 'kit_pcr', 'RdRP', 'gen_e_n', 'interpretasi',
                    'komentar', 'verifikator']

pcr_agst.columns = ['no', 'no_lab', 'nama', 'jk', 'nik',
                    'tgl_lahir', 'no_telp', 'jenis_spesimen', 'tgl_swab', 'alamat',
                    'unit_kerja', 'tgl_terima_sampel', 'tgl_periksa',
                    'tgl_hasil', 'kit_pcr', 'RdRP', 'gen_n', 'gen_e', 'interpretasi',
                    'komentar', 'verifikator']

pcr_sept.columns = ['no', 'no_lab', 'nama', 'jk',
                    'nik', 'tgl_lahir', 'no_telp', 'jenis_spesimen',
                    'tgl_swab', 'alamat', 'unit_kerja', 'tgl_terima_sampel',
                    'tgl_periksa', 'tgl_hasil', 'kit_pcr', 'ORF1ab', 'gen_n', 'gen_e', 'interpretasi', 'komentar',
                    'verifikator']

# get data vaksinasi only pekerjaan and nik
dataVaksin = getDataVaksinasiRedcap('2021-03-01', '2021-08-22')
dataVaksin.nik.drop_duplicates(inplace=True)

dataVaksin = dataVaksin[['nik', 'pekerjaan', 'tgl_vaksin']]

# merger data vaksinasi and data pcr
juli = pd.merge(pcr_juli, dataVaksin, how="left", on="nik")
agst = pd.merge(pcr_agst, dataVaksin, how="left", on="nik")
sept = pd.merge(pcr_sept, dataVaksin, how="left", on="nik")

juli.pekerjaan.fillna('', inplace=True)
agst.pekerjaan.fillna('', inplace=True)
sept.pekerjaan.fillna('', inplace=True)

# mapping blank value


def isi_pekerjaan(x):
    if x == '':
        x = 'Lainnya'
    return x


juli.pekerjaan = juli['pekerjaan'].map(isi_pekerjaan)
agst.pekerjaan = agst['pekerjaan'].map(isi_pekerjaan)
sept.pekerjaan = sept['pekerjaan'].map(isi_pekerjaan)

# save to dataset dashboard
with pd.ExcelWriter('dataset-dashboard/dataset-testing.xlsx') as writer:
    juli.to_excel(writer, sheet_name='PCR Juli', index=False)
    agst.to_excel(writer, sheet_name='PCR Agustus', index=False)
    sept.to_excel(writer, sheet_name='PCR September', index=False)
