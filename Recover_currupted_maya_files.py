import maya.cmds as mc
#selected the ctrls on which animation keys are missing and run this Script
selection = mc.ls(sl = True)

for object in selection:
    attributes = mc.listAttr(object, k = True)
    for attr in attributes:
        try:
            mc.connectAttr(object.split(":")[1]+"_"+attr+".output",object+"."+attr, f = True)
        except:
            pass