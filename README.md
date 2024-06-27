# Sistema de Gestión Hospitalaria

Este es un proyecto para la materia de Calidad de Software donde desarrollé un sistema de gestión hospitalaria utilizando Django. El sistema permite gestionar pacientes, doctores y citas.

## Funcionalidades

- **Gestión de Pacientes**: Puedo agregar, editar, eliminar y ver detalles de los pacientes.
- **Gestión de Doctores**: Puedo hacer lo mismo con los doctores, y sus nombres siempre llevan el prefijo "Doc.".
- **Gestión de Citas**: Puedo manejar las citas entre pacientes y doctores, especificando la fecha y el motivo.

## Requisitos

- Python 3.6 o superior
- Django 3.0 o superior

## Instalación

1. **Clonar el repositorio**

   ```sh
   git clone https://github.com/tu-usuario/sistema-gestion-hospitalaria.git
   cd sistema-gestion-hospitalaria
   ```

2. **Crear y activar un entorno virtual**

   ```sh
   python -m venv venv
   source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
   ```

3. **Instalar las dependencias**

   ```sh
   pip install -r requirements.txt
   ```

4. **Aplicar migraciones**

   ```sh
   cd hospital
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Ejecutar el servidor**

   ```sh
   python manage.py runserver
   ```

6. **Abrir el navegador**

   Navego a `http://127.0.0.1:8000` para ver la aplicación.

## Uso

Puedo gestionar pacientes, doctores y citas a través de una interfaz sencilla y limpia hecha con Bootstrap.

## Evaluación

Este proyecto se evaluará en función de su funcionalidad y la documentación del código. Es un examen para la materia de Calidad de Software.

---
