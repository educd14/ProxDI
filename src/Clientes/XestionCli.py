import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

#HEMOS QUITADO LA FUNCIÓN QUE HACE QUE AL CLICKAR EN "OCUPACIÓN" SE ORDENEN LAS CELDAS DE MOMENTO
class Fiestra(Gtk.Window):

    def __init__(self):  # constructor
        Gtk.Window.__init__(self, title="Xestión de Clientes")
        self.set_default_size(600, 400)

        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.modelo = Gtk.ListStore(str, str, str, str, str, str)
        self.modelo.append(["53242337F", "Alfredo", "Dominguez", "M", "986172748", "Garcia Barbon"])
        self.modelo.append(["93758295N", "Maria", "Garzon", "F", "986352378", "Zaragoza"])
        self.modelo.append(["58394052G", "Eugenia", "Val", "F", "986642347", "Valencia"])
        self.modelo.append(["28503758L", "Eduardo", "Collazo", "M", "986152764", "Pintor Colmeiro"])



        vista = Gtk.TreeView(model=self.modelo)
        vista.set_hexpand(True)
        vista.set_vexpand(True)
        boxV.pack_start(vista, True, True, 0)

        celdaDNI = Gtk.CellRendererText()
        celdaDNI.set_property("editable", False)

        columnaDNI = Gtk.TreeViewColumn('DNI', celdaDNI, text=0)
        celdaNome = Gtk.CellRendererText()
        celdaNome.set_property("editable", False)

        columnaNome = Gtk.TreeViewColumn('Nome', celdaNome, text=1)
        celdaApelido = Gtk.CellRendererText()
        celdaApelido.set_property("editable", False)
        columnaApelido = Gtk.TreeViewColumn('Apelido', celdaApelido, text=2)

        celdaSexo = Gtk.CellRendererText()
        celdaSexo.set_property("editable", False)
        columnaSexo = Gtk.TreeViewColumn('Sexo', celdaSexo, text=3)


        celdaTelefono = Gtk.CellRendererText()
        celdaTelefono.set_property("editable", False)
        columnaTelefono = Gtk.TreeViewColumn('Telefono', celdaTelefono, text=4)

        celdaDireccion = Gtk.CellRendererText()
        celdaDireccion.set_property("editable", False)
        columnaDireccion = Gtk.TreeViewColumn('Dirección', celdaDireccion, text=5)

        vista.append_column(columnaDNI)
        vista.append_column(columnaNome)
        vista.append_column(columnaApelido)
        vista.append_column(columnaSexo)
        vista.append_column(columnaTelefono)
        vista.append_column(columnaDireccion)


        grid = Gtk.Grid(column_homogeneous=True,
                         column_spacing=10,
                         row_spacing=10)

        self.lblDni = Gtk.Label("DNI:")
        self.txtDni = Gtk.Entry()
        self.lblNome = Gtk.Label("Nome:")
        self.txtNome = Gtk.Entry()
        self.lblApelido = Gtk.Label("Apelido:")
        self.txtApelido = Gtk.Entry()
        self.lblSexo = Gtk.Label("Sexo:")
        self.txtSexo = Gtk.Entry()
        self.lblTelefono = Gtk.Label("Telefono:")
        self.txtTelefono = Gtk.Entry()
        self.lblDireccion = Gtk.Label("Dirección:")
        self.txtDireccion = Gtk.Entry()
        self.btnAplicar = Gtk.Button(label = "Aplicar")
        self.btnGuardar = Gtk.Button(label="Guardar clientes en PDF")
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

        grid.add(self.lblDni)
        grid.attach(self.txtDni,0,1,1,1)
        grid.attach_next_to(self.lblNome,self.lblDni,Gtk.PositionType.RIGHT,1,1)
        grid.attach(self.txtNome, 1, 1, 1, 1)
        grid.attach_next_to(self.lblApelido,self.lblNome,Gtk.PositionType.RIGHT,1,1)
        grid.attach(self.txtApelido, 2, 1, 1, 1)
        grid.attach_next_to(self.lblSexo,self.txtDni,Gtk.PositionType.BOTTOM,1,1)
        grid.attach(self.txtSexo, 0, 3, 1, 1)
        grid.attach_next_to(self.lblTelefono,self.lblSexo,Gtk.PositionType.RIGHT,1,1)
        grid.attach(self.txtTelefono, 1, 3, 1, 1)
        grid.attach_next_to(self.lblDireccion,self.lblTelefono,Gtk.PositionType.RIGHT,1,1)
        grid.attach(self.txtDireccion, 2, 3, 1, 1)
        grid.attach(self.cmbAccion,1,4,1,1)
        grid.attach(self.btnAplicar,2,5,1,1)
        grid.attach(self.btnGuardar,0,5,1,1)


        boxV.pack_start(grid, True, True, 10)

        self.add(boxV)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

if __name__ == "__main__":
    Fiestra()
    Gtk.main()