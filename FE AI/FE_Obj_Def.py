class BaseStats:    
    def __init__(self, name):
        self.unit_stats = {
            'name' : name,
            'hp' : 0,
            'lvl' : 0,
            'Str' : 0,
            'Mag' : 0,
            'Dex' : 0,
            'Spd' : 0,
            'Def' : 0,
            'Res' : 0,
            'Lck' : 0,
            'bld' : 0
        }

        #Need to assign unit stats at some point, but can bodge in something for testing
        for key in self.unit_stats:
            if key != 'name':
                self.unit_stats[key] = 1

unit1 = BaseStats('Alear')

print(unit1.unit_stats)