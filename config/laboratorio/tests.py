from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):
    @classmethod 
    def setUpTestData(cls):
        # Crear datos de prueba
        cls.laboratorio = Laboratorio.objects.create(
            nombre='Laboratorio Test',
            ciudad='Ciudad Test', 
            pais='País Test'
        )

    def test_laboratorio_data(self):
        # Verificar que los datos coinciden
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, 'Laboratorio Test')
        self.assertEqual(laboratorio.ciudad, 'Ciudad Test')
        self.assertEqual(laboratorio.pais, 'País Test')

    def test_laboratorio_list_view(self):
        # Verificar que la URL devuelve HTTP 200
        response = self.client.get(reverse('laboratorio:laboratorio_list'))
        self.assertEqual(response.status_code, 200)
        # Verificar que se usa la plantilla correcta
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_list.html')
        # Verificar contenido HTML esperado
        self.assertContains(response, 'Laboratorio Test')
        self.assertContains(response, 'Ciudad Test')
        self.assertContains(response, 'País Test')