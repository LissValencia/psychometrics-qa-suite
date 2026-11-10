"""
PsychoMetrics QA Suite - GAD-7 Processor & Data Validation Module
Autor: Lisset Valencia
Descripción: Procesa las respuestas de la escala de ansiedad GAD-7, 
calcula el puntaje total y aplica validaciones estricta de QA sobre los datos de entrada.
"""

def validate_and_score_gad7(responses):
    """
    Valida un diccionario o lista de respuestas para la escala GAD-7.
    
    Reglas de Negocio / QA:
    1. Deben entregarse exactamente 7 ítems.
    2. Cada valor debe ser un entero entre 0 y 3.
    3. Ningún valor puede ser nulo (None) o de tipo inválido.
    """
    if not isinstance(responses, list):
        raise TypeError("Error QA: Las respuestas deben ser entregadas en formato de lista.")
    
    if len(responses) != 7:
        raise ValueError(f"Error QA: Se esperaban 7 respuestas, pero se recibieron {len(responses)}.")
    
    total_score = 0
    for idx, score in enumerate(responses, start=1):
        if not isinstance(score, int) or isinstance(score, bool):
            raise TypeError(f"Error QA en ítem {idx}: El valor '{score}' no es un entero válido.")
        
        if score < 0 or score > 3:
            raise ValueError(f"Error QA en ítem {idx}: El valor {score} está fuera del rango permitido (0-3).")
            
        total_score += score
        
    # Clasificación clínica basada en el puntaje total
    if total_score <= 4:
        severity = "Ansiedad mínima"
    elif total_score <= 9:
        severity = "Ansiedad leve"
    elif total_score <= 14:
        severity = "Ansiedad moderada"
    else:
        severity = "Ansiedad severa"
        
    return {
        "status": "SUCCESS",
        "total_score": total_score,
        "severity": severity,
        "items_processed": len(responses)
    }

if __name__ == "__main__":
    # Prueba manual básica
    sample_data = [2, 1, 3, 0, 1, 2, 1]
    result = validate_and_score_gad7(sample_data)
    print("Prueba de ejecución exitosa:")
    print(result)
