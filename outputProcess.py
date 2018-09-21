import matplotlib.pyplot as myPlot
import numpy as np

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

fp1 = open(durationOutput1, "r")
fp1Q = open(queueOutput1, "r")

fp2 = open(durationOutput2, "r")
fp2Q = open(queueOutput2, "r")

fp3 = open(durationOutput3, "r")
fp3Q = open(queueOutput3, "r")

fp4 = open(durationOutput4, "r")
fp4Q = open(queueOutput4, "r")

########################################################################

duration1 = [(float)(lines) for lines in fp1.readlines()]
duration2 = [(float)(lines) for lines in fp2.readlines()]
duration3 = [(float)(lines) for lines in fp3.readlines()]
duration4 = [(float)(lines) for lines in fp4.readlines()]

queue1 = [(float)(lines) for lines in fp1Q.readlines()]
queue2 = [(float)(lines) for lines in fp2Q.readlines()]
queue3 = [(float)(lines) for lines in fp3Q.readlines()]
queue4 = [(float)(lines) for lines in fp4Q.readlines()]

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

u1.sort()
u2.sort()
u3.sort()
u4.sort()

y1.sort()
y2.sort()
y3.sort()
y4.sort()

########################################################################

myPlot.figure(1)

#Data1
myPlot.subplot(221)
myPlot.plot(u1)
myPlot.title("Average 1")

#Data2
myPlot.subplot(222)
myPlot.plot(u2)
myPlot.title("Average 2")

#Data3
myPlot.subplot(223)
myPlot.plot(y1)
myPlot.title("Queue 1")

#Data4
myPlot.subplot(224)
myPlot.plot(y2)
myPlot.title("Queue 2")

myPlot.show()

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

print("End.")
