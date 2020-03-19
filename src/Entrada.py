import gi

from src.SqliteBD import MethodsBD

gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class VentanaPrincipal():
    def __init__(self):
        #Creación tablas BD
        MethodsBD.tablas()

        builder = Gtk.Builder()
        #Asignamos a nuestro builder el archivo de nuestro proyecto Glade
        builder.add_from_file("formEntrada.glade")

        vEntrada = builder.get_object("vEntrada")
        vEntrada.set_default_size(200, 150)

        self.btnClientes = builder.get_object("btnClientes")
        self.btnProdutos = builder.get_object("btnProdutos")
        self.btnSalir = builder.get_object("btnSalir")

        self.btnClientes.connect("clicked", self.on_btnClientes_clicked)
        self.btnProdutos.connect("clicked", self.on_btnProdutos_clicked)
        self.btnSalir.connect("clicked", self.on_btnSalir_clicked)
        vEntrada.connect("destroy", Gtk.main_quit)

        #Y mostramos toda la ventana "main"
        vEntrada.show_all()


    def on_btnClientes_clicked(self, boton):
        """do"""
    def on_btnProdutos_clicked(self, boton):
        """do"""
    def on_btnSalir_clicked(self, boton):
        Gtk.main_quit()

#ACTIVAMOS NUESTRA INTERFAZ GRÁFICA
if __name__ == "__main__":
    VentanaPrincipal()
    Gtk.main()