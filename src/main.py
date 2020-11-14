import os
from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('main.html')

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
         return redirect(request.url)
   return render_template('upload.html')

@app.route('/result/', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form['text']
      return render_template("result.html",result = result)

if __name__ == '__main__':
   # I added this for 'flash' function, not sure what it's supposed to do.
   app.secret_key = os.urandom(24)
   app.run(debug = True)