#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    runner.py
# @author  Lena Kalleske
# @author  Daniel Krajzewicz
# @author  Michael Behrisch
# @author  Jakob Erdmann
# @date    2009-03-26
# @version $Id$

from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import random

# we need to import python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa

def run():
    """execute the TraCI control loop"""

    #just some aux variables
    step = 0
    time_elapsed = 0
    time_elapsed2 = 0
    phase_two = 0
    phase_three = 0

    # we start with phase 2 where EW has green
    traci.trafficlight.setPhase("0", 0)
    car_quant = 0
    car_quant2 = 0
    while traci.simulation.getMinExpectedNumber() > 0:

        #Advances one step within the simulation
        traci.simulationStep()

        #Logic if the traffic light is on phase 2
        if traci.trafficlight.getPhase("0") == 2:
            phase_two += 1
            # we are not already switching
            if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
                car_quant += 1

                #checks if 10 cars have passed over the detector
                if car_quant > 9:
                    traci.trafficlight.setPhase("0", 3)
                    car_quant = 0
                    time_elapsed = 0
                    phase_two = 0

                #checks if it has passed over 30s with a vehicle on the lane
                elif time_elapsed > 20:
                    traci.trafficlight.setPhase("0", 3)
                    car_quant = 0
                    time_elapsed = 0
                    phase_two = 0
            else:
                # otherwise try to keep green for EW
                traci.trafficlight.setPhase("0", 2)

            #checks if there has passed over 30s in phase 2 (that'll be the max duration of a phase)
            if phase_two > 30:
                traci.trafficlight.setPhase("0", 3)
                car_quant = 0
                time_elapsed = 0
                phase_two = 0


        #Logic if the traffic light is on phase 3
        elif traci.trafficlight.getPhase("0") == 0:
            phase_three += 1
            # we are not already switching
            if traci.inductionloop.getLastStepVehicleNumber("1") > 0:
                car_quant2 += 1

                #checks if 10 cars have passed over the detector
                if car_quant2 > 9:
                    traci.trafficlight.setPhase("0", 1)
                    car_quant2 = 0
                    time_elapsed2 = 0
                    phase_three = 0

                #checks if it has passed over 30s with a vehicle on the lane
                elif time_elapsed2 > 20:
                    traci.trafficlight.setPhase("0", 1)
                    car_quant2 = 0
                    time_elapsed2 = 0
                    phase_three = 0
            else:
                # otherwise try to keep green for horizontal
                traci.trafficlight.setPhase("0", 0)

            #checks if there has passed over 30s in phase 3 (that'll be the max duration of a phase)
            if phase_three > 30:
                traci.trafficlight.setPhase("0", 1)
                car_quant2 = 0
                time_elapsed2 = 0
                phase_three = 0


        step += 1
        if car_quant > 0:
            time_elapsed += 1
        if car_quant2 > 0:
            time_elapsed2 += 1

    traci.close()
    sys.stdout.flush()


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, "-c", "secondTry.sumocfg",
                             "--tripinfo-output", "tripinfo.xml"])
    run()
