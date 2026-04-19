# AI Text Humanizer

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**Herramienta de análisis y reescritura de texto usando IA local**

[Características](#características) • [Instalación](#instalación) • [Uso](#uso) • [Ética](#consideraciones-éticas)

</div>

---

## ⚠️ ADVERTENCIA IMPORTANTE - LEE ESTO PRIMERO

### Consideraciones Éticas

Esta herramienta fue desarrollada con propósitos **educativos e investigativos**. El uso de esta tecnología tiene implicaciones éticas significativas:

#### ✅ **Usos Legítimos:**
- Investigación académica sobre detección de IA
- Análisis de limitaciones de detectores actuales
- Mejora de habilidades de escritura con transparencia
- Desarrollo de herramientas de parafraseo legítimas
- Estudios sobre procesamiento de lenguaje natural

#### ❌ **Usos Inapropiados:**
- Fraude académico (plagio)
- Evasión de políticas institucionales sin divulgación
- Engaño en contextos profesionales
- Violación de términos de servicio de plataformas educativas

**El usuario es completamente responsable del uso de esta herramienta.** Los desarrolladores no respaldan ni apoyan usos no éticos.

---

## 🎯 Características

- **Detección Multi-Plataforma**: Analiza texto usando múltiples detectores de IA gratuitos
- **IA Local**: Usa Ollama con modelos locales (sin enviar datos a terceros)
- **Iterativo**: Ciclo automático de reescritura y verificación
- **Multi-Idioma**: Soporte para español, inglés y otros idiomas
- **Reportes Detallados**: Análisis completo de resultados
- **100% Gratuito**: Sin APIs de pago
- **CLI Interactivo**: Interfaz de línea de comandos fácil de usar

## 📋 Requisitos Previos

### Sistema
- Python 3.8 o superior
- Ollama instalado ([Instrucciones](https://ollama.ai))
- Navegador Chromium/Chrome (para Playwright)
- 8GB+ RAM recomendado

### Instalar Ollama y Modelo

```bash
# Instalar Ollama (macOS/Linux)
curl -fsSL https://ollama.ai/install.sh | sh

# Descargar modelo qwen2.5:14b
ollama pull qwen2.5:14b

# Verificar instalación
ollama list
```

## 🚀 Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/ai-text-humanizer.git
cd ai-text-humanizer
```

### 2. Crear Entorno Virtual

```bash
python -m venv venv

# Activar en Linux/macOS
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate
```

### 3. Instalar Dependencias

```bash
pip install -r requirements.txt

# Instalar navegadores para Playwright
playwright install chromium
```

## 💻 Uso

### Modo Básico

```bash
python -m src.main
```

El programa te guiará interactivamente:

1. **Seleccionar idioma**: español, inglés, etc.
2. **Pegar texto**: El texto que deseas analizar
3. **Análisis automático**: Se ejecutan múltiples detectores
4. **Reescritura iterativa**: La IA local reescribe el texto
5. **Verificación**: Se vuelve a analizar hasta obtener resultado óptimo
6. **Reporte final**: Análisis completo y texto humanizado

### Modo Avanzado

```bash
# Especificar idioma directamente
python -m src.main --language es

# Usar archivo de entrada
python -m src.main --input texto.txt

# Configurar número de iteraciones máximas
python -m src.main --max-iterations 5

# Umbral de confianza de IA (0-100)
python -m src.main --threshold 10
```

### Ejemplo de Sesión

```
🤖 AI Text Humanizer v1.0.0
==========================

[?] Selecciona el idioma del texto:
  > Español
    English
    Français

[?] Método de entrada:
  > Pegar texto
    Cargar desde archivo

Pega tu texto (Ctrl+D o Enter dos veces para terminar):
> [Tu texto aquí...]

📊 Analizando texto con detectores de IA...
  ✓ GPTZero: 85% IA detectada
  ✓ Copyleaks: 78% IA detectada
  ✓ Writer.com: 82% IA detectada

Promedio: 81.67% - ALTO contenido de IA detectado

🔄 Reescribiendo con IA local (qwen2.5:14b)...
⏳ Iteración 1/5...

📊 Re-analizando versión humanizada...
  ✓ GPTZero: 23% IA detectada
  ✓ Copyleaks: 15% IA detectada
  ✓ Writer.com: 18% IA detectada

Promedio: 18.67% - Mejora significativa

🎉 ¡Objetivo alcanzado! Texto humanizado exitosamente.

📄 Guardando reporte en: output/report_20240418_115530.txt
💾 Guardando texto humanizado en: output/humanized_20240418_115530.txt
```

## 🏗️ Arquitectura

```
src/
├── main.py                 # Punto de entrada principal
├── detectors/             # Módulo de detección
│   ├── base_detector.py   # Clase base para detectores
│   ├── gptzero.py        # Detector GPTZero
│   ├── copyleaks.py      # Detector Copyleaks
│   ├── writer.py         # Detector Writer.com
│   └── manager.py        # Orquestador de detectores
├── rewriter/             # Módulo de reescritura
│   └── ollama_engine.py  # Motor de reescritura con Ollama
└── utils/                # Utilidades
    ├── logger.py         # Sistema de logging
    └── text_processor.py # Procesamiento de texto
```

## 🔧 Configuración

Edita `config/config.yaml` para personalizar:

```yaml
# Configuración de IA Local
ollama:
  model: "qwen2.5:14b"
  temperature: 0.7
  max_tokens: 4096

# Detectores habilitados
detectors:
  - gptzero
  - copyleaks
  - writer
  - sapling

# Configuración de iteraciones
rewriting:
  max_iterations: 5
  target_threshold: 10  # Máximo % de IA aceptable
  min_improvement: 5    # Mejora mínima requerida entre iteraciones

# Idiomas soportados
languages:
  - es  # Español
  - en  # English
  - fr  # Français
  - de  # Deutsch
```

## 📊 Detectores Soportados

| Detector | Gratis | Requiere Cuenta | Precisión |
|----------|--------|-----------------|-----------|
| GPTZero | ✅ | ❌ | Alta |
| Copyleaks | ✅ (limitado) | ✅ | Alta |
| Writer.com | ✅ | ❌ | Media |
| Sapling | ✅ | ❌ | Media |
| ZeroGPT | ✅ | ❌ | Media |

**Nota**: Algunos servicios pueden tener límites de uso. El programa maneja automáticamente fallos y usa detectores disponibles.

## 🛠️ Desarrollo

### Ejecutar Tests

```bash
pytest tests/
```

### Contribuir

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-caracteristica`)
3. Commit cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo `LICENSE` para más detalles.

## 🤝 Contribuidores

- **Uso Responsable**: Lee `docs/ETHICS.md` antes de usar
- **Reporte de Bugs**: Usa GitHub Issues
- **Sugerencias**: Pull Requests bienvenidos

## 📚 Recursos Adicionales

- [Documentación de Ollama](https://ollama.ai/docs)
- [Playwright Documentation](https://playwright.dev/python/)
- [Ética en IA](docs/ETHICS.md)
- [Guía de Uso Detallada](docs/USAGE.md)

## ⚖️ Disclaimer Legal

Este software se proporciona "tal cual", sin garantías de ningún tipo. El uso de esta herramienta es responsabilidad exclusiva del usuario. Los desarrolladores no se hacen responsables de:

- Violaciones de políticas académicas o institucionales
- Consecuencias legales derivadas del mal uso
- Daños o pérdidas resultantes del uso del software

**Úsalo éticamente, úsalo responsablemente.**

---

<div align="center">
Hecho con 💙 para investigación y educación
</div>
