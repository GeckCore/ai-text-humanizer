# 🚀 Inicio Rápido - AI Text Humanizer

## ⚡ Instalación en 5 Minutos

### 1. Instalar Ollama

**Linux/macOS:**
```bash
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Descarga desde https://ollama.ai/download

### 2. Clonar y Configurar

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/ai-text-humanizer.git
cd ai-text-humanizer

# Ejecutar instalador automático
chmod +x install.sh
./install.sh
```

El script automáticamente:
- ✅ Crea entorno virtual
- ✅ Instala dependencias
- ✅ Descarga modelo de IA
- ✅ Configura navegadores

### 3. ¡Listo para Usar!

```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Ejecutar
python -m src.main
```

---

## 📝 Primer Uso

### Ejemplo Completo

```bash
# 1. Ejecutar programa
python -m src.main

# 2. Seleccionar idioma
> Español

# 3. Pegar texto
Pega tu texto aquí...
[Enter dos veces]

# 4. Ver análisis
📊 Resultados:
  GPTZero: 85% IA detectada
  Writer: 78% IA detectada
  ...

# 5. Confirmar humanización
¿Humanizar? Y

# 6. Esperar proceso
🔄 Iteración 1/5...
📈 Score: 45% (-40 puntos)
...

# 7. Resultados guardados en:
output/humanized_TIMESTAMP.txt
output/report_TIMESTAMP.txt
```

---

## ⚙️ Comandos Útiles

### Uso Básico

```bash
# Modo interactivo
python -m src.main

# Desde archivo
python -m src.main --input mi_texto.txt

# Especificar idioma
python -m src.main --language en

# Configurar iteraciones
python -m src.main --max-iterations 10
```

### Configuración

```bash
# Editar configuración
nano config/config.yaml

# Cambiar modelo (más ligero)
ollama:
  model: "qwen2.5:7b"

# Cambiar detectores habilitados
detectors:
  enabled:
    - gptzero
    - writer
```

---

## 🎯 Casos de Uso Comunes

### Caso 1: Análisis Rápido (Solo Detectar)

```bash
python -m src.main --input texto.txt
# Cuando pregunte "¿Humanizar?", responde: N
```

### Caso 2: Humanización Estándar

```bash
python -m src.main \
  --language es \
  --input ensayo.txt \
  --max-iterations 5 \
  --threshold 15
```

### Caso 3: Máxima Calidad

Edita `config/config.yaml`:
```yaml
ollama:
  model: "qwen2.5:32b"
  temperature: 0.9

rewriting:
  max_iterations: 10
  target_threshold: 5
```

Luego:
```bash
python -m src.main --input documento.txt
```

---

## 🔍 Interpretación de Resultados

| Score | Significado | Acción |
|-------|-------------|--------|
| 0-15% | ✅ Excelente - Muy humano | Listo para usar |
| 16-40% | ⚡ Bueno - Moderado | Considerar 1-2 iteraciones más |
| 41-70% | ⚠️ Regular - Alto | Necesita más trabajo |
| 71-100% | ❌ Malo - Muy detectado | Reescritura manual recomendada |

---

## ❓ Solución Rápida de Problemas

### Problema: "Ollama not available"

```bash
# Verificar instalación
ollama --version

# Iniciar servicio
ollama serve

# Verificar modelo
ollama list
ollama pull qwen2.5:14b
```

### Problema: "Out of memory"

```bash
# Usar modelo más pequeño
ollama pull qwen2.5:7b

# Editar config.yaml
ollama:
  model: "qwen2.5:7b"
```

### Problema: Detectores fallan

```bash
# Verificar internet
ping google.com

# Editar config.yaml - aumentar timeout
detectors:
  gptzero:
    timeout: 60
```

---

## 📚 Próximos Pasos

### Leer Documentación Completa

1. **[README.md](README.md)** - Visión general y características
2. **[docs/USAGE.md](docs/USAGE.md)** - Guía detallada de uso
3. **[docs/ETHICS.md](docs/ETHICS.md)** - ⚠️ **MUY IMPORTANTE** - Lee antes de usar

### Personalizar Configuración

```bash
# Copia config de ejemplo
cp config/config.yaml config/local_config.yaml

# Edita tu configuración local
nano config/local_config.yaml

# Usa tu configuración
python -m src.main --config config/local_config.yaml
```

### Probar Ejemplos

```bash
# Ejecutar con texto de ejemplo
python -m src.main --input examples/sample_text_es.txt
```

---

## 🎓 Mejores Prácticas

### ✅ Hacer

- Lee la [documentación ética](docs/ETHICS.md)
- Verifica los resultados manualmente
- Ajusta configuración según tus necesidades
- Usa responsablemente

### ❌ Evitar

- No uses para fraude académico
- No violes políticas institucionales
- No confíes ciegamente en resultados
- No uses sin verificar contenido

---

## 💡 Tips Pro

### Mejorar Resultados

1. **Texto Original de Calidad**
   - Corrige ortografía primero
   - Asegura coherencia
   - Elimina redundancias

2. **Configuración Óptima**
   - Más iteraciones = mejor resultado
   - Temperatura alta = más variación
   - Modelo grande = mejor calidad

3. **Revisión Post-Proceso**
   - Siempre lee el resultado
   - Verifica que el significado se mantiene
   - Corrige errores si los hay

### Procesamiento por Lotes

```bash
# Crear script
#!/bin/bash
for file in textos/*.txt; do
    python -m src.main \
      --language es \
      --input "$file" \
      --max-iterations 5
done
```

---

## 🆘 Obtener Ayuda

### Recursos

- **Documentación**: [docs/](docs/)
- **Issues**: [GitHub Issues](https://github.com/tu-usuario/ai-text-humanizer/issues)
- **Discussions**: [GitHub Discussions](https://github.com/tu-usuario/ai-text-humanizer/discussions)

### Antes de Pedir Ayuda

1. ✓ Lee la documentación
2. ✓ Busca en issues existentes
3. ✓ Revisa logs en `logs/`
4. ✓ Incluye información detallada

---

## ⚠️ Recordatorio Importante

**Esta herramienta es para investigación y educación.**

Lee [docs/ETHICS.md](docs/ETHICS.md) para entender:
- Usos legítimos
- Usos no éticos
- Responsabilidades
- Consecuencias

**Úsala responsablemente.** 🙏

---

¿Listo? ¡Empieza ahora! 🚀

```bash
python -m src.main
```
