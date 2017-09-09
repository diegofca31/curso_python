class Cliente(object):

    estado_cuenta = None

    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def __len__(self):
        return self.edad

    def __str__(self):
        #return self.nombre + ' ' + self.apellidos
        #return ' '.join(self.nombre,self.apellidos)
        return self.getNombres()

    def getNombres(self):
        data = 'Cliente %s %s' % (self.nombre, self.apellidos)
        return data

    @property
    def nombre_completo(self):
        return ', '.join((self.apellidos,self.nombre))

if __file__ == '__main__':
    #cliente = Cliente('Jose Carlos', 'Gomez', 26)
    cliente = Cliente(apellidos='CCalla', nombre='Diego', edad=26)

    print(cliente.nombre_completo)
    print(cliente.edad)

