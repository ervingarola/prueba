class Productos:
    def __init__(self, id_producto, nombre, fecha_ingreso, fecha_vencimiento):###### es un contructr sirvve para configurar el estado inicial de un objeto
        self.id_producto = id_producto ###### es un metodo que permite acceder a los atributosdentro de la clase
        self.nombre = nombre
        self.fecha_ingreso = fecha_ingreso
        self.fecha_vencimiento = fecha_vencimiento

class Trabajadores:
    def __init__(self, id_trabajador, nombre, cargo):
        self.id_trabajador = id_trabajador
        self.nombre = nombre
        self.cargo = cargo

class Proveedores:
    def __init__(self, id_proveedor, nombre, nombre_vendedor, direccion, telefono):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.nombre_vendedor = nombre_vendedor
        self.direccion = direccion
        self.telefono = telefono
