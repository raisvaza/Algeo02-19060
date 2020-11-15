import tbl
import math
import database

# return tabel yang isinya masih lengkap ada nilai sim, per query
def tabelSimQuery(database, query):
    # pembersihan query
    query = tbl.stem(query)
    query = tbl.removeStopWord(query)
    term_query = query.rsplit(" ")

    # deklarasi
    banyak_term = len(term_query)
    banyak_dokumen = len(database[0])
    tabel = [[0 for j in range (banyak_dokumen + 2)] for i in range (banyak_term + 2)]

    # pengisian baris pertama termasuk kode dokumen
    tabel[0][0] = 'Term'
    tabel[0][1] = 'Query'
    for j in range (2, banyak_dokumen + 2):
        tabel[0][j] = database[0][j - 2]

    # memasukkan frekuensi kemunculan term di query ke tabel
    term_terpakai = 0
    for i in range (1, banyak_term + 1):
        l = 1
        exist = False
        while ((l < i) and (not exist)):
            if (tabel[l][0] == term_query[i - 1]):
                tabel[l][1] += 1
                exist = True
            else:
                l = l + 1
        if (not exist):
            tabel[term_terpakai + 1][0] = term_query[i - 1]
            tabel[term_terpakai + 1][1] += 1
            term_terpakai += 1
            
    # memasukkan frekuensi kemunculan term di setiap dokumen ke tabel
    for j in range (2, banyak_dokumen + 2):
        # pembersihan dokumen
        isi = tbl.stem(database[2][j - 2])
        isi = tbl.removeStopWord(isi)
        term_isi = isi.rsplit(" ")
        # term_isi = ['judul', 'dokumen', '1', 'ini', 'adalah', 'kalimat', 'pertama', 'dokumen', '1', 'ini', 'adalah', 'kalimat', 'kedua', 'dokumen', '1']
        # INI ADALAH CONTOH
        banyak_term_isi = len(term_isi)

        for i in range (1, banyak_term + 1):
            k = 0
            found = False
            while (k < banyak_term_isi):
                if ((tabel[i][0] == term_isi[k])):
                    tabel[i][j] += 1
                k += 1

    # pengisian baris terakhir (baris sim)
    for j in range (banyak_dokumen + 2):
        tabel[banyak_term + 1][j] = 0

    # panjang vektor Q
    magQ = float(0)
    for i in range (1, banyak_term + 1):
        magQ += (tabel[i][1]) ** 2
    magQ = math.sqrt(magQ)

    # pengisian nilai sim ke tabel
    for j in range (2, banyak_dokumen + 2):
        sim = float(0)
        magD = float(0)
        for i in range (1, banyak_term + 1):
            # perkalian dot, bagian atas rumus sim
            sim += tabel[i][1] * tabel[i][j]
            # panjang vektor D, bagian bawah rumus sim
            magD += (tabel[i][j]) ** 2
        magD = math.sqrt(magD)
        if (magD != 0 and magQ != 0):
            tabel[banyak_term + 1][j] = sim / (magQ * magD)
        else:
            tabel[banyak_term + 1][j] = 0

    hasil = tbl.compactTable(tabel)

    return hasil