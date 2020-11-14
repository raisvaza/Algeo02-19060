import os
import math
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
app = Flask(__name__)

# deklarasi
term_terpakai = 0
banyak_dokumen = 2

# fungsi biasa (stem, remove, similarity)
def stem(artikel):
   # Bikin stemmer
   factory = StemmerFactory()
   stemmer = factory.create_stemmer()
   sentence = artikel
   output = stemmer.stem(sentence)
   return output

def remove_stop_word(artikel):
   # Penghapusan stopwords
   factory = StopWordRemoverFactory()
   stopword = factory.create_stop_word_remover()
   removed_artikel = stopword.remove(artikel)
   return removed_artikel

# return tabel yang isinya masih lengkap ada nilai sim, input string
def tabel_similarity(query):
   # deklarasi
   banyak_term = len(query)
   global term_terpakai
   tabel = [[0 for j in range (banyak_dokumen + 2)] for i in range (banyak_term + 2)]

   # pengisian baris pertama termasuk kode dokumen
   tabel[0][0] = 'Term'
   tabel[0][1] = 'Query'
   for j in range (2, banyak_dokumen + 2):
      tabel[0][j] = 'D' + str(j - 1)                   # URGENT INI BAKAL DISESUAIKAN SAMA DATABASE

   # memasukkan frekuensi kemunculan term di query ke tabel
   term_terpakai = 0
   for k in range (1, banyak_term + 1):
      l = 1
      exist = False
      while ((l < k) and (not exist)):
         print(l)
         if (tabel[l][0] == query[k - 1]):
            tabel[l][1] += 1
            exist = True
         else:
            l = l + 1         
      if (not exist):
         tabel[k][0] = query[k - 1]
         tabel[k][1] += 1
         term_terpakai += 1

   # memasukkan frekuensi kemunculan term di setiap dokumen ke tabel


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

   return tabel

def tabel_vektor(database):
    # deklarasi
    term_terpakai = 0
    banyak_dokumen = len(database[0])
    banyak_term = 0
    # INI ADALAH DUMMY 15
    for z in range (banyak_dokumen):
        banyak_term += len(remove_stop_word(stem(database[2][z])).split)
    tabel = [[0 for j in range (banyak_dokumen + 1)] for i in range (banyak_term + 1)]

    # pengisian baris pertama termasuk kode (nama) dokumen
    tabel[0][0] = 'Term'
    for j in range (1, banyak_dokumen + 1):
        tabel[0][j] = database[0][j - 1]

    for z in range (banyak_dokumen):
        # pembersihan dokumen
        isi = stem(database[2][z])
        isi = remove_stop_word(isi)
        term_isi = isi.rsplit(" ")
        # term_isi = ['judul', 'dokumen', '1', 'ini', 'adalah', 'kalimat', 'pertama', 'dokumen', '1', 'ini', 'adalah', 'kalimat', 'kedua', 'dokumen', '1']
        # INI ADALAH DUMMY
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

    return tabel

''' database = INI ADALAH DUMMY
['Term', 'dokumen1.txt', 'dokumen2.txt']
['judul', 1, 1]
['dokumen', 3, 3]
['1', 3, 3]
['ini', 2, 2]
['adalah', 2, 2]
['kalimat', 2, 2]
['pertama', 1, 1]
['kedua', 1, 1]
'''

def tabel_sim(tab_data,query):
    # pecah query
    query = stem(query)
    query = remove_stop_word(query)
    # query = "dokumen ini uwu"
    # INI ADALAH DUMMY
    term_query = query.rsplit(" ")

    # deklarasi
    term_terpakai = 0
    banyak_term = len(term_query)
    tabel = [[0 for j in range (len(tab_data) + 1)] for i in range (banyak_term + 2)]

    # pengisian baris pertama
    tabel[0][0] = 'Term'
    tabel[0][1] = 'Query'

    # memasukkan term
    for i in range (1, banyak_term + 1):
        tabel[i][0] = term_query[i - 1]

    # memasukkan frekuensi kemunculan term di query ke tabel
    for i in range (banyak_term):
        l = 1
        exist = False
        while ((l < term_terpakai + 1) and (not exist)):
            if (tabel[l][0] == term_query[i]):
                tabel[l][1] += 1
                exist = True
            else:
                l += 1
        if (not exist):
            tabel[term_terpakai + 1][0] = term_query[i]
            tabel[term_terpakai + 1][1] += 1
            term_terpakai += 1

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
            for j in range (2, len(tabel[0])):
                tabel[i][j] = 0

    return tabel

# return tabel yang tinggal ditampilkan, input array of array
def tabelhasil(tabel):
    hasil = [[0 for j in range (len(tabel[0]))] for i in range (len(tabel) - 1)]
    for i in range (len(hasil)):
        hasil[i] = tabel[i]
    return hasil

def sortBySim(table):
    # Mengurutkan tabel berdasarkan indeks simnya, secara descending
    indeks_sim = len(table) - 1
    jumlah_dokumen = len(table[indeks_sim])
    print(indeks_sim)
    print(jumlah_dokumen)
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

# THIS IS THE NORMAL '/'

@app.route('/')
def home():
   return render_template('main.html')

# THIS IS WHEN '/' SENDS POST METHOD

@app.route('/', methods=['POST'])
def home_post():
   if request.method == "POST":
      query = request.form['query']
      # Redirects to /result/<query>
      return redirect(url_for('result', q = query))

@app.route('/about/')
def about():
   return render_template('about.html')

# UPLOADING A TXT FILE TO DOCUMENTS FILE
# Harus di-run dari directory main.py, aka bukan Open With > Python!

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = ['txt']

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS

# Check extension!

def isAllowed(filename):
   if not "." in filename:
      return False

   # Split after dot (get extension part)
   extension = filename.rsplit(".", 1)[1]

   if extension.lower() in app.config['ALLOWED_EXTENSIONS']:
      return True
   else:
      return False

# Actual function!

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
   if request.method == "POST":
      if request.files:
         textfile = request.files["fileToUpload"]

         # File name is Empty
         if textfile.filename == "":
            flash('No selected file.')
            return redirect(request.url)

         # File extension is not allowed
         if not isAllowed(textfile.filename):
            flash('Not a .txt file.')
            return redirect(request.url)

         # Get absolute address
         address = os.path.abspath(app.config['UPLOAD_FOLDER'])

         textfile.save(os.path.join(address, textfile.filename))
         flash('File saved')
         return redirect(request.url)
   return render_template('upload.html')

@app.route('/result/<q>')
def result(q):
   query2 = stem(q)
   query2 = remove_stop_word(q)
   query3 = query2.rsplit(" ")
   tabelsim = tabel_similarity(query3) # ini tabel yang masih ada nilai sim nya di baris terakhir
   tabeldisplay = tabelhasil(tabelsim) # ini tabel yang sudah tinggal ditampilkan
   return render_template('result.html', result = tabeldisplay)

if __name__ == '__main__':
   # I added this for 'flash' function, not sure what it's supposed to do.
   # Anyways, the flash function did not work so fml right? :)
   app.secret_key = os.urandom(24)
   app.run(debug = True)