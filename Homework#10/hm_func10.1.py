import requests
from bs4 import BeautifulSoup
import re


#def pars(name_hor):

url = 'https://www.numama.ru'
response = requests.get(url)
#print(response)

soup = BeautifulSoup(response.text, 'html')
print(soup)
soup = str(soup)
# print('a class="mod_bcon_content" href='in soup)
# print(re.findall(r'a class="mod_bcon_content" href=', soup))

# start = soup.find('<a class="mod_bcon_content"')
# find_str = soup[start: start+100]
# start1 = soup[start: start+100].find('href="')
# end = soup[start: start+100].find('" s')
# print(find_str[start1 + 6: end])


link_list = []
start = 0
for _ in range(5):
    start_ind = soup.find('<a class="mod_bcon_content" href=', start + 1)
    temp_str = soup[start_ind + 34: start_ind + 150]
    end_ind = temp_str.find('" s')
    temp_link = temp_str[:end_ind]
    link_list.append(temp_link)
    start = soup.find(temp_link) + 10
print(link_list)

name_list = ['с чем играть годовалому', 'введение прикорма детям до года', 'какие игрушки нужны до 6 месяцев', 'как развивать ребенка 9 месяцев', 'какие игрушки нужны в 2 месяца']

name_link_dict = {}

for name, link in zip(name_list, link_list):
    name_link_dict[name] = link
print(name_link_dict)

name = input('Введите нужный пункт: ')


response = requests.get('https://www.numama.ru' + name_link_dict[name.lower()])

soup = BeautifulSoup(response.text, 'html')

soup = str(soup)
start_ind_text = soup.find('<div><p><span style="color:') + 10
end_ind_text = soup.find('</span></p></div>')
print(soup[start_ind_text: end_ind_text])