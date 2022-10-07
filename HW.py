SC=int(input('Enter Your Score (0-100):'))
if SC>100 or SC<0:
    print('Your score is out of rang')
else:
    if SC>=90 : grade = 'A'
    elif SC>=82 :grade = 'B+'
    elif SC>=75 :grade = 'B'
    elif SC>=68 :grade = 'C+'
    elif SC>=60 :grade = 'C'
    elif SC>=53 :grade = 'D+'
    elif SC>=45 :grade = 'D'
    elif SC>=1 :grade = 'F'
    else :grade = 'I'
print('Your get grade ',grade)


