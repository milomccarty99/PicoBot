class State:
	def __init__(self, num, surrList, goList, stateList):
		self.num = num
		self.surrList = surrList
		self.goList = goList
		self.stateList = stateList
		self.surrListGo

		for i in range(0,len(surrList)):
			applyRule(goList[i],surrList[i], stateList[i])

	def applyrule(surr,go, nextState):
		pos = 0
		for t in range(0,3):
			if(surr[t] =='*'):
				#todo: handle permutations
				pos += t
			elif (surr[t] == 'x'):
				pos +=0
			else:
				pos += t
			surrListGo[t] = [go, nextState]

	#given the surroundings of state, returns a tuple of the direction to travel and the next state
	def gotowards(surr):
		pos = 0;
		for t in range(0,3):
			if (surr[t] == 'x'):
				pos+=0
			else:
				pos+=t
		return surrListGo[t]

class StateMachine:
	def __init__(self, str):
		self.linesList = str.splitlines()
		self.rules
		self.validstates
		self.step = 0
		self.state = 0
		rulesList

		for i in range(0,len(linesList)):
			if(linesList[i].contains('#') or linesList[i].isspace()):
				#do nothing
				pass
			else:
				line = linesList[i].split(' ');
				if (len(line) != 5):
					#error
					pass
				else :
					validstates.append[line[0]]
					rulesList[line[0]][0].append(line[1]) # surr
					rulesList[line[0]][1].append(line[3]) # direction
					rulesList[line[0]][2].append(line[4]) # state 
		for i in range(0,len(validstates)):
			rules.append(State(validstates[i],rulesList[validstates[i]][0],rulesList[validstates[i]][1],rulesList[validstates[i]][2]))

	def getrules():
		return rules

	def stepforward(surr):
		surrGo = rules[state].gotowards(surr)
		state = surr[1];
		return surrGo[0]
