#Se basan en la especificacion de una funcion o programa
#Prueba inputs y valida Outputs
#Prueba caja negra: No se conoce la implementacion interna
#Unit testing: Pruebas unitarias , prueban funcion por funcion
#Integration testing: Pruebas de integracion, prueban que todos los modulos funcionan entre si
#Functional testing: Pruebas funcionales, prueban toda la aplicacion

import unittest

def suma(num_1, num_2):
    return abs(num_1) + num_2


class CajaNegraTest(unittest.TestCase):
# Aca se crean los casos de prueba
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5
        resultado = suma(num_1,num_2)
        self.assertEqual(resultado, 15)
    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7
        resultado = suma(num_1,num_2)
        self.assertEqual(resultado, -17)

if __name__ == '__main__':
    unittest.main()

