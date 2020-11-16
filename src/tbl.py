import math
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# database = [['dokumen1.txt','dokumen2.txt'], ['Judul Dokumen 1','Judul Dokumen 2'], ['Judul Dokumen 1 Ini adalah kalimat pertama dokumen 1. Ini adalah kalimat kedua dokumen 1.','Judul Dokumen 1 Ini adalah kalimat pertama dokumen 2. Ini adalah kalimat kedua dokumen 2.'], ['Ini adalah kalimat pertama dokumen 1.','Ini adalah kalimat pertama dokumen 2.'], [42, 69]]
# INI ADALAH CONTOH

def tabelVektor(database):
    # deklarasi
    term_terpakai = 0
    banyak_dokumen = len(database[0])
    banyak_term = 0
    # banyak_term = 15
    # INI ADALAH CONTOH
    for z in range (banyak_dokumen):
        term1 = stem(database[2][z])
        term2 = removeStopWord(term1)
        banyak_term += len(term2.split())
    tabel = [[0 for j in range (banyak_dokumen + 1)] for i in range (banyak_term + 1)]

    # pengisian baris pertama termasuk kode (nama) dokumen
    tabel[0][0] = 'Term'
    for j in range (1, banyak_dokumen + 1):
        tabel[0][j] = database[0][j - 1]

    for z in range (banyak_dokumen):
        # pembersihan dokumen
        isi = stem(database[2][z])
        isi = removeStopWord(isi)
        term_isi = isi.rsplit(" ")
        # term_isi = ['judul', 'dokumen', '1', 'ini', 'adalah', 'kalimat', 'pertama', 'dokumen', '1', 'ini', 'adalah', 'kalimat', 'kedua', 'dokumen', '1']
        # INI ADALAH CONTOH
        banyak_term_isi = len(term_isi)

        # memasukkan frekuensi kemunculan term di setiap dokumen ke tabel
        for i in range (banyak_term_isi):
            l = 1
            exist = False
            while ((l < term_terpakai + 1) and (not exist)):
                if (tabel[l][0] == term_isi[i]):
                    tabel[l][z + 1] += 1
                    exist = True
                else:
                    l = l + 1
            if (not exist):
                tabel[term_terpakai + 1][0] = term_isi[i]
                tabel[term_terpakai + 1][z + 1] += 1
                term_terpakai += 1

        hasil = []
        hasil = compactTable(tabel)

    return hasil

# tabel_vektor = [['Term', 'dokumen1.txt', 'dokumen2.txt'],['judul', 1, 1],['dokumen', 3, 3],['1', 3, 3],['ini', 2, 2],['adalah', 2, 2],['kalimat', 2, 2],['pertama', 1, 1],['kedua', 1, 1]]
# INI ADALAH CONTOH

def tabelSim(tab_data, query):
    # pecah query
    query = stem(query)
    query = removeStopWord(query)
    # query = "dokumen ini sangat ini adalah bagus"
    # INI ADALAH CONTOH
    term_query = query.rsplit(" ")

    # deklarasi
    # term_terpakai = 0
    banyak_term = len(term_query)
    tabel = [[0 for j in range (len(tab_data[0]) + 1)] for i in range (banyak_term + 2)]

    # pengisian baris pertama termasuk kode (nama) dokumen
    tabel[0][0] = 'Term'
    tabel[0][1] = 'Query'
    for j in range (2, len(tabel[0])):
        tabel[0][j] = tab_data[0][j - 1]

    # memasukkan term
    indeks = 1
    for i in range (banyak_term):
        l = 1
        exist = False
        while ((l < len(tabel) and (not exist))):
            if (tabel[l][0] == term_query[i]):
                exist = True
            else:
                l += 1
        if (not exist):
            tabel[indeks][0] = term_query[i]
            indeks += 1

    # memasukkan frekuensi kemunculan term di query ke tabel
    for i in range (banyak_term):
        l = 1
        found = False
        while ((l < indeks) and (not found)):
            if (tabel[l][0] == term_query[i]):
                tabel[l][1] += 1
                found = True
            else:
                l += 1

    # salin isi tab_data ke tabel untuk mengisi bagian lain dengan searching
    for i in range (1, len(tabel) - 1):
        k = 1
        found = False
        while ((k < len(tab_data)) and (not found)):
            if ((tabel[i][0] == tab_data[k][0])):
                for j in range (2, len(tabel[0])):
                    tabel[i][j] = tab_data[k][j - 1]
                found = True
            else:
                k += 1
        if (not found):
            k2 = 1
            found2 = False
            while ((k2 < i) and (not found2)):
                if ((tabel[i][0] == tabel[k2][0])):
                    found2 = True
                else:
                    k2 += 1
            if (not found2):
                for j in range (2, len(tabel[0])):
                    tabel[i][j] = 0

    # panjang vektor Q
    magQ = float(0)
    for i in range (1, indeks + 1):
        magQ += (tabel[i][1]) ** 2
    magQ = math.sqrt(magQ)

    # pengisian nilai sim ke tabel
    for j in range (2, len(tabel[0])):
        sim = float(0)
        magD = float(0)
        for i in range (1, indeks):
            # perkalian dot, bagian atas rumus sim
            sim += tabel[i][1] * tabel[i][j]
            # panjang vektor D, bagian bawah rumus sim
            magD += (tabel[i][j]) ** 2
        magD = math.sqrt(magD)
        if (magD != 0 and magQ != 0):
            tabel[indeks][j] = sim / (magQ * magD)
        else:
            tabel[indeks][j] = 0

    hasil = compactTable(tabel)
    
    return hasil

# tabel_sim = [['Term', 'Query', 'dokumen1.txt', 'dokumen2.txt'], ['dokumen', 1, 3, 3], ['ini', 2, 2, 2], ['sangat', 1, 0, 0], ['adalah', 1, 2, 2], ['uwu', 1, 0, 0], [0, 0, 0.7717436331412897, 0.7717436331412897]]
# INI ADALAH CONTOH

# return tabel untuk ditampilkan di hasil search
def tabelDisplay(tabel):
    temp = sortBySim(tabel)
    hasil = [[0 for j in range (len(tabel[0]))] for i in range (len(tabel) - 1)]
    for i in range (len(hasil)):
        hasil[i] = temp[i]
    for j in range (2, len(hasil[0])):
        hasil[0][j] = "D" + str(j - 1)
    return hasil

# ['dokumen1.txt', 'Judul Dokumen 1', 42, 0.7717436331412897, 'Ini adalah kalimat pertama dokumen 1.']
# ['dokumen2.txt', 'Judul Dokumen 2', 69, 0.7717436331412897, 'Ini adalah kalimat pertama dokumen 2.']
# INI ADALAH CONTOH

def dataByQuery(database, tabelsim):
    indeks_sim = len(tabelsim) - 1
    temp = [[0 for j in range (len(database[0]))] for i in range (5)]

    # Copying data from database
    temp[0] = database[0]
    temp[1] = database[1]
    temp[2] = database[4]
    temp[4] = database[3]

    # Copying sim data
    for i in range(len(database[0])):
        temp[3][i] = tabelsim[indeks_sim][i+2]

    # Sort by sim
    temp = sortQueryTable(temp)

    # Transpose for printing
    hasil = transpose(temp)
    return hasil

def transpose(table):
    # Transpose tabel biasa
    temp = [[0 for j in range(len(table))] for i in range (len(table[0]))]
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            temp[i][j] = table[j][i]
    return temp

def sortQueryTable(before):
    table = [[0 for j in range(len(before[0]))] for i in range (len(before))]
    # Copy before ke table
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = before[i][j]

    indeks_sim = 3
    jumlah_sorting = len(table[0])

    # Metode sorting diri sendiri
    for i in range(jumlah_sorting):
        for j in range(i+1, jumlah_sorting):
            if table[indeks_sim][j] > table[indeks_sim][i]:
                for k in range(0, 5):
                    temp = table[k][i]
                    table[k][i] = table[k][j]
                    table[k][j] = temp
    return table

'''

# transpose tabel untuk ditampilkan di html
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

'''


# Mengurutkan tabel berdasarkan indeks simnya, secara descending
def sortBySim(before):
    table = [[0 for j in range(len(before[0]))] for i in range (len(before))]
    # Copy before ke table
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = before[i][j]
    
    indeks_sim = len(table) - 1
    jumlah_dokumen = len(table[indeks_sim])

    # Metode sorting diri sendiri
    for i in range(2, jumlah_dokumen):
        for j in range(i+1, jumlah_dokumen):
            if table[indeks_sim][j] > table[indeks_sim][i]:
                temp = table[indeks_sim][i]
                table[indeks_sim][i] = table[indeks_sim][j]
                table[indeks_sim][j] = temp
                for k in range(0, indeks_sim):
                    temp = table[k][i]
                    table[k][i] = table[k][j]
                    table[k][j] = temp
    return table

# hapus baris yang isinya hanya 0
def compactTable(table):
    hasil = []
    i = 0
    while (i < len(table)):
        empty = True
        j = 0
        while ((j < len(table[0])) and (empty)):
            if (table[i][j] != 0):
                empty = False
            else:
                j += 1
        if (not empty):
            hasil.append(table[i])
        i += 1
    return hasil

def stem(artikel):
    # Bikin stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    sentence = artikel
    output = stemmer.stem(sentence)
    return output

def removeStopWord(artikel):
    # Penghapusan stopwords
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    removed_artikel = stopword.remove(artikel)
    return removed_artikel

def getNamaJudul(database):
    # Membuat array D1, D2, D3, dst dan judul dokumen bersangkutan
    hasil = [["*" for j in range (2)] for i in range (len(database[0]))]
    for i in range (len(hasil)):
        hasil[i][0] = "D" + str(i + 1)
        hasil[i][1] = database[0][i]
    return hasil

def hapusHeader(tabel):
    # Menghapus baris pertama tabel
    hasil = [[0 for j in range (len(tabel[0]))] for i in range (len(tabel) - 1)]
    for i in range (1, len(tabel)):
        hasil[i - 1] = tabel[i]
    return hasil