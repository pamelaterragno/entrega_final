# Entrega Final - Blog Django

Este es un proyecto web estilo **Blog** desarrollado en Python con el framework **Django**. La aplicación permite la creación, visualización, edición y eliminación de publicaciones. Además, incluye gestión de usuarios con autenticación, perfiles personalizados y un sistema de mensajería entre usuarios.

## 📚 Contenido

* Home
* About (Acerca del blog)
* Blog (Listado de publicaciones)
* CRUD de publicaciones (solo para usuarios logueados)
* Registro de usuarios
* Login / Logout
* Edición de perfil
* Cambio de contraseña
* Subida de foto de perfil
* Sistema de mensajería entre usuarios

---

## 🚀 Instalación

1. Cloná el repositorio:

```bash
git clone https://github.com/pamelaterragno/entrega_final.git
```

2. Creá y activá un entorno virtual:

```bash
python -m venv venv
source venv/Scripts/activate   # En Windows
```

3. Instalá las dependencias:

```bash
pip install -r requirements.txt
```

4. Aplicá las migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Creá un superusuario:

```bash
python manage.py createsuperuser
```

6. Ejecutá el servidor:

```bash
python manage.py runserver
```

---

## 🛠️ Requisitos Técnicos

* Python 3.13.2
* Django 5.2.3
* Uso de herencia de templates.
* Sistema de autenticación con login, logout y registro.
* CRUD completo protegido por autenticación.
* Perfil de usuario editable con imagen.
* Sistema de mensajería funcional.
* Git con control de versiones.
* `.gitignore` configurado para excluir:

  * `__pycache__/`
  * `db.sqlite3`
  * `media/`
  * Archivos `*.log`

---


## 📽️ Video de demostración



---
