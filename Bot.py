import tkinter as tk
from tkinter import font
import re

# --- CONFIGURACIÓN DEL CÓDIGO A "ESCRIBIR" ---
# Puedes meter aquí cualquier código complejo para que parezca más pro.
FAKE_CODE = """import numpy as np
import tensorflow as tf
from datetime import datetime

class NeuralMatrixProcessor:
    def __init__(self, layers=[128, 64, 32]):
        self.depth = len(layers)
        self.weights = []
        self.bias = None
        print(f"[{datetime.now()}] Initializing Core...")

    def optimize_buffers(self, data_stream):
        # Optimizando punteros de memoria para procesamiento en paralelo
        mask = np.random.choice([0, 1], size=data_stream.shape)
        return tf.math.multiply(data_stream, mask)

    async def execute_query(self, query_id):
        # Simulación de handshake asíncrono
        endpoint = f"https://api.internal.network/v3/{query_id}"
        async with session.get(endpoint) as response:
            return await response.json()

def main():
    processor = NeuralMatrixProcessor()
    raw_data = np.random.rand(1024, 1024)
    processed = processor.optimize_buffers(raw_data)
    print("Kernel status: ONLINE")

if __name__ == "__main__":
    main()
"""

class FakeVSCode:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Studio Code - matrix_processor.py")
        self.root.geometry("1000x700")
        self.root.configure(bg="#1e1e1e")
        
        self.index = 0
        self.setup_ui()
        self.root.bind("<Key>", self.type_code)

    def setup_ui(self):
        # Barra lateral (Sidebar)
        self.sidebar = tk.Frame(self.root, width=50, bg="#333333")
        self.sidebar.pack(side="left", fill="y")
        
        # Área de archivos (Explorador)
        self.explorer = tk.Frame(self.root, width=150, bg="#252526")
        self.explorer.pack(side="left", fill="y")
        tk.Label(self.explorer, text=" EXPLORER", fg="#aaaaaa", bg="#252526", font=("Segoe UI", 10)).pack(pady=10)
        tk.Label(self.explorer, text="  main.py", fg="#ffffff", bg="#37373d", anchor="w").pack(fill="x")
        
        # Barra de estado inferior
        self.status = tk.Frame(self.root, height=20, bg="#007acc")
        self.status.pack(side="bottom", fill="x")
        tk.Label(self.status, text="  Line 1, Col 1  |  UTF-8  |  Python 3.10.2", fg="white", bg="#007acc", font=("Segoe UI", 8)).pack(side="left")

        # Editor de texto
        self.text_font = font.Font(family="Consolas", size=12)
        self.editor = tk.Text(
            self.root, bg="#1e1e1e", fg="#d4d4d4", 
            insertbackground="#ffffff", relief="flat",
            font=self.text_font, padx=10, pady=10,
            highlightthickness=0
        )
        self.editor.pack(expand=True, fill="both")
        
        # Configuración de colores para resaltado (Syntax Highlighting)
        self.editor.tag_configure("keyword", foreground="#569cd6")
        self.editor.tag_configure("string", foreground="#ce9178")
        self.editor.tag_configure("comment", foreground="#6a9955")
        self.editor.tag_configure("function", foreground="#dcdcaa")

    def highlight(self):
        # Resaltado básico por regex
        content = self.editor.get("1.0", tk.END)
        for tag, pattern in [
            ("keyword", r'\b(def|class|import|from|if|return|async|await|with|as)\b'),
            ("string", r'".*?"|\'.*?\''),
            ("comment", r'#.*'),
            ("function", r'\b\w+(?=\()')
        ]:
            self.editor.tag_remove(tag, "1.0", tk.END)
            for match in re.finditer(pattern, content):
                start = f"1.0 + {match.start()} chars"
                end = f"1.0 + {match.end()} chars"
                self.editor.tag_add(tag, start, end)

    def type_code(self, event):
        # Evitar teclas de sistema
        if event.keysym in ["Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R"]:
            return

        if self.index < len(FAKE_CODE):
            # Escribir el siguiente caracter
            char = FAKE_CODE[self.index]
            self.editor.insert(tk.END, char)
            self.index += 1
            self.editor.see(tk.END) # Auto-scroll
            self.highlight()
        return "break" # Evita que se escriba la tecla real pulsada

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeVSCode(root)
    root.mainloop()
