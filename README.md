# Aplicación de Registro de Eventos 

Proyecto desarrollado en **Django** como parte del Bootcamp Talento Digital.  
La aplicación permite **registrar eventos** junto con una lista de **participantes** asociados.

---

## Funcionalidades

- Registrar eventos con:
  - Nombre (máx. 100 caracteres, obligatorio)
  - Fecha (debe ser futura, obligatorio)
  - Ubicación (opcional)
- Agregar múltiples participantes por evento:
  - Nombre del participante (obligatorio)
  - Correo electrónico (obligatorio, validado como email)
- Validaciones:
  - No se permite guardar un evento con fecha pasada.
  - Los errores se muestran debajo de cada campo.
- Plantillas reutilizables y base con Bootstrap.
- Mensajes de confirmación y error usando el sistema de `messages` de Django.

---

## Requisitos

- Python 3.10+  
- Django 5.x  
- Virtualenv (recomendado)

---

## Instalación y ejecución

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/CatalinaMonserrat/Aplicaci-n_registro_eventos.git
   cd registro-eventos
2. Crear y activar entorno virtual:
   ```bash
   python -m venv env
   # Windows PowerShell
   env\Scripts\activate
   # Linux/Mac
   source env/bin/activate
4. Instalar dependencias:
   ```bash
   pip install django
5. Aplicar migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
6. Ejecutar servidor de desarrollo:
   ```bash
   python manage.py runserver
7. Abrir en el navegador:
👉 http://127.0.0.1:8000/

---

## Estructura del Proyecto
```bash
gestor_eventos/
│   manage.py
│   README.md
│
├── gestor_eventos/        # Configuración principal del proyecto
│
├── registro/              # App de registro de eventos
   ├── models.py          # Modelos: Evento y Participante
   ├── forms.py           # Formularios con validaciones
   ├── views.py           # Lógica GET/POST
   ├── templates/
      ├── base.html
      └── registro/
          ├── registrar_evento.html
          ├── _form_evento.html
          ├── _form_participantes.html
          └── exito.html
   
