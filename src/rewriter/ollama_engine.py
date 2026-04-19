"""
Ollama Rewriter Engine - Humanizes AI-generated text
VERSIÓN MEJORADA con prompts optimizados
"""

import ollama
from typing import Optional
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


class OllamaRewriter:
    """Rewrite text using local Ollama model with improved prompts"""
    
    def __init__(self, config: dict):
        """Initialize Ollama rewriter"""
        self.config = config
        self.ollama_config = config['ollama']
        self.model = self.ollama_config['model']
        self.temperature = self.ollama_config['temperature']
        self.max_tokens = self.ollama_config['max_tokens']
        
        # Verify Ollama is available
        self._verify_ollama()
    
    def _verify_ollama(self):
        """Verify Ollama is installed and model is available"""
        try:
            models_response = ollama.list()
            
            if isinstance(models_response, dict):
                models_list = models_response.get('models', [])
            else:
                models_list = models_response
            
            model_names = []
            for model in models_list:
                if isinstance(model, dict):
                    name = model.get('name') or model.get('model') or model.get('id')
                    if name:
                        model_names.append(name)
                elif isinstance(model, str):
                    model_names.append(model)
            
            logger.info(f"Available Ollama models: {model_names}")
            
            model_found = False
            for name in model_names:
                if self.model in name or name in self.model:
                    model_found = True
                    break
            
            if not model_found:
                logger.warning(f"Model {self.model} not found. Available: {model_names}")
                logger.warning(f"Attempting to use anyway. Run: ollama pull {self.model}")
            else:
                logger.info(f"Ollama model {self.model} is ready")
            
        except Exception as e:
            logger.error(f"Error verifying Ollama: {e}")
            raise Exception(f"Ollama not available: {e}")
    
    def humanize(self, text: str, language: str, iteration: int = 1) -> Optional[str]:
        """
        Humanize text to bypass AI detectors
        
        Args:
            text: Text to humanize
            language: Target language
            iteration: Current iteration number
            
        Returns:
            Humanized text or None on error
        """
        try:
            prompt = self._build_humanization_prompt(text, language, iteration)
            
            logger.info(f"Humanizing text (iteration {iteration}) with {self.model}")
            
            # Use higher temperature for more variation
            temp = min(0.9, self.temperature + (iteration * 0.05))
            
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                options={
                    'temperature': temp,
                    'num_predict': self.max_tokens,
                    'top_p': 0.9,
                    'top_k': 40
                }
            )
            
            humanized = response['response'].strip()
            humanized = self._clean_response(humanized)
            
            logger.info(f"Successfully humanized text ({len(humanized)} chars)")
            
            return humanized
            
        except Exception as e:
            logger.error(f"Error humanizing text: {e}")
            return None
    
    def _build_humanization_prompt(self, text: str, language: str, iteration: int) -> str:
        """Build improved prompt for humanization"""
        
        language_names = {
            'es': 'español',
            'en': 'English',
            'fr': 'français',
            'de': 'Deutsch',
            'pt': 'português',
            'it': 'italiano'
        }
        
        lang_name = language_names.get(language, language)
        
        # PROMPT MEJORADO con técnicas anti-detección
        if iteration == 1:
            prompt = f"""Eres un escritor experto. Tu tarea es REESCRIBIR completamente el siguiente texto para que NO sea detectable como escrito por IA.

TÉCNICAS CRÍTICAS - DEBES APLICAR TODAS:

1. VARIACIÓN DE ESTRUCTURA:
   - Alterna entre oraciones cortas y largas
   - Usa frases subordinadas de forma irregular
   - Rompe patrones simétricos
   - Varía la posición de sujeto y verbo

2. IMPERFECCIONES HUMANAS:
   - Añade algunas frases levemente redundantes (como hacen los humanos)
   - Usa ocasionalmente construcciones menos formales
   - Incluye transiciones naturales pero no perfectas
   - Varía el ritmo del texto (no todo uniforme)

3. ESTILO PERSONAL:
   - Usa expresiones coloquiales apropiadas
   - Añade matices subjetivos sutiles
   - Varía el vocabulario (evita repetir palabras técnicas)
   - Incluye conectores naturales variados

4. ANTI-PATRONES IA:
   - NO uses listas simétricas
   - NO uses estructura de 3 puntos (bullet pattern)
   - NO uses palabras como "además", "asimismo" en exceso
   - NO hagas párrafos del mismo largo
   - NO uses patrones repetitivos

IMPORTANTE:
- Mantén el SIGNIFICADO EXACTO del texto original
- NO añadas información nueva
- NO elimines ideas principales
- Escribe en {lang_name}
- El resultado debe sonar como si lo escribiera UNA PERSONA REAL

TEXTO ORIGINAL:
{text}

TEXTO REESCRITO (escribe SOLO el texto, sin explicaciones):"""

        else:
            # Iteraciones posteriores: más agresivo
            prompt = f"""El texto anterior fue detectado como IA. Necesitas reescribirlo de forma MÁS HUMANA.

CAMBIOS ADICIONALES NECESARIOS (iteración {iteration}):

1. MAYOR VARIACIÓN:
   - Cambia completamente la estructura de oraciones
   - Usa sinónimos diferentes a los intentos anteriores
   - Altera el orden de presentación de ideas
   - Añade más irregularidad en la estructura

2. MÁS NATURALIDAD:
   - Incluye expresiones más coloquiales
   - Usa contracciones cuando sea natural
   - Añade pequeñas digresiones naturales
   - Varía más el ritmo y flujo

3. ROMPER PATRONES IA:
   - Evita completamente estructuras paralelas
   - No uses enumeraciones explícitas
   - Varía drásticamente la longitud de oraciones
   - Usa construcciones más complejas y naturales

TEXTO A MEJORAR:
{text}

NUEVA VERSIÓN MÁS HUMANA (SOLO el texto):"""
        
        return prompt
    
    def _clean_response(self, text: str) -> str:
        """Clean up response from potential artifacts"""
        # Remove markdown code blocks
        if text.startswith('```'):
            lines = text.split('\n')
            text = '\n'.join(lines[1:-1]) if len(lines) > 2 else text
        
        # Remove common AI prefixes
        prefixes_to_remove = [
            "TEXTO REESCRITO:",
            "NUEVA VERSIÓN:",
            "VERSIÓN HUMANIZADA:",
            "Aquí está el texto:",
            "Here is the text:",
        ]
        
        for prefix in prefixes_to_remove:
            if text.startswith(prefix):
                text = text[len(prefix):].strip()
        
        text = text.strip()
        
        return text
