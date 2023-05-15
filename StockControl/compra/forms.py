from django.forms import ModelForm, NumberInput, EmailInput
from django.utils.translation import gettext_lazy as _
from .models import Producto, Proveedor


class ProveedorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-2'

    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'}),
            'dni': NumberInput(attrs={'class': 'form-control', 'min': 0, 'step': 1, 'style': 'width:20ch'}),
            'tel': NumberInput(attrs={'min': 0, 'step': 1, 'style': 'width:20ch'}),
        }
        labels = {
            'nombre': _('Nombre'),
            'apellido': _('Apellido'),
            'razon_soc': _('Razón Social'),
            'dni': _('DNI'),
            'tel': _('Teléfono/Móvil'),
            'domicilio':_('Domicilio')
        }

class ProductoForm(ModelForm):
    # precio = FloatField(validators=[floatValidator])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.error_messages['required'] = 'Este campo es requerido'
            if visible.html_name == 'precio' or visible.html_name == 'stock_actual':
                visible.field.widget.attrs[
                    'oninvalid'] = "this.setCustomValidity('El valor ingresado no es correcto.')"  # ValidationMessage personalizado
                # La siguiente línea de código evita que el ValidationMessage se muestre incluso con el campo completado, puesto que
                # la línea anterior establece la validación del lado del cliente (navegador) como inválida siempre, evitando que el
                # formulario pueda ser enviado, aún con los campos completos y válidos.
                visible.field.widget.attrs['oninput'] = "this.setCustomValidity('')"

            else:
                visible.field.widget.attrs[
                    'oninvalid'] = "this.setCustomValidity('Este campo es requerido.')"  # ValidationMessage personalizado
                visible.field.widget.attrs[
                    'oninput'] = "this.setCustomValidity('')"  # Esto evita que el ValidationMessage se muestre incluso con el campo completado

    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'precio': NumberInput(
                attrs={
                    'min': 1,
                    'step': 0.25,
                }
            ),
            'stock_actual': NumberInput(attrs={'min': 1, 'step': 1})
        }
        labels = {
            'descripcion': _('Producto'),
            'precio': _('Precio'),
            'stock_actual': _('Cantidad'),
            'proveedor': _('Proveedor')
        }
        error_messages = {
            'precio': {
                'step': 'El precio debe ser superior a 0.'
            }
        }
        help_texts = {
            # 'precio': _('Ingrese valores decimales que sean múltiplos de 10 o 5.')
        }

    # def clean_precio(self):
    #     data = self.cleaned_data['precio']
    #     print(type(data))
    #     print(data)
    #     if data is not None:
    #         decimalString = str(data).split('.')
    #         decimal = int(decimalString[1])
    #         if not (decimal % 5 == 0):
    #             raise ValidationError(message=_('Ingrese un valor cuyo decimal sea múltiplo de 5.'))
    #     else:
    #         raise ValidationError('Este campo es requerido.')
    #     return data

    # def clean_descripcion(self):
    #     data = self.cleaned_data['descripcion']
    #     if data is None:
    #         raise ValidationError('Este campo es requerido.')
    #     return data
    #
    # def clean_marca(self):
    #     data = self.cleaned_data['marca']
    #     if data is None:
    #         raise ValidationError('Este campo es requerido.')
    #     return data
    #
    # def clean_stock_actual(self):
    #     data = self.cleaned_data['stock_actual']
    #     if data is None:
    #         raise ValidationError('Este campo es requerido.')
    #     return data
    #
    # def clean_proveedor(self):
    #     data = self.cleaned_data['proveedor']
    #     if data is None:
    #         raise ValidationError('Este campo es requerido.')
    #     return data
