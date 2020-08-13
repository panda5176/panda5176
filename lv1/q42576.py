def solution(participant, completion):
	answer = ''
	c_dic = {}

	for c in completion:
		if c in c_dic:
			c_dic[c] += 1
			
		else:
			c_dic[c] = 1
	
	for p in participant:
		if p not in c_dic:
			answer = p
			break

		elif c_dic[p] == 0:
			answer = p
			break

		else:
			c_dic[p] -= 1

	return answer