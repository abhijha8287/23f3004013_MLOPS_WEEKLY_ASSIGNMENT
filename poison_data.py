import pandas as pd
import numpy as np
import random

def poison_dataset(input_file, output_file, poison_percent):

    df = pd.read_csv(input_file)

    n = len(df)

    poison_count = int(n * poison_percent / 100)

    indices = random.sample(range(n), poison_count)

    for i in indices:

        df.iloc[i,0] = np.random.uniform(4,8)
        df.iloc[i,1] = np.random.uniform(2,5)
        df.iloc[i,2] = np.random.uniform(1,7)
        df.iloc[i,3] = np.random.uniform(0,3)

        df.iloc[i,4] = random.choice([
            'Iris-setosa',
            'Iris-versicolor',
            'Iris-virginica'
        ])

    df.to_csv(output_file,index=False)

    print(f"Created {poison_percent}% poisoned dataset")

poison_dataset("iris.csv","iris_5.csv",5)

poison_dataset("iris.csv","iris_10.csv",10)

poison_dataset("iris.csv","iris_50.csv",50)
