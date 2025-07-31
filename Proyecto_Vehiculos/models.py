from django.db import models


# Create your models here.



class Marca(models.Model):
    nombre_marca = models.CharField(max_length=100 , unique=True)
    informacion_marca = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_marca


class Vehiculo(models.Model):
    TIPOS_DE_VEHICULO = [
        ('Auto', 'Auto'),
        ('Moto', 'Moto'),
        ('Camioneta', 'Camioneta')
    ]
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name='vehiculos')
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    tipo_vehiculo = models.CharField(max_length=100, choices=TIPOS_DE_VEHICULO, default="Auto")
    Precio = models.CharField(max_length=100)

    def __str__(self):
        return self.marca + " " + self.modelo + " " + str(self.año) + " " + str(self.tipo_vehiculo) + " " + str(self.Precio)
    
class VehiculoElec(models.Model):
    TIPOS_DE_VEHICULO = [
        ('Auto Electrico', 'Auto Electrico'),
        ('Moto Electrico', 'Moto Electrico'),  
        ('Camioneta Electrica', 'Camioneta Electrica')
    ]
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE, related_name='vehiculos_electricos')
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    tipo_vehiculo = models.CharField(max_length=100, choices=TIPOS_DE_VEHICULO, default="Auto Electrico")
    Precio = models.CharField(max_length=100)

    def __str__(self):
        return self.marca + " " + self.modelo + " " + str(self.año) + " " + str(self.tipo_vehiculo) + " " + str(self.Precio)
    
class VehiculoUsado(models.Model):
    TIPOS_DE_VEHICULO = [
        ('Auto Usado', 'Auto Usado'),
        ('Moto Usado', 'Moto Usado'),  
        ('Camioneta Usada', 'Camioneta Usada')
    ]
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE, related_name='vehiculos_usados')
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()
    tipo_vehiculo = models.CharField(max_length=100, choices=TIPOS_DE_VEHICULO, default="Auto Usado")
    Precio = models.CharField(max_length=100)

    def __str__(self):
        return self.marca + " " + self.modelo + " " + str(self.año) + " " + str(self.tipo_vehiculo) + " " + str(self.Precio)
    

    
class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="modelos", to_field="nombre_marca")
    modelo = models.CharField(max_length=100)
    año = models.IntegerField()

    def __str__(self):
        return self.modelo + " " + str(self.año)
    
    
    
class Comentario(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    texto = models.TextField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} en {self.vehiculo.marca} {self.vehiculo.modelo}'

class ComentarioUso(models.Model):
    vehiculo = models.ForeignKey(VehiculoUsado, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    texto = models.TextField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} en {self.vehiculo.marca} {self.vehiculo.modelo}'


class ComentarioElec(models.Model):
    vehiculo = models.ForeignKey(VehiculoElec, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    texto = models.TextField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} en {self.vehiculo.marca} {self.vehiculo.modelo}'