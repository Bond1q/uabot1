import requests
from bs4 import BeautifulSoup as BS

def get_question(rand):
    r = requests.get(f'https://zno.osvita.ua/ukrainian/all/{rand}')


    html = BS(r.content, 'html.parser')
    question = []
    items = html.find('div', class_='question')


    img = items.find("img")


    question.append(items.get_text())
    if img:
        q = str(img).find("/")
        z = str(img).find("p")
        image = str(img)[q:z+2]
        question.append('https://zno.osvita.ua/'+ str(image))

        return question[0],question[1]
    else:
        return question[0]

def get_answer(rand):
    r = requests.get(f'https://zno.osvita.ua/ukrainian/all/{rand}')
    variatns = []

    answers = []
    html = BS(r.content, 'html.parser')
    items = html.find('div', class_='answers')
    answer_count = items.find_all('div',class_ = 'answer')

    for el in  answer_count:
        answers.append(el.get_text())
    for i in answers:
        first_letter = i[0]
        i = i.replace(i[0],"",1)
        variatns.append(f"{first_letter}  {i}")
    length = len(variatns)
    return variatns

def combinating(text):
    return "\n\n".join(text)


def get_true_answer(rand):
    r = requests.get(f'https://zno.osvita.ua/ukrainian/all/{rand}')

    html = BS(r.content, 'html.parser')
    items = html.find_all('input', type = 'hidden')

    true_answer = items[4:5]

    return  str(true_answer)[-5:-4]




