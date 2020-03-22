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

    def __init__(self):
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
                celda.connect("toggled", self.on_celdaCheck_toggled, self.modeloP)
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
        self.lblFactura = Gtk.Label("Seleccione os produtos na pestaña de produtos e logo o cliente o que quere facer a factura")
        self.btnFactura = Gtk.Button(label="Factura")
        self.btnVolver2 = Gtk.Button(label = "Volver")

        #COMBO PARA LA FACTURA RECOGE DNI
        self.cmbCliente = Gtk.ComboBox()
        cli = Gtk.ListStore(str)
        datos = MethodsBD.selectTablaClientes()
        self.clientes = []

        for clientes in datos:
            cli.append([clientes[0]])

        self.cmbCliente.set_model(cli)
        celdaTexto = Gtk.CellRendererText()
        self.cmbCliente.pack_start(celdaTexto,True)
        self.cmbCliente.add_attribute(celdaTexto, "text", 0)
        self.cmbCliente.set_active(0)

        #VISTA DE PRODUCTOS PARA LA FACTURA

        self.columnasP2 = ["ID", "Produto", "Precio(€)"]
        self.modelo2 = Gtk.ListStore(int, str, int)
        self.vista2 = Gtk.TreeView(model=self.modelo2)
        self.vista2.set_hexpand(True)
        self. vista2.set_vexpand(True)

        self.produtos2 = []

        for i in range(len(self.columnasP2)):
                celda2 = Gtk.CellRendererText()
                celda2.set_alignment(0.5, 0)
                self.columna2 = Gtk.TreeViewColumn(self.columnasP2[i], celda2, text=i)
                self.columna2.set_alignment(0.5)
                self.columna2.set_expand(True)
                self.vista2.append_column(self.columna2)


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
        self.btnFactura.connect("clicked", self.on_btnFactura_clicked)

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

            # OPCION AÑADIR

            idBDValid = self.idBDCheck(int(self.txtID.get_text()))

            if (idBDValid == False and self.txtID.get_text().isdigit() and self.txtProduto.get_text() != "" and self.txtPrecio.get_text().isdigit()):
                MethodsBD.insertTablaProdutos(int(self.txtID.get_text()),self.txtProduto.get_text(),int(self.txtPrecio.get_text()))
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                           "Produto añadido Correctamente")
                dialog.run()
                dialog.destroy()
                self.tablaProdutoRefresh()


            elif (self.txtID.get_text().isdigit() == False):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce unha ID válida")
                dialog.run()
                dialog.destroy()

            elif (self.txtProduto.get_text() == ""):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un nome válido")
                dialog.run()
                dialog.destroy()
            elif(idBDValid):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                        "El ID del producto ya se encuentra en la base de datos")
                dialog.run()
                dialog.destroy()

            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un precio válido")
                dialog.run()
                dialog.destroy()

        elif modAcc[indice][0] == 1:

            # OPCION MODIFICAR

            idBDValid = self.idBDCheck(int(self.txtID.get_text()))

            if (idBDValid and self.txtID.get_text().isdigit() and self.txtProduto.get_text() != "" and self.txtPrecio.get_text().isdigit()):
                MethodsBD.updateTablaProdutos(int(self.txtID.get_text()),self.txtProduto.get_text(),int(self.txtPrecio.get_text()))
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                           "Produto modificado Correctamente")
                dialog.run()
                dialog.destroy()
                self.tablaProdutoRefresh()


            elif (self.txtID.get_text().isdigit() == False):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce unha ID válida")
                dialog.run()
                dialog.destroy()

            elif (self.txtProduto.get_text() == ""):

                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un nome válido")
                dialog.run()
                dialog.destroy()
            elif (idBDValid == False):
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                        "El ID del producto no se encuentra en la base de datos")
                dialog.run()
                dialog.destroy()

            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.WARNING, Gtk.ButtonsType.OK,

                                           "Introduce un precio válido")
                dialog.run()
                dialog.destroy()
        elif modAcc[indice][0] == 2:

            #OPCION ELIMINAR

            idBDValid = self.idBDCheck(int(self.txtID.get_text()))

            if (idBDValid):
                MethodsBD.deleteTablaProductos(self.txtID.get_text())
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                        "Produto eliminado correctamente")
                dialog.run()
                dialog.destroy()
                self.tablaProdutoRefresh()
            else:
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                        "El ID del producto no se encuentra en la base de datos")
                dialog.run()
                dialog.destroy()

    def tablaProdutoRefresh(self):

        self.modeloP.clear()
        self.produtos = []
        produtosBD = MethodsBD.selectTablaProductos()
        for produto in produtosBD:
            self.produtos.append(
                [produto[0], produto[1], produto[2], False])

        for elemento in self.produtos:
            self.modeloP.append(elemento)

    def on_celdaCheck_toggled(self, control, fila, modelo):
        modelo[fila][3] = not modelo[fila][3]
        self.listaFactura()


    def listaFactura(self):
        self.modelo2.clear()
        self.produtos2 = []
        for produto in self.modeloP:
            if produto[3] == True:
                self.produtos2.append(
                    [produto[0], produto[1], produto[2]])
        for elemento in self.produtos2:
            self.modelo2.append(elemento)

    def idBDCheck(self, id):
        """Metodo que comprueba si la ID del GTKEntry está en la BD
            :param id: id del produto
            :return boolean: True o False en función del resultado.
        """

        produtosBD = MethodsBD.selectTablaProductos()
        for produto in produtosBD:
            if produto[0] == id:
                return True

        return False

    def on_btnFactura_clicked(self, boton):
        """Método que crea un pdf con la factura del cliente
            y productos seleccionados.
            :param boton: boton.
            :return: No devuelve ningún parámetro.
        """

        if self.produtos2 is not None:
            #Cogemos los datos a través del DNI del cliente

            modeldni = self.cmbCliente.get_model()
        dni = self.cmbCliente.get_active_iter()
        datosCli = MethodsBD.selectTablaClientesDni(modeldni[dni][0])
        cliente = []
        for cli in datosCli:
            cliente.append(["","","","",'Datos Cliente'])
            cliente.append(["","","",'DNI: ', cli[0]])
            cliente.append(["","","",'Nome: ', cli[1]])
            cliente.append(["","","",'Apelidos: ', cli[2]])
            cliente.append(["","","",'Direccion: ', cli[5],])
            cliente.append([""])

            #Hacemos el modelo para la tabla de la factura, los datos de productos ya lo tenemos recogidos en una lista

            data = []
            precioFinal = 0.0
            data.append(["ID", "Nome", "Precio"])
            for produto in self.produtos2:
                data.append([produto[0], produto[1], str(produto[2]) + " €"])
                precioFinal = precioFinal + produto[2]

            data.append(['', 'PRECIO TOTAL:', str(precioFinal) + " €"])

            # Creamos el PDF

            file = 'Factura' + cli[0] + '.pdf'
            diractual = os.getcwd()
            pdf = SimpleDocTemplate(diractual + "/" + file, pagesize=letter)

            # Agregamos datos del cliente

            datCli = Table(cliente, colWidths=50, rowHeights=15)
            numCols = len(cliente)
            datCli.setStyle(TableStyle([
                ('TEXTCOLOR', (0, 0), (4, numCols-1), colors.firebrick),

                ('ALIGN', (0, 0), (0, -1), 'LEFT'),
            ]))

            # Agregamos tabla de factura con los productos
            tablaFact = Table(data, colWidths=100, rowHeights=25)

            numCols = len(data)
            tablaFact.setStyle(TableStyle([
                ('TEXTCOLOR', (0, 0), (2, 0), colors.firebrick),

                ('TEXTCOLOR', (0, numCols - 1), (2, numCols - 1), colors.red),

                ('ALIGN', (0, 0), (0, -1), 'LEFT'),

                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

                ('BOX', (0, 0), (-1, numCols - 2), 1, colors.black),

                ('INNERGRID', (0, 0), (-1, numCols - 2), 0.5, colors.black)
            ]))



            # Añadimos los elementos al PDF
            elementos = []
            elementos.append(datCli)
            elementos.append(tablaFact)
            pdf.build(elementos)
            wb.open_new(diractual + "/" + file)
