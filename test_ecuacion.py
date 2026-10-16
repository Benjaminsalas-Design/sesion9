# test_ecuacion.py 
import math
import unittest 
from ecuacion import resolver_ecuacion 
  
class TestResolverEcuacion(unittest.TestCase): 

    # ------------------ PRUEBAS BASE ------------------
  
    def test_dos_soluciones_reales(self): 
        """Valida ecuaciones cuadraticas con dos soluciones reales distintas."""
        # 1. Arrange
        a, b, c = 1, -5, 6
        tipo_esperado = "dos_soluciones"
        x1_esperado, x2_esperado = 3.0, 2.0

        # 2. Act
        res = resolver_ecuacion(a, b, c) 

        # 3. Assert
        self.assertIn("soluciones", res)
        self.assertEqual(res["tipo"], tipo_esperado) 
        self.assertEqual(len(res["soluciones"]), 2)
        self.assertAlmostEqual(res["soluciones"][0], x1_esperado) 
        self.assertAlmostEqual(res["soluciones"][1], x2_esperado) 
  
    def test_una_solucion(self): 
        """Verifica la existencia y valor unico cuando el discriminante es cero."""
        # 1. Arrange
        a, b, c = 1, -2, 1
        tipo_esperado = "una_solucion"
        solucion_esperada = 1.0

        # 2. Act
        res = resolver_ecuacion(a, b, c) 

        # 3. Assert
        self.assertIn("soluciones", res)
        self.assertEqual(res["tipo"], tipo_esperado) 
        self.assertEqual(len(res["soluciones"]), 1)
        self.assertAlmostEqual(res["soluciones"][0], solucion_esperada) 
  
    def test_sin_solucion_real(self): 
        """Confirma que retorne lista vacia si el discriminante es negativo."""
        # 1. Arrange
        a, b, c = 1, 0, 1
        tipo_esperado = "sin_solucion_real"

        # 2. Act
        res = resolver_ecuacion(a, b, c) 

        # 3. Assert
        self.assertIn("soluciones", res)
        self.assertEqual(res["tipo"], tipo_esperado) 
        self.assertEqual(res["soluciones"], []) 
  
    def test_ecuacion_lineal(self): 
        """Valida la resolucion de ecuaciones lineales cuando a = 0 y b != 0."""
        # 1. Arrange
        a, b, c = 0, 2, 4
        tipo_esperado = "lineal"
        solucion_esperada = -2.0

        # 2. Act
        res = resolver_ecuacion(a, b, c) 

        # 3. Assert
        self.assertIn("soluciones", res)
        self.assertEqual(res["tipo"], tipo_esperado) 
        self.assertEqual(len(res["soluciones"]), 1)
        self.assertAlmostEqual(res["soluciones"][0], solucion_esperada) 
  
    def test_coeficientes_invalidos(self): 
        """Verifica que lance ValueError si a y b son ambos cero."""
        # 1. Arrange
        a, b, c = 0, 0, 5

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError): 
            resolver_ecuacion(a, b, c) 
  
    def test_multiples_casos_con_subTest(self): 
        """Evalua multiples combinaciones parametrizadas usando subTests."""
        # 1. Arrange
        casos = [ 
            (1, 0, -4, "dos_soluciones", [2.0, -2.0]), 
            (2, -4, 2, "una_solucion", [1.0]), 
            (1, 2, 5, "sin_solucion_real", []), 
        ] 
        
        # 2. Act & 3. Assert
        for a, b, c, tipo_esp, sol_esp in casos: 
            with self.subTest(a=a, b=b, c=c): 
                res = resolver_ecuacion(a, b, c) 
                self.assertIn("soluciones", res)
                self.assertEqual(res["tipo"], tipo_esp) 
                self.assertEqual(len(res["soluciones"]), len(sol_esp))
                for obt, esp in zip(res["soluciones"], sol_esp): 
                    self.assertAlmostEqual(obt, esp) 

    # ------------------ PRUEBAS ADICIONALES (RETO) ------------------

    def test_coeficientes_grandes(self):
        """Maneja coeficientes de alto valor sin desbordamiento de memoria."""
        # 1. Arrange
        a, b, c = 1000000, 1000000, 1000000

        # 2. Act
        res = resolver_ecuacion(a, b, c)

        # 3. Assert
        self.assertEqual(res["tipo"], "sin_solucion_real")
        self.assertEqual(res["soluciones"], [])

    def test_coeficientes_cero_parciales(self):
        """Resuelve el caso limite x^2 = 0 retornando solucion cero."""
        # 1. Arrange
        a, b, c = 1, 0, 0

        # 2. Act
        res = resolver_ecuacion(a, b, c)

        # 3. Assert
        self.assertEqual(res["tipo"], "una_solucion")
        self.assertEqual(len(res["soluciones"]), 1)
        self.assertAlmostEqual(res["soluciones"][0], 0.0)

    def test_coeficiente_a_negativo(self):
        """Resuelve correctamente ecuaciones con coeficiente principal negativo."""
        # 1. Arrange
        a, b, c = -1, 0, 4

        # 2. Act
        res = resolver_ecuacion(a, b, c)

        # 3. Assert
        self.assertEqual(res["tipo"], "dos_soluciones")
        self.assertEqual(len(res["soluciones"]), 2)
        self.assertAlmostEqual(res["soluciones"][0], -2.0)
        self.assertAlmostEqual(res["soluciones"][1], 2.0)

    def test_todos_coeficientes_cero(self):
        """Lanza ValueError cuando todos los coeficientes a, b y c son cero."""
        # 1. Arrange
        a, b, c = 0, 0, 0

        # 2. Act & 3. Assert
        with self.assertRaises(ValueError):
            resolver_ecuacion(a, b, c)

    def test_alta_precision_decimal(self):
        """Valida raices irracionales con precision alta de 10 decimales."""
        # 1. Arrange
        a, b, c = 1, 0, -2

        # 2. Act
        res = resolver_ecuacion(a, b, c)

        # 3. Assert
        self.assertEqual(res["tipo"], "dos_soluciones")
        self.assertEqual(len(res["soluciones"]), 2)
        self.assertAlmostEqual(res["soluciones"][0], math.sqrt(2), places=10)
        self.assertAlmostEqual(res["soluciones"][1], -math.sqrt(2), places=10)


if __name__ == '__main__': 
    unittest.main()