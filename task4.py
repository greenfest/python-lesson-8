from des import DesKey
import random
key0 = DesKey(b"igra_pole_chudes")

def getQuestions():
    with open ("questions.txt", "r", encoding="utf-8") as f:
            questionList = f.read().splitlines()
    numberQuestion = random.randrange(0, len(questionList))
    questionAnswer = str(questionList[numberQuestion])
    for i in range(0, len(questionAnswer)):
        if questionAnswer[i] == ";":
            question = questionAnswer[0:i]
            answer = (key0.decrypt(eval(questionAnswer[i+1:len(questionAnswer)]), padding=True)).decode("utf-8")
    return answer, question                

welcomeMessage=input('Добро пожаловать в игру "Поле чудес"!\nЧтобы начать игру, нажмите "Enter".\nДля выхода из игры напишите "exit".\nДля ввода новых вопросов напишите "new"\n')


def addQuestions():
    while True:
        question = input('Введите вопрос или "q" для выхода: ')
        if question == "q":
            break
        else: 
            answer = bytes((input('Введите ответ: ')).upper(), "utf-8")
        with open ("questions.txt", "a", encoding="utf-8") as f:
            f.write(f'{question};{key0.encrypt(answer, padding=True)}\n')    

def maskWord(st, wd, ggs):

    result = ''
    gg = []
    ch = ''
    for ch in st:
        if not ch == '■ ':
            if not ch in gg:
                gg.append(ch)

    if not ggs in gg:
        gg.append(ggs)

    for ggs in wd:
        if ggs in gg:
            result += ggs
        else: 
            result += " ■ "

    return result

if welcomeMessage == "new": addQuestions()

answer, question = getQuestions()

print(f'Вопрос: {question}')

wd = answer
st = ' False■ ' * len(wd)



play = True
while play:
    ggs = (input('Назовите букву?\n ')).upper()
    if ggs == "exit": play = False
    st = maskWord(st, wd, ggs)
    print (st)
    if maskWord(st, wd, ggs) == wd:  
        print ('Вы победили!')
        play = False