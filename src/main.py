#!/usr/bin/env python3
"""
AI Text Humanizer - Main Entry Point
Herramienta para analizar y humanizar texto generado por IA
"""

import sys
import os
from pathlib import Path
from typing import Optional
import click
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich import print as rprint

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils.logger import setup_logger
from src.utils.text_processor import TextProcessor
from src.detectors.manager import DetectorManager
from src.rewriter.ollama_engine import OllamaRewriter
from src.utils.config_loader import ConfigLoader

console = Console()
logger = setup_logger(__name__)


class AITextHumanizer:
    """Main application class"""
    
    def __init__(self, config_path: Optional[str] = None):
        """Initialize the application"""
        self.config = ConfigLoader(config_path).config
        self.text_processor = TextProcessor(self.config)
        self.detector_manager = DetectorManager(self.config)
        self.rewriter = OllamaRewriter(self.config)
        
    def show_banner(self):
        """Display application banner"""
        banner = """
[bold cyan]╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║           🤖  AI TEXT HUMANIZER  v1.0.0                  ║
║                                                           ║
║     Analiza y humaniza texto generado por IA             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝[/bold cyan]

[yellow]⚠️  USO RESPONSABLE: Esta herramienta es para investigación[/yellow]
[yellow]   y educación. Lee el README antes de usar.[/yellow]
"""
        console.print(banner)
        
    def select_language(self, language: Optional[str] = None) -> str:
        """Select or validate language"""
        if language:
            # Validate provided language
            valid_codes = [lang['code'] for lang in self.config['languages']]
            if language in valid_codes:
                return language
            else:
                logger.warning(f"Invalid language code: {language}")
        
        # Interactive selection
        languages = self.config['languages']
        choices = [f"{lang['code']} - {lang['name']}" for lang in languages]
        
        answer = questionary.select(
            "Selecciona el idioma del texto:",
            choices=choices
        ).ask()
        
        if not answer:
            sys.exit(0)
            
        return answer.split(" - ")[0]
    
    def get_input_text(self, input_file: Optional[str] = None) -> str:
        """Get text input from user or file"""
        if input_file:
            try:
                with open(input_file, 'r', encoding='utf-8') as f:
                    text = f.read()
                console.print(f"✅ Texto cargado desde: {input_file}")
                return text
            except Exception as e:
                logger.error(f"Error loading file: {e}")
                console.print(f"[red]❌ Error al cargar archivo: {e}[/red]")
                sys.exit(1)
        
        # Interactive input
        console.print("\n[cyan]📝 Pega tu texto a continuación[/cyan]")
        console.print("[dim](Presiona Enter dos veces para terminar)[/dim]\n")
        
        lines = []
        empty_lines = 0
        
        while True:
            try:
                line = input()
                if not line:
                    empty_lines += 1
                    if empty_lines >= 2:
                        break
                else:
                    empty_lines = 0
                    lines.append(line)
            except EOFError:
                break
                
        text = '\n'.join(lines)
        
        if not text.strip():
            console.print("[red]❌ No se ingresó ningún texto[/red]")
            sys.exit(1)
            
        return text
    
    def analyze_text(self, text: str) -> dict:
        """Analyze text with AI detectors"""
        console.print("\n[cyan]📊 Analizando texto con detectores de IA...[/cyan]\n")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console
        ) as progress:
            task = progress.add_task("Ejecutando detectores...", total=None)
            results = self.detector_manager.detect(text)
            progress.update(task, completed=True)
        
        # Display results
        self._display_detection_results(results)
        return results
    
    def _display_detection_results(self, results: dict):
        """Display detection results in a table"""
        table = Table(title="Resultados de Detección")
        table.add_column("Detector", style="cyan")
        table.add_column("% IA Detectada", style="yellow")
        table.add_column("Estado", style="green")
        
        total = 0
        count = 0
        
        for detector, result in results.items():
            if result['success']:
                percentage = result['ai_percentage']
                total += percentage
                count += 1
                
                status = "✅ Alto" if percentage > 50 else "✓ Bajo"
                table.add_row(
                    detector.upper(),
                    f"{percentage:.1f}%",
                    status
                )
            else:
                table.add_row(
                    detector.upper(),
                    "N/A",
                    f"❌ {result.get('error', 'Error')}"
                )
        
        console.print(table)
        
        if count > 0:
            average = total / count
            color = "red" if average > 50 else "yellow" if average > 20 else "green"
            console.print(f"\n[{color}]📈 Promedio: {average:.2f}% IA detectada[/{color}]")
            
            if average > 50:
                console.print("[red]⚠️  ALTO contenido de IA detectado[/red]")
            elif average > 20:
                console.print("[yellow]⚡ Contenido de IA moderado[/yellow]")
            else:
                console.print("[green]✨ Bajo contenido de IA[/green]")
    
    def humanize_text(self, text: str, language: str, max_iterations: int, threshold: float) -> tuple:
        """Humanize text iteratively"""
        console.print(f"\n[cyan]🔄 Iniciando proceso de humanización...[/cyan]")
        console.print(f"[dim]Idioma: {language} | Máx. iteraciones: {max_iterations} | Umbral: {threshold}%[/dim]\n")
        
        current_text = text
        iteration = 0
        best_score = 100.0
        best_text = text
        
        history = []
        
        while iteration < max_iterations:
            iteration += 1
            console.print(f"[bold cyan]📍 Iteración {iteration}/{max_iterations}[/bold cyan]")
            
            # Rewrite text
            console.print("  ⏳ Reescribiendo con IA local...")
            humanized = self.rewriter.humanize(current_text, language, iteration)
            
            if not humanized:
                console.print("[red]  ❌ Error en reescritura[/red]")
                break
            
            # Re-analyze
            console.print("  📊 Re-analizando texto humanizado...")
            results = self.detector_manager.detect(humanized)
            
            # Calculate average
            scores = [r['ai_percentage'] for r in results.values() if r['success']]
            if not scores:
                console.print("[red]  ❌ No se pudo analizar el texto[/red]")
                break
                
            avg_score = sum(scores) / len(scores)
            
            # Display mini results
            console.print(f"  📈 Score actual: {avg_score:.1f}%")
            
            # Track history
            history.append({
                'iteration': iteration,
                'score': avg_score,
                'text': humanized,
                'results': results
            })
            
            # Check if improved
            if avg_score < best_score:
                improvement = best_score - avg_score
                best_score = avg_score
                best_text = humanized
                console.print(f"  [green]✨ Mejoró {improvement:.1f}% puntos[/green]")
            else:
                console.print(f"  [yellow]⚠️  No mejoró (mejor: {best_score:.1f}%)[/yellow]")
            
            # Check if reached threshold
            if avg_score <= threshold:
                console.print(f"\n[green]🎉 ¡Objetivo alcanzado! ({avg_score:.1f}% ≤ {threshold}%)[/green]")
                break
            
            current_text = humanized
            console.print()
        
        return best_text, best_score, history
    
    def save_output(self, original: str, humanized: str, score: float, history: list, language: str):
        """Save output files"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        output_dir = Path(self.config['output']['directory'])
        output_dir.mkdir(exist_ok=True)
        
        # Save humanized text
        if self.config['output']['save_humanized_text']:
            text_file = output_dir / f"humanized_{timestamp}.txt"
            with open(text_file, 'w', encoding='utf-8') as f:
                f.write(humanized)
            console.print(f"💾 Texto humanizado guardado: [cyan]{text_file}[/cyan]")
        
        # Save report
        if self.config['output']['save_reports']:
            report_file = output_dir / f"report_{timestamp}.txt"
            with open(report_file, 'w', encoding='utf-8') as f:
                f.write("="*60 + "\n")
                f.write("AI TEXT HUMANIZER - REPORTE DE RESULTADOS\n")
                f.write("="*60 + "\n\n")
                f.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Idioma: {language}\n")
                f.write(f"Score final: {score:.2f}% IA detectada\n")
                f.write(f"Iteraciones: {len(history)}\n\n")
                
                f.write("-"*60 + "\n")
                f.write("HISTORIAL DE ITERACIONES\n")
                f.write("-"*60 + "\n\n")
                
                for entry in history:
                    f.write(f"Iteración {entry['iteration']}: {entry['score']:.2f}%\n")
                
                f.write("\n" + "-"*60 + "\n")
                f.write("TEXTO ORIGINAL\n")
                f.write("-"*60 + "\n\n")
                f.write(original)
                
                f.write("\n\n" + "-"*60 + "\n")
                f.write("TEXTO HUMANIZADO (MEJOR VERSIÓN)\n")
                f.write("-"*60 + "\n\n")
                f.write(humanized)
                
            console.print(f"📄 Reporte guardado: [cyan]{report_file}[/cyan]")


@click.command()
@click.option('--language', '-l', help='Código de idioma (es, en, fr, etc.)')
@click.option('--input', '-i', 'input_file', help='Archivo de texto de entrada')
@click.option('--max-iterations', '-m', default=5, help='Máximo de iteraciones')
@click.option('--threshold', '-t', default=15.0, help='Umbral objetivo de % IA')
@click.option('--config', '-c', help='Ruta a archivo de configuración personalizado')
def main(language, input_file, max_iterations, threshold, config):
    """
    AI Text Humanizer - Analiza y humaniza texto generado por IA
    """
    try:
        app = AITextHumanizer(config)
        app.show_banner()
        
        # Select language
        lang = app.select_language(language)
        
        # Get input text
        text = app.get_input_text(input_file)
        
        # Validate text
        if len(text) < app.config['text']['min_length']:
            console.print(f"[red]❌ Texto muy corto (mín. {app.config['text']['min_length']} caracteres)[/red]")
            sys.exit(1)
        
        console.print(f"\n[green]✅ Texto recibido: {len(text)} caracteres[/green]")
        
        # Initial analysis
        initial_results = app.analyze_text(text)
        
        # Ask if user wants to humanize
        if questionary.confirm("¿Deseas humanizar este texto?", default=True).ask():
            humanized, score, history = app.humanize_text(
                text, lang, max_iterations, threshold
            )
            
            # Final analysis
            console.print("\n[cyan]📊 Análisis final del texto humanizado:[/cyan]\n")
            final_results = app.analyze_text(humanized)
            
            # Save outputs
            app.save_output(text, humanized, score, history, lang)
            
            console.print("\n[green]✅ Proceso completado exitosamente[/green]")
        else:
            console.print("\n[yellow]👋 Proceso cancelado[/yellow]")
            
    except KeyboardInterrupt:
        console.print("\n\n[yellow]⚠️  Proceso interrumpido por el usuario[/yellow]")
        sys.exit(0)
    except Exception as e:
        logger.exception("Error crítico en la aplicación")
        console.print(f"\n[red]❌ Error: {e}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
