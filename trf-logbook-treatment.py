from extraction import logbookTreatment, relawanTreatment
import pandas as pd


df = logbookTreatment(['Pasien Asrama dan Non Asrama Unpad', 'Positif C19'])

dataset = {}
for i in df['valueRanges']:
    dataset[i['range']] = i['values']

treatment = pd.DataFrame(
    dataset["'Pasien Asrama dan Non Asrama Unpad'!A1:DQ1007"])
treatment.columns = treatment.iloc[0]
treatment.drop(labels=[1, 0], axis=0, inplace=True)
treatment.columns

treatment = treatment[['NAMA LENGKAP PASIEN', 'USIA', 'ALAMAT', 'NO HP (WA)', 'NIK', 'NPM/ NIP', 'FAKULTAS/ UNIT KERJA', 'KATEGORI PROFESI (TENDIK/DOSEN/KELUARGA/MAHASISWA/KARYAWAN/ SATGAS)',
                       'TANGGAL AWAL KONSUL', 'TANGGAL CHECK IN (ASRAMA ISOLASI UNPAD)', 'TANGGAL CHECK OUT ( ASRAMA ISOLASI UNPAD)', 'RIWAYAT PENYAKIT SEBELUM COVID', 'GOLONGAN DARAH (A/B/AB/O)',
                       'RHESUS ( Rh+/ Rh- )', 'RENCANA TINDAK LANJUT (RUJUK ATAU ISOMAN)', 'BANTUAN OKSIGEN/AMBULANS',
                       'LOKASI ISOMAN ATAU TEMPAT PERAWATAN ( RUMAH/ KOS/ PUPR/ WILASA 8/ EYKMAN/ RS/FASILITAS PEMERINTAH)',
                       'TANGGAL ONSET GEJALA', 'TANGGAL TES DIAGNOSTIK', 'JENIS TES (PCR/ANTIGEN)',
                       'TANGGAL ESTIMASI SELESAI ISOMAN ATAU PERAWATAN', 'RIWAYAT VAKSINASI (BELUM/SUDAH)',
                       'TANGGAL VAKSINASI DOSIS 1', 'TANGGAL VAKSINASI DOSIS 2',
                       'HASIL FU 1', 'TREATMENT 1', 'HASIL FU 2', 'TREATMENT 2',
                       'HASIL FU 3', 'TREATMENT 3', 'HASIL FU 4', 'TREATMENT 4',
                       'HASIL FU 5', 'TREATMENT 5', 'HASIL FU 6', 'TREATMENT 6',
                       'HASIL FU 7', 'TREATMENT 7', 'HASIL FU 8', 'TREATMENT 8',
                       'HASIL FU 9', 'TREATMENT 9', 'HASIL FU 10', 'TREATMENT 10',
                       'HASIL FU 11', 'TREATMENT 11', 'HASIL FU 12', 'TREATMENT 12',
                       'HASIL FU 13', 'TREATMENT 13', 'HASIL FU 14', 'TREATMENT 14',
                       'HASIL FU 15', 'TREATMENT 15', 'HASIL FU 16', 'TREATMENT 16',
                       'HASIL FU 17', 'TREATMENT 17', 'HASIL FU 18', 'TREATMENT 18',
                       'HASIL FU 19', 'TREATMENT 19', 'HASIL FU 20', 'TREATMENT 20', 'PULANG PAKSA/SELESAI ISOMAN (KHUSUS UNTUK PASIEN ASRAMA)', 'OUTCOME (SEMBUH/MENINGGAL)', 'RELAWAN YANG MENANGANI', 'ASAL FAKULTAS RELAWAN']]

treatment = treatment.rename(columns={'NAMA LENGKAP PASIEN': 'nm_pasien', 'USIA': 'usia',
                                      'ALAMAT': 'alamat', 'NO HP (WA)': 'tlp', 'NIK': 'nik', 'NPM/ NIP': 'npm_nip', 'FAKULTAS/ UNIT KERJA': 'unit_kerja',
                                      'KATEGORI PROFESI (TENDIK/DOSEN/KELUARGA/MAHASISWA/KARYAWAN/ SATGAS)': 'profesi',
                                      'TANGGAL AWAL KONSUL': 'tgl_konsul', 'TANGGAL CHECK IN (ASRAMA ISOLASI UNPAD)': 'tgl_checkin', 'TANGGAL CHECK OUT ( ASRAMA ISOLASI UNPAD)': 'tgl_checkout', 'RIWAYAT PENYAKIT SEBELUM COVID': 'riwayat_sakit', 'GOLONGAN DARAH (A/B/AB/O)': 'goldar',
                                      'RHESUS ( Rh+/ Rh- )': 'rhesus', 'RENCANA TINDAK LANJUT (RUJUK ATAU ISOMAN)': 'fu_pasien', 'BANTUAN OKSIGEN/AMBULANS': 'bantuan_diterima',
                                      'LOKASI ISOMAN ATAU TEMPAT PERAWATAN ( RUMAH/ KOS/ PUPR/ WILASA 8/ EYKMAN/ RS/FASILITAS PEMERINTAH)': 'lokasi_isoman',
                                      'TANGGAL ONSET GEJALA': 'tgl_onset_gejala', 'TANGGAL TES DIAGNOSTIK': 'tgl_test', 'JENIS TES (PCR/ANTIGEN)': 'jenis_test',
                                      'TANGGAL ESTIMASI SELESAI ISOMAN ATAU PERAWATAN': 'est_selesai_isolasi', 'RIWAYAT VAKSINASI (BELUM/SUDAH)': 'riwayat_vaksin',
                                      'TANGGAL VAKSINASI DOSIS 1': 'tgl_vaksin1', 'TANGGAL VAKSINASI DOSIS 2': 'tgl_vaksin2',
                                      'HASIL FU 1': 'fu_1', 'TREATMENT 1': 'treatment_1', 'HASIL FU 2': 'fu_2', 'TREATMENT 2': 'treatment_2',
                                      'HASIL FU 3': 'fu_3', 'TREATMENT 3': 'treatment_3', 'HASIL FU 4': 'fu_4', 'TREATMENT 4': 'treatment_4',
                                      'HASIL FU 5': 'fu_5', 'TREATMENT 5': 'treatment_5', 'HASIL FU 6': 'fu_6', 'TREATMENT 6': 'treatment_6',
                                      'HASIL FU 7': 'fu_7', 'TREATMENT 7': 'treatment_7', 'HASIL FU 8': 'fu_8', 'TREATMENT 8': 'treatment_8',
                                      'HASIL FU 9': 'fu_9', 'TREATMENT 9': 'treatment_9', 'HASIL FU 10': 'fu_10', 'TREATMENT 10': 'treatment_10',
                                      'HASIL FU 11': 'fu_11', 'TREATMENT 11': 'treatment_11', 'HASIL FU 12': 'fu_12', 'TREATMENT 12': 'treatment_12',
                                      'HASIL FU 13': 'fu_13', 'TREATMENT 13': 'treatment_13', 'HASIL FU 14': 'fu_14', 'TREATMENT 14': 'treatment_14',
                                      'HASIL FU 15': 'fu_15', 'TREATMENT 15': 'treatment_15', 'HASIL FU 16': 'fu_16', 'TREATMENT 16': 'treatment_16',
                                      'HASIL FU 17': 'fu_17', 'TREATMENT 17': 'treatment_17', 'HASIL FU 18': 'fu_18', 'TREATMENT 18': 'treatment_18',
                                      'HASIL FU 19': 'fu_19', 'TREATMENT 19': 'treatment_19', 'HASIL FU 20': 'fu_20', 'TREATMENT 20': 'treatment_20', 'PULANG PAKSA/SELESAI ISOMAN (KHUSUS UNTUK PASIEN ASRAMA)': 'status_isoman', 'OUTCOME (SEMBUH/MENINGGAL)': 'kondisi_akhir', 'RELAWAN YANG MENANGANI': 'nm_relawan', 'ASAL FAKULTAS RELAWAN': 'fakultas_relawan'})

treatment[[
    'tgl_konsul',
    'tgl_checkin',
    'tgl_test',
    'tgl_onset_gejala',
    'est_selesai_isolasi',
    'tgl_checkout',
    'tgl_vaksin1',
    'tgl_vaksin2']] = treatment[[
        'tgl_konsul',
        'tgl_checkin',
        'tgl_test',
        'tgl_onset_gejala',
        'est_selesai_isolasi',
        'tgl_checkout',
        'tgl_vaksin1',
        'tgl_vaksin2']].replace('-', '').astype('datetime64[ns]')


# treatment['tlp'] = treatment['tlp'].str.replace('[^\d]d+', '', regex=True)
treatment.tlp = treatment.tlp.str.replace('[^\d]+', '', regex=True)
treatment.nm_pasien = treatment.nm_pasien.str.upper()
treatment[['tlp', 'nik', 'npm_nip']] = treatment[[
    'tlp', 'nik', 'npm_nip']].replace('-', '')

# List Relawan Treatment
relawan = treatment[['nm_relawan', 'fakultas_relawan']].drop_duplicates()
relawan.dropna(inplace=True)

with pd.ExcelWriter('dataset-dashboard/dataset-logbook-treatment.xlsx') as writer:
    treatment.to_excel(writer, sheet_name='Treatmen', index=False)
    relawan.to_excel(writer, sheet_name='Daftar Relawan', index=False)
