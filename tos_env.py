import numpy as np
import time
import sys
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk

class Tos(tk.TK, object):
    def __init__(self):
        print ('Initialize the environment.')
        # do something
    def build_tos(self):
        print ('Build tos.')
        # do something
    def reset(self):
        print ('Reset.')
        # do something
    def step(self, action):
        print ('Step.')
        # do something
    def render(self):
        print ('Render.')
        # do something
