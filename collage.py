
import os
from collage.gui import main


if __name__ == '__main__':
    if not os.path.exists(os.path.join(os.path.expanduser("~"), ".collage")):
        os.mkdir(os.path.join(os.path.expanduser("~"), ".collage"))
    home = os.path.join(os.path.expanduser("~"), ".collage")
    glade_gui = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "collage/dat/glade/main.glade")
    main.Collage(glade_gui, home).run()
