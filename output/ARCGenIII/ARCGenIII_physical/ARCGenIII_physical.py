from ARCGenIIIPORIS import *

class ARCGenIII_physical(ARCGenIIIPORIS):
    # Go to ARCGengIIIPORIS.py, navigate to the ##### Action triggers ##### section
    # which is normally at the bottom of the class, and copy here the methods 
    # to start overriding them, in order to convert the virtual device into a physical one
    # Once this class has any content, remove the pass clause

    pass


thismodel = ARCGenIII_physical(1)

thismodel.getRoot().setNodeAttribute("uno","dos",True)

print("Let's test our model ",thismodel.getRoot().getName())
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("Current binning value is",thismodel.prBinning.getSelectedValue().getName())

thismodel.sysARCGenIII.selectMode(thismodel.mdARCGenIIIMode_Real)
print("Current mode is ",thismodel.getRoot().getSelectedMode().getName())
print("After change, Current binning value is",thismodel.prBinning.getSelectedValue().getName())

dom = thismodel.toXML()
pretty_xml_as_string = dom.toprettyxml()
# print(pretty_xml_as_string) 

print("Let's parse")
othermodel = PORISDoc(2)
othermodel.fromXML(dom)

print("Let's dump")
dom2 = othermodel.toXML()
pretty_xml_as_string = dom2.toprettyxml()
print(pretty_xml_as_string) 