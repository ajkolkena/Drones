import time

from turtledrone import TRDrone
drone = TRDrone()
drone.takeoff()
drone.write("{} says hi to {}".format('Ashleigh', drone.name))
time.sleep(5)
drone.land()
drone.halt()
