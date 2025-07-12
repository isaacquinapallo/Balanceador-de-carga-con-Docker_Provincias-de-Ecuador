# Balanceador de carga con Docker, Flask y Nginx — Provincias de Ecuador

Este proyecto implementa un balanceador de carga usando Nginx y Docker, distribuyendo tráfico entre dos aplicaciones Flask que muestran un mapa del Ecuador y datos de sus provincias desde una base de datos MySQL.

---

## Tecnologías usadas

- **Docker & Docker Compose**
- **Flask (Python)**
- **Nginx**
- **MySQL**
- **Google My Maps**

---

## Funcionalidades

Dos servidores Flask independientes mostrando:
- Mapa interactivo de Ecuador (Google Maps embebido).
- Lista de provincias con nombre, capital, área y población.

Base de datos centralizada en MySQL.

Balanceo de carga con Nginx, enviando las peticiones de forma alternada a ambos servidores.

Visualización clara del servidor que respondió en cada petición.

---

## Instalación

1️. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

2️. Copia tu archivo SQL (`provincias.sql`) en la raíz si no lo has importado aún.

3️. Levanta los servicios

```bash
docker-compose up --build
```

4️. Abre tu navegador y visita:

```
http://localhost
```

Refresca la página varias veces para ver cómo cambia entre **Servidor 1** y **Servidor 2**.

---

## Archivos principales

- `app/app.py` — Código Flask
- `app/templates/index.html` — Plantilla HTML
- `docker-compose.yml` — Orquestación de contenedores
- `nginx.conf` — Configuración de Nginx como balanceador
- `provincias.sql` — Script SQL con la tabla y datos

---

## Notas importantes

- Este proyecto utiliza el servidor de desarrollo Flask (no apto para producción).
- El puerto de MySQL (`3306`) queda mapeado por si quieres conectarte externamente.
- Google My Maps embebido no necesita credenciales de API.

---

## Capturas (opcional)

Puedes agregar aquí imágenes para mostrar:
- Diagrama de arquitectura
  
  <img width="233" height="293" alt="image" src="https://github.com/user-attachments/assets/7873c636-6a24-4f73-8ae2-d16fe0564716" />


- Pantalla principal con mapa
  
  <img width="623" height="825" alt="image" src="https://github.com/user-attachments/assets/4afb6c5f-a5a9-422c-849e-418a7c0320fc" />

  
- Balanceo (pantallas mostrando Servidor 1 y 2)
  
    <img width="832" height="412" alt="image" src="https://github.com/user-attachments/assets/a9ef2efa-4b5b-4599-acbb-5d91c734f028" />
    
---

## Autor

- **Isaac Quinapallo**
