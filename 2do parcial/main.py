import customtkinter as ctk
from tkinter import messagebox
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class AppConsultas(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Consultas Diversificadas - Carlos Maldonado")
        self.geometry("1100x650")
        self.main_container = ctk.CTkFrame(self)
        self.main_container.pack(fill="both", expand=True)
        self.mostrar_login()

    def mostrar_login(self):
        for widget in self.main_container.winfo_children(): widget.destroy()
        self.frame_login = FrameLogin(self.main_container, self.validar_acceso)
        self.frame_login.place(relx=0.5, rely=0.5, anchor="center")

    def mostrar_dashboard(self, usuario):
        for widget in self.main_container.winfo_children(): widget.destroy()
        self.dashboard = FrameDashboard(self.main_container, usuario)
        self.dashboard.pack(fill="both", expand=True)

    def validar_acceso(self, user, password):
        if not os.path.exists("usuarios.txt"):
            messagebox.showerror("Error", "Archivo usuarios.txt no encontrado")
            return
        
        with open("usuarios.txt", "r") as f:
            for linea in f:
                u, p = linea.strip().split(",")
                if u == user and p == password:
                    self.mostrar_dashboard(user)
                    return
        messagebox.showerror("Error", "Credenciales inválidas")

class FrameLogin(ctk.CTkFrame):
    def __init__(self, master, callback):
        super().__init__(master, width=300, height=350, corner_radius=15)
        ctk.CTkLabel(self, text="LOGIN", font=("Arial", 24, "bold")).pack(pady=20)
        self.ent_user = ctk.CTkEntry(self, placeholder_text="Usuario", width=200)
        self.ent_user.pack(pady=10)
        self.ent_pass = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*", width=200)
        self.ent_pass.pack(pady=10)
        ctk.CTkButton(self, text="Entrar", command=lambda: callback(self.ent_user.get(), self.ent_pass.get())).pack(pady=20)

class FrameDashboard(ctk.CTkFrame):
    def __init__(self, master, usuario):
        super().__init__(master)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu = ctk.CTkScrollableFrame(self, width=250, label_text="CONSULTAS")
        self.menu.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.visor_frame = ctk.CTkFrame(self)
        self.visor_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        self.txt_resultado = ctk.CTkTextbox(self.visor_frame, font=("Consolas", 12))
        self.txt_resultado.pack(fill="both", expand=True, padx=10, pady=10)

        self.generar_menu()

    def generar_menu(self):
        self.consultas_db = {
            "Inventario Crítico": "ID | Producto | Stock | Ubicación\n001 | Paracetamol | 2 | Pasillo A\n005 | Insulina | 1 | Refri 2",
            "Ventas de Hoy": "Hora | Folio | Total | Método\n10:15 | #882 | $450.00 | Tarjeta\n12:30 | #883 | $1,200.0 | Efectivo",
            "Estado del Servidor": "Componente | Estado | Carga\nCPU | Optimo | 15%\nRAM | Alerta | 89%\nDatabase | Conectado | Lat: 2ms",
            "Usuarios Logueados": "Usuario | Terminal | Inicio de Sesión\nAdmin | Localhost | 08:00 AM\nLain8 | Win-Remote | 10:30 AM",
            "Auditoría de Cambios": "Fecha | Acción | Usuario | Tabla\n23/04 | UPDATE | CarlosM | Inventario\n23/04 | DELETE | Admin | Logs_Temp",
            "Pedidos a Proveedores": "Proveedor | Pedido | Fecha Est. | Total\nFarmaRed | Antibióticos | 25/04 | $15,400\nBioLabs | Reactivos | 28/04 | $8,900",
            "Pacientes en Espera": "Ticket | Paciente | Tiempo Espera\nA-12 | Juan Pérez | 15 min\nB-05 | Maria Luna | 05 min",
            "Resumen de Nómina": "Depto | Empleados | Monto Quincenal\nSistemas | 4 | $45,000\nVentas | 12 | $82,300",
            "Top Productos Mes": "Rango | Producto | Unidades Vendidas\n1 | Vitamina C | 450\n2 | Cubrebocas | 380",
            "Alertas de Seguridad": "[AVISO] Intento de acceso fallido desde IP 192.168.1.50\n[EXITO] Backup de base de datos generado (2.4 GB)"
        }

        for nombre in self.consultas_db.keys():
            btn = ctk.CTkButton(self.menu, text=nombre, anchor="w",
                                command=lambda n=nombre: self.mostrar(n))
            btn.pack(pady=5, fill="x")

    def mostrar(self, clave):
        self.txt_resultado.delete("1.0", "end")
        header = f"{'='*50}\nREPORTE DE: {clave.upper()}\n{'='*50}\n\n"
        self.txt_resultado.insert("0.0", header + self.consultas_db[clave])

if __name__ == "__main__":
    app = AppConsultas()
    app.mainloop()