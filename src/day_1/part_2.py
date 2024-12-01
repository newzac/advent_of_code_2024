import pandas as pd
import os

dirname = os.path.dirname(__file__)
input_data = os.path.join(dirname, 'input.txt')

df = pd.read_csv(input_data, sep='\s+')

asorted = df['a'].sort_values().to_list()
bsorted = df['b'].sort_values().to_list()
list_sim = 0

for alid in asorted:
    indices = [i for i, x in enumerate(bsorted) if x == alid]
    o = len(indices)
    similarity = alid * o
    list_sim += similarity

print(f'Total Similarity: {list_sim}')
