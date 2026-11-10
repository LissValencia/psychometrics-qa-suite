"""
PsychoMetrics QA Suite - Automated Unit Tests for GAD-7 Processor
Autor: Lisset Valencia
Descripción: Casos de prueba automatizados (Happy Path, Boundary Values y Edge Cases)
para validar la calidad de datos en la escala de ansiedad GAD-7.
"""

import pytest
from src.validators.gad7_processor import validate_and_score_gad7

def test_happy_path_minimal_anxiety():
    """Valida puntaje mínimo (0 en todos los ítems)."""
    responses = [0, 0, 0, 0, 0, 0, 0]
    result = validate_and_score_gad7(responses)
    assert result["status"] == "SUCCESS"
    assert result["total_score"] == 0
    assert result["severity"] == "Ansiedad mínima"

def test_happy_path_severe_anxiety():
    """Valida puntaje máximo (3 en todos los ítems)."""
    responses = [3, 3, 3, 3, 3, 3, 3]
    result = validate_and_score_gad7(responses)
    assert result["status"] == "SUCCESS"
    assert result["total_score"] == 21
    assert result["severity"] == "Ansiedad severa"

def test_boundary_value_moderate_anxiety():
    """Valida valor al límite de ansiedad moderada (puntaje total = 10)."""
    responses = [2, 1, 3, 0, 1, 2, 1]
    result = validate_and_score_gad7(responses)
    assert result["total_score"] == 10
    assert result["severity"] == "Ansiedad moderada"

def test_error_invalid_length_too_few():
    """QA Edge Case: Prueba que falle si se envían menos de 7 ítems."""
    with pytest.raises(ValueError) as exc_info:
        validate_and_score_gad7([1, 2, 3])
    assert "Se esperaban 7 respuestas" in str(exc_info.value)

def test_error_invalid_score_out_of_range():
    """QA Edge Case: Prueba que falle si un puntaje es mayor a 3 (e.g., 5)."""
    with pytest.raises(ValueError) as exc_info:
        validate_and_score_gad7([0, 1, 2, 5, 1, 0, 0])
    assert "fuera del rango permitido" in str(exc_info.value)

def test_error_invalid_data_type():
    """QA Edge Case: Prueba que falle si se envía un texto o tipo no entero."""
    with pytest.raises(TypeError) as exc_info:
        validate_and_score_gad7([0, 1, "invalido", 2, 1, 0, 0])
    assert "no es un entero válido" in str(exc_info.value)
