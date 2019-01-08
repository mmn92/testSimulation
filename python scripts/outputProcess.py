import matplotlib.pyplot as myPlot
import numpy as np

########################################################################

durationOutput1 = "durationOutputNoTL1.txt"
queueOutput1 = "queueOutputNoTL1.txt"

durationOutput2 = "durationOutputNoTL2.txt"
queueOutput2 = "queueOutputNoTL2.txt"

durationOutput3 = "durationOutputNoTL3.txt"
queueOutput3 = "queueOutputNoTL3.txt"

durationOutput4 = "durationOutputNoTL4.txt"
queueOutput4 = "queueOutputNoTL4.txt"

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

print("processing data for no traffic lights - scenario 1")

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

# sd0 contains the std deviation values of trip duration
sd0 = []
sd0.append(np.std(u1))
sd0.append(np.std(u2))
sd0.append(np.std(u3))
sd0.append(np.std(u4))

# sd1 contains the std deviation values of queue duration
sd1 = []
sd1.append(np.std(y1))
sd1.append(np.std(y2))
sd1.append(np.std(y3))
sd1.append(np.std(y4))

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
    print(m0.index(i)+1,"%6.2f" % i, " (%3.2f)" % sd0[m0.index(i)]," - ","%6.2f" % j, " (%3.2f)" % sd1[m0.index(i)])
print("Total average:\n  %6.2f" % np.mean(m0), " (%3.2f)" % np.mean(sd0)," - ", "%6.2f" % np.mean(m1), " (%3.2f)" % np.mean(sd1))
########################################################################
#Plot trip duration data
myPlot.figure(1)

#Data1
myPlot.subplot(221)
myPlot.plot(u1)
myPlot.title("Caminho 1")

#Data2
myPlot.subplot(222)
myPlot.plot(u2)
myPlot.title("Caminho 2")

#Data3
myPlot.subplot(223)
myPlot.plot(u3)
myPlot.title("Caminho 3")

#Data4
myPlot.subplot(224)
myPlot.plot(u4)
myPlot.title("Caminho 4")

myPlot.show()

########################################################################
#Plot queue time data

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

#########################################################################
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
