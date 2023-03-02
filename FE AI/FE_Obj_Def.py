import random

class Unit:    
    def __init__(self, name):
        self.unit_stats = {
            'name' : name,
            'hp'  : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'lvl' : {'current': 0, 'base' : 1},
            'Str' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'Mag' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'Dex' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'Spd' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'Def' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'Res' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'Lck' : {'current': 0, 'base' : 0, 'growth' : 0.0},
            'bld' : {'current': 0, 'base' : 0, 'growth' : 0.0}
        }

        #Need to assign unit stats at some point, but can bodge in something for testing
        for key in self.unit_stats:
            if key != 'name':
                self.unit_stats[key]['base'] = 1
                self.unit_stats[key]['growth'] = 0.5
                self.unit_stats[key]['current'] = self.unit_stats[key]['base']

    def level_up(self):
        self.unit_stats['lvl'] = self.unit_stats['lvl']['current'] + 1
        x= 1 - random.random()
        for key in self.unit_stats:
            if (key not in ['name','lvl']) and ((1 - random.random()) > self.unit_stats[key]['growth']):
                self.unit_stats[key]['current'] = self.unit_stats[key]['current'] + 1
                lvl_text = lvl_text + key + '+1\n'
        return lvl_text
            

unit1 = Unit('Alear')

print(unit1.level_up())
print(unit1.unit_stats)