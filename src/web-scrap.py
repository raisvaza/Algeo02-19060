from urllib.request import urlopen
from bs4 import BeautifulSoup

link = input("Masukkan tautan web yang ingin di-web-scrap: ")
html = urlopen(link).read()
soup = BeautifulSoup(html, "lxml")

judul = str(soup.find(True, "read__title").get_text())
nama_file = list(str(soup.find(True, "read__title").get_text()))
for i in range (len(nama_file)):
    if nama_file[i] == ' ':
        nama_file[i] = '-'
nama_file = "".join(nama_file)
nama_file = nama_file.replace("?","") + ".txt"

konten = soup.find(True, "read__content")

konten_bersih = konten.find_all(["p","h2","h3"])
for paragraf in konten_bersih:
    if paragraf.find(class_=["inner-link-baca-juga","photo"]):
        paragraf.decompose()


temp = ""
for paragraf in konten_bersih:
    if len(paragraf.get_text()) != 0:
        temp = temp + str(paragraf.get_text()) + "\n"

artikel = judul + "\n\n" + temp

f = open(nama_file, "w+")
f.write(artikel)
f.close