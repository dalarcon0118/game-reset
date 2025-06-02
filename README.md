# Game Reset - Plataforma de Gestión de Loterías y Juegos

## Descripción General

Game Reset es una aplicación de microservicios multi-tenant diseñada para la gestión integral de operaciones de lotería y juegos. El sistema proporciona una plataforma robusta para que bancos, sucursales y listeros administren juegos, sorteos, apuestas y registros financieros. El proyecto está dividido en un backend desarrollado con Django y un frontend (presumiblemente una aplicación móvil o web).

## Estructura del Proyecto

El proyecto está organizado en dos componentes principales:

-   **`backend/`**: Contiene la lógica del servidor, la API y la gestión de la base de datos. Desarrollado con Django y Django REST Framework.
-   **`frontend/`**: Contiene la interfaz de usuario para interactuar con el sistema. (Se necesita más información para detallar las tecnologías específicas).

## Características Principales (Backend)

Basado en el README del backend, las características clave incluyen:

-   **Multi-tenancy**: Entornos aislados para diferentes organizaciones utilizando `django-tenant-schemas`.
-   **Estructura Jerárquica**: Organización basada en árboles (Bancos, Sucursales, Listeros) utilizando `django-mptt`.
-   **Gestión de Juegos**: Creación y administración de diferentes tipos de juegos.
-   **Gestión de Sorteos**: Programación y gestión de sorteos.
-   **Registro de Apuestas**: Seguimiento de las apuestas realizadas por los clientes.
-   **Seguimiento Financiero**: Monitorización de los estados financieros en toda la organización.
-   **Reglas de Pago**: Configuración de reglas de pago personalizadas para diferentes juegos.
-   **Límites de Números**: Establecimiento de límites para números específicos para gestionar el riesgo.

## Arquitectura del Backend

La aplicación backend sigue una arquitectura de microservicios con los siguientes componentes principales:

-   **Authentication**: Gestión de usuarios y autenticación.
-   **Structure**: Gestión de la estructura organizativa jerárquica.
-   **Game Type**: Configuración y gestión de tipos de juego.
-   **Draw**: Programación de sorteos y resultados.
-   **Bet**: Registro y seguimiento de apuestas.
-   **Payout Rule**: Configuración de los pagos de los juegos.
-   **Number Limit Rule**: Gestión de riesgos para números específicos.
-   **Financial Statement**: Seguimiento e informes financieros.

## Pila Tecnológica (Backend)

-   **Backend**: Django, Django REST Framework
-   **Base de Datos**: PostgreSQL
-   **Autenticación**: JWT (JSON Web Tokens)
-   **Caché**: Redis
-   **Cola de Mensajes**: RabbitMQ
-   **Multi-tenancy**: `django-tenant-schemas`
-   **Estructura de Árbol**: `django-mptt`

## Pila Tecnológica (Frontend)

La información del frontend es limitada, pero la estructura de carpetas sugiere el uso de:

-   **Framework**: Posiblemente React Native con Expo (basado en `app.json`, `app/` estructura con archivos `.tsx`).
-   **Lenguaje**: TypeScript.
-   **Gestor de Paquetes**: Yarn (basado en `yarn.lock`).

## Cómo Empezar

### Backend

Consulte el archivo README.md en el directorio backend para obtener instrucciones detalladas sobre la configuración y ejecución del backend.

Para ejecutar migraciones en el contenedor Docker:

1. Ejecutar migraciones directamente:
```bash
docker-compose -f docker-compose.dev.yml exec web python manage.py makemigrations
docker-compose -f docker-compose.dev.yml exec web python manage.py migrate
```

### Frontend

(Se necesitan instrucciones específicas para el frontend. Generalmente implicaría instalar dependencias con `yarn install` y luego iniciar el servidor de desarrollo, por ejemplo, con `yarn start` o `expo start`).

## Documentación de la API (Backend)

La documentación de la API del backend está disponible en `/api/docs/` cuando el servidor del backend está en funcionamiento.

## Contribuir

(Detalles sobre cómo contribuir al proyecto, si aplica).

## Licencia

[Especificar la licencia del proyecto aquí]