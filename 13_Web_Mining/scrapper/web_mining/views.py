from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def fetch_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    skills_arr = []
    exp_arr = []

    skills = soup.select("div.main .div .name")
    for skill in skills:
        skills_arr.append(skill.text)

    exps = soup.select("div.main .div .exp")
    for exp in exps:
        exp_arr.append(exp.text)

    # for i in range(0, len(exp_arr)):
    #     print(f'Skill : {skills_arr[i]}\nExperience : {exp_arr[i]}')
    #     print('----------------------')

    main_dict = {
        'Skills' : skills_arr,
        'Experience' : exp_arr
    }

    return skills_arr, exp_arr
    
def home(request):
    url = 'http://127.0.0.1:5500/source/index.html' 
    skills, exp = fetch_data(url)
    return render(request, 'home.html', { "skills": skills , "exps" : exp})