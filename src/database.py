import os

namaDokumen = []
judulDokumen = []
kontenDokumen = []
paragrafPertamaDokumen = []
jumlahKataDokumen = []

direktoriDokumen = "static"

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
        f.close()

        f = open(direktoriDokumen + "/" + filename, "r")
        judul = f.readline()
        pertama = f.readline()
        pertama = f.readline()
        paragrafPertamaDokumen.append(pertama)
        f.close()

        f = open(direktoriDokumen + "/" + filename, "r")
        isiArtikel = f.readlines()
        isiKontenDokumen(isiArtikel)
        
        isiJumlahKataDokumen(judul,isiArtikel)

        f.close()

database = [namaDokumen, judulDokumen, kontenDokumen, paragrafPertamaDokumen, jumlahKataDokumen]
