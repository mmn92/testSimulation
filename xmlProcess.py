#This file will gather the output files (.xml) from the simulations done with
#Traffic Lights
from xml.etree.ElementTree import ElementTree
import matplotlib.pyplot as myPlot
import numpy as np

xmlFile = "trafficLight.xml"
xmlFile2 = "trafficLightQ.xml"

###############################################################################
durationOutput1 = "durationOutputTL1.txt"
queueOutput1 = "queueOutputTL1.txt"

durationOutput2 = "durationOutputTL2.txt"
queueOutput2 = "queueOutputTL2.txt"

durationOutput3 = "durationOutputTL3.txt"
queueOutput3 = "queueOutputTL3.txt"

durationOutput4 = "durationOutputTL4.txt"
queueOutput4 = "queueOutputTL4.txt"
###############################################################################

fp1 = open(durationOutput1, "a+")
fp1Q = open(queueOutput1, "a+")

fp2 = open(durationOutput2, "a+")
fp2Q = open(queueOutput2, "a+")

fp3 = open(durationOutput3, "a+")
fp3Q = open(queueOutput3, "a+")

fp4 = open(durationOutput4, "a+")
fp4Q = open(queueOutput4, "a+")

###############################################################################

tree = ElementTree()
tree.parse(xmlFile)
root = tree.getroot()

tree2 = ElementTree()
tree2.parse(xmlFile2)
root2 = tree2.getroot()

print(root.tag, " | ",root2.tag)
print("")

###############################################################################
#Scans the .XML file to find and allocate the desired info in the arrays
#Each edge has a separate file
for child in root:
    if child.get('departLane') == "1to0_0":
        fp1.write("%s\n" % child.get('duration'))
    if child.get('departLane') == "2to0_0":
        fp2.write("%s\n" % child.get('duration'))
    if child.get('departLane') == "3to0_0":
        fp3.write("%s\n" % child.get('duration'))
    if child.get('departLane') == "4to0_0":
        fp4.write("%s\n" % child.get('duration'))

for child2 in root2.findall(".//lane[@queueing_length]"):
    if child2.get('id') == "1to0_0":
        fp1Q.write("%s\n" % child2.get('queueing_length'))
    if child2.get('id') == "2to0_0":
        fp2Q.write("%s\n" % child2.get('queueing_length'))
    if child2.get('id') == "3to0_0":
        fp3Q.write("%s\n" % child2.get('queueing_length'))
    if child2.get('id') == "4to0_0":
        fp4Q.write("%s\n" % child2.get('queueing_length'))
###############################################################################

fp1.close()
fp2.close()
fp3.close()
fp4.close()

fp1Q.close()
fp2Q.close()
fp3Q.close()
fp4Q.close()

###############################################################################

print("\nEnd")
