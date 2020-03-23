Comandos linux env
******************
Para poder ejecutar el programa sin ningún problema necesitaremos ciertas librerías, en el siguiente
comando podréis instalar todas ellas.

::

    sudo apt install build-essential libcairo2-dev pkg-config python3-dev libgtk-3-dev glade python3-sphinx



Guía del Programa
*****************

La aplicación funciona en un entorno gŕafico de Gtk3.
Trata de una gestión de un local en el que, usando una Base de datos SQlite3, tenemos una lista de clientes
y productos del cual gracias a la libreria ReportLab podremos hacer un documento de los clientes o facturas.

Menú
----

Lo primero que encontramos es un menú donde podremos elegir dos opciones, la gestión de clientes
o los productos y servicios.

                .. image:: /src/Images/Menu.jpg

Xestión de Clientes
-------------------

En este formulario tendremos una lista de todos los clientes en nuestra base de datos,
podremos añadir, modificar o eliminar cualquier cliente introduciendo los valores y
seleccionando la accion deseada y aplicando en el botón.

                .. image:: /src/Images/cli.jpg

También tenemos la opción de guardar la lista entera de clientes en formato PDF.

                .. image:: /src/Images/cli2.jpg


Productos/Servicios
---------------------

En este formulario tendremos dos pestañas:

Productos
+++++++++

Aquí tendremos una lista de todos los productos en nuestra base de datos,
podremos añadir, modificar o eliminar cualquier producto introduciendo los valores y
seleccionando la accion deseada y aplicando en el botón.

Además tendremos la opción de seleccionar los productos que querramos usar para realizar una factura

                .. image:: /src/Images/prod.jpg

Servizos
++++++++

Aquí tendremos un servicio de facturación, se nos mostrará una lista de los productos que hemos
seleccionado anteriormente. En caso de no quedar muy claro y no ver ningun lista, hay una pequeña
indicación de lo que se debe hacer.

                .. image:: /src/Images/prod2.jpg

Luego tendremos la opción de elegir el DNI del cliente al que le haremos la factura, siempre recogiendolo
de nuestra base de datos, al pulsar el botón obtendremos un documento PDF con la factura del cliente.

                .. image:: /src/Images/prod3.jpg

