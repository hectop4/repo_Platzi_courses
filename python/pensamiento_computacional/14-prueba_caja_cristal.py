#Se basan en el flujo de la aplicación, en la lógica de la aplicación.
#Prueban las ramificacions, bucles y excepciones o recursiones
#regression testing: Pruebas de regresion, prueban que los cambios no rompan lo que ya estaba funcionando
#mocks: Simulan el comportamiento de objetos reales de la aplicacion

import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristalTest(unittest.TestCase):
    
    def test_es_mayor_de_edad(self):
        edad = 20
        
        resultado = es_mayor_de_edad(edad)
        
        self.assertEqual(resultado, True)
    def test_es_menor_de_edad(self):
        edad = 15
        
        resultado = es_mayor_de_edad(edad)
        
        self.assertEqual(resultado, False)
    




if __name__ == '__main__':
    unittest.main()