import os
import math
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
app = Flask(__name__)

# deklarasi
term_terpakai = 0

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
      tabel[0][j] = 'D' + str(j - 1)

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
      tabel[banyak_term + 1][j] = sim / (magQ * magD)
   return tabel

# return tabel yang tinggal ditampilkan, input array of array
def tabelhasil(tabel):
   hasil = [[0 for j in range (banyak_dokumen + 2)] for i in range (term_terpakai + 1)]
   for i in range (term_terpakai + 1):
      hasil[i] = tabel[i]
   return hasil

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

UPLOAD_FOLDER = '../documents'
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

         path = "documents/News_txt.txt"
         all_files = os.listdir(path)
         return redirect(request.url)
   return render_template('upload.html')

@app.route('/result/<q>', methods = ['POST', 'GET'])
def result():
   if request.method == "POST":
      query = request.form['query']
      query2 = stem(query)
      query2 = remove_stop_word(query)
      query3 = query2.rsplit(" ")
      tabelsim = tabel_similarity(query3) # ini tabel yang masih ada nilai sim nya di baris terakhir
      tabeldisplay = tabelhasil(tabelsim) # ini tabel yang sudah tinggal ditampilkan
      return redirect(url_for('result', q = query))

if __name__ == '__main__':
   # I added this for 'flash' function, not sure what it's supposed to do.
   # Anyways, the flash function did not work so fml right? :)
   app.secret_key = os.urandom(24)
   app.run(debug = True)