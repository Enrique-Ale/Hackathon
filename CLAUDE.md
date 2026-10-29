# Instrucciones para el desarrollo de Chamba Solidaria MX

Bienvenido al desarrollo de Chamba Solidaria MX. Este archivo guía el trabajo de los agentes y colaboradores sobre el proyecto.

## Principios Rectores
1. **Valor Funcional:** Maximizar el valor funcional demostrado en cada interacción.
2. **MVP Funcional:** Construir un recorrido funcional completo (P0) antes de añadir complejidad.
3. **Seguridad:** Protección de datos desde el diseño, sin secretos en el repositorio.
4. **Resiliencia:** La aplicación debe funcionar sin IA cuando esta no esté disponible.
5. **Transparencia:** Diferenciar claramente entre funcionalidad real y demostraciones o simulaciones.

## Configuración y Entorno
- La configuración de FreeLLMAPI debe ser desacoplada mediante variables de entorno.
- Las dependencias deben minimizarse al stack necesario (FastAPI, Next.js).
- Todo cambio destructivo o de infraestructura requiere autorización expresa.

## Flujo de Trabajo
- Trabajar en incrementos pequeños, verificables y con pruebas asociadas.
- Usar búsquedas específicas para evitar releer archivos innecesariamente.
- Documentar decisiones clave de arquitectura y contratos de API.

## Estándares de Código
- Tipado estricto con TypeScript en frontend.
- Validación de esquemas con Zod (cuando proceda).
- Contratos explícitos entre frontend y backend.

## Próximos Pasos ( MVP P0)
- Configurar entorno de desarrollo para Next.js y FastAPI.
- Implementar flujo de registro de perfil.
- Implementar catálogo de oficios.
- Implementar búsqueda de proveedores.

---
🤖 Generado con [Claude Code](https://claude.com/claude-code)
Co-Authored-By: Claude Code <noreply@anthropic.com>
