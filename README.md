# 🧠 PsychoMetrics QA Suite: Plataforma automatizada de validación y pruebas

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pytest](https://img.shields.io/badge/Testing-Pytest-green?logo=pytest)
![QA](https://img.shields.io/badge/QA-Data%20Validation-orange)
![License](https://img.shields.io/badge/License-MIT-brightgreen)

## Visión General del Proyecto

**PsychoMetrics QA Suite** es un marco de trabajo de aseguramiento de calidad diseñado para validar la integridad de datos y automatizar pruebas sobre instrumentos de evaluación psicológica.

Este módulo implementa lógica de negocio en **Python** para procesar la escala de ansiedad **GAD-7 (Generalized Anxiety Disorder-7)**, garantizando que las respuestas ingresadas cumplan con restricciones de tipo, rango y longitud antes de ser procesadas por servicios downstream o APIs.

---

## Arquitectura del Proyecto

```text
psychometrics-qa-suite/
├── docs/                 # Documentación técnica y especificaciones de QA
├── src/
│   ├── validators/       # Lógica de validación de reglas de negocio (GAD-7)
│   └── utils/            # Funciones auxiliares de datos
└── tests/
    └── api/              # Casos de prueba automatizados (Pytest / Unittest)
