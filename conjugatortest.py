import requests
import lxml.html


"""
French demo - no alteration needed
"""

test_url = "https://cooljugator.com/fr/aller"  # gets conjugations for french verb "manger"
html = requests.get(test_url)
doc = lxml.html.fromstring(html.content)

first_p_sing_conj = doc.xpath('/html/body/div[2]/div[3]/div[1]/div[1]/section/div[2]/div/div/div/div[1]/div[16]/div/div[1]')[0].text
print(first_p_sing_conj)

"""
German demo - just add ich + slightly different location to Fr
"""
test_url = "https://cooljugator.com/de/gehen"  # gets conjugations for french verb "manger"
html = requests.get(test_url)
doc = lxml.html.fromstring(html.content)

first_p_sing_conj = "ich " + doc.xpath('/html/body/div[2]/div[3]/div[1]/div[1]/section/div[2]/div/div/div/div[1]/div[30]/div/div[1]')[0].text
print(first_p_sing_conj)

"""
Italian demo - just add io + same location to french
"""

test_url = "https://cooljugator.com/it/fare"  # gets conjugations for french verb "manger"
html = requests.get(test_url)
doc = lxml.html.fromstring(html.content)

first_p_sing_conj = "io " + doc.xpath('/html/body/div[2]/div[3]/div[1]/div[1]/section/div[2]/div/div/div/div[1]/div[16]/div/div[1]')[0].text
print(first_p_sing_conj)

"""
Spanish demo - just need to add yo + same location to French
"""

test_url = "https://cooljugator.com/es/entender"  # gets conjugations for french verb "manger"
html = requests.get(test_url)
doc = lxml.html.fromstring(html.content)

first_p_sing_conj = "yo " + doc.xpath('/html/body/div[2]/div[3]/div[1]/div[1]/section/div[2]/div/div/div/div[1]/div[16]/div/div[1]')[0].text
print(first_p_sing_conj)
