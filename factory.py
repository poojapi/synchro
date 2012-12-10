from threading import Thread
from threading import Lock, Condition
import time

CHASSIS, ENGINE, TIRES, BODY = 0, 1, 2, 3

class FactoryFloor():
	def __init__(self):
		self.lock = Lock()
		self.floor = []




	  # find a car in a given state and take it to off the floor
	def find_car(self, state):
		for i in range(0, len(self.floor):
			if self.floor[i].state == state:
				item = self.floor[i]
				del self.floor[i]
				return item
		print "FAIL", state

	def alice_done(self, car):


	def bob_ready(self):
	

	def bob_done(self, car):


	def charlie_ready(self):


	def charlie_done(self, car):
	
	
	def debbie_ready(self):


ff = FactoryFloor()

class Car:
	def __init__(self):
		self.state = CHASSIS

class Alice(Thread):
	def run(self):
		while True:
			# create a car chassis and place it on the
			# factory floor
			car = Car() # builds a car
			ff.alice_done(car)
			time.sleep(10) # Alice takes a break after each car

class Bob(Thread):
	def run(self):
		while True:
			car = ff.bob_ready()
			 # either put the engine on or bolt on the body
			car.state += 1
			ff.bob_done(car)

class Charlie(Thread):
	def run(self):
		while True:
			car = ff.charlie_ready()
			 # put the tires on
			car.state += 1
			ff.charlie_done(car)

class Debbie(Thread):
	def run(self):
		while True:
			car = ff.debbie_ready()
			 # put the body on
			car.state += 1
			# car is done

alice = Alice()
bob = Bob()
charlie = Charlie()
debbie = Debbie()
alice.start()
bob.start()
charlie.start()
debbie.start()

