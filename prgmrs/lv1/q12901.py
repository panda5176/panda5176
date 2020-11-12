def solution(a, b):
	answer = ''
	day = [31,29,31,30,31,30,31,31,30,31,30,31]
	week = ['SUN','MON','TUE','WED','THU','FRI','SAT']

	for m in range(a-1):
		b += day[m]
	
	answer = week[((b-1) % 7 + 5)%7]

	return answer