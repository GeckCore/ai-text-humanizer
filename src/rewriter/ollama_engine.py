"""
Ollama Rewriter Engine - Humanizes AI-generated text
"""

import ollama
from typing import Optional
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


class OllamaRewriter:
    """Rewrite text using local Ollama model"""
    
    def __init__(self, config: dict):
        """
        Initialize Ollama rewriter
        
        Args:
            config: Application configuration
        """
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
            # List available models
            models = ollama.list()
            model_names = [m['name'] for m in models.get('models', [])]
            
            if self.model not in model_names:
                logger.warning(f"Model {self.model} not found. Available: {model_names}")
                raise Exception(f"Model {self.model} not available. Run: ollama pull {self.model}")
            
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
            
            response = ollama.generate(
                model=self.model,
                prompt=prompt,
                options={
                    'temperature': self.temperature,
                    'num_predict': self.max_tokens
                }
            )
            
            humanized = response['response'].strip()
            
            # Clean up potential markdown artifacts
            humanized = self._clean_response(humanized)
            
            logger.info(f"Successfully humanized text ({len(humanized)} chars)")
            
            return humanized
            
        except Exception as e:
            logger.error(f"Error humanizing text: {e}")
            return None
    
    def _build_humanization_prompt(self, text: str, language: str, iteration: int) -> str:
        """Build prompt for humanization"""
        
        language_names = {
            'es': 'español',
            'en': 'English',
            'fr': 'français',
            'de': 'Deutsch',
            'pt': 'português',
            'it': 'italiano'
        }
        
        lang_name = language_names.get(language, language)
        
        # Base strategies
        strategies = [
            "Varía la estructura de las oraciones de manera natural",
            "Usa un tono más conversacional y personal",
            "Incorpora transiciones naturales entre ideas",
            "Añade matices sutiles y expresiones coloquiales apropiadas",
            "Ajusta el ritmo y flujo del texto para sonar más humano",
            "Elimina patrones repetitivos típicos de IA"
        ]
        
        # Adjust strategy based on iteration
        if iteration > 1:
            strategies.append("Enfócate en hacer el texto aún más natural y menos detectabl como IA")
            strategies.append("Introduce variaciones significativas respecto a la versión anterior")
        
        prompt = f"""Eres un experto escritor en {lang_name}. Tu tarea es reescribir el siguiente texto para que suene completamente natural y humano, evitando cualquier patrón que pueda ser detectado como generado por IA.

ESTRATEGIAS A APLICAR:
{chr(10).join(f'- {s}' for s in strategies)}

IMPORTANTE:
- Mantén el MISMO significado y contenido del texto original
- NO agregues información nueva
- NO cambies el mensaje principal
- Escribe en {lang_name} natural y fluido
- Haz que suene como si lo hubiera escrito una persona real
- Evita estructuras demasiado formales o perfectas
- Usa vocabulario variado y natural

TEXTO A REESCRIBIR:

{text}

TEXTO HUMANIZADO:"""
        
        return prompt
    
    def _clean_response(self, text: str) -> str:
        """Clean up response from potential markdown artifacts"""
        # Remove markdown code blocks if present
        if text.startswith('```'):
            lines = text.split('\n')
            text = '\n'.join(lines[1:-1]) if len(lines) > 2 else text
        
        # Remove leading/trailing whitespace
        text = text.strip()
        
        return text
