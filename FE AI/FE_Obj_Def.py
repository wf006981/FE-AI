class BaseStats:    
    def __init__(self, name):
        self.unit_stats = {
            'name' : name,
            'hp'  : {'base' : 0, 'growth' : 0.0},
            'lvl' : {'base' : 0, 'growth' : 0.0},
            'Str' : {'base' : 0, 'growth' : 0.0},
            'Mag' : {'base' : 0, 'growth' : 0.0},
            'Dex' : {'base' : 0, 'growth' : 0.0},
            'Spd' : {'base' : 0, 'growth' : 0.0},
            'Def' : {'base' : 0, 'growth' : 0.0},
            'Res' : {'base' : 0, 'growth' : 0.0},
            'Lck' : {'base' : 0, 'growth' : 0.0},
            'bld' : {'base' : 0, 'growth' : 0.0}
        }

        #Need to assign unit stats at some point, but can bodge in something for testing
        for key in self.unit_stats:
            if key != 'name':
                self.unit_stats[key]['base'] = 1
                self.unit_stats[key]['growth'] = 0.1

unit1 = BaseStats('Alear')

print(unit1.unit_stats)