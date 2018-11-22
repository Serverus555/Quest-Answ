import random
import re
quiz=open("quiz.txt", 'r')
ans=open('answ.txt', 'r')
quizl=re.split('\n\d\)', quiz.read())
random.shuffle(quizl)
print(quizl)