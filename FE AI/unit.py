import random
import pandas as pd

class Unit:    
    def __init__(self, name):
        #Start by initialising stats as a dictionary
        #Probably going to import this as a JSON eventually but for now this will surfice,
        #Currently testing on Alear's stats
        self.unit_stats = {
            'name' : name,
            'hp'  : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'lvl' : {'current': 0, 'base' : 1},
            'str' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'mag' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'dex' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'spd' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'def' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'res' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'lck' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'bld' : {'current': 0, 'base' : 0, 'growth' : 0.0}
        }

        df = pd.read_csv('unit_base_stats.csv')
        for column in df.columns:
            for i,row in df.iterrows():
                if column == 'name':
                    self.unit_stats[column] = row[column]
                else:
                    col_spl = column.split('_')
                    self.unit_stats[col_spl[0]][col_spl[1]] = row[column] if col_spl[1] == 'base' else (row[column] / 100)
                

        #Initialise the base, growth, and current rates
        for key in self.unit_stats:
            if key != 'name':
                self.unit_stats[key]['current'] = self.unit_stats[key]['base']

    def level_up(self):
        lvl_text = ''
        self.unit_stats['lvl']['current'] = self.unit_stats['lvl']['current'] + 1
        for key in self.unit_stats:
            if (key not in ['name','lvl']) and ((1 - random.random()) > self.unit_stats[key]['growth']):
                self.unit_stats[key]['current'] = self.unit_stats[key]['current'] + 1
                lvl_text = lvl_text + key + '+1;'
        return lvl_text