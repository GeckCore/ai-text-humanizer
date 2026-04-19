# Changelog

Todos los cambios notables en este proyecto se documentarán en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

## [Unreleased]

### Por Añadir
- Soporte para más detectores de IA
- Interfaz web opcional
- API REST para integración
- Soporte para procesamiento por lotes
- Cache de resultados para mejorar performance

## [1.0.0] - 2024-04-18

### Añadido
- ✨ Primera release pública
- 🎯 Detección multi-plataforma con 4 detectores:
  - GPTZero
  - Writer.com
  - ZeroGPT
  - Sapling
- 🤖 Integración con Ollama para reescritura local
- 🌐 Soporte para 6 idiomas:
  - Español
  - English
  - Français
  - Deutsch
  - Português
  - Italiano
- 🔄 Sistema iterativo de humanización
- 📊 Reportes detallados de resultados
- 💾 Guardado automático de outputs
- 🎨 CLI interactivo con Rich
- ⚙️ Configuración YAML personalizable
- 📝 Documentación completa:
  - README.md
  - USAGE.md
  - ETHICS.md
  - CONTRIBUTING.md
- 🧪 Suite de tests básica
- 🔧 Script de instalación automatizada
- 🐳 GitHub Actions para CI/CD
- 📄 Licencia MIT
- ⚠️ Advertencias éticas claras

### Características Técnicas
- Detección paralela configurable
- Manejo robusto de errores
- Logging completo
- Retry automático para fallos de red
- Soporte para procesamiento por chunks
- Validación de texto
- Sistema de plugins para detectores

### Documentación
- Guía de instalación paso a paso
- Ejemplos de uso
- Guía de solución de problemas
- Mejores prácticas
- FAQ
- Consideraciones éticas detalladas

---

## Tipos de Cambios

- **Añadido** para nuevas características
- **Cambiado** para cambios en funcionalidad existente
- **Deprecado** para características que se eliminarán pronto
- **Eliminado** para características eliminadas
- **Corregido** para corrección de bugs
- **Seguridad** para vulnerabilidades

---

## Versionado

Este proyecto usa [Semantic Versioning](https://semver.org/lang/es/):

- **MAJOR** versión: cambios incompatibles en API
- **MINOR** versión: nuevas funcionalidades compatibles
- **PATCH** versión: correcciones de bugs compatibles

Ejemplo: `1.2.3` = MAJOR.MINOR.PATCH
