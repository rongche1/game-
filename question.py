import random
import os
from datetime import date 
states = {'Abia': 'Umuahia','Adamawa':'Yola','Akwa Ibom':'Uyo','Anambra':'Akwa', 'Bauchi':'Bauchi','Bayelsa':'Yenogoa','Benue':'Makurdi','Borno':'Maiduguri','Cross River':'calabar','Delta':'Asaba','Ebonyi':'Abakaliki','Edo':'Benin','Ekiti':'Ado-Ekiti','Enugu':'Enugu','Gombe':'Gombe','Imo':'Owerri','Jigawa':'Dutse','Kaduna':'Kaduna','Kano':'Kano','Kebbi':'Birnin Kebbi','Kogi':'Lokoja','Kwara':'Ilorin','Lagos':'Ikeja','Nasarawa':'Lafia','Niger':'Minna','Ogun':'Abeokuta','Ondo':'Akure','Osun':'Osogbo','Oyo':'Ibadan','Plateau':'Jos','Rivers':'Port-Harcourt','Sokoto':'Sokoto','Taraba':'Jalingo','Yobe':'Damaturu','Zamfara':'Gusau','Federal Capital Territory':'Abuja'}
for quiznum in range(35):
    quizfile = os.mkdir(f'qusfiles{(quiznum)}.txt')
    answerfile = os.mkdir(f'answerfil{(quiznum)}.txt')
    quiz_file = open(quizfile,'w')
    answer_file =open(answerfile,'w')
    name = input('write your name in full ')
    dates = date.today()
    quiz_file.write(f'Name: {name}\nDate: {dates}\nperiod: 20mins')
    quiz_file.write(('  '*20)+f'STATE AND CAPITAL QUIZ')
    quiz_file.write('\n\n\n')
    state = list(states.keys())
    random.shuffle(state)
for question in range(36):
    correct_answer = states[state[question]]
    wrong_answer = list(states.values())
    for wrong in wrong_answer:
        if wrong in correct_answer:
            wrong_answer.remove(wrong)
    option = random.sample(wrong_answer,3)
    option = option + [correct_answer]
    random.shuffle(option)
    question += 1
    quiz_file.write(f'{question}. what is the  capital of {state[question]} \n')
    for i in range(4):
          alpha = 'ABCD'
          quiz_file.write(f'{alpha[i]}. {option[i]}/n')
    quiz_fil.write('\n\n')
    an = alpha[option.index(correct_answer)]
    answer_file.write('answers for state and capital quiz')
    answer_file.write(f'{question}.{an}\n')
    quiz_file.close()
    answer_file.close()