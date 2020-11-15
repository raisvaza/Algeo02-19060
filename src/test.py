def transpose(database, tabel):
    hasil = [[0 for j in range (5)] for i in range (len(database[0]))]
    # mengisi nilai sim dan nama dokumen
    for i in range (len(hasil)):
        hasil[i][3] = tabel[len(tabel) - 1][i + 2]
        hasil[i][0] = tabel[0][i + 2]
    # mengisi judul, jumlah kata, dan kalimat pertama dengan searching
    for i in range (len(hasil)):
        found = False
        j = 0
        while ((j < len(database[0])) and (not found)):
            if (hasil[i][0] == database[0][j]):
                found = True
                hasil[i][1] = database[1][j]
                hasil[i][2] = database[4][j]
                hasil[i][4] = database[3][j]
            j += 1
    return hasil

tabel_sim = [['Term', 'Query', 'dokumen1.txt', 'dokumen2.txt'], ['dokumen', 1, 3, 3], ['ini', 2, 2, 2], ['sangat', 1, 0, 0], ['adalah', 1, 2, 2], ['uwu', 1, 0, 0], [0, 0, 0.7717436331412897, 0.7717436331412897]]
database = [['dokumen1.txt','dokumen2.txt'], ['Judul Dokumen 1','Judul Dokumen 2'], ['Judul Dokumen 1 Ini adalah kalimat pertama dokumen 1. Ini adalah kalimat kedua dokumen 1.','Judul Dokumen 1 Ini adalah kalimat pertama dokumen 2. Ini adalah kalimat kedua dokumen 2.'], ['Ini adalah kalimat pertama dokumen 1.','Ini adalah kalimat pertama dokumen 2.'], [42, 69]]

tabel = transpose(database,tabel_sim)
for i in range (len(tabel)):
    print(tabel[i])
