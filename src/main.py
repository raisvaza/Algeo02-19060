import os
import tbl, database, tblquery
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

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

UPLOAD_FOLDER = 'static'
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
   data = database.database
   tabelsim = tblquery.tabelSimQuery(data, q) # ini tabel yang masih ada nilai sim nya di baris terakhir
   tabeldisplay = tbl.tabelDisplay(tabelsim) # ini tabel yang akan ditampilkan
   tabelisi = tbl.dataByQuery(data, tabelsim) # ini tabel yang dipakai untuk menampilkan data txt

   # DUMMY DATA FOR JINJA TESTING
   #tabelisi = [["judul1.txt","judul 1", 100,0.9,"Kalimat pertama dokumen"],["judul2.txt","judul 2", 100,0.9,"Kalimat pertama dokumen"],["judul3.txt","judul 3", 100,0.9,"Kalimat pertama dokumen"]]
   #tabeldisplay = [["Terms","Query","D1","D2","D3"],["makan",1,1,2,3],["minum",1,1,2,3],["sapi",2,1,2,3]]
   
   return render_template('result.html', tabel = tabeldisplay, isi = tabelisi)

@app.route('/terms/')
def terms():
   data = database.database
   tabelTerms = tbl.tabelVektor(data) # ini tabel semua term dari semua dokumen
   tabelJudul = tbl.getNamaJudul(data)
   tabelTerms = tbl.hapusHeader(tabelTerms)
   return render_template('terms.html', judul = tabelJudul, terms = tabelTerms)

if __name__ == '__main__':
   # I added this for 'flash' function, not sure what it's supposed to do.
   # Anyways, the flash function did not work so fml right? :)
   app.secret_key = os.urandom(24)
   app.run(debug = True)