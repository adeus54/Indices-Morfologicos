import arcpy
import pythonaddins
import os

class IndiceElongacion(object):
    """Implementation for geologia_addin.btnCalcularElongacion (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # name of toolbox without tbx extension
        toolboxName = "HerramientasG"

        # name of tool to be executed
        toolName = "CalcularElongacion"

        # create string with path to toolbox
        toolboxPath = os.path.join(os.path.dirname(__file__), toolboxName + ".tbx")

        # call geoprocessing tool
        pythonaddins.GPToolDialog(toolboxPath, toolName)
        
        pass

class IndiceGradiente(object):
    """Implementation for geologia_addin.btnGradiente (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # name of toolbox without tbx extension
        toolboxName = "HerramientasG"

        # name of tool to be executed
        toolName = "CalcularGradiente"

        # create string with path to toolbox
        toolboxPath = os.path.join(os.path.dirname(__file__), toolboxName + ".tbx")

        # call geoprocessing tool
        pythonaddins.GPToolDialog(toolboxPath, toolName)
        pass