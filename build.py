from __future__ import print_function

from architect import ARCHITECT
from architect import WORKER

import sys

if __name__ == "__main__":
	fileName = sys.argv[1]
	print("\nStarting...")
	print("First reading the blueprint...")
	print("File provided: ", fileName)

	workersAvailable = 2 #don't change this or it'll break

	daedalus = ARCHITECT(workersAvailable)
	daedalus.check_for_errors(fileName)
	daedalus.read_blueprint(fileName)

	worker1 = WORKER(0)
	worker2 = WORKER(1)

	worker1.instructionSet, worker2.instructionSet = daedalus.plan_construction()
	
