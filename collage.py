#!/usr/bin/env python3

import os
from collage.gui import Collage


def get_home():
    '''
    Create a home directory for collage in the user's
    home if it doesn't already exist.

    '''
    if not os.path.exists(os.path.join(os.path.expanduser("~"), ".collage")):
        os.mkdir(os.path.join(os.path.expanduser("~"), ".collage"))
    return os.path.join(os.path.expanduser("~"), ".collage")

if __name__ == '__main__':
    glade_gui = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "collage/dat/glade/main.glade")
    Collage(glade_gui, get_home()).run()
