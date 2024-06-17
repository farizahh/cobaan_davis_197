import pandas as pd

# Nama file CSV
fn1 = 'imdb_top.csv'
    
# Membaca file CSV ke dalam DataFrame dengan encoding 'latin1'
df1 = pd.read_csv(fn1, encoding='latin1')

# Menampilkan DataFrame sebagai tabel
df1