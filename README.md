# 📚 Gestión Biblioteca - Odoo

Módulo personalizado desarrollado para **Odoo 19 Community** como proyecto práctico de aprendizaje de desarrollo con Odoo y Python.

El módulo permite gestionar libros, editoriales y géneros desde una aplicación integrada en Odoo.

## 🚀 Funcionalidades

- Gestión de libros.
- Gestión de editoriales.
- Gestión de géneros.
- Relación entre libros y editoriales.
- Relación entre libros y múltiples géneros.
- Control del estado disponible/prestado de los libros.
- Acciones para prestar y devolver libros.
- Validación del número de páginas.
- Clasificación automática de libros según su número de páginas.
- Campo ISBN añadido mediante herencia de modelos.
- Vistas personalizadas de lista y formulario.
- Menús y acciones propios dentro de Odoo.

## 🧩 Conceptos de Odoo utilizados

Durante el desarrollo se han aplicado:

- Modelos personalizados con `models.Model`.
- Campos `Char`, `Integer` y `Boolean`.
- Relaciones `Many2one`, `One2many` y `Many2many`.
- Métodos de negocio.
- `ensure_one()`.
- `UserError` y `ValidationError`.
- Campos computados con `@api.depends`.
- Restricciones con `@api.constrains`.
- ORM de Odoo: `search()`, `browse()`, `create()`, `write()` y `unlink()`.
- Trabajo con recordsets mediante `mapped()`, `filtered()` y `sorted()`.
- Herencia de modelos mediante `_inherit`.
- Herencia de vistas mediante `inherit_id` y `xpath`.
- Control de acceso mediante `ir.model.access.csv`.

## 🛠️ Tecnologías

- Python
- Odoo 19 Community
- PostgreSQL
- XML
- Git / GitHub

## 📂 Estructura

gestion_biblioteca/
├── models/
│   ├── editorial.py
│   ├── genero.py
│   ├── libro.py
│   └── libro_extension.py
├── security/
│   └── ir.model.access.csv
├── views/
│   └── libro_views.xml
├── __init__.py
└── __manifest__.py

## 🎯 Objetivo del proyecto

Este proyecto forma parte de mi formación práctica en desarrollo backend con Python y Odoo.

El objetivo ha sido aprender la estructura y funcionamiento de un módulo de Odoo desarrollando una aplicación funcional desde cero, trabajando con modelos, ORM, relaciones, vistas, seguridad, lógica de negocio y herencia.

## 👨‍💻 Autor

**Anxo Pena Blanco**

Desarrollador de Aplicaciones Multiplataforma (DAM), orientado al desarrollo backend con Python y Java y actualmente ampliando conocimientos en Odoo, APIs e inteligencia artificial.