from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep


opts = Options()
opts.headless = True

driver = webdriver.Firefox(options=opts)
driver.get("https://conjugator.reverso.net/conjugation-french-verb-{}.html")

# anticipate asking permission for cookie settings
cookie_accept = driver.find_element(By.ID, "didomi-notice-agree-button")
cookie_accept.click()

# search
sleep(1)
verbToSearch = "manger"
search_bar = driver.find_element(By.ID, "txtVerb")
search_bar.send_keys(verbToSearch)

driver.find_element(By.ID, "lbConjugate").click()
sleep(0.5)
h2s = driver.find_elements(By.TAG_NAME, "h2")
for x in h2s:
    print(x.text)