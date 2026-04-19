# Tests - AI Text Humanizer

## 🧪 Suite de Tests

Este directorio contiene todos los tests unitarios y de integración del proyecto.

## 📁 Estructura

```
tests/
├── __init__.py
├── test_config_loader.py      # Tests del cargador de configuración
├── test_text_processor.py     # Tests del procesador de texto
└── README.md                  # Este archivo
```

## 🚀 Ejecutar Tests

### Tests Básicos

```bash
# Todos los tests
pytest tests/ -v

# Test específico
pytest tests/test_text_processor.py -v

# Con cobertura
pytest tests/ --cov=src --cov-report=html
```

### Tests con Opciones

```bash
# Modo verbose con output detallado
pytest tests/ -vv

# Solo tests que fallaron la última vez
pytest tests/ --lf

# Detener en el primer fallo
pytest tests/ -x

# Ejecutar tests en paralelo
pytest tests/ -n auto
```

## 📊 Cobertura de Código

Objetivo: **>80%** cobertura

```bash
# Generar reporte de cobertura
pytest --cov=src --cov-report=term --cov-report=html tests/

# Ver reporte en navegador
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

## ✍️ Escribir Nuevos Tests

### Template Básico

```python
"""
Tests for [module_name]
"""

import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.module import YourClass


@pytest.fixture
def instance():
    """Create instance for testing"""
    return YourClass()


class TestYourClass:
    """Tests for YourClass"""
    
    def test_method_normal_case(self, instance):
        """Test normal usage"""
        result = instance.method("input")
        assert result == "expected"
    
    def test_method_edge_case(self, instance):
        """Test edge case"""
        result = instance.method("")
        assert result == ""
    
    def test_method_error_case(self, instance):
        """Test error handling"""
        with pytest.raises(ValueError):
            instance.method(None)
```

### Mejores Prácticas

1. **Un test, una aserción** (cuando sea posible)
2. **Nombres descriptivos** - `test_validate_rejects_empty_text`
3. **Arrange-Act-Assert** - Estructura clara
4. **Use fixtures** - Evite duplicación
5. **Test edge cases** - No solo el happy path
6. **Mock dependencies** - Aísle el código bajo test

### Fixtures Útiles

```python
@pytest.fixture
def sample_text():
    """Sample text for testing"""
    return "This is a sample text for testing."

@pytest.fixture
def config():
    """Mock configuration"""
    return {
        'text': {
            'min_length': 50,
            'max_length': 50000
        }
    }

@pytest.fixture
def temp_file(tmp_path):
    """Create temporary file"""
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")
    return file_path
```

## 🔍 Tests Existentes

### test_text_processor.py

Tests para el procesador de texto:
- ✅ Validación de texto
- ✅ Limpieza de texto
- ✅ Conteo de palabras
- ✅ Estadísticas de texto
- ✅ Chunking de texto

### test_config_loader.py

Tests para el cargador de configuración:
- ✅ Carga de configuración por defecto
- ✅ Verificación de claves requeridas
- ✅ Obtención de valores
- ✅ Valores anidados
- ✅ Valores por defecto

## 📝 Tests Pendientes

### Alta Prioridad

- [ ] Tests para detectores individuales
- [ ] Tests para detector manager
- [ ] Tests para Ollama rewriter
- [ ] Tests de integración end-to-end

### Media Prioridad

- [ ] Tests de rendimiento
- [ ] Tests de manejo de errores
- [ ] Tests de CLI
- [ ] Tests de logging

### Baja Prioridad

- [ ] Tests de stress
- [ ] Tests de seguridad
- [ ] Tests de localización

## 🐛 Debugging Tests

### Test Falla?

```bash
# Ver output completo
pytest tests/test_file.py::test_name -vv -s

# Usar debugger
pytest tests/test_file.py::test_name --pdb

# Ver warnings
pytest tests/ -v -W all
```

### Usar Logging en Tests

```python
import logging

def test_something(caplog):
    with caplog.at_level(logging.INFO):
        # your test code
        pass
    
    assert "expected log message" in caplog.text
```

## 🔧 Configuración de Tests

La configuración de pytest está en `pyproject.toml`:

```toml
[tool.pytest.ini_options]
minversion = "7.0"
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = "-v --strict-markers --cov=src"
```

## 📚 Recursos

- [Pytest Documentation](https://docs.pytest.org/)
- [Testing Best Practices](https://docs.pytest.org/en/stable/goodpractices.html)
- [Coverage.py](https://coverage.readthedocs.io/)

## 🤝 Contribuir

Para añadir nuevos tests:

1. Crea archivo `test_<module>.py`
2. Escribe tests siguiendo el template
3. Ejecuta tests localmente
4. Verifica cobertura
5. Haz commit y push

```bash
# Antes de commit
pytest tests/ -v
black tests/
flake8 tests/
```

## ⚙️ CI/CD

Los tests se ejecutan automáticamente en GitHub Actions:
- En cada push a main
- En cada pull request
- Con Python 3.8, 3.9, 3.10, 3.11

Ver: `.github/workflows/ci.yml`

---

¿Preguntas sobre tests? Abre un issue en GitHub.
