import random


def scoresGrades():
	for i in range (0, 10):
		score = random.randint(60,100) 
		
		# if score >= 90:
		# 	grade = "A"
		# elif score >= 80:
		# 	grade = "B"
		# elif score >= 70:
		# 	grade = "C"
		# elif score >= 60:
		# 	grade = "D"
		# else:
		# 	grade = "F"

		if score < 70:
			grade = "D"
		elif score < 80:
			grade = "C"
		elif score < 90:
			grade = "B"
		elif score <= 100:
			grade = "A"

		print "Score: " + str(score) + "; Your grade is " + grade

	print "End of the Program. Bye!"

scoresGrades();