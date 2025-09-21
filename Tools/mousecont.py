from pynput import mouse
def mouse_control():
    m=mouse.Controller();
    m.position=(50,50) # in pixel it will move the mouse pointer...
mouse_control()