from threading import Thread
from threading import Lock, Condition
import time

CHASSIS, ENGINE, TIRES, BODY = 0, 1, 2, 3

class FactoryFloor():
	def __init__(self):
		self.lock = Lock()
		self.floor = []
		self.chassisDone = Condition(self.lock)
		self.engineDone = Condition(self.lock)
		self.tiresDone = Condition(self.lock)

	  # find a car in a given state and take it to off the floor
	def find_car(self, state):
		for i in range(0, len(self.floor)):
			if self.floor[i].state == state:
				item = self.floor[i]
				del self.floor[i]
				return item
		print "FAIL", state

	def alice_done(self, car):
		with self.lock:
			self.floor.append(car)
			self.chassisDone.notify()

	def bob_ready(self):
		with self.lock:
			item = self.find_car(CHASSIS)
			while item is None:
				self.chassisDone.wait()
				item = self.find_car(CHASSIS)
			return item

	def bob_done(self, car):
		with self.lock:
			self.floor.append(car)
			self.engineDone.notify()

	def charlie_ready(self):
		with self.lock:
			item = self.find_car(ENGINE)
			while item is None:
				self.engineDone.wait()
				item = self.find_car(ENGINE)
			return item

	def charlie_done(self, car):
		with self.lock:
			self.floor.append(car)	
			self.tiresDone.notify()
	
	def debbie_ready(self):
		with self.lock:
			item = self.find_car(TIRES)
			while item is None:
				self.tiresDone.wait()
				item = self.find_car(TIRES)
			return item

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
			print 'Alice spawned car'
			ff.alice_done(car)
			time.sleep(10) # Alice takes a break after each car

class Bob(Thread):
	def run(self):
		while True:
			car = ff.bob_ready()
			print 'Bob got car'
			 # either put the engine on or bolt on the body
			car.state += 1
			ff.bob_done(car)

class Charlie(Thread):
	def run(self):
		while True:
			car = ff.charlie_ready()
			print 'Charlie got car'
			 # put the tires on
			car.state += 1
			ff.charlie_done(car)

class Debbie(Thread):
	def run(self):
		while True:
			car = ff.debbie_ready()
			print 'Debbie got car'
			 # put the body on
			car.state += 1
			# car is done
			print 'car is done'

alice = Alice()
bob = Bob()
charlie = Charlie()
debbie = Debbie()
alice.start()
bob.start()
charlie.start()
debbie.start()

