# Prompts de Inteligencia Artificial - Evaluación N°1 Backend

Este documento registra el uso de herramientas de IA (Claude) como apoyo
para el desarrollo del proyecto, según lo requerido en la pauta de evaluación.

## 1. Generación de datos de prueba (JSON)

**Prompt utilizado:**
"Genera un fixture JSON de Django con datos ficticios para los modelos
Teacher, Course, Student y StudentCourse, con 3 profesores, 4 cursos,
5 estudiantes y 7 inscripciones cruzadas."

**Resultado:** Se utilizó para generar el archivo `academic/fixtures/initial_data.json`
con datos de prueba realistas para precargar la base de datos.

## 2. Estructura de plantillas HTML/Bootstrap

**Prompt utilizado:**
"Ayúdame a crear una plantilla base en Django con Bootstrap 5 vía CDN,
con navbar de navegación, y dos plantillas hijas que muestren tablas
de datos cargadas dinámicamente vía fetch()."

**Resultado:** Se utilizó como base para `base.html`, `courses.html` y `students.html`,
implementando el patrón de "enmascaramiento" de la API DRF mediante JavaScript asíncrono.

## 3. Arquitectura general del proyecto

**Prompt utilizado:**
"Explícame cómo estructurar un proyecto Django + DRF donde las vistas HTML
consuman los endpoints de la propia API vía fetch(), en vez de usar
Django Templates directamente con los objetos del ORM."

**Resultado:** Definió la separación entre las vistas de API (ListAPIView)
y las vistas HTML (render de templates), conectadas mediante JavaScript.