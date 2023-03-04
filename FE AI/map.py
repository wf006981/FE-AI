class map():
    def __init__(self, id):
        self.map_id = id
        self.x_dimension = 0
        self.y_dimension = 0
        self.map = []
        #testfen.jpg
        self.fen = 'tttttttt/t6t/t1UUU2t/t6t/t6t/t2a3t/t1uuu2t/tttttttt 0'

        self.initialise_map(self.map_id, self.fen)

    def __str__(self):
        print_string = ''
        i = 0
        for x in self.map:
            if i != 0 and i % self.x_dimension == 0:
                print_string += '\n'
            print_string += x
            i += 1
        return print_string

    def initialise_map(self, id = 0, fen = ''):
        self.x_dimension = 8
        self.y_dimension = 8
        for x in fen:
            if(x.isdigit()):
                for k in range(0,int(x)):
                    self.map.append('.')
            else:
                if(x != '/'):
                    self.map.append(x)
    
current_map = map(0)

print(current_map)