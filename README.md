# Algeo02-19060
Simple Search Engine

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
![Placeholder](src/img/shot.png)

## Technologies
* Python - version 3.9.0
* Flask - version 1.1.2
* Werkzeug - version 1.0.1
* Jinja2 - version 2.11.2

## Setup
Run main.py (located in /src) in a Python environment and explore the website!

## Code Examples
Input query to the search bar provided to run this part of the code:
```
@app.route('/result/<q>')
def result(q):
   data = database.database
   tabelsim = tblquery.tabelSimQuery(data, q) # ini tabel yang masih ada nilai sim nya di baris terakhir
   tabeldisplay = tbl.tabelDisplay(tabelsim) # ini tabel yang akan ditampilkan
   tabelisi = tbl.dataByQuery(data, tabelsim) # ini tabel yang dipakai untuk menampilkan data file txt
   return render_template('result.html', tabel = tabeldisplay, isi = tabelisi)
```

## Features
List of features ready:
* Search feature
* Upload documents feature
* Term-Document frequency table

To-do list:
* Pray for the best!

## Status
Project is: _finished_.

## Inspiration
Project inspired by a tough college, based on a mindful of inspirations.

## Contact
Created by [@raisvaza](https://www.github.com/raisvaza) [@iedrania](https://www.github.com/iedrania) [@imanikarina](https://www.github.com/imanikarina), three students of ITB.