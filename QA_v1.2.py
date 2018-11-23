import random
import re
quiz=open("quiz.txt", 'r')
ans=open('answ.txt', 'r')
quizl=re.split('\n\d\)', quiz.read())
answl=re.split('\n\d\)', ans.read())
quiz.seek(0)
answl.remove('')
quizl.remove('')
lenq=len(quizl)
adict={}
answnum=0
for i in quizl:
    adict[i]=answl[answnum]
    answnum+=1
random.shuffle(quizl)
result=0
for q in range(lenq):
    print(quizl[q])
    a=input('Введите ответ')
    if adict[quizl[q]].strip()==a.strip():
        result+=1
print(str(result)+'/'+str(lenq))
quiz.close()
ans.close()