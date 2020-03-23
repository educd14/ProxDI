import gi
import os

from src import Entrada
from src.SqliteBD import MethodsBD

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table
from reportlab.platypus import TableStyle
import webbrowser as wb

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Fiestra(Gtk.Window):
    """Ventana de Xestión de Clientes.
            **Métodos:**
                - __init__
                - on_btnVolver_clicked
                - on_vista_changed
                - on_btnAplicar_clicked
                - tablaClienteRefresh
                - dniCheck
                - tlfCheck
                - sexCheck
                - dniBDCheck
                - on_btnGuardar_clicked
                - on_btnSalir_clicked
    """

    def __init__(self):
        """Inicializa la ventana de Gestión de Clientes con la interfaz.
        """

        Gtk.Window.__init__(self, title="Xestión de Clientes")
        self.set_default_size(600, 400)

        boxV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        #TABLA CLIENTES

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

        #Señales
        self.btnVolver.connect("clicked", self.on_btnVolver_clicked)
        self.btnAplicar.connect("clicked", self.on_btnAplicar_clicked)
        self.btnGuardar.connect("clicked", self.on_btnGuardar_clicked)
        self.connect("destroy", self.on_btnSalir_clicked)


    def on_btnVolver_clicked(self, boton):
        """Metodo que vuelve al formulario de inicio.
            :param widget: boton
            :return: No devuelve ningún parámetro.
        """
        Entrada.VentanaPrincipal().vEntrada.show_all()
        self.set_visible(False)

    def on_vista_changed(self, seleccion):
        """Metodo que al clickar en datos del TreeView se muestren en los entries
            :param seleccion: Datos seleccionados
            :return: No devuelve ningún parámetro.
        """
        (modelo, punteiro) = seleccion.get_selected()

        if punteiro is not None:

            self.txtDni.set_text(modelo[punteiro][0])
            self.txtNome.set_text(modelo[punteiro][1])
            self.txtApelido.set_text(modelo[punteiro][2])
            self.txtSexo.set_text((modelo[punteiro][3]))
            self.txtTelefono.set_text((modelo[punteiro][4]))
            self.txtDireccion.set_text((modelo[punteiro][5]))

    def on_btnAplicar_clicked(self, boton):
        """Metodo que según la opción del ComboBox, añade,
            modifica o elimina un valor de la tabla clientes.
            :param boton: boton
            :return: No devuelve ningún parámetro.
        """
        modAcc = self.cmbAccion.get_model()
        indice = self.cmbAccion.get_active_iter()


        if modAcc[indice][0] == 0:

            #OPCION AÑADIR

            dniValid = self.dniCheck(self.txtDni.get_text())
            sexValid = self.sexCheck(self.txtSexo.get_text())
            tlfValid = self.tlfCheck(self.txtTelefono.get_text())
            dniBDValid = self.dniBDCheck(self.txtDni.get_text())


            if (dniBDValid == False and dniValid and sexValid and tlfValid and self.txtNome.get_text() != "" and self.txtApelido.get_text() != "" and self.txtDireccion.get_text() != ""):
                MethodsBD.insertTablaClientes(self.txtDni.get_text(), self.txtNome.get_text(), self.txtApelido.get_text(), self.txtSexo.get_text(), self.txtTelefono.get_text(), self.txtDireccion.get_text())
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                           "Cliente añadido Correctamente")
                dialog.run()
                dialog.destroy()
                self.tablaClienteRefresh()


            elif (tlfValid == False):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un teléfono válido")
                dialog.run()
                dialog.destroy()

            elif (sexValid == False):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un sexo válido")
                dialog.run()
                dialog.destroy()

            elif(self.txtNome.get_text() == ""):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un nome válido")
                dialog.run()
                dialog.destroy()

            elif (self.txtApelido.get_text() == ""):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un apelido válido")
                dialog.run()
                dialog.destroy()

            elif (self.txtDireccion.get_text() == ""):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce unha direccion válida")
                dialog.run()
                dialog.destroy()

            elif (dniValid == False):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un DNI válido")
                dialog.run()
                dialog.destroy()
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "El DNI ya se encuentra en la Base de datos")
                dialog.run()
                dialog.destroy()

        elif modAcc[indice][0] == 1:

            #OPCION MODIFICAR

            dniValid = self.dniCheck(self.txtDni.get_text())
            sexValid = self.sexCheck(self.txtSexo.get_text())
            tlfValid = self.tlfCheck(self.txtTelefono.get_text())
            dniBDValid = self.dniBDCheck(self.txtDni.get_text())

            if (dniBDValid and dniValid and sexValid and tlfValid and self.txtNome.get_text() != "" and self.txtApelido.get_text() != "" and self.txtDireccion.get_text() != ""):
                        MethodsBD.updateTablaClientes(self.txtDni.get_text(), self.txtNome.get_text(), self.txtApelido.get_text(), self.txtSexo.get_text(), self.txtTelefono.get_text(), self.txtDireccion.get_text())
                        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                                   "Cliente modificado correctamente")
                        dialog.run()
                        dialog.destroy()
                        self.tablaClienteRefresh()
            elif (tlfValid == False):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                                   "Introduce un teléfono válido")
                dialog.run()
                dialog.destroy()

            elif (sexValid == False):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un sexo válido")
                dialog.run()
                dialog.destroy()

            elif (self.txtNome.get_text() == ""):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un nome válido")
                dialog.run()
                dialog.destroy()

            elif (self.txtApelido.get_text() == ""):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un apelido válido")
                dialog.run()
                dialog.destroy()

            elif (self.txtDireccion.get_text() == ""):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce unha direccion válida")
                dialog.run()
                dialog.destroy()

            elif (dniValid == False):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un DNI válido")
                dialog.run()
                dialog.destroy()
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "El DNI no se encuentra en la Base de datos")
                dialog.run()
                dialog.destroy()

        elif modAcc[indice][0] == 2:

            #OPCION ELIMINAR

            dniValid = self.dniCheck(self.txtDni.get_text())
            dniBDValid = self.dniBDCheck(self.txtDni.get_text())

            if (dniValid and dniBDValid):
                MethodsBD.deleteTablaClientes(self.txtDni.get_text())
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "Cliente eliminado correctamente")
                dialog.run()
                dialog.destroy()
                self.tablaClienteRefresh()
            elif (dniValid == False):
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "Introduzca un DNI correcto")
                dialog.run()
                dialog.destroy()
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                       "El DNI no se encuentra en la Base de datos")
                dialog.run()
                dialog.destroy()

    def tablaClienteRefresh(self):
        """Metodo actualiza la tabla clientes
            :param: No recibe parámetros.
            :return: No devuelve ningún parámetro.
        """

        self.modeloC.clear()
        self.clientes = []
        clientesBD = MethodsBD.selectTablaClientes()
        for cliente in clientesBD:
            self.clientes.append(
                [cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]])

        for elemento in self.clientes:
            self.modeloC.append(elemento)


    def dniCheck(self, dni):
        """Nos indica si un DNI es valido.
            :param dni: Dni de la persona.
            :return boolean: true o false en función del resultado.
        """

        if len(dni) == 9:
            try:
                if dni[8].isalpha():
                    return True
                else:
                    return False
            except:
                print("ERROR DNI")
                pass
        return False


    def tlfCheck(self, tlf):
        """Metodo que valida que el teléfono sea un número válido.
            :param tlf: tlf de la persona
            :return boolean: True o False en función del resultado.
        """

        if len(tlf) == 9:
            try:
                if tlf.isnumeric():
                    return True
                else:
                    return False
            except:
                print("ERROR TLF")
                pass
        return False

    def sexCheck(self, sex):
        """Metodo que valida que el sexo sea válido.
            :param sex: sexo de la persona
            :return boolean: True o False en función del resultado.
        """

        if len(sex) == 1:
            try:
                if sex == "M" or sex == "F":
                    return True
                else:
                    return False
            except:
                print("ERROR SEXO")
                pass
        return False

    def dniBDCheck(self, dni):
        """Metodo que comprueba si el DNI del GTKEntry esta en la BD.
            :param dni: dni de la persona.
            :return boolean: True o False en función del resultado.
        """

        clientesBD = MethodsBD.selectTablaClientes()
        for cliente in clientesBD:
            if cliente[0] == dni:
                return True

        return False

    def on_btnGuardar_clicked(self, boton):
        """Método que crea un pdf con la lista de clientes.
            :param boton: boton.
            :return: No devuelve ningún parámetro.
        """
        #Cogemos los datos

        data = []
        data.append(["DNI", "Nombre", "Apellidos", "Sexo", "Telefono", "Direccion"])
        clientes = MethodsBD.selectTablaClientes()
        for cliente in clientes:
            data.append([cliente[0], cliente[1], cliente[2], cliente[3], cliente[4], cliente[5]])

        # Creamos el PDF
        file = 'ListaClientes.pdf'
        diractual = os.getcwd()
        pdf = SimpleDocTemplate(diractual + "/" + file, pagesize=letter)

        # Creamos una tabla
        table = Table(data)
        elementos = []
        elementos.append(table)

        # Estilamos la tabla

        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.burlywood),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 20),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 15),
        ])
        table.setStyle(style)

        # Alternamos colores de las filas

        numCols = len(data)
        for i in range(1, numCols):
            if i % 2 == 0:
                bc = colors.lightgrey
            else:
                bc = colors.ghostwhite
            colorCol = TableStyle([('BACKGROUND', (0, i), (-1, i), bc)])
            table.setStyle(colorCol)

        # Añadimos bordes a la tabla

        bordes = TableStyle(
            [
                ('BOX', (0, 0), (-1, -1), 1, colors.black),
                ('LINEBEFORE', (0, 0), (-1, numCols), 1, colors.black),
                ('LINEABOVE', (0, 0), (-1, 1), 1, colors.black)
            ]
        )
        table.setStyle(bordes)
        pdf.build(elementos)
        wb.open_new(diractual + "/" + file)


    def on_btnSalir_clicked(self, boton):
        """Metodo para cerrar el programa
            :param boton: boton
            :return: No devuelve ningún parámetro.
        """
        exit(0)