from xml.etree.ElementTree import ElementTree
import matplotlib.pyplot as myPlot
import numpy as np

xmlFile = "trafficLight.xml"
xmlFile2 = "trafficLightQ.xml"

########################################################################
durationOutput1 = "durationOutputTL1.txt"
queueOutput1 = "queueOutputTL1.txt"

durationOutput2 = "durationOutputTL2.txt"
queueOutput2 = "queueOutputTL2.txt"

durationOutput3 = "durationOutputTL3.txt"
queueOutput3 = "queueOutputTL3.txt"

durationOutput4 = "durationOutputTL4.txt"
queueOutput4 = "queueOutputTL4.txt"
########################################################################

fp1 = open(durationOutput1, "a+")
fp1Q = open(queueOutput1, "a+")

fp2 = open(durationOutput2, "a+")
fp2Q = open(queueOutput2, "a+")

fp3 = open(durationOutput3, "a+")
fp3Q = open(queueOutput3, "a+")

fp4 = open(durationOutput4, "a+")
fp4Q = open(queueOutput4, "a+")

########################################################################

tree = ElementTree()
tree.parse(xmlFile)
root = tree.getroot()

tree2 = ElementTree()
tree2.parse(xmlFile2)
root2 = tree2.getroot()

print(root.tag, " | ",root2.tag)
print("")

#duration1 = []
#duration2 = []
#duration3 = []
#duration4 = []

#queue1 = []
#queue2 = []
#queue3 = []
#queue4 = []

###############################################################################
#Scans the XML file to find and allocate the desired info in the arrays
#Adapt this piece of code to save the values in a file, after every simulation
#This way, data from many simulations can be analyzed together
for child in root:
    if child.get('departLane') == "1to0_0":
        #duration1.append((float)(child.get('duration')))
        fp1.write("%s\n" % child.get('duration'))
    if child.get('departLane') == "2to0_0":
        #duration2.append((float)(child.get('duration')))
        fp2.write("%s\n" % child.get('duration'))
    if child.get('departLane') == "3to0_0":
        #duration3.append((float)(child.get('duration')))
        fp3.write("%s\n" % child.get('duration'))
    if child.get('departLane') == "4to0_0":
        #duration4.append((float)(child.get('duration')))
        fp4.write("%s\n" % child.get('duration'))

for child2 in root2.findall(".//lane[@queueing_length]"):
    if child2.get('id') == "1to0_0":
        #queue1.append((float)(child2.get('queueing_length')))
        fp1Q.write("%s\n" % child2.get('queueing_length'))
    if child2.get('id') == "2to0_0":
        #queue2.append((float)(child2.get('queueing_length')))
        fp2Q.write("%s\n" % child2.get('queueing_length'))
    if child2.get('id') == "3to0_0":
        #queue3.append((float)(child2.get('queueing_length')))
        fp3Q.write("%s\n" % child2.get('queueing_length'))
    if child2.get('id') == "4to0_0":
        #queue4.append((float)(child2.get('queueing_length')))
        fp4Q.write("%s\n" % child2.get('queueing_length'))
###############################################################################

#u1 = np.asarray(duration1)
#u2 = np.asarray(duration2)
#u3 = np.asarray(duration3)
#u4 = np.asarray(duration4)

#y1 = np.asarray(queue1)
#y2 = np.asarray(queue2)
#y3 = np.asarray(queue3)
#y4 = np.asarray(queue4)

#m0 contains the mean values of each u-array
#m0 = []
#m0.append(np.mean(u1))
#m0.append(np.mean(u2))
#m0.append(np.mean(u3))
#m0.append(np.mean(u4))

#m1 contains the mean values of each y-array
#m1 = []
#m1.append(np.mean(y1))
#m1.append(np.mean(y2))
#m1.append(np.mean(y3))
#m1.append(np.mean(y4))

#print("Mean values from the simulation:\nTrip time | Queue length")
#for i,j in zip(m0,m1):
#    print(m0.index(i)+1,"%6.2f" % i, " - ","%6.2f" % j)
#print("Total average:\n  %6.2f" % np.mean(m0), " - ", "%6.2f" % np.mean(m1))

########################################################################
#myPlot.figure(1)

#Data1
#myPlot.subplot(221)
#myPlot.plot(u1.flatten())
#myPlot.title("Average 1")

#Data2
#myPlot.subplot(222)
#myPlot.plot(u2.flatten())
#myPlot.title("Average 2")

#Data3
#myPlot.subplot(223)
#myPlot.plot(u3.flatten())
#myPlot.title("Average 3")

#Data4
#myPlot.subplot(224)
#myPlot.plot(u4.flatten())
#myPlot.title("Average 4")

#myPlot.show()
########################################################################

fp1.close()
fp2.close()
fp3.close()
fp4.close()

fp1Q.close()
fp2Q.close()
fp3Q.close()
fp4Q.close()

########################################################################

print("\nEnd")
