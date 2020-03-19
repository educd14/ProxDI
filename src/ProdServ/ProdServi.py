import gi

from src import Entrada
from src.SqliteBD import MethodsBD

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#HEMOS QUITADO LA FUNCIÓN QUE HACE QUE AL CLICKAR EN "OCUPACIÓN" SE ORDENEN LAS CELDAS DE MOMENTO
class Fiestra(Gtk.Window):

    def __init__(self):  # constructor
        Gtk.Window.__init__(self, title="Xestión de Clientes")
        self.set_default_size(600, 400)

        self.notebook = Gtk.Notebook();
        self.add(self.notebook)

        #Notebook1 - PRODUTOS

        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        """TABLA PRODUTOS"""

        self.columnasP = ["ID", "Produto", "Precio(€)",""]
        self.modeloP = Gtk.ListStore(int, str, int,bool)
        self.produtos = []
        self.vista = Gtk.TreeView(model=self.modeloP)
        self.vista.set_hexpand(True)
        self.vista.set_vexpand(True)
        seleccion = self.vista.get_selection()
        seleccion.connect("changed", self.on_vista_changed)

        produtosBD = MethodsBD.selectTablaProductos()
        for produto in produtosBD:
            self.produtos.append(
                [produto[0], produto[1], produto[2], False])

        for elemento in self.produtos:
            self.modeloP.append(elemento)

        for i in range(len(self.columnasP)):
            if i == 3:

                celda = Gtk.CellRendererToggle()
                celda.set_alignment(0.5, 0)
                self.columna = Gtk.TreeViewColumn(self.columnasP[i], celda, active=i)
                self.columna.set_alignment(0.5)
                self.columna.set_expand(True)
                self.vista.append_column(self.columna)
            else:
                celda = Gtk.CellRendererText()
                celda.set_alignment(0.5, 0)
                self.columna = Gtk.TreeViewColumn(self.columnasP[i], celda, text=i)
                self.columna.set_alignment(0.5)
                self.columna.set_expand(True)
                self.vista.append_column(self.columna)

        boxV.pack_start(self.vista, True, True, 0)


        grid = Gtk.Grid(column_homogeneous=True,
                         column_spacing=10,
                         row_spacing=10)

        self.lblID = Gtk.Label("ID:")
        self.txtID = Gtk.Entry()
        self.lblProduto = Gtk.Label("Produto:")
        self.txtProduto = Gtk.Entry()
        self.lblPrecio = Gtk.Label("Precio:")
        self.txtPrecio = Gtk.Entry()
        self.btnAplicar = Gtk.Button(label = "Aplicar")
        self.cmbAccion = Gtk.ComboBox()
        acciones = Gtk.ListStore(int,str)
        acciones.append([0,"Añadir"])
        acciones.append([1,"Modificar"])
        acciones.append([2,"Eliminar"])
        self.cmbAccion.set_model(acciones)
        celdaTexto = Gtk.CellRendererText()
        self.cmbAccion.pack_start(celdaTexto,True)
        self.cmbAccion.add_attribute(celdaTexto, "text", 1)
        self.cmbAccion.set_active(0)
        self.btnVolver = Gtk.Button(label = "Volver")

        grid.add(self.lblID)
        grid.attach(self.txtID,0,1,1,1)
        grid.attach_next_to(self.lblProduto,self.lblID,Gtk.PositionType.RIGHT,1,1)
        grid.attach(self.txtProduto, 1, 1, 1, 1)
        grid.attach_next_to(self.lblPrecio,self.lblProduto,Gtk.PositionType.RIGHT,1,1)
        grid.attach(self.txtPrecio, 2, 1, 1, 1)
        grid.attach(self.cmbAccion,1,4,1,1)
        grid.attach(self.btnAplicar,2,5,1,1)
        grid.attach(self.btnVolver,0,5,1,1)


        #Notebook2 - SERVIZO

        gridS = Gtk.Grid(column_homogeneous=True,
                         column_spacing=10,
                         row_spacing=10)
        self.lblServizo = Gtk.Label("FACTURA")
        self.lblFactura = Gtk.Label("Seleccione o cliente o que quere facer a factura")
        self.cmbCliente = Gtk.ComboBox()
        self.cmbCliente.set_model(acciones)
        celdaTexto = Gtk.CellRendererText()
        self.cmbCliente.pack_start(celdaTexto, True)
        self.cmbCliente.add_attribute(celdaTexto, "text", 1)
        self.cmbCliente.set_active(0)
        self.btnFactura = Gtk.Button(label="Factura")
        self.modelo2 = Gtk.ListStore(int, str, int)
        self.vista2 = Gtk.TreeView(model=self.modelo2)
        self.vista2.set_hexpand(True)
        self. vista2.set_vexpand(True)
        self.btnVolver2 = Gtk.Button(label = "Volver")

        gridS.attach(self.lblServizo,1,1,2,1)
        gridS.attach(self.vista2,1,2,2,1)
        gridS.attach(self.lblFactura,1,3,2,1)
        gridS.attach(self.cmbCliente, 1, 5, 1, 1)
        gridS.attach_next_to(self.btnFactura, self.cmbCliente, Gtk.PositionType.RIGHT, 1, 1)
        gridS.attach(self.btnVolver2,1,6,2,2)




        boxV.pack_start(grid, True, True, 10)
        self.notebook.append_page(boxV, Gtk.Label("Produtos"))
        self.notebook.append_page(gridS, Gtk.Label("Servizo"))


        self.show_all()
        self.connect("destroy", Gtk.main_quit)

        # Señales
        self.btnVolver.connect("clicked", self.on_btnVolver_clicked)
        self.btnVolver2.connect("clicked", self.on_btnVolver_clicked)
        self.btnAplicar.connect("clicked", self.on_btnAplicar_clicked)

        # Volver al inicio

    def on_btnVolver_clicked(self, boton):
        """Metodo que vuelve al formulario de inicio.
                :param widget: boton
                :return: No devuelve ningún parámetro.
        """
        Entrada.VentanaPrincipal().vEntrada.show_all()
        self.set_visible(False)

    def on_vista_changed(self, seleccion):
        (modelo, punteiro) = seleccion.get_selected()

        if punteiro is not None:

            self.txtID.set_text(str(modelo[punteiro][0]))
            self.txtProduto.set_text(modelo[punteiro][1])
            self.txtPrecio.set_text(str(modelo[punteiro][2]))

    def on_btnAplicar_clicked(self, boton):
        modAcc = self.cmbAccion.get_model()
        indice = self.cmbAccion.get_active_iter()

        if modAcc[indice][0] == 0:
            """Añadir"""
        elif modAcc[indice][0] == 1:
            """Modificar"""
        elif modAcc[indice][0] == 2:
            MethodsBD.deleteTablaProductos(self.txtID.get_text())
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "Produto Eliminado Correctamente")
            dialog.run()
            dialog.destroy()
            self.tablaProdutoRefresh()

    def tablaProdutoRefresh(self):

        self.modeloP.clear()
        self.produtos2 = []
        produtosBD = MethodsBD.selectTablaProductos()
        for produto in produtosBD:
            self.produtos2.append(
                [produto[0], produto[1], produto[2], False])

        for elemento in self.produtos2:
            self.modeloP.append(elemento)

if __name__ == "__main__":
    Fiestra()
    Gtk.main()