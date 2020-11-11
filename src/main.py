namaDokumen = []
isiDokumen = []

def baca_dokumen (namaDokumen):
    f = open(namaDokumen, "r").read
    isiDokumen.append(f)