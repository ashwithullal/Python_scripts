import maya.cmds as mc
import glob
from functools import partial

class Asset_Loader():
    WINDOW_NAME = "ASSET_LOADER 1.0"

    def __init__(self,*args):

        if mc.window(self.WINDOW_NAME, query= True, exists = True):
            mc.deleteUI(self.WINDOW_NAME, window = True)
        self.window = mc.window(self.WINDOW_NAME, t = "Asset_loader", s = False, h = 100, w = 300)
        mc.columnLayout()
        self.assets = mc.textScrollList("Scroll_List", numberOfRows = 30 , w = 300 , allowMultiSelection = True)
        mc.button("LOAD", command = partial(self.load_assets))
        mc.showWindow(self.WINDOW_NAME)

        self.Asset_Name_Path = {}
        self.text_scroll_List_populate(*args)

    def path(self):
        #enter path here in this format,
        # enter multiple path in the list if u have assets in many folders
        #eg [r"D:\\assets\\CHARACTERS\\MAYA\\*.ma",r"D:\\assets\\PROPS\\MAYA\\*.ma",r"D:\\assets\\SETS\\MAYA\\*.ma"]
        self.asset_path = [r"D:\\assets\\CHARACTERS\\MAYA\\*.ma"]
        return self.asset_path

    def text_scroll_list_populate(self,*args):
        self.Asset_Name_Path = {}
        file_path = self.path()
        for elements in file_path:
            for files in glob.glob(elements):
                maya_file = files.split("\\")[-1]
                mc.textScrollList(self.assets,edit = True, append = maya_file)
                self.Asset_Name_Path[maya_file] = files

    def load_assets(self,*args):
        scroll_list_selection = mc.textScrollList(self.assets,query = True, si = True)
        for object in scroll_list_selection:
            mc.file(self.Asset_Name_Path[object], r = True)
            print "Loading>>>>>>>>>>>>>" + object

if __name__ == "__main__":
    asset_loader_window = Asset_Loader()