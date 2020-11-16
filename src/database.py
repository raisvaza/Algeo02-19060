import os

namaDokumen = []
judulDokumen = []
kontenDokumen = []
paragrafPertamaDokumen = []
jumlahKataDokumen = []

direktoriDokumen = "static"

def isiKontenDokumen(dokumen):
# Memasukkan isi konten dokumen ke array kontenDokumen
    konten = ""
    for p in dokumen:
        if p != judul:
            konten = konten + p
    kontenDokumen.append(konten)

def isiJumlahKataDokumen(judulDokumen,konten):
# Memasukkan jumlah kata dokumen ke array jumlahKataDokumen
    jumlahKata = len(judulDokumen) + len(konten)
    jumlahKataDokumen.append(jumlahKata)

def newFileIn(direktoriDokumen, filename): # TAMBAH DATA DI DATABASE
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
