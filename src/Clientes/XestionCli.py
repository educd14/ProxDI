import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

#HEMOS QUITADO LA FUNCIÓN QUE HACE QUE AL CLICKAR EN "OCUPACIÓN" SE ORDENEN LAS CELDAS DE MOMENTO
class Fiestra(Gtk.Window):

    def __init__(self):  # constructor
        Gtk.Window.__init__(self, title="Xestión de Clientes")
        self.set_default_size(400, 300)

        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        self.modelo = Gtk.ListStore(str, str, str, str, str, str)
        self.modelo.append(["532423F", "Alfredo", "Dominguez", "M", "986172748", "Garcia Barbon"])

        vista = Gtk.TreeView(model=self.modelo)
        seleccion = vista.get_selection()
       # seleccion.connect("changed", self.on_vista_changed)
        boxV.pack_start(vista, True, True, 0)

        celdaDNI = Gtk.CellRendererText()
        celdaDNI.set_property("editable", False)  # con false no se pueden editar las celdas

        columnaDNI = Gtk.TreeViewColumn('DNI', celdaDNI, text=0)

        celdaNome = Gtk.CellRendererText()
        celdaNome.set_property("editable", False)
       # celdaNome.connect("edited", self.on_celdaDireccion_edited, self.modelo)

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

        vista.append_column(columnaDNI)  # añadir al treeview la columna
        vista.append_column(columnaNome)
        vista.append_column(columnaApelido)
        vista.append_column(columnaSexo)
        vista.append_column(columnaTelefono)
        vista.append_column(columnaDireccion)

        self.add(boxV)  # al añadir el boxH esta línea sobra
        self.show_all()
        self.connect("destroy", Gtk.main_quit)
"""
        boxH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.txtHotel = Gtk.Entry()
        self.txtDireccion = Gtk.Entry()
        self.txtOcupacion = Gtk.Entry()
        self.chkMascota = Gtk.CheckButton()
        self.cmbCategoria = Gtk.ComboBox()
        btnNovo = Gtk.Button("Novo")
        btnNovo.connect("clicked", self.on_btnNovo_clicked, self.modelo)
        boxH.pack_start(self.txtHotel, True, False, 0)
        boxH.pack_start(self.txtDireccion, True, False, 0)
        boxH.pack_start(self.txtOcupacion, True, False, 0)
        boxH.pack_start(self.chkMascota, True, False, 0)
        boxH.pack_start(self.cmbCategoria, True, False, 0)
        boxH.pack_start(btnNovo, True, False, 0)
        boxV.pack_start(boxH, True, False, 0)
        caixaFiltro = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.chkFiltro = Gtk.CheckButton(label='Filtro ocupación')
        self.chkFiltro.connect("toggled", self.on_chkFiltro_toggled, modeloFiltrado)
        caixaFiltro.pack_start(self.chkFiltro, True, True, 0)

        boxV.pack_start(caixaFiltro, True, False, 0)
        self.add(boxV)

        self.cmbCategoria.set_model(modeloCat)
        self.cmbCategoria.pack_start(celdaText, True)
        self.cmbCategoria.add_attribute(celdaText, "text", 0)
"""

"""

    def on_celdaCheck_toggled(self, control, fila, modelo):  # nos deja marcar/desmarcar las opciones
        modelo[fila][3] = not modelo[fila][3]

    def on_celdaDireccion_edited(self, control, fila, texto, modelo):  # podemos editar la celda de direcciones
        modelo[fila][1] = texto

    def on_btnNovo_clicked(self, boton, modelo):
        modCat = self.cmbCategoria.get_model()
        indice = self.cmbCategoria.get_active_iter()
        modelo.append([self.txtHotel.get_text(),
                       self.txtDireccion.get_text(),
                       float(self.txtOcupacion.get_text()),
                       self.chkMascota.get_active(),
                       modCat[indice][1],
                       modCat[indice][0]])  # indice y columna

    def on_celdaCombo_changed(self, control, posicion, indice, modelo, modeloCat):
        modelo[int(posicion)][5] = modeloCat[indice][0]
        # modelo[int(posicion)][4] = modeloCat[indice][1]
        print(modelo[int(posicion)][5], str(modelo [int(posicion)][4]))

    def on_vista_changed(self, seleccion):
        (modelo, punteiro) = seleccion.get_selected()
        self.txtHotel.set_text(modelo[punteiro][0])
        self.txtDireccion.set_text(modelo[punteiro][1])
        self.txtOcupacion.set_text(str(modelo[punteiro][2]))
        if modelo[punteiro][3]:
            self.chkMascota.set_active(True)
        else:
            self.chkMascota.set_active(False)
        print(modelo[punteiro][4]-1)
        self.cmbCategoria.set_active(modelo[punteiro][4]-1)
        # print(modelo[punteiro][0], modelo[punteiro][1], modelo[punteiro][2])

    def ocupacion(self, modelo, punteiro, porcentaxeOcupacion):
        if self.filtradoOcupacion is None or self.filtradoOcupacion is False:
            return True
        else:
            return self.modelo[punteiro][2] > porcentaxeOcupacion

    def on_chkFiltro_toggled(self, control, modeloFiltrado):
        self.filtradoOcupacion = not self.filtradoOcupacion
        modeloFiltrado.refilter()

    def ordeAlfabetico(modelo,fila1,fila2,datosUsuario):
        #DEVUELVE 2 VALORES, EL SEGUNDO NO NOS IMPORTA POR ESO LO GUARDAMS EN UNA BARRA BAJA
        columna_ordear, _ = modelo.get_sort_column_id()
        valor1 = modelo.get_value(fila1,columna_ordear)
        valor2 = modelo.get_value(fila2,columna_ordear)

        if valor1 < valor2:
            return -1
        elif valor1 == valor2:
            return 0
        else:
            return 1

"""
if __name__ == "__main__":
    Fiestra()
    Gtk.main()