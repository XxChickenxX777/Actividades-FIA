import customtkinter as ctk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class Graficador(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Graficador de Funciones Lineales")
        self.geometry("650x550")
        self.minsize(500, 450)

        self.frame_inputs = ctk.CTkFrame(self)
        self.frame_inputs.pack(pady=15, padx=20, fill="x")

        self.label_m = ctk.CTkLabel(self.frame_inputs, text="Pendiente (m):", font=("Arial", 14))
        self.label_m.pack(side="left", padx=(10, 5), pady=10)
        
        self.entry_m = ctk.CTkEntry(self.frame_inputs, width=70, placeholder_text="Ej. 2")
        self.entry_m.pack(side="left", padx=5, pady=10)

        self.label_b = ctk.CTkLabel(self.frame_inputs, text="Término Indep. (b):", font=("Arial", 14))
        self.label_b.pack(side="left", padx=(20, 5), pady=10)
        
        self.entry_b = ctk.CTkEntry(self.frame_inputs, width=70, placeholder_text="Ej. -1")
        self.entry_b.pack(side="left", padx=5, pady=10)

        self.btn_graficar = ctk.CTkButton(self.frame_inputs, text="Graficar", command=self.generar_grafica)
        self.btn_graficar.pack(side="left", padx=(20, 10), pady=10)

        self.label_error = ctk.CTkLabel(self, text="", text_color="red", font=("Arial", 12, "bold"))
        self.label_error.pack(pady=0)

        self.frame_grafica = ctk.CTkFrame(self)
        self.frame_grafica.pack(pady=10, padx=20, fill="both", expand=True)

        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_grafica)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)
        
        self.ax.axhline(0, color='black', linewidth=1)
        self.ax.axvline(0, color='black', linewidth=1)
        self.ax.grid(color='gray', linestyle='--', linewidth=0.5)
        self.ax.set_title("f(x) = mx + b")
        self.canvas.draw()

    def generar_grafica(self):
        self.label_error.configure(text="")

        m_str = self.entry_m.get().strip()
        b_str = self.entry_b.get().strip()

        try:
            m = float(m_str.replace(',', '.'))
            b = float(b_str.replace(',', '.'))
        except ValueError:
            self.label_error.configure(text="Datos incorrectos. Por favor, ingresa solo números válidos.")
            return

        self.ax.clear()

        x = np.linspace(-10, 10, 100)
        y = (m * x) + b

        self.ax.axhline(0, color='black', linewidth=1.2)
        self.ax.axvline(0, color='black', linewidth=1.2)
        self.ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

        label_ecuacion = f"f(x) = {m}x + {b}"
        self.ax.plot(x, y, color='blue', linewidth=2, label=label_ecuacion)

        self.ax.set_title("Gráfica de Función Lineal")
        self.ax.set_xlabel("Eje X")
        self.ax.set_ylabel("Eje Y")
        self.ax.legend()

        self.ax.set_xlim([-10, 10])
        
        self.canvas.draw()

if __name__ == "__main__":
    app = Graficador()
    app.mainloop()