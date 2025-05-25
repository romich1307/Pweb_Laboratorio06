# Pweb_Laboratorio06
## Sistema de Notas por Alumno y Curso

Este es un sistema web desarrollado con Django que permite gestionar alumnos, cursos y registrar notas por alumno y curso.

---

## Requisitos

- Python 3.10 o superior
- Django 5.2.1
- Git (opcional, solo si deseas clonar el proyecto)

---

## Instalación y ejecución del proyecto

1. **Clonar el repositorio**
    ```bash
    git clone https://github.com/romich1307/Pweb_Laboratorio06.git
    cd Pweb_Laboratorio06
    ```

2. **Crear entorno virtual (opcional pero recomendado)**
    ```bash
    python -m venv env
    ```

3. **Activar entorno virtual**

    - En **Windows**:
        ```bash
        env\Scripts\activate
        ```
    - En **Linux/Mac**:
        ```bash
        source env/bin/activate
        ```

4. **Instalar dependencias**
    ```bash
    pip install django
    ```

5. **Aplicar migraciones**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Crear superusuario** (opcional, para acceso a `/admin`)
    ```bash
    python manage.py createsuperuser
    ```

7. **Ejecutar el servidor**
    ```bash
    python manage.py runserver
    ```

---

## Estructura del Proyecto

```
Pweb_Laboratorio06/
├── sistema_notas/           # Proyecto Django
├── administracion/          # App principal
│   ├── models.py            # Modelos: Alumno, Curso, NotaAlumnoCurso
│   ├── forms.py             # Formularios personalizados
│   ├── views.py             # Vistas para registrar datos
│   ├── templates/           # HTMLs de formularios y vistas
│   └── static/              # Estilos CSS
└── db.sqlite3               # Base de datos SQLite
```

---

## Autores

- Camargo Hilachoque Romina Giuliana
- Mayta Quispe Paola Adamari