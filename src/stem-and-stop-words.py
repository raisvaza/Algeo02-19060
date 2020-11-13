from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

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