import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

class DataFrame:

    def __init__(self, filepath):

        data_file = open(filepath, 'r')

        data = []
        for line in data_file:
            data.append(json.loads(line))

        times = [row[0] for row in data]
        sensor_data = [np.array(row[1]) for row in data]
        avg = [(matrix.sum() / 64) for matrix in sensor_data]
        std = [matrix.std() for matrix in sensor_data]

        self.df = pd.DataFrame()
        self.df['Time'] = pd.to_datetime(times, yearfirst=True)
        self.df['Sensor Data'] = sensor_data
        self.df['Energy Mean'] = avg

        self.normaliser = self.df['Energy Mean'].mean()
        self.df['Clipping Threshold'] = self.df['Energy Mean'] / self.normaliser

        print(self.df['Clipping Threshold'])
        #print(self.df['Clipping Threshold']*self.df['Energy Std. Deviation'])


        self.df['Energy Std. Deviation'] = std

        self.df['Person Passed'] = self.df['Energy Std. Deviation'].clip_lower(1.2)

        self.df.set_index('Time', inplace=True)

        #print(self.df['Person Passed'])
