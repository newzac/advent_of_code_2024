import pandas as pd
import os

dirname = os.path.dirname(__file__)
input_data = os.path.join(dirname, 'input.txt')

df = pd.read_csv(input_data, sep='\s+')

asorted = df['a'].sort_values().to_list()
bsorted = df['b'].sort_values().to_list()
total = 0

for i, alid in enumerate(asorted):
    blid = bsorted[i]
    distance = max(alid, blid) - min(alid, blid)
    total = total + distance

print(f'Total distance: {total}')
