from django.db import models
from django.core.validators import MinValueValidator
from datetime import date

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(
        max_length=100,
        default='',  # Valor por defecto para ciudad
        help_text='Ciudad donde se encuentra el laboratorio'
    )
    pais = models.CharField(
        max_length=100,
        default='',    # Valor por defecto para país
        help_text='País donde se encuentra el laboratorio'
    )
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Laboratorio"
        verbose_name_plural = "Laboratorios"

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.OneToOneField(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='director'
    )
    especialidad = models.CharField(
        max_length=100,
        default='Sin especialidad',
        help_text='Especialidad del Director General'
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Director General"
        verbose_name_plural = "Directores Generales"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    laboratorio = models.ForeignKey(
        Laboratorio,
        on_delete=models.CASCADE,
        related_name='productos'
    )
    f_fabricacion = models.DateField(
        validators=[MinValueValidator(date(2015, 1, 1))]
    )
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"