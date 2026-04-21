import tkinter as tk
from tkinter import font
import re

# Fragmento de código profesional para simular
CODE_DATA = """import numpy as np
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

class SignalProcessor:
    \"\"\"Analizador de espectro para señales complejas v2.1.0\"\"\"
    def __init__(self, sampling_rate: int, duration: float):
        self.fs = sampling_rate
        self.t = np.linspace(0, duration, int(self.fs * duration), endpoint=False)
        self.buffer = None

    @staticmethod
    def _apply_hanning_window(data):
        return data * np.hanning(len(data))

    def generate_synthetic_stream(self, freqs: list):
        \"\"\"Genera una señal multicanal con ruido gaussiano\"\"\"
        signal = sum(np.sin(2 * np.pi * f * self.t) for f in freqs)
        noise = np.random.normal(0, 0.5, len(self.t))
        self.buffer = signal + noise
        return self.buffer

    def compute_fft_core(self):
        # Optimización de memoria para transformación rápida
        if self.buffer is None:
            raise ValueError("Buffer de señal vacío")
            
        N = len(self.buffer)
        windowed_signal = self._apply_hanning_window(self.buffer)
        yf = fft(windowed_signal)
        xf = fftfreq(N, 1 / self.fs)[:N//2]
        
        return xf, 2.0/N * np.abs(yf[0:N//2])

def main():
    # Parámetros de inicialización del núcleo
    FS = 44100
    DURATION = 2.0
    
    engine = SignalProcessor(sampling_rate=FS, duration=DURATION)
    data = engine.generate_synthetic_stream(freqs=[50, 120, 440])
    
    print(f"[SYSTEM]: Procesando {len(data)} muestras...")
    xf, yf = engine.compute_fft_core()
    
    # Exportar resultados a matriz de transformación
    output_matrix = np.column_stack((xf, yf))
    return output_matrix

if __name__ == "__main__":
    matrix_result = main()
    print("Kernel execution successful. Data ready.")
"""

class ProEditorSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Studio Code - processor_core.py")
        self.root.geometry("1100x750")
        self.root.configure(bg="#1e1e1e")
        
        self.char_index = 0
        self.setup_ui()
        self.root.bind("<Key>", self.inject_code)

    def setup_ui(self):
        # Colores VS Code
        bg_dark = "#1e1e1e"
        bg_sidebar = "#333333"
        bg_explorer = "#252526"
        accent_blue = "#007acc"
        text_white = "#cccccc"

        # Barra lateral izquierda (Iconos)
        self.left_bar = tk.Frame(self.root, width=50, bg=bg_sidebar)
        self.left_bar.pack(side="left", fill="y")
        
        # Explorador de archivos
        self.explorer = tk.Frame(self.root, width=200, bg=bg_explorer)
        self.explorer.pack(side="left", fill="y")
        tk.Label(self.explorer, text="EXPLORER", fg=text_white, bg=bg_explorer, font=("Segoe UI", 9, "bold")).pack(pady=10, padx=10, anchor="w")
        tk.Label(self.explorer, text=" > PROJECT_CORE", fg=text_white, bg=bg_explorer, font=("Segoe UI", 8)).pack(padx=10, anchor="w")
        tk.Label(self.explorer, text="    python_env", fg="#6a9955", bg=bg_explorer, font=("Segoe UI", 8)).pack(padx=15, anchor="w")
        tk.Label(self.explorer, text="  🐍 processor_core.py", fg="#569cd6", bg="#37373d", font=("Segoe UI", 9), padx=10).pack(fill="x", pady=2)

        # Barra de pestañas
        self.tab_bar = tk.Frame(self.root, height=35, bg="#2d2d2d")
        self.tab_bar.pack(side="top", fill="x")
        tk.Label(self.tab_bar, text="  processor_core.py  x ", fg="white", bg=bg_dark, font=("Segoe UI", 9)).pack(side="left", fill="y")

        # Barra de estado inferior
        self.status = tk.Frame(self.root, height=22, bg=accent_blue)
        self.status.pack(side="bottom", fill="x")
        tk.Label(self.status, text="  master* | Ln 42, Col 12 | Spaces: 4 | UTF-8 | Python 3.11.5", fg="white", bg=accent_blue, font=("Segoe UI", 8)).pack(side="left")

        # Área del Editor
        self.text_font = font.Font(family="Consolas", size=13)
        self.editor = tk.Text(
            self.root, bg=bg_dark, fg="#d4d4d4",
            insertbackground="white", relief="flat",
            font=self.text_font, padx=20, pady=20,
            highlightthickness=0, undo=True
        )
        self.editor.pack(expand=True, fill="both")

        # Configuración de Syntax Highlighting
        self.editor.tag_configure("kw", foreground="#569cd6")      # Keywords
        self.editor.tag_configure("str", foreground="#ce9178")     # Strings
        self.editor.tag_configure("com", foreground="#6a9955")     # Comments
        self.editor.tag_configure("fn", foreground="#dcdcaa")      # Functions
        self.editor.tag_configure("cls", foreground="#4ec9b0")     # Classes
        self.editor.tag_configure("num", foreground="#b5cea8")     # Numbers
        self.editor.tag_configure("dec", foreground="#dcdcaa")     # Decorators

    def highlight_syntax(self):
        content = self.editor.get("1.0", tk.END)
        self.editor.mark_set("range_start", "1.0")
        
        # Mapa de patrones
        patterns = [
            ("com", r'#.*'),
            ("str", r'".*?"|\'.*?\''),
            ("kw", r'\b(def|class|import|from|if|return|while|for|in|else|elif|try|except|as|with|yield|lambda|pass|raise|None|True|False)\b'),
            ("fn", r'\b\w+(?=\()'),
            ("cls", r'\b[A-Z]\w+'),
            ("num", r'\b\d+\b'),
            ("dec", r'@\w+'),
        ]

        for tag, pattern in patterns:
            self.editor.tag_remove(tag, "1.0", tk.END)
            for match in re.finditer(pattern, content):
                start = f"1.0 + {match.start()} chars"
                end = f"1.0 + {match.end()} chars"
                self.editor.tag_add(tag, start, end)

    def inject_code(self, event):
        # Bloquea teclas especiales para no romper la UI
        if event.keysym in ["Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R", "Caps_Lock"]:
            return

        if self.char_index < len(CODE_DATA):
            char = CODE_DATA[self.char_index]
            self.editor.insert(tk.END, char)
            self.char_index += 1
            
            # Autoscroll
            self.editor.see(tk.END)
            
            # Aplicar colores cada 2 caracteres para no saturar el procesador
            if self.char_index % 2 == 0:
                self.highlight_syntax()
                
        return "break" # Impide que la tecla real se escriba

if __name__ == "__main__":
    root = tk.Tk()
    app = ProEditorSimulator(root)
    root.mainloop()
