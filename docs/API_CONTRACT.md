# Contrato de API - Chamba Solidaria MX (MVP P0)

## Endpoints Principales

### Usuarios
- `POST /usuarios/`
  - Descripción: Crea un nuevo usuario.
  - Request Body: `UsuarioCreate` (nombre, email, telefono, es_trabajador, es_cliente).
  - Response: `UsuarioOut`

- `GET /usuarios/`
  - Descripción: Lista todos los usuarios registrados.

### Trabajadores
- `POST /perfiles-trabajadores/`
  - Descripción: Crea un perfil profesional para un usuario.
  - Request Body: `PerfilTrabajadorCreate` (usuario_id, oficio_principal, zona_cobertura, disponibilidad, rango_precio_min, rango_precio_max, descripcion).
  - Response: `PerfilTrabajadorOut`

- `GET /trabajadores/`
  - Descripción: Lista trabajadores disponibles.
  - Query Params: `oficio` (opcional, filtra por oficio).

### Solicitudes de Servicio
- `POST /solicitudes/`
  - Descripción: Registra una nueva necesidad de servicio.
  - Request Body: `SolicitudServicioCreate` (cliente_id, oficio_requerido, descripcion, ubicacion).
  - Response: `SolicitudServicioOut`

- `GET /solicitudes/`
  - Descripción: Lista todas las solicitudes.
