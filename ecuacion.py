# ecuacion.py
import math 

def resolver_ecuacion(a, b, c): 
    """Resuelve ax^2 + bx + c = 0.""" 
    if a == 0: 
        if b == 0: 
            raise ValueError( 
                'No es una ecuacion valida: a y b no pueden ser ambos 0' 
            ) 
        return {"tipo": "lineal", "soluciones": [-c / b]} 
  
    disc = b ** 2 - 4 * a * c 
  
    if disc < 0: 
        return {"tipo": "sin_solucion_real", "soluciones": []} 
  
    if disc == 0: 
        return {"tipo": "una_solucion", "soluciones": [-b / (2 * a)]} 
  
    raiz = math.sqrt(disc) 
    x1 = (-b + raiz) / (2 * a) 
    x2 = (-b - raiz) / (2 * a) 
    return {"tipo": "dos_soluciones", "soluciones": [x1, x2]}