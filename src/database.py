import os

namaDokumen = []
judulDokumen = []
kontenDokumen = []
paragrafPertamaDokumen = []
jumlahKataDokumen = []

direktoriDokumen = "../test"

def isiKontenDokumen(dokumen):
# Memasukkan judul dokumen ke array kontenDokumen
    konten = ""
    for p in dokumen:
        if p != judul:
            konten = konten + p
    kontenDokumen.append(konten)

def isiJumlahKataDokumen(judulDokumen,konten):
# Memasukkan judul dokumen ke array jumlahKataDokumen
    jumlahKata = len(judulDokumen) + len(konten)
    jumlahKataDokumen.append(jumlahKata)

for filename in os.listdir(direktoriDokumen):
    if filename.endswith(".txt"):
        namaDokumen.append(filename)

        f = open(direktoriDokumen + "/" + filename, "r")

        judul = f.readline()
        judulDokumen.append(judul)

        isiArtikel = f.readline()
        isiArtikel = f.readlines()
        isiKontenDokumen(isiArtikel)

        f.close()
        f = open(direktoriDokumen + "/" + filename, "r")
        judul = f.readline()
        pertama = f.readline()
        pertama = f.readline()

        paragrafPertamaDokumen.append(pertama)
        
        isiJumlahKataDokumen(judul,isiArtikel)

database = [namaDokumen, judulDokumen, kontenDokumen, paragrafPertamaDokumen, jumlahKataDokumen]
