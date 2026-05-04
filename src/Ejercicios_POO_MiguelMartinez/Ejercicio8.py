class Producto:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"Producto: {self.nombre} con id {self.id}"

    def __eq__(self, other):
        return self.id == other.id

macarrones = Producto(123, "macarrones")
espaguetis = Producto(123, "espaguetis")
pasta = Producto(123, "macarrones")

print(macarrones == espaguetis)
print(macarrones == pasta)
print(espaguetis == pasta)
print(macarrones == macarrones)
print(pasta == pasta)