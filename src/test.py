import tbl, database
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

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

def tabelVektor(database):
    # deklarasi
    term_terpakai = 0
    banyak_dokumen = len(database[0])
    tabel = [[0 for j in range (1)] for i in range (1)]

    # pengisian baris pertama termasuk kode (nama) dokumen
    tabel[0][0] = 'Term'
    for j in range (1, banyak_dokumen + 1):
        tabel[0].append("D" + str(j - 1))

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
                    print(l)
                    print(z+1)
                    print(tabel[l])
                    print(tabel[l][z+1])
                    tabel[l][z + 1] += 1
                    exist = True
                else:
                    l = l + 1
            if (not exist):
                tabel.append([term_isi[i]])
                for j in range (z):
                    tabel[term_terpakai].append(0)
                tabel[term_terpakai].append(1)
                term_terpakai += 1
                print(tabel)
                
    hasil = compactTable(tabel)

    return hasil

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

data = database.database
tabelvektor = tabelVektor(data) # ini tabel semua term dari semua dokumen
for i in range (len(tabelvektor)):
    print(tabelvektor[i])
