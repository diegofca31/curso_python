from models.Clients import Cliente

#cliente = Cliente('Jose Carlos', 'Gomez Marquez', 26)
cliente = Cliente(apellidos='Gomez Marquez', nombre='Jose Carlos', edad=25)
cliente.edad=26

print(cliente.nombre_completo)
print(cliente.edad)