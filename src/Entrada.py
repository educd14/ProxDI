import gi

from src.Clientes import XestionCli
from src.ProdServ import ProdServi
from src.SqliteBD import MethodsBD

from gi.overrides.Gdk import Gdk

gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class VentanaPrincipal():
    def __init__(self):
        css = '''
        
                    label {
                    font: 20px Courier-bold;
                    }
                    button { 
                    background:  #ffcc99;
                    padding: 5px 10px;
                    font: 14px Courier-bold;
                    color: #000000;
                    }
                                        '''
        cssProvider = Gtk.CssProvider()
        cssProvider.load_from_data(bytes(css.encode()))
        screen = Gdk.Screen.get_default()
        styleContext = Gtk.StyleContext()
        styleContext.add_provider_for_screen(screen, cssProvider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        #Creación tablas BD
        MethodsBD.tablas()

        builder = Gtk.Builder()
        #Asignamos a nuestro builder el archivo de nuestro proyecto Glade
        builder.add_from_file("formEntrada.glade")

        self.vEntrada = builder.get_object("vEntrada")
        self.vEntrada.set_default_size(220, 150)

        self.btnClientes = builder.get_object("btnClientes")
        self.btnProdutos = builder.get_object("btnProdutos")
        self.btnSalir = builder.get_object("btnSalir")

        #Señales
        self.btnClientes.connect("clicked", self.on_btnClientes_clicked)
        self.btnProdutos.connect("clicked", self.on_btnProdutos_clicked)
        self.btnSalir.connect("clicked", self.on_btnSalir_clicked)
        self.vEntrada.connect("destroy", self.on_btnSalir_clicked)

        #Y mostramos toda la ventana "main"
        self.vEntrada.show_all()


    def on_btnClientes_clicked(self, boton):
         """
                  Metodo para entrar al formulario Xestión de Clientes
                  :param Widget: botón
                  :return: No devuelve ningún parámetro.
                  """
         XestionCli.Fiestra().show_all()
         self.vEntrada.set_visible(False)

    def on_btnProdutos_clicked(self, boton):
        """
                 Metodo para entrar al formulario Produtos e Servizos
                 :param Widget: botón
                 :return: No devuelve ningún parámetro.
                 """
        ProdServi.Fiestra().show_all()
        self.vEntrada.set_visible(False)

    def on_btnSalir_clicked(self, boton):
        exit(0)
