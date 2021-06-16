import maya.cmds as mc

# listing all the unknown plugin in the scene file
unknown_plugins = mc.unknownPlugin(q=True, l=True)
for plugin in unknown_plugins:
    mc.unknownPlugin(plugin, remove=True)
    print("deleted  :" + plugin)

# Use option saveAs to make a copy of the file and save it.
# Changes will be reflected in the new file.
