# 🌎 Balanceador de carga con Docker, Flask y Nginx — Provincias de Ecuador

Este proyecto implementa un balanceador de carga usando **Nginx** y **Docker**, distribuyendo tráfico entre dos aplicaciones Flask que muestran un mapa del Ecuador y datos de sus provincias desde una base de datos MySQL.

---

## 🚀 Tecnologías usadas

- 🐳 **Docker & Docker Compose**
- 🔥 **Flask (Python)**
- 🌐 **Nginx**
- 🐬 **MySQL**
- 🗺 **Google My Maps**

---

## 🗺 Funcionalidades

✅ Dos servidores Flask independientes mostrando:
- Mapa interactivo de Ecuador (Google Maps embebido).
- Lista de provincias con nombre, capital, área y población.

✅ Base de datos centralizada en MySQL.

✅ Balanceo de carga con Nginx, enviando las peticiones de forma alternada a ambos servidores.

✅ Visualización clara del servidor que respondió en cada petición.

---

## ⚙️ Arquitectura

```
[Usuario]
    ↓
[NGINX - Balanceador]
    ↓         ↓
[Flask App 1]  [Flask App 2]
        ↓
   [MySQL DB]
```

---

## 💻 Instalación

1️⃣ Clona el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

2️⃣ Copia tu archivo SQL (`provincias.sql`) en la raíz si no lo has importado aún.

3️⃣ Levanta los servicios

```bash
docker-compose up --build
```

4️⃣ Abre tu navegador y visita:

```
http://localhost
```

💡 Refresca la página varias veces para ver cómo cambia entre **Servidor 1** y **Servidor 2**.

---

## 🗄 Archivos principales

- `app/app.py` — Código Flask
- `app/templates/index.html` — Plantilla HTML
- `docker-compose.yml` — Orquestación de contenedores
- `nginx.conf` — Configuración de Nginx como balanceador
- `provincias.sql` — Script SQL con la tabla y datos

---

## 🛡️ Notas importantes

- Este proyecto utiliza el servidor de desarrollo Flask (no apto para producción).
- El puerto de MySQL (`3306`) queda mapeado por si quieres conectarte externamente.
- Google My Maps embebido no necesita credenciales de API.

---

## 📸 Capturas (opcional)

Puedes agregar aquí imágenes para mostrar:
- Diagrama de arquitectura
- Pantalla principal con mapa
- Balanceo (pantallas mostrando Servidor 1 y 2)

---

## 👨‍💻 Autor

- **Tu Nombre**
- **[Tu correo o perfil GitHub](https://github.com/tu-usuario)**

---

### ⭐ Si te sirvió o quieres apoyarme, dale una ⭐ al repo.
