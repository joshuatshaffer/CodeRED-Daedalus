import math
import csv

class WORKER:
	def __init__(self, unitNumber):
		self.devID = "/dev/ttyACM" + str(unitNumber) #for linux
		#self.devID = "/dev/????" #for macOS
		self.instructionSet = []
	
	def translate_for_arduino(self, order):
		print()
	
	def execute_order (self, order):
		print("Executing: ", order)
	

class ARCHITECT:
	def __init__(self, workersAvailable):
		self.workersAvailable = workersAvailable; #possibly up to 4, minimum of 1
		self.layout = [];

	def check_for_errors(self, fileName):
		"""
		Current validation measures in place:
		- no floating blocks (i.e. block requires one to be below)
		- ...
		"""
		tempList = []
		with open(fileName, "r") as blueprint:
			reader = csv.reader(blueprint)
		blueprint.close()	
	
	def read_blueprint(self, fileName):
		tempList = []
		with open(fileName, "r") as blueprint:
			reader = csv.reader(blueprint)
			for row in reader:
				#filtering useful information (i.e. coordinates of only existing blocks)
				if int(row[3]) > 0: #0 is empty
					tempList.append(row)
		blueprint.close()

		self.layout = tempList
		#print(self.layout)

	def plan_construction(self):
		"""
		First sort 12 x 12 map into two halves

	       y^   W
	      11|
		|________
		|
	       0|_________>x
		0   W	11
		
		
		'W' denotes Worker unit location:
			Worker #1 at (6,-1,0) and
			Worker #2 at (6,12,0)

		Worker #1 will get bottom half, and Worker #2 will get upper half
		"""
		#temporary instructionSet
		instructionSet = [[] for _ in xrange(self.workersAvailable)]
		#sort bottom and upper half
		for block in self.layout:
			if int(block[1]) < 6: #looking at y-coordinate
				instructionSet[0].append(block)
			else:
				instructionSet[1].append(block)
	
		print("Worker #1 - bottom half")
		print(instructionSet[0])
		print("Worker #2 - upper half")
		print(instructionSet[1])

		print("Sorting instructionSet into required order of completion")
		#Worker #1 to start from (0,5) and snake its way down to (11,0)
		tempList = [[] for _ in xrange(self.workersAvailable)]
		for z in xrange(0, 1):
			for y in range(5, -1, -1): #need to start from back to front so arm doesn't collide
				for x in range(0, 11):
					for block in instructionSet[0]:
						if int(block[0]) == x and int(block[1]) == y and int(block[2]) == z:
							tempList[0].append(block)
		print("Worker #1 is done.")
		print(tempList[0])
		#Worker #2 to start from (11,6) and snake its way up to (0,11)
		for z in xrange(0, 1):
			for y in range(6, 11):
				for x in range(11, 5, -1):
					for block in instructionSet[1]:
						if int(block[0]) == x and int(block[1]) == y and int(block[2]) == z:
							tempList[1].append(block)

		print("Worker #2 is done.")
		print(tempList[1])
		return tempList[0], tempList[1]

