import pandas as pd
import numpy as np

dict = {"Negara" : ["Indonesia", "Jepang", "Karawang"],
"Ibu Kota" : ["Jakarta", "Tokyo", "Jatisari"],
"Luas" : [1905, 3245, 9999],
"Populasi" : [287, 445, 999]}
df = pd.DataFrame(dict)
print(df)