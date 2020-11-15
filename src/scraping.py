from urllib.request import urlopen
from bs4 import BeautifulSoup

# PROGRAM WEB SCRAP UNTUK ARTIKEL-ARTIKEL DI KOMPAS.COM

# Memasukkan tautan yang ingin di-web-scrap
link = input("Masukkan tautan web yang ingin di-web-scrap: ")
html = urlopen(link).read()
soup = BeautifulSoup(html, "lxml")

# Ekstraksi judul artikel dan penyimpanan nama file
judul = str(soup.find(True, "read__title").get_text())
nama_file = list(str(soup.find(True, "read__title").get_text()))
for i in range (len(nama_file)):
    if nama_file[i] == ' ':
        nama_file[i] = '-'
nama_file = "".join(nama_file)
nama_file = nama_file.replace("?","") + ".txt"

# Ekstraksi konten artikel dan pembersihan konten dari iklan dan foto
konten = soup.find(True, "read__content")

konten_bersih = konten.find_all(["p","h2","h3","ol","ul","table"])
for paragraf in konten_bersih:
    if paragraf.find(class_=["inner-link-baca-juga","photo"]):
        paragraf.decompose()

# Penghapusan paragraf kosong
temp = ""
for paragraf in konten_bersih:
    if len(paragraf.get_text()) != 0:
        temp = temp + str(paragraf.get_text()) + "\n"

# Penggabungan judul dengan konten artikel
artikel = judul + "\n\n" + temp

# Penyimpanan artikel sebagai dokumen
f = open("/static/" + nama_file, "w+")
f.write(artikel)
f.close