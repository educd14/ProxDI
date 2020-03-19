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

        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        #Refrescamos tabla clientes
        """TABLA CLIENTES"""

        self.columnasC = ["DNI", "Nome", "Apelido", "Sexo", "Telefono", "Direccion"]
        self.modeloC = Gtk.ListStore(str, str, str, str, str, str)
        self.clientes = []
        self.vista = Gtk.TreeView(model=self.modeloC)
        self.vista.set_hexpand(True)
        self.vista.set_vexpand(True)
        seleccion = self.vista.get_selection()
        seleccion.connect("changed", self.on_vista_changed)

        clientesBD = MethodsBD.selectTablaClientes()
        for cliente in clientesBD:
            self.clientes.append(
                [cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]])

        for elemento in self.clientes:
            self.modeloC.append(elemento)

        for i in range(len(self.columnasC)):
            celda = Gtk.CellRendererText()
            celda.set_alignment(0.5, 0)
            self.columna = Gtk.TreeViewColumn(self.columnasC[i], celda, text=i)
            self.columna.set_alignment(0.5)
            self.columna.set_expand(True)
            self.vista.append_column(self.columna)


        boxV.pack_start(self.vista, True, True, 0)


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
        self.btnVolver = Gtk.Button(label="Volver")
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
        grid.attach(self.btnGuardar,0,5,1,2)
        grid.attach(self.btnVolver,1,5,1,1)


        boxV.pack_start(grid, True, True, 10)

        self.add(boxV)
        self.show_all()
        self.connect("destroy", Gtk.main_quit)

        #Señales
        self.btnVolver.connect("clicked", self.on_btnVolver_clicked)
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

            self.txtDni.set_text(modelo[punteiro][0])
            self.txtNome.set_text(modelo[punteiro][1])
            self.txtApelido.set_text(modelo[punteiro][2])
            self.txtSexo.set_text((modelo[punteiro][3]))
            self.txtDireccion.set_text((modelo[punteiro][4]))
            self.txtTelefono.set_text((modelo[punteiro][5]))

    def on_btnAplicar_clicked(self, boton):
        modAcc = self.cmbAccion.get_model()
        indice = self.cmbAccion.get_active_iter()

        if modAcc[indice][0] == 0:
            """Añadir"""
        elif modAcc[indice][0] == 1:
            """Modificar"""
        elif modAcc[indice][0] == 2:
            MethodsBD.deleteTablaClientes(self.txtDni.get_text())
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "Cliente Eliminado Correctamente")
            dialog.run()
            dialog.destroy()
            self.tablaClienteRefresh()

    def tablaClienteRefresh(self):

        self.modeloC.clear()
        self.clientes2 = []
        clientesBD = MethodsBD.selectTablaClientes()
        for cliente in clientesBD:
            self.clientes2.append(
                [cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]])

        for elemento in self.clientes2:
            self.modeloC.append(elemento)

if __name__ == "__main__":
    Fiestra()
    Gtk.main()