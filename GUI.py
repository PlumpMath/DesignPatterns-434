__author__ = 'Toshiba'

from tkinter import *
from tkinter import ttk

class GUI:

    def __init__(self, master):
        self.frame_header = ttk.Frame(master, width = 50, height = 300, relief = SUNKEN)
        self.frame_header.grid(row =0, column =0, stick = 'n', rowspan = 2, padx = 10, pady = 10, ipady = 10)
        self.image = PhotoImage(file = 'download_1_.png')
        ttk.Label(self.frame_header, text = "Image Workflow Control").grid(row =0, column = 0, padx = 10, pady = 10)
        ttk.Label(self.frame_header, image = self.image).grid(row =1, column = 0, padx = 10, pady = 10)
        ttk.Label(self.frame_header, wraplength = 200, text = "Normalized difference vegetation index(NDVI) prepared for a red "
                                            "and infrared channel from a scene in semi Arid Australia").grid(row = 2, column = 0)


        self.frame_setDirectory = ttk.Frame(master, width = 200, height = 300, relief = SUNKEN)
        self.frame_setDirectory.grid(row = 2, column = 0, padx = 10, pady = 10, stick = 'n', ipady = 10)
        ttk.Label(self.frame_setDirectory, text = "Parameters [path] for Set Directory").grid(row = 0, column = 0, padx = 10, pady = 10)
        self.entry_setDirectory = ttk.Entry(self.frame_setDirectory, width = 24).grid(row = 1, column = 0)


        self.frame_selectChannels = ttk.Frame(master, width = 200, height = 300, relief = SUNKEN)
        self.frame_selectChannels.grid(row = 3, column = 0, padx = 10, pady = 10, stick = 'n')
        ttk.Label(self.frame_selectChannels, text = "Parameters [path] for Select channel").grid(row = 0, column = 0, columnspan= 2)
        checkbuttonRed = ttk.Checkbutton(self.frame_selectChannels, text = 'RED').grid(row = 1, column = 0, sticky= 'w')
        checkbuttonBlue = ttk.Checkbutton(self.frame_selectChannels, text = 'BLUE').grid(row = 1, column = 1, sticky= 'w')
        checkbuttonGreen = ttk.Checkbutton(self.frame_selectChannels, text = 'GREEN').grid(row = 2, column = 0, sticky= 'w')
        checkbuttonInfraRed = ttk.Checkbutton(self.frame_selectChannels, text = 'INFRARED').grid(row = 2, column = 1, sticky= 'w')


        self.frame_window = ttk.Frame(master, width = 200, height = 300, relief = SUNKEN)
        self.frame_window.grid(row = 0, column = 1, stick = 'n', padx = 10, pady = 10, ipady = 10)
        ttk.Label(self.frame_window, text = "Parameters [path] for Window").grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        ttk.Label(self.frame_window, text = "Min X").grid(row = 1, column = 0)
        self.entry_setDirectory = ttk.Entry(self.frame_window, width = 10).grid(row = 1, column = 1)
        ttk.Label(self.frame_window, text = "Min Y").grid(row = 2, column = 0)
        self.entry_setDirectory = ttk.Entry(self.frame_window, width = 10).grid(row = 2, column = 1)
        ttk.Label(self.frame_window, text = "Max X").grid(row = 3, column = 0)
        self.entry_setDirectory = ttk.Entry(self.frame_window, width = 10).grid(row = 3, column = 1)
        ttk.Label(self.frame_window, text = "Max Y").grid(row = 4, column = 0)
        self.entry_setDirectory = ttk.Entry(self.frame_window, width = 10).grid(row = 4, column = 1)


        self.frame_setDirectory = ttk.Frame(master, width = 200, height = 300, relief = SUNKEN)
        self.frame_setDirectory.grid(row = 1, column = 1, stick = 'n', padx = 10, pady = 10, ipady = 10)
        ttk.Label(self.frame_setDirectory, text = "Data Compression [PCA] and [CCA]").grid(row = 0, column = 0, columnspan =3, padx = 10, pady = 10)
        ttk.Label(self.frame_setDirectory, text = "Select first ").grid(row = 1, column = 0)
        Spinbox(self.frame_setDirectory, from_ = 0, to= 10, width = 3).grid(row = 1, column = 1)
        ttk.Label(self.frame_setDirectory, text = " PCA components").grid(row = 1, column = 2)
        ttk.Label(self.frame_setDirectory, text = "Select first ").grid(row = 2, column = 0)
        Spinbox(self.frame_setDirectory, from_ = 0, to= 10, width = 3).grid(row = 2, column = 1)
        ttk.Label(self.frame_setDirectory, text = " CCA components").grid(row = 2, column = 2)


        self.frame_superviseDirectory = ttk.Frame(master, width = 200, height = 300, relief = SUNKEN)
        self.frame_superviseDirectory.grid(row = 2, column = 1, rowspan = 2, stick = 'n', padx = 10, pady = 10, ipady = 10)
        ttk.Label(self.frame_superviseDirectory, text = "Supervised Classification Parameters").grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Label(self.frame_superviseDirectory, text = "Training Shappette for [make signature]").grid(row = 1, column = 0, padx = 10, pady = 10)
        self.entry_setDirectory1 = ttk.Entry(self.frame_superviseDirectory, width = 24).grid(row = 2, column = 0)
        ttk.Label(self.frame_superviseDirectory, wraplength = 200, text = "Training site class in ascending order of ID (e.g 1st Forest, 2nd Water)").grid(row = 3, column = 0)
        self.textClassificationComments = Text(self.frame_superviseDirectory, width = 15, height = 8).grid(row = 4, column = 0)


        self.frame_PickMast = ttk.Frame(master, width = 200, height = 300, relief = SUNKEN)
        self.frame_PickMast.grid(row = 0, column = 2, stick = 'n', padx = 10, pady = 10, ipady = 10)
        ttk.Label(self.frame_PickMast, wraplength = 200, text = "Parameters [files] for the land cover assesstment [pick mass]component").grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        ttk.Label(self.frame_PickMast, text = "Thematic layer 1").grid(row = 1, column = 0)
        self.entry_setDirectory = ttk.Entry(self.frame_PickMast, width = 10).grid(row = 1, column = 1)
        ttk.Label(self.frame_PickMast, text = "Thematic layer 2").grid(row = 2, column = 0)
        self.entry_setDirectory = ttk.Entry(self.frame_PickMast, width = 10).grid(row = 2, column = 1)
        ttk.Label(self.frame_PickMast, text = "Thematic layer 3").grid(row = 3, column = 0)
        self.entry_setDirectory = ttk.Entry(self.frame_PickMast, width = 10).grid(row = 3, column = 1)
        ttk.Label(self.frame_PickMast, text = "Thematic layer 4").grid(row = 4, column = 0)
        self.entry_setDirectory = ttk.Entry(self.frame_PickMast, width = 10).grid(row = 4, column = 1)


        self.custom = ttk.Frame(master, width = 200, height = 300, relief = SUNKEN)
        self.custom.grid(row = 1, column = 2, rowspan = 3, stick = 'n', padx = 10, pady = 10, ipady = 10)
        ttk.Label(self.custom, text = "Build custom workflow ").grid(row = 0, column = 0, padx = 10, pady = 10)
        ttk.Label(self.custom, wraplength = 200,  text = "Select in order of execution. Routine functions (set directory, image cropping, create spectral signatures, "
                                      " import training test site data, display export, assess cover, error message analysis are performed automatically ").grid(row = 1, column = 0)


        self.modules = ttk.Frame(self.custom)
        self.modules.grid(row = 2, column = 0, padx = 10, pady = 10, ipadx = 10, ipady = 10)
        ttk.Label(self.modules, text = "Modules ").grid(row = 0,columnspan = 2, column = 0, padx = 10, pady = 10)
        ttk.Label(self.modules, text = "Available \n components ").grid(row = 1, column = 0)
        ttk.Label(self.modules, text = "Selected \n Components ").grid(row = 1, column = 1)
        self.textClassificationComments1 = Text(self.modules, width = 15, height = 10).grid(row = 2, column = 0, rowspan = 6, padx = 10, pady = 10)
        Spinbox(self.modules, from_ = 0, to= 10, width = 8).grid(row = 2, column = 1)
        ttk.Button(self.modules, text = 'Add').grid(row = 3, column = 1)
        ttk.Button(self.modules, text = 'Remove').grid(row = 4, column = 1)
        ttk.Button(self.modules, text = 'Clear').grid(row = 5, column = 1)
        ttk.Button(self.modules, text = 'Load').grid(row = 6, column = 1)
        ttk.Button(self.modules, text = 'Save').grid(row = 7, column = 1)


        self.frame_workflow = ttk.Frame(master, width = 200, height = 300, relief = SUNKEN)
        self.frame_workflow.grid(row = 0, column = 3, rowspan = 4, stick = 'n', padx = 10, pady = 10, ipady = 10)
        ttk.Label(self.frame_workflow, text = "Workflows ").grid(row = 1, column = 0, padx = 10, pady = 10)
        workflow = StringVar()
        ttk.Radiobutton(self.frame_workflow, text = 'Unsupervised [k means]',variable = workflow, value = 'Unsupervised [k means]').grid(row =2 , column = 0, sticky= 'w', padx = 10)
        ttk.Radiobutton(self.frame_workflow, text = 'Supervised [multiple + error messages]' ,variable = workflow, value ='Supervised [multiple + error messages]').grid(row =3 , column = 0, sticky = 'w', padx = 10)
        ttk.Radiobutton(self.frame_workflow, text = 'Land cover assesstment' ,variable = workflow, value = 'Land cover assesstment').grid(row =4 , column = 0, sticky = 'w', padx = 10)
        ttk.Radiobutton(self.frame_workflow, text = 'Customized workflow' ,variable = workflow, value = 'Customized workflow').grid(row =5 , column = 0, sticky = 'w', padx = 10)
        ttk.Radiobutton(self.frame_workflow, text = 'Deserialize load from xml ' ,variable = workflow, value ='Deserialize load from xml ').grid(row =6 , column = 0, sticky = 'w', padx = 10)
        self.frameSelect = ttk.Frame(self.frame_workflow)
        self.frameSelect.grid(row = 7, column = 0)
        ttk.Label(self.frameSelect, text = "Select or \n enter the ").grid(row = 0, column = 0)
        xml = StringVar()
        combobox = ttk.Combobox(self.frameSelect, width = 9, textvariable = xml).grid(row = 0, column = 1)
        ttk.Label(self.frameSelect, text = " XML").grid(row = 0, column = 2)
        checkbuttonRed = ttk.Checkbutton(self.frame_workflow, text = 'Enable component step reporting ').grid(row = 8, column = 0)

        self.framebuttons = ttk.Frame(self.frame_workflow)
        self.framebuttons.grid(row = 9, column = 0)
        ttk.Label(self.framebuttons, text = "1 ").grid(row = 0, column = 0)
        ttk.Button(self.framebuttons, text = 'Update Parameters').grid(row = 0, column = 1, sticky= 'w')
        ttk.Label(self.framebuttons, text = "2 ").grid(row = 1, column = 0)
        ttk.Button(self.framebuttons, text = 'Validate Parameters').grid(row = 1, column = 1, sticky= 'w')
        ttk.Label(self.framebuttons, text = "3 ").grid(row = 2, column = 0)
        ttk.Button(self.framebuttons, text = 'View workflow description (opt)').grid(row = 2, column = 1, sticky= 'w')
        ttk.Label(self.framebuttons, text = "4 ").grid(row = 3, column = 0)
        ttk.Button(self.framebuttons, text = 'Execute workflow').grid(row = 3, column = 1, sticky= 'w')
        ttk.Label(self.framebuttons, text = "5 ").grid(row = 4, column = 0)
        ttk.Button(self.framebuttons, text = 'Report Workflow (transform XML').grid(row = 4, column = 1, sticky= 'w')
        ttk.Label(self.framebuttons, text = "6 ").grid(row = 5, column = 0)
        ttk.Button(self.framebuttons, text = 'Exit Application').grid(row = 5, column = 1, sticky= 'w')



def main():

    root = Tk()
    GUI1 = GUI(root)
    root.mainloop()

if __name__ == "__main__": main()
