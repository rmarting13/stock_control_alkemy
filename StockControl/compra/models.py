from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models


# Customized validators:

# Estos Validators pueden ser utilizados en los contructores de los ModelFields, por ejemplo: models.FloatField(validators=[floatValidator])
def floatValidator(value):
    try:
        decimalString = str(value).split('.')
        decimal = int(decimalString[1])
        if not (decimal % 5 == 0):
            raise ValidationError(message='Ingrese un valor cuyo decimal sea múltiplo de 5.')
    except TypeError:
        raise ValidationError('Este campo es requerido.')


def textValidator(value):
    if value is None:
        raise ValidationError('Este campo es requerido.')


class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    razon_soc = models.CharField(max_length=255, null=True)
    dni = models.CharField(max_length=8)
    email = models.EmailField(max_length=255, null=True,
                              validators=[EmailValidator(message="Ingrese una dirección de email válida.")])
    tel = models.CharField(max_length=255, null=True)
    domicilio = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.razon_soc}'


class Producto(models.Model):
    descripcion = models.CharField(max_length=255)
    marca = models.CharField(max_length=255, null=True)
    precio = models.FloatField()
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, related_name='productos', on_delete=models.SET_NULL, null=True)

    # Sobreescribimos el método save() para que el valor se guarde con una presición de 2 decimales.
    def save(self, *args, **kwargs):
        self.precio = round(self.precio, 2)
        super(Producto, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.descripcion}'

