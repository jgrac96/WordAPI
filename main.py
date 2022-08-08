"""
Author: James Grace from https://www.educative.io/blog/python-fastapi-tutorial
Date: 8th August 2022

Basic API to provide present perfect of verb
"""
from fastapi import FastAPI, APIRouter
import requests
import lxml.html

app = FastAPI(
    title="WordAPI",
    openapi_url="/openapi.json"
)

api_router = APIRouter()


@api_router.get("/", status_code=200)
def root() -> dict:
    return {"msg": "Hello, World"}


@api_router.get("/perfect_pres/")
def read_testing(lang: str, infinitive: str):
    lang_codes = {"german": "de", "french": "fr", "italian": "it", "spanish": "es"}
    prefix_needed = {"german": "ich ", "french": "", "italian": "io ", "spanish": "yo "}
    xpaths = {
        "french": "/html/body/div[2]/div[3]/div[1]/div[1]/section/div[2]/div/div/div/div[1]/div[16]/div/div[1]",
        "german": "/html/body/div[2]/div[3]/div[1]/div[1]/section/div[2]/div/div/div/div[1]/div[30]/div/div[1]",
        "italian": "/html/body/div[2]/div[3]/div[1]/div[1]/section/div[2]/div/div/div/div[1]/div[16]/div/div[1]",
        "spanish": "/html/body/div[2]/div[3]/div[1]/div[1]/section/div[2]/div/div/div/div[1]/div[16]/div/div[1]"
    }

    try:
        request_url = "https://cooljugator.com/{}/{}".format(lang_codes[lang], infinitive)
        html_doc = lxml.html.fromstring(requests.get(request_url).content)
        conjugation = prefix_needed[lang] + html_doc.xpath(xpaths[lang])[0].text

        return {
            "langauge": lang,
            "verb": infinitive,
            "past_conjugation": conjugation,
            "success": True
        }

    except IndexError:
        return {
            "language": lang,
            "verb": infinitive,
            "past_conjugation": None,
            "success": False
        }


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8011, log_level="debug")
