# Algeo02-19060
A Simple Search Engine

## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)
* [Contact](#contact)

## General info
This simple search engine program is a submission to the Linear Algebra and Geometry subject's assignment as an application of vector's dot product concept for information retrieval.
## Screenshots
![Placeholder](src/img/placeholder.png)

## Technologies
* Python - version 3.9.0
* Flask - version 1.1.2
* Werkzeug - version 1.0.1

## Setup
Run main.py (located in /src) in a Python environment.

## Code Examples
Input query to the search bar provided to run this part of the code:
```
@app.route('/result/<q>')
def result(q):
   tabelvektor = tbl.tabelVektor(database) # ini tabel semua term dari semua dokumen
   tabelsim = tbl.tabelSim(tabelvektor, q) # ini tabel yang masih ada nilai sim nya di baris terakhir
   tabeldisplay = tbl.tabelDisplay(tabelsim) # ini tabel yang akan ditampilkan
   tabelisi = tbl.transpose(database, tabelsim) # ini tabel yang dipakai untuk menampilkan data txt
   return render_template('result.html', tabel = tabeldisplay, isi = tabelisi)
```

## Features
List of features ready:
* Search feature
* Upload documents feature

To-do list:
* Testing and debugging
* See complete term-document frequency table

## Status
Project is: _in progress_, _finished_, needs further testing.

## Inspiration
Project inspired by a tough college, based on a mindful of inspiration.

## Contact
Created by [@](https://www.flynerd.pl/) three students of ITB.