from xml.etree.ElementTree import ElementTree
import matplotlib.pyplot as myPlot
import numpy as np

xmlFile = "tripinfo.xml"
xmlFile2 = "trafficLightQ.xml"

tree = ElementTree()
tree.parse(xmlFile)
root = tree.getroot()

tree2 = ElementTree()
tree2.parse(xmlFile2)
root2 = tree2.getroot()

print(root.tag, " | ",root2.tag)
print("")

duration1 = []
duration2 = []
duration3 = []
duration4 = []

queue1 = []
queue2 = []
queue3 = []
queue4 = []

###############################################################################
#Scans the XML file to find and allocate the desired info in the arrays
#Adapt this piece of code to save the values in a file, after every simulation
#This way, data from many simulations can be analyzed together
for child in root:
    if child.get('departLane') == "1to0_0":
        duration1.append((float)(child.get('duration')))
    if child.get('departLane') == "2to0_0":
        duration2.append((float)(child.get('duration')))
    if child.get('departLane') == "3to0_0":
        duration3.append((float)(child.get('duration')))
    if child.get('departLane') == "4to0_0":
        duration4.append((float)(child.get('duration')))

for child2 in root2.findall(".//lane[@queueing_length]"):
    if child2.get('id') == "1to0_0":
        queue1.append((float)(child2.get('queueing_length')))
    if child2.get('id') == "2to0_0":
        queue2.append((float)(child2.get('queueing_length')))
    if child2.get('id') == "3to0_0":
        queue3.append((float)(child2.get('queueing_length')))
    if child2.get('id') == "4to0_0":
        queue4.append((float)(child2.get('queueing_length')))
###############################################################################

u1 = np.asarray(duration1)
u2 = np.asarray(duration2)
u3 = np.asarray(duration3)
u4 = np.asarray(duration4)

y1 = np.asarray(queue1)
y2 = np.asarray(queue2)
y3 = np.asarray(queue3)
y4 = np.asarray(queue4)

#m0 contains the mean values of each u-array
m0 = []
m0.append(np.mean(u1))
m0.append(np.mean(u2))
m0.append(np.mean(u3))
m0.append(np.mean(u4))

#m1 contains the mean values of each y-array
m1 = []
m1.append(np.mean(y1))
m1.append(np.mean(y2))
m1.append(np.mean(y3))
m1.append(np.mean(y4))

print("Mean values from the simulation:\nTrip time | Queue length")
for i,j in zip(m0,m1):
    print(m0.index(i)+1,"%6.0f" % i, " - ","%6.0f" % j)
print("Total average:\n  %6.0f" % np.mean(m0), " - ", "%6.0f" % np.mean(m1))

########################################################################
#Plotting trip duration
myPlot.figure(1)

#Data1
myPlot.subplot(221)
myPlot.plot(u1.flatten())
myPlot.title("Caminho 1")

#Data2
myPlot.subplot(222)
myPlot.plot(u2.flatten())
myPlot.title("Caminho 2")

#Data3
myPlot.subplot(223)
myPlot.plot(u3.flatten())
myPlot.title("Caminho 3")

#Data4
myPlot.subplot(224)
myPlot.plot(u4.flatten())
myPlot.title("Caminho 4")

myPlot.show()

########################################################################
#Plotting queue duration

myPlot.figure(2)

#Data1
myPlot.subplot(221)
myPlot.plot(y1)
myPlot.title("Caminho 1")

#Data2
myPlot.subplot(222)
myPlot.plot(y2)
myPlot.title("Caminho 2")

#Data3
myPlot.subplot(223)
myPlot.plot(y3)
myPlot.title("Caminho 3")

#Data4
myPlot.subplot(224)
myPlot.plot(y4)
myPlot.title("Caminho 4")

myPlot.show()
########################################################################

print("\nEnd")
