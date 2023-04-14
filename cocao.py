from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Aqui não tem nada gordão"}

@app.get("/manga/{id}")
async def root(id):
    options = Options()
    # enable headless mode
    options.add_argument("--no-sandbox")
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')

    # driver = webdriver.Chrome(executable_path=os.environ['CHROME_PATH'])
    # driver = webdriver.Chrome(service=Service(os.environ['CHROME_PATH']), options=options)
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.get(f'https://mangalivre.net/manga/null/{id}')

    try:
        series_title = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div[5]/div[2]/span[1]/h1').text
        series_author_tmp = (driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div[5]/div[2]/span[2]').text).split(" ")
        series_author = f"{series_author_tmp[1]} {series_author_tmp[2]}"
        series_dec = driver.find_element(By.XPATH, '//*[@id="series-data"]/div[2]/span[3]/span').text
        series_tot_cap = driver.find_element(By.XPATH, '//*[@id="chapter-list"]/div[3]/h2/span[2]').text
    except Exception as e:
        return {e}

    driver.quit()
    return {
        "title": series_title,
        "author": series_author,
        "description": series_dec,
        "total_chapters": series_tot_cap
    }

# options = Options()
# # enable headless mode
# options.headless = True

# driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
# driver.get('https://mangalivre.net/manga/null/1')

# series_title = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div[5]/div[2]/span[1]/h1').text
# series_author_tmp = (driver.find_element(By.XPATH, '/html/body/div[5]/div/div[3]/div[5]/div[2]/span[2]').text).split(" ")
# series_author = f"{series_author_tmp[1]} {series_author_tmp[2]}"
# series_dec = driver.find_element(By.XPATH, '//*[@id="series-data"]/div[2]/span[3]/span').text
# series_tot_cap = driver.find_element(By.XPATH, '//*[@id="chapter-list"]/div[3]/h2/span[2]').text

# driver.quit()

# manga_infos = {
#     "title": series_title,
#     "author": series_author,
#     "description": series_dec,
#     "total_chapters": series_tot_cap
# }
