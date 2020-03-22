
import gi

from src.Entrada import VentanaPrincipal

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# if __name__ == "__main__":
#VentanaPrincipal()
#     Gtk.main(
def main_func():
    VentanaPrincipal()
    Gtk.main()


main_func()