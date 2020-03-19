import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#HEMOS QUITADO LA FUNCIÓN QUE HACE QUE AL CLICKAR EN "OCUPACIÓN" SE ORDENEN LAS CELDAS DE MOMENTO
class Fiestra(Gtk.Window):

    def __init__(self):  # constructor
        Gtk.Window.__init__(self, title="Xestión de Clientes")
        self.set_default_size(600, 400)

        self.notebook = Gtk.Notebook();
        self.add(self.notebook)

        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.modelo = Gtk.ListStore(int,str,int,bool)
        self.modelo.append([1, 'Pantalla LED 20"', 119.99,False])
        self.modelo.append([2, "Nvidia 1060 GTX", 156.95,False])
        self.modelo.append([3, "Teclado Corsair", 34.99,False])
        self.modelo.append([4, "SDD Seagate", 54.99,False])



        vista = Gtk.TreeView(model=self.modelo)
        vista.set_hexpand(True)
        vista.set_vexpand(True)
        boxV.pack_start(vista, True, True, 0)

        celdaID = Gtk.CellRendererText()
        celdaID.set_property("editable", False)

        columnaID = Gtk.TreeViewColumn('ID', celdaID, text=0)
        celdaProduto = Gtk.CellRendererText()
        celdaProduto.set_property("editable", False)

        columnaProduto = Gtk.TreeViewColumn('Produto', celdaProduto, text=1)
        celdaPrecio = Gtk.CellRendererText()
        celdaPrecio.set_property("editable", False)
        columnaPrecio = Gtk.TreeViewColumn('Precio(€)', celdaPrecio, text=2)

        celdaSeleccion = Gtk.CellRendererToggle()
        columnaSeleccion = Gtk.TreeViewColumn("",celdaSeleccion, active=3)


        vista.append_column(columnaID)
        vista.append_column(columnaProduto)
        vista.append_column(columnaPrecio)
        vista.append_column(columnaSeleccion)


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
        acciones.append([1,"Añadir"])
        acciones.append([2,"Modificar"])
        acciones.append([3,"Eliminar"])
        self.cmbAccion.set_model(acciones)
        celdaTexto = Gtk.CellRendererText()
        self.cmbAccion.pack_start(celdaTexto,True)
        self.cmbAccion.add_attribute(celdaTexto, "text", 1)
        self.cmbAccion.set_active(0)

        grid.add(self.lblID)
        grid.attach(self.txtID,0,1,1,1)
        grid.attach_next_to(self.lblProduto,self.lblID,Gtk.PositionType.RIGHT,1,1)
        grid.attach(self.txtProduto, 1, 1, 1, 1)
        grid.attach_next_to(self.lblPrecio,self.lblProduto,Gtk.PositionType.RIGHT,1,1)
        grid.attach(self.txtPrecio, 2, 1, 1, 1)
        grid.attach(self.cmbAccion,1,4,1,1)
        grid.attach(self.btnAplicar,2,5,1,1)

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

        gridS.attach(self.lblServizo,1,1,2,1)
        gridS.attach(self.vista2,1,2,2,1)
        gridS.attach(self.lblFactura,1,3,2,1)
        gridS.attach(self.cmbCliente, 1, 5, 1, 1)
        gridS.attach_next_to(self.btnFactura, self.cmbCliente, Gtk.PositionType.RIGHT, 1, 1)




        boxV.pack_start(grid, True, True, 10)
        self.notebook.append_page(boxV, Gtk.Label("Produtos"))
        self.notebook.append_page(gridS, Gtk.Label("Servizo"))

        
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    Fiestra()
    Gtk.main()