import math

"""

isi tabel sebagai referensi:

Term    0,0     Query 0,1   D1 0,2  D2 0,3  ...     DSekian
Term1   1,0     1,1         1,2     1,3     ...     
Term2   2,0     2,1         2,2     2,3     ...
...     ...     ...         ...     ...     ...
TermN   N,0     N,1         N,2     N,3     ...
SIM     N+1,0   N+1,1       N+1,2   N+1,3   ...

"""

def tabel_similarity():
    # testing
    banyak_dokumen = 2
    banyak_term = 3

    # deklarasi
    tabel = [[0 for j in range (banyak_dokumen + 2)] for i in range (banyak_term + 2)]

    # pengisian baris pertama termasuk kode dokumen
    tabel[0][0] = 'Term'
    tabel[0][1] = 'Query'
    for j in range (2, banyak_dokumen + 2):
        tabel[0][j] = 'D' + str(j - 1)

    # memasukkan frekuensi kemunculan term di query ke tabel

    # memasukkan frekuensi kemunculan term di setiap dokumen ke tabel

    # testing
    tabel[1] = ['Menteri',0,2,3]
    tabel[2] = ['minta',0,3,7]
    tabel[3] = ['Korupsi',2,5,1]

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
        tabel[banyak_term + 1][j] = sim / (magQ * magD)

    # cetak tabel
    print(tabel)




