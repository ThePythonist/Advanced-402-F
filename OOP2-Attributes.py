class Car:
    # Class Attribute
    zarfiat = 5

    # Instance Attribute
    def __init__(self, model):
        self.model = model


# Accessing class attribute
# print(Car.zarfiat)

# Creating instances
persia = Car(1402)
dena = Car(1396)

# Accessing instance attribute
# print(persia.model)
# print(dena.model)

# Modifying instance attribute
# persia.model = 1403
# print(persia.model)
# print(dena.model)

# Modifying class attribute
Car.zarfiat = 8
print(persia.zarfiat)
print(dena.zarfiat)
