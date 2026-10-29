# Chamba Solidaria MX

Plataforma mexicana que conecta a personas que necesitan servicios con trabajadores independientes, oficios, profesionales, colectivos y cooperativas.

## Misión
Construir y estabilizar **Chamba Solidaria MX** para facilitar la capacitación, la cooperación económica territorial y la vinculación voluntaria con NODESS y otras organizaciones.

## Stack Tecnológico (Referencia MVP)
- **Frontend:** Next.js, React, TypeScript, Tailwind CSS, Lucide.
- **Backend:** Python, FastAPI.
- **Base de Datos:** Relacional (SQLite para MVP).
- **IA:** Integración con FreeLLMAPI (Multiagente).

## Estructura del Proyecto
- `/frontend`: Aplicación cliente (Next.js).
- `/backend`: API REST y lógica de negocio (FastAPI).
- `/docs`: Documentación de diseño y contratos.
- `/data`: Datos de demostración y fixtures.

## Ejecución y Desarrollo

### Backend
1. Navega a la carpeta `/backend`.
2. Crea un entorno virtual e instala las dependencias:
   ```bash
   python -m venv venv
   # En Windows:
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:
   ```bash
   uvicorn backend.app.main:app --reload
   ```
4. Poblar base de datos con datos de prueba:
   ```bash
   python -m backend.app.load_data
   ```

### Frontend
1. Navega a la carpeta `/frontend`.
2. Instala dependencias:
   ```bash
   npm install
   ```
3. Ejecuta el servidor de desarrollo:
   ```bash
   npm run dev
   ```

## Documentación de la API (P0)

La API está documentada mediante FastAPI (puedes ver el esquema interactivo en `/docs` al ejecutar el servidor).

### Endpoints principales
- `POST /usuarios/`: Registro de usuario.
- `POST /perfiles-trabajadores/`: Creación de perfil profesional.
- `GET /trabajadores/`: Listado/búsqueda de trabajadores (filtro `?oficio=`).
- `POST /solicitudes/`: Registro de necesidades de servicio.
- `GET /solicitudes/`: Listado de solicitudes.

---
🤖 Generado con [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude Code <noreply@anthropic.com>
