import Board

class State:
	def __init__(self, state, surrList, goList, stateList):
		self.state = state
		self.surrList = surrList
		self.goList = goList
		self.stateList = stateList
		self.surrListGo = [[]for i in range(0,100)]
		self.state = 0
		for i in range(0,len(surrList)):
			self.applyrule(state, surrList[i],goList[i], stateList[i])

	def applyrule(self,state, surr,go, nextState, t=0, pos=0):
		
		while(t<4):
			if(surr[t] =='*'):
				#todo: handle permutations
				self.applyrule(state,surr,go,nextState,t+1,pos)
				self.applyrule(state,surr,go,nextState,t+1,pos+t)
			elif (surr[t] == 'x'):
				pos +=0
			else:
				pos += t
			t+=1
		print("surroundings for rule " + surr + " pos: " + str(pos))
		self.surrListGo[pos] = [go, nextState]

	#given the surroundings of state, returns a tuple of the direction to travel and the next state
	def gotowards(self, surr):
		pos = 0;
		for t in range(0,3):
			if (surr[t] == 'x'):
				pos+=0
			else:
				pos+=t
		temp = self.surrListGo[t]
		return temp

class StateMachine:
	def __init__(self, rawRules, startx, starty):
		#print(rawRules)
		self.linesList = rawRules.splitlines()
		self.validstates = []
		self.step = 0
		self.state = 0
		self.rules = []
		self.board = Board.Board(startx, starty,25,25)
		rulesList = [[[] for i in range(0,100)] for j in range(0,100)]
		for i in range(0,len(self.linesList)):
			#print(self.linesList[i])
			if(("#" in self.linesList[i]) or self.linesList[i].isspace() or (self.linesList[i]=='\n')):
				#do nothing
				print("skipping line")
				
			else:
				
				line = self.linesList[i].split(' ');
				#print("processing" + str(line))
				if(len(line) >= 5):
					self.validstates.append(int(line[0]))
					rulesList[int(line[0])][0].append(line[1]) # surr
					rulesList[int(line[0])][1].append(line[3]) # direction
					rulesList[int(line[0])][2].append(line[4]) # state 
		#print("valid states" + str(self.validstates))
		for i in range(0,len(self.validstates)):
			#print("working on rule for state" + str(i) + str(rulesList[i]))
			self.rules.append(State(self.validstates[i],rulesList[self.validstates[i]][0],rulesList[self.validstates[i]][1],rulesList[self.validstates[i]][2]))

	def getrules(self):
		return self.rules

	def stepforward(self):
		#print("currnt state:"+ str(self.state) + "")
		#print(self.rules)
		#print(self.board.getSurr())
		surrGo = self.rules[self.state].gotowards(self.board.getSurr())
		print("moving direction: " + surrGo[0])
		self.board.moveDirection(surrGo[0])
	def getBoard(self):
		return self.board.getBoard()
		
