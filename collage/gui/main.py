
from gi.repository import Gtk
from collage.obj import Library
from collage.gui import PhotoStack


class Collage (object):

    def __init__(self, glade_gui, home):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_gui)
        self.builder.connect_signals(self)
        self.library = Library(home)

    def run(self):
        Gtk.main()

    def on_quit(self, widget):
        Gtk.main_quit()
