# Ejemplos de Uso

Este directorio contiene archivos de ejemplo para probar AI Text Humanizer.

## Archivos Disponibles

### `sample_text_es.txt`
Texto de ejemplo en español sobre inteligencia artificial. Perfecto para:
- Primera prueba del sistema
- Verificar que todo funciona correctamente
- Entender el flujo del programa

**Uso:**
```bash
python -m src.main --input examples/sample_text_es.txt --language es
```

## Crear Tus Propios Ejemplos

### Formato Recomendado

- **Extensión:** `.txt`
- **Encoding:** UTF-8
- **Longitud:** 100-5000 palabras
- **Formato:** Texto plano sin formato especial

### Ejemplo de Estructura

```
Tu texto aquí, puede ser de varios párrafos.

Segundo párrafo con más contenido. Asegúrate de que
el texto sea coherente y bien escrito.

Tercer párrafo con conclusiones.
```

## Probar con Tus Textos

### Paso 1: Crear Archivo

```bash
# Crear tu archivo de texto
echo "Tu texto aquí..." > examples/mi_texto.txt
```

### Paso 2: Ejecutar

```bash
# Procesar tu texto
python -m src.main --input examples/mi_texto.txt
```

### Paso 3: Ver Resultados

Los resultados se guardarán en el directorio `output/`:
- `humanized_TIMESTAMP.txt` - Texto humanizado
- `report_TIMESTAMP.txt` - Reporte completo

## Idiomas Soportados

Puedes crear ejemplos en cualquier idioma soportado:

- `sample_text_es.txt` - Español
- `sample_text_en.txt` - English
- `sample_text_fr.txt` - Français
- `sample_text_de.txt` - Deutsch
- `sample_text_pt.txt` - Português
- `sample_text_it.txt` - Italiano

## Tips para Buenos Ejemplos

### ✅ Buenas Prácticas

- Texto bien escrito y coherente
- Sin errores ortográficos evidentes
- Longitud apropiada (no muy corto ni muy largo)
- Tema claro y definido
- Estructura lógica con párrafos

### ❌ Evitar

- Texto con muchos errores
- Mezcla de idiomas
- Formato especial (tablas, código)
- Texto muy técnico o con jerga
- Contenido sensible o privado

## Casos de Uso Ejemplo

### Ejemplo 1: Ensayo Académico

```text
La evolución de la tecnología ha transformado...
[Contenido de ensayo aquí]
```

### Ejemplo 2: Artículo de Blog

```text
Hoy quiero hablar sobre las mejores prácticas...
[Contenido de blog aquí]
```

### Ejemplo 3: Reporte de Investigación

```text
Este estudio examina el impacto de...
[Contenido de reporte aquí]
```

## Compartir Ejemplos

Si creas buenos ejemplos que puedan ayudar a otros:

1. Fork el repositorio
2. Añade tu ejemplo en `examples/`
3. Actualiza este README
4. Crea un Pull Request

¡Las contribuciones son bienvenidas!

---

Para más información:
- [README principal](../README.md)
- [Guía de uso](../docs/USAGE.md)
- [Inicio rápido](../QUICKSTART.md)
