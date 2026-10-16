# Practica Avanzada - Semana 9, Sesion 2
## Pruebas Unitarias para un Resolvedor de Ecuaciones Cuadraticas

**Curso:** Construccion de Software  
**Docente:** Ing. Henderson Nozart Gibaja Reyes  
**Estudiante / Lider:** Benjamin Salas (`Benjaminsalas-Design`)  
**Entorno:** Python 3 | VS Code / PyCharm | Framework `unittest` | Git & GitHub  

---

## 1. Descripcion del Proyecto

Este proyecto implementa un resolvedor automatico de ecuaciones cuadraticas de la forma ax^2 + bx + c = 0 en la libreria `ecuacion.py` y una suite avanzada de pruebas unitarias en `test_ecuacion.py`.

El desarrollo se realizo bajo estandares de ingenieria de software:
- Funciones puras: Logica desacoplada de la interfaz de usuario (sin `input()` ni `print()`).
- Principios FIRST: Pruebas rapidas, independientes, repetibles, autovalidables y oportunas.
- Patron AAA (Arrange - Act - Assert): Estructura clara en tres bloques para cada caso de prueba.
- Control de versiones: Uso de Git, estrategia de ramificacion para Hotfix y reglas de exclusion en `.git/info/exclude`.

---

## 2. Estructura del Codigo

- `ecuacion.py`: Contiene la funcion `resolver_ecuacion(a, b, c)` que evalua los coeficientes y retorna un diccionario con las claves `"tipo"` y `"soluciones"`.
- `test_ecuacion.py`: Contiene la clase `TestResolverEcuacion` que hereda de `unittest.TestCase` con 11 casos de prueba automatizados.

---

## 3. Casos de Prueba Implementados (11 Tests)

### Pruebas Base (6)
1. `test_dos_soluciones_reales`: Verifica dos soluciones reales distintas cuando el discriminante es mayor a cero.
2. `test_una_solucion`: Verifica una solucion unica o raiz doble cuando el discriminante es igual a cero.
3. `test_sin_solucion_real`: Confirma que retorne una lista vacia si el discriminante es negativo.
4. `test_ecuacion_lineal`: Valida la resolucion de ecuaciones de primer grado cuando a = 0 y b != 0.
5. `test_coeficientes_invalidos`: Comprueba que lance una excepcion `ValueError` cuando a = 0 y b = 0.
6. `test_multiples_casos_con_subTest`: Parametriza multiples combinaciones dentro de un solo metodo mediante `subTest`.

### Pruebas Adicionales / Casos de Borde (5)
7. `test_coeficientes_grandes`: Evalua estabilidad con valores de 1,000,000 para prevenir desbordamientos.
8. `test_coeficientes_cero_parciales`: Resuelve el caso limite x^2 = 0 (a=1, b=0, c=0).
9. `test_coeficiente_a_negativo`: Valida la resolucion cuando el coeficiente principal es negativo.
10. `test_todos_coeficientes_cero`: Verifica la excepcion estricta `ValueError` cuando a=0, b=0, c=0.
11. `test_alta_precision_decimal`: Compara raices irracionales con una precision de 10 posiciones decimales.

---

## 4. Tabla Resumen de Aserciones Utilizadas

| Asercion | Proposito en el Proyecto | Ejemplo de Uso |
| :--- | :--- | :--- |
| `assertEqual(a, b)` | Compara cadenas e integridad de datos exacta. | `self.assertEqual(res["tipo"], "dos_soluciones")` |
| `assertAlmostEqual(a, b, places=N)` | Compara flotantes omitiendo errores de imprecision binaria. | `self.assertAlmostEqual(res["soluciones"][0], math.sqrt(2), places=10)` |
| `assertRaises(Exception)` | Captura y valida que se lancen excepciones esperadas. | `with self.assertRaises(ValueError): resolver_ecuacion(0, 0, 5)` |
| `assertIn(item, container)` | Garantiza la estructura del diccionario antes de acceder. | `self.assertIn("soluciones", res)` |
| `subTest(**params)` | Evalua subcasos en bucle reportando fallos de forma aislada. | `with self.subTest(a=a, b=b, c=c): ...` |

---

## 5. Experimentos Practicos Realizados

### Experimento de Fallo Intencional
1. Se modifico temporalmente la formula del discriminante en `ecuacion.py` invirtiendo el signo: `disc = b**2 + 4*a*c`.
2. Al ejecutar `python -m unittest test_ecuacion -v`, la suite detecto la anomalia e imprimio un reporte detallado con estado `FAIL`.
3. Se restauro la formula correcta `disc = b**2 - 4*a*c` devolviendo la suite a estado `OK`.

### Flujo de Trabajo Hotfix en Git
1. Se creo una rama de parche de emergencia: `git checkout -b hotfix/corregir-validacion-coeficientes`.
2. Se re-verifico la validacion estricta de parametros en `ecuacion.py`.
3. Se valido que las 11 pruebas continuaran en verde.
4. Se registro el commit con el prefijo `hotfix:` y se fusiono a la rama principal `main`.

### Configuracion de Exclusion en Git (.gitignore e ignorado propio)
1. Se creo un archivo `.gitignore` para excluir carpetas temporales de compilacion (`__pycache__/` y `*.pyc`).
2. Para omitir el propio rastreo del archivo `.gitignore` sin eliminarlo del disco local, se me configuro la exclusion en el indice interno de Git mediante los comandos:
   ```bash
   echo .gitignore >> .git/info/exclude
   git rm --cached .gitignore