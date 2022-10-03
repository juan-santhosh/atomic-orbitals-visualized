import os
#from math import pi, sin, cos

from periodic_table import periodic_table_list
import atomic_orbitals

from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import *
from direct.task import Task

from panda3d.core import TransparencyAttrib, WindowProperties


class bcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'
    

RED = (0.75, 0.0, 0.0, 1.0)
YELLOW = (0.75, 0.75, 0.0, 1.0)
BLUE = (0.0, 0.0, 0.25, 0.75)

TRANSPARENCY_FACTOR = 0.075

os.system('clear')
atomInput = int(input("What is the atomic number of the atom you want to look up ? \n> "))
selected_atom = atomInput

atom_reference = periodic_table_list[selected_atom - 1]


class AtomLookup(ShowBase):
    def __init__(self):

        ShowBase.__init__(self)

        nucleus = self.loader.loadModel("models/spherical_nucleus_dummy_model.fbx")
        nucleus.reparentTo(self.render)
        self.correct_render_order(nucleus)
        nucleus.setScale(0.05, 0.05, 0.05)

        selected_subshell_types = ["s", "p", "d"]
        electrons = atomic_orbitals.calc_orbitals(selected_atom)

        print(
            f"""
            {bcolors.BOLD}Name:{bcolors.ENDC} {atom_reference.name}
            {bcolors.BOLD}Chemical Symbol:{bcolors.ENDC} {atom_reference.chemical_symbol}
            {bcolors.BOLD}Atomic Number:{bcolors.ENDC} {atom_reference.atomic_number}
            {bcolors.BOLD}Atomic Mass:{bcolors.ENDC} {atom_reference.mass_number}
            {bcolors.BOLD}Electron Configuration:{bcolors.ENDC} {atom_reference.electron_configuration}
            """
        )

        # print(f"{electrons}\n")

        print(f"{bcolors.UNDERLINE}ZOOM OUT WITH RIGHT-CLICK AND DRAG TO SEE ATOM")
        print("LEFT-CLICK AND DRAG TO PAN VIEW")
        print(f"MIDDLE MOUSE CLICK TO ROTATE VIEW \n{bcolors.ENDC}")

        for i in range(len(electrons)):
            scale_value = int(electrons[i][0]) / 10

            if "s" in electrons[i]:
                s_orbital = self.loader.loadModel("models/s_orbital.fbx")
                
                if "s" in selected_subshell_types:
                    s_orbital.reparentTo(self.render)
                    self.correct_render_order(s_orbital)
                    self.display_orbitals(s_orbital, scale_value * 3, RED, TRANSPARENCY_FACTOR)

            if "p" in electrons[i]:
                p_orbital = self.loader.loadModel("models/p_orbital_scale.fbx")

                if "x" in electrons[i]:
                    p_orbital.setP(p_orbital, 90)

                if "z" in electrons[i]:
                    p_orbital.setH(p_orbital, 90)

                if "p" in selected_subshell_types:
                    p_orbital.reparentTo(self.render)
                    self.correct_render_order(p_orbital)
                    self.display_orbitals(p_orbital, scale_value * 2, YELLOW, TRANSPARENCY_FACTOR)
            
            if "d" in electrons[i]:
                d_orbital = self.loader.loadModel("models/d_orbital_scale.fbx")
                dz2_orbital = self.loader.loadModel("models/d_z^2_orbital_scale.fbx")

                if "yz" in electrons[i]:
                    d_orbital.setH(d_orbital, 90)

                if "xy" in electrons[i]:
                    d_orbital.setR(d_orbital, 90)
                
                if "x^2-y^2" in electrons[i]:
                    d_orbital.setH(d_orbital, 45)
                    d_orbital.setR(d_orbital, 90)

                if "z^2" in electrons[i]:
                    dz2_orbital.setP(dz2_orbital, 90)

                if "d" in selected_subshell_types:
                    d_orbital.reparentTo(self.render)
                    self.correct_render_order(d_orbital)
                    self.display_orbitals(d_orbital, scale_value * 2, BLUE, TRANSPARENCY_FACTOR)

                    if "z^2" in electrons[i]:
                        dz2_orbital.reparentTo(self.render)
                        self.correct_render_order(dz2_orbital)
                        self.display_orbitals(dz2_orbital, scale_value * 2, BLUE, TRANSPARENCY_FACTOR)
                
            
        # s_button = DirectButton(text="S", pos=(0.95, 0, 0.85), scale=.1, command=show_hide_s_subshell)
        # p_button = DirectButton(text="P", pos=(1.05, 0, 0.85), scale=.1, command=show_hide_p_subshell)
        # d_button = DirectButton(text="D", pos=(1.15, 0, 0.85), scale=.1, command=show_hide_d_subshell)

        # self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")
        # self.disableMouse()
        # self.camera.setPos(0, -200, 0)

    # def spinCameraTask(self, task):
    #     angleDegrees = task.time * 12.0
    #     angleRadians = angleDegrees * (pi / 180.0)
    #     self.camera.setPos(400 * sin(angleRadians), -400 * cos(angleRadians), 3)
    #     self.camera.setHpr(angleDegrees, 0, 0)

    #     return Task.cont

    def display_orbitals(self, orbital, scale, colour, transparency):
        orbital.setScale(scale)
        orbital.setColor(colour)
        orbital.setTransparency(TransparencyAttrib.MAlpha)
        orbital.setAlphaScale(transparency)
        
    def correct_render_order(self, orbital):
        orbital.setBin("fixed", 0)
        orbital.setDepthTest(False)
        orbital.setDepthWrite(False)
    

app = AtomLookup()

props = WindowProperties()
props.setTitle(f"Unhybridized {atom_reference.name} Atom")
app.win.requestProperties(props)

app.run()
