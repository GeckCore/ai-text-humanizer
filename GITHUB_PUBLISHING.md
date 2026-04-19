# 📤 Guía para Publicar en GitHub

## Paso 1: Crear Repositorio en GitHub

1. Ve a https://github.com/new
2. Nombre del repositorio: `ai-text-humanizer`
3. Descripción: "Herramienta para analizar y humanizar texto generado por IA"
4. Visibilidad: **Público** (para que otros puedan usar)
5. **NO** marques "Initialize with README" (ya tenemos uno)
6. **NO** marques "Add .gitignore" (ya tenemos uno)
7. **NO** marques "Choose a license" (ya tenemos LICENSE)
8. Click "Create repository"

## Paso 2: Inicializar Git Local

```bash
# Navegar al directorio del proyecto
cd ai-text-humanizer

# Inicializar git
git init

# Añadir todos los archivos
git add .

# Primer commit
git commit -m "feat: initial release v1.0.0

- Multi-platform AI detection (GPTZero, Writer, ZeroGPT, Sapling)
- Local AI rewriting with Ollama
- Support for 6 languages
- Interactive CLI interface
- Comprehensive documentation
- Automated testing suite
- Ethical use guidelines"
```

## Paso 3: Conectar con GitHub

```bash
# Reemplaza 'tu-usuario' con tu username de GitHub
git remote add origin https://github.com/tu-usuario/ai-text-humanizer.git

# Verificar remote
git remote -v

# Push a GitHub
git branch -M main
git push -u origin main
```

## Paso 4: Configurar GitHub (Opcional pero Recomendado)

### A. Configurar Topics

En tu repositorio de GitHub:
1. Click en "⚙️ Settings" (engranaje junto a About)
2. En "Topics", añade:
   - `ai`
   - `natural-language-processing`
   - `text-humanizer`
   - `ai-detection`
   - `ollama`
   - `python`
   - `nlp`
   - `text-rewriting`

### B. Configurar About

1. Description: "🤖 Herramienta para analizar y humanizar texto generado por IA usando modelos locales"
2. Website: (opcional) tu sitio web
3. Topics: (ya configurados arriba)

### C. Habilitar Issues

1. Settings → General
2. Features → ✓ Issues

### D. Habilitar Discussions

1. Settings → General
2. Features → ✓ Discussions
3. Ir a "Discussions" tab
4. Setup discussions

### E. Configurar Branch Protection (Recomendado)

1. Settings → Branches
2. Add branch protection rule:
   - Branch name pattern: `main`
   - ✓ Require pull request reviews before merging
   - ✓ Require status checks to pass before merging
   - ✓ Require branches to be up to date before merging

### F. Añadir Description Template para Issues

Crear `.github/ISSUE_TEMPLATE/bug_report.md`:

```markdown
---
name: Bug Report
about: Report a bug
title: '[BUG] '
labels: bug
assignees: ''
---

**Describe the bug**
A clear and concise description.

**To Reproduce**
Steps to reproduce:
1. Go to '...'
2. Click on '....'
3. See error

**Expected behavior**
What you expected to happen.

**Screenshots**
If applicable.

**Environment:**
 - OS: [e.g. Ubuntu 22.04]
 - Python: [e.g. 3.10.5]
 - Version: [e.g. 1.0.0]

**Logs**
```
Paste relevant logs
```

**Additional context**
Any other context.
```

## Paso 5: Crear Primera Release

1. En GitHub, ir a "Releases"
2. Click "Create a new release"
3. Tag version: `v1.0.0`
4. Release title: `v1.0.0 - Initial Public Release`
5. Description:

```markdown
## 🎉 First Public Release!

### ✨ Features

- **Multi-Platform AI Detection**
  - GPTZero
  - Writer.com
  - ZeroGPT
  - Sapling AI
  
- **Local AI Rewriting**
  - Powered by Ollama
  - Uses qwen2.5:14b model
  - 100% private and offline
  
- **Multi-Language Support**
  - Español, English, Français
  - Deutsch, Português, Italiano
  
- **User-Friendly Interface**
  - Interactive CLI
  - Progress tracking
  - Detailed reports

### 📚 Documentation

- Comprehensive README
- Detailed usage guide
- Ethical use guidelines
- Contributing guide

### 🔧 Installation

```bash
git clone https://github.com/tu-usuario/ai-text-humanizer.git
cd ai-text-humanizer
chmod +x install.sh
./install.sh
```

### ⚠️ Important

This tool is for research and educational purposes.
Please read `docs/ETHICS.md` before using.

---

**Full Changelog**: https://github.com/tu-usuario/ai-text-humanizer/blob/main/CHANGELOG.md
```

6. Adjuntar archivos (opcional):
   - Source code (zip)
   - Source code (tar.gz)

7. Click "Publish release"

## Paso 6: Añadir Badges al README

Editar `README.md` y añadir al inicio (después del título):

```markdown
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/tu-usuario/ai-text-humanizer.svg)](https://github.com/tu-usuario/ai-text-humanizer/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/tu-usuario/ai-text-humanizer.svg)](https://github.com/tu-usuario/ai-text-humanizer/issues)
[![GitHub Forks](https://img.shields.io/github/forks/tu-usuario/ai-text-humanizer.svg)](https://github.com/tu-usuario/ai-text-humanizer/network)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
```

Commit y push:
```bash
git add README.md
git commit -m "docs: add badges to README"
git push
```

## Paso 7: Configurar GitHub Pages (Opcional)

Si quieres documentación web:

1. Settings → Pages
2. Source: "Deploy from a branch"
3. Branch: `main` / `docs`
4. Save

## Paso 8: Promover el Proyecto

### A. Social Media

Comparte en:
- Twitter/X
- LinkedIn
- Reddit (r/MachineLearning, r/Python)
- Dev.to
- Hacker News

Ejemplo de post:
```
🚀 Lanzamiento: AI Text Humanizer

Herramienta open-source para:
✅ Detectar texto generado por IA
✅ Humanizar texto usando IA local (Ollama)
✅ 6 idiomas soportados
✅ 100% gratis y privado

GitHub: [tu-link]

#AI #NLP #Python #OpenSource
```

### B. Submit a Product Hunt (Opcional)

https://www.producthunt.com/posts/new

### C. Add to Awesome Lists

Busca listas de "Awesome AI" o "Awesome NLP" y submit via PR.

## Paso 9: Mantener el Proyecto

### Workflow de Desarrollo

```bash
# Crear rama para feature
git checkout -b feature/nueva-caracteristica

# Hacer cambios
# ... editar archivos ...

# Commit
git add .
git commit -m "feat: add new feature"

# Push
git push origin feature/nueva-caracteristica

# En GitHub: Crear Pull Request
# Después de review: Merge
```

### Versionado

Para nuevas versiones:

```bash
# Actualizar CHANGELOG.md
# Actualizar version en setup.py

git add CHANGELOG.md setup.py
git commit -m "chore: bump version to 1.1.0"
git tag v1.1.0
git push origin main --tags

# Crear release en GitHub
```

## Paso 10: Responder a Issues y PRs

### Issues
- Responde en 24-48 horas
- Usa labels (bug, enhancement, question)
- Cierra cuando se resuelva

### Pull Requests
- Review código
- Ejecuta tests
- Da feedback constructivo
- Mergea o rechaza con explicación

## Tips para Éxito

### ✅ Hacer

- Mantén README actualizado
- Responde a issues rápido
- Documenta bien
- Acepta contribuciones
- Sé amable y profesional
- Actualiza regularmente

### ❌ Evitar

- Abandonar el proyecto
- Ignorar issues
- Rechazar PRs sin explicación
- Código sin documentar
- Breaking changes sin aviso

## Recursos Útiles

- [GitHub Guides](https://guides.github.com/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [Conventional Commits](https://www.conventionalcommits.org/)

---

## Checklist Final

Antes de publicar, verifica:

- [ ] README.md completo y claro
- [ ] LICENSE presente
- [ ] .gitignore configurado
- [ ] CONTRIBUTING.md disponible
- [ ] docs/ETHICS.md presente y claro
- [ ] Tests funcionando
- [ ] Dependencies listadas
- [ ] Instalación documentada
- [ ] Ejemplos incluidos
- [ ] CI/CD configurado
- [ ] Repository description añadida
- [ ] Topics añadidos
- [ ] Issues habilitados

¡Listo para publicar! 🚀

```bash
git push origin main
```

¡Buena suerte con tu proyecto! 🎉
