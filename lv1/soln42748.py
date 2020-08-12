def solution(array, commands):
	answer = []

	for comm in commands:
		arr = array[comm[0]-1:comm[1]]
		answer.append(sorted(arr)[comm[2]-1])

	return answer