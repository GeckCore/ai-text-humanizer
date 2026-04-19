# Guía de Contribución

¡Gracias por tu interés en contribuir a AI Text Humanizer! Este documento proporciona pautas para contribuir al proyecto.

## 🤝 Código de Conducta

### Nuestro Compromiso

Este proyecto se compromete a proporcionar una experiencia libre de acoso para todos, independientemente de:
- Edad, tamaño corporal, discapacidad
- Etnia, identidad y expresión de género
- Nivel de experiencia, educación, estatus socioeconómico
- Nacionalidad, apariencia personal, raza, religión
- Identidad u orientación sexual

### Comportamiento Esperado

- Usar lenguaje acogedor e inclusivo
- Respetar diferentes puntos de vista y experiencias
- Aceptar críticas constructivas con gracia
- Enfocarse en lo que es mejor para la comunidad
- Mostrar empatía hacia otros miembros

### Comportamiento Inaceptable

- Lenguaje o imágenes sexualizadas
- Trolling, comentarios insultantes o despectivos
- Acoso público o privado
- Publicar información privada de otros sin permiso
- Conducta que razonablemente se consideraría inapropiada

## 🐛 Reportar Bugs

### Antes de Reportar

1. Verifica que estés usando la última versión
2. Busca en issues existentes
3. Recopila información sobre el bug

### Cómo Reportar

Crea un issue incluyendo:

```markdown
**Descripción del Bug**
Descripción clara y concisa del problema.

**Pasos para Reproducir**
1. Ir a '...'
2. Ejecutar '...'
3. Ver error

**Comportamiento Esperado**
Qué esperabas que pasara.

**Comportamiento Actual**
Qué pasó en realidad.

**Screenshots**
Si aplica, añade screenshots.

**Entorno**
- OS: [e.g. Ubuntu 22.04]
- Python: [e.g. 3.10.5]
- Versión: [e.g. 1.0.0]

**Logs**
```
Pega logs relevantes aquí
```

**Contexto Adicional**
Cualquier otra información relevante.
```

## 💡 Sugerir Características

### Antes de Sugerir

1. Verifica que la característica no existe
2. Busca en issues por sugerencias similares
3. Considera si es útil para la mayoría de usuarios

### Cómo Sugerir

Crea un issue incluyendo:

```markdown
**Problema a Resolver**
Describe el problema que esta característica resolvería.

**Solución Propuesta**
Describe cómo visualizas la solución.

**Alternativas Consideradas**
Describe alternativas que consideraste.

**Contexto Adicional**
Screenshots, ejemplos, etc.
```

## 🔧 Contribuir Código

### Proceso de Desarrollo

1. **Fork el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/ai-text-humanizer.git
   cd ai-text-humanizer
   ```

2. **Crear una rama**
   ```bash
   git checkout -b feature/nueva-caracteristica
   # o
   git checkout -b fix/bug-especifico
   ```

3. **Configurar entorno**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Hacer cambios**
   - Escribe código claro y bien documentado
   - Sigue el estilo de código existente
   - Añade tests para nueva funcionalidad
   - Actualiza documentación si es necesario

5. **Ejecutar tests**
   ```bash
   # Tests unitarios
   pytest tests/ -v
   
   # Cobertura
   pytest --cov=src tests/
   
   # Linting
   flake8 src
   black src --check
   ```

6. **Commit cambios**
   ```bash
   git add .
   git commit -m "feat: añadir nueva característica"
   ```
   
   Usa conventional commits:
   - `feat:` nueva característica
   - `fix:` corrección de bug
   - `docs:` cambios en documentación
   - `style:` formato, sin cambios de código
   - `refactor:` refactorización de código
   - `test:` añadir tests
   - `chore:` mantenimiento

7. **Push y Pull Request**
   ```bash
   git push origin feature/nueva-caracteristica
   ```
   
   Luego crea un Pull Request en GitHub.

### Estándares de Código

#### Python Style Guide

Seguimos [PEP 8](https://pep8.org/):

```python
# Good
def calculate_average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.
    
    Args:
        numbers: List of numbers
        
    Returns:
        Average value
    """
    return sum(numbers) / len(numbers)


# Bad
def calc_avg(nums):
    return sum(nums)/len(nums)
```

#### Docstrings

Usa Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """
    Short description.
    
    Longer description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When something is wrong
    """
    pass
```

#### Type Hints

Usa type hints siempre que sea posible:

```python
from typing import List, Dict, Optional

def process_text(text: str, options: Optional[Dict] = None) -> List[str]:
    """Process text with options."""
    pass
```

### Tests

#### Escribir Tests

Cada nueva característica debe incluir tests:

```python
import pytest
from src.module import function


class TestFunction:
    """Tests for function."""
    
    def test_normal_case(self):
        """Test normal usage."""
        result = function("input")
        assert result == "expected"
    
    def test_edge_case(self):
        """Test edge case."""
        result = function("")
        assert result == ""
    
    def test_error_case(self):
        """Test error handling."""
        with pytest.raises(ValueError):
            function(None)
```

#### Cobertura

Objetivo: >80% cobertura de código

```bash
pytest --cov=src --cov-report=html tests/
# Abre htmlcov/index.html
```

### Documentación

#### Actualizar Docs

Si tu cambio afecta el uso:

1. Actualiza README.md
2. Actualiza docs/USAGE.md
3. Añade ejemplos si es necesario
4. Actualiza CHANGELOG.md

#### Formato

- Usa Markdown
- Incluye ejemplos de código
- Mantén lenguaje claro y conciso
- Añade screenshots cuando ayude

## 📝 Pull Request Process

### Checklist PR

Antes de enviar, verifica:

- [ ] El código sigue el style guide
- [ ] Todos los tests pasan
- [ ] Se añadieron tests para nueva funcionalidad
- [ ] La documentación está actualizada
- [ ] Los commits siguen conventional commits
- [ ] No hay conflictos con main
- [ ] El código está bien comentado

### Template PR

```markdown
## Descripción
Breve descripción de los cambios.

## Tipo de Cambio
- [ ] Bug fix
- [ ] Nueva característica
- [ ] Breaking change
- [ ] Documentación

## ¿Cómo se ha Probado?
Describe las pruebas realizadas.

## Checklist
- [ ] Mi código sigue el style guide
- [ ] He realizado self-review
- [ ] He comentado código complejo
- [ ] He actualizado documentación
- [ ] Mis cambios no generan warnings
- [ ] He añadido tests
- [ ] Tests nuevos y existentes pasan

## Screenshots
Si aplica, añade screenshots.
```

### Proceso de Review

1. **Automated Checks**: CI/CD ejecuta tests automáticamente
2. **Code Review**: Un maintainer revisará tu código
3. **Feedback**: Puede haber comentarios o solicitudes de cambio
4. **Iteración**: Haz los cambios sugeridos
5. **Merge**: Una vez aprobado, se hará merge

## 🚀 Áreas de Contribución

### Prioridades Actuales

1. **Detectores**
   - Añadir más detectores de IA
   - Mejorar precisión de detectores existentes
   - Manejar mejor errores de red

2. **Reescritura**
   - Optimizar prompts para mejor humanización
   - Soporte para más idiomas
   - Estrategias de reescritura mejoradas

3. **UX/UI**
   - Mejorar interfaz CLI
   - Añadir barra de progreso más detallada
   - Mejores mensajes de error

4. **Documentación**
   - Más ejemplos de uso
   - Tutoriales en video
   - Traducción a otros idiomas

5. **Tests**
   - Aumentar cobertura
   - Tests de integración
   - Tests de performance

### Buenas Primeras Contribuciones

Busca issues etiquetados con:
- `good-first-issue`
- `help-wanted`
- `documentation`

## 📧 Contacto

- **Issues**: [GitHub Issues](https://github.com/tu-usuario/ai-text-humanizer/issues)
- **Discussions**: [GitHub Discussions](https://github.com/tu-usuario/ai-text-humanizer/discussions)
- **Email**: [tu-email@ejemplo.com]

## 📜 Licencia

Al contribuir, aceptas que tus contribuciones se licencien bajo la misma licencia MIT del proyecto.

---

¡Gracias por contribuir! 🎉
