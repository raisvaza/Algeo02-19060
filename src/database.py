import os

namaDokumen = []
judulDokumen = []
kontenDokumen = []
paragrafPertamaDokumen = []
jumlahKataDokumen = []

direktoriDokumen = "../test"

def isiNamaDokumen(dokumen):
# Memasukkan nama dokumen ke array namaDokumen
    namaDokumen.append(dokumen)

def isiJudulDokumen(dokumen):
# Memasukkan judul dokumen ke array judulDokumen
    judulDokumen.append(dokumen)

def isiKontenDokumen(dokumen):
# Memasukkan judul dokumen ke array kontenDokumen
    konten = ""
    for p in dokumen:
        if p != judul:
             konten = konten + p
    kontenDokumen.append(konten)

def isiParagrafPertamaDokumen(indeksDokumen):
# Memasukkan judul dokumen ke array paragrafPertamaDokumen
    paragrafPertama = ""
    for char in kontenDokumen[indeksDokumen]:
        if char != "\n" :
            paragrafPertama = paragrafPertama + char
        else:
            break
    paragrafPertamaDokumen.append(paragrafPertama)

def isiJumlahKataDokumen(judulDokumen,konten):
# Memasukkan judul dokumen ke array jumlahKataDokumen
    jumlahKata = len(judulDokumen) + len(konten)
    jumlahKataDokumen.append(jumlahKata)

for filename in os.listdir(direktoriDokumen):
    if filename.endswith(".txt"):

        isiNamaDokumen(filename)

        f = open(direktoriDokumen + "/" + filename, "r")
        
        judul = f.readline()
        isiJudulDokumen(judul)

        isiArtikel = f.readlines()
        isiKontenDokumen(isiArtikel)

        indeksDokumen = 0
        isiParagrafPertamaDokumen(indeksDokumen)
        
        isiJumlahKataDokumen(jumlahKataDokumen[indeksDokumen],kontenDokumen[indeksDokumen])
        indeksDokumen += 1

database = []
database.append(namaDokumen)
database.append(judulDokumen)
database.append(kontenDokumen)
database.append(paragrafPertamaDokumen)
database.append(jumlahKataDokumen)