import platform
from termoverflow.__init__ import VERSION
import typer
from rich import print
from rich.markdown import Markdown
import requests
import json
import markdownify
import urllib.parse
import os

app = typer.Typer()

def getSearchUrl(query: str):
    return f"https://api.stackexchange.com/2.3/search?order=desc&sort=activity&intitle={urllib.parse.quote(query)}&site=stackoverflow"

def requestSearch(query: str) -> dict:
    url = getSearchUrl(query)
    response = requests.get(url)
    return json.loads(response.text)

def getSearchResultAnswers(id: int) -> str:
    url = f"https://api.stackexchange.com/2.3/questions/{id}/answers?order=desc&sort=votes&site=stackoverflow"
    response = requests.get(url)
    return json.loads(response.text)["items"][:10]

def getSearchResultBodyRichMD(id: int) -> Markdown:
    url = f"https://api.stackexchange.com/2.3/questions/{id}?order=desc&sort=activity&site=stackoverflow&filter=withbody"
    response = requests.get(url)
    html = json.loads(response.text)["items"][0]["body"]
    return Markdown(markdownify.markdownify(html, heading_style="ATX"))

def getAnswerBodyRichMD(id: int) -> Markdown:
    url = f"https://api.stackexchange.com/2.3/answers/{id}?order=desc&sort=activity&site=stackoverflow&filter=withbody"
    response = requests.get(url)
    html = json.loads(response.text)["items"][0]["body"]
    return Markdown(markdownify.markdownify(html, heading_style="ATX"))

@app.command()
def s(term: str):
    """\
    Seach questions and answers in StackOverflow.
    """
    r = requestSearch(term)["items"][0]
    print(Markdown(f'**{r["title"]}**'))
    print("")
    print(getSearchResultBodyRichMD(r["question_id"]))
    print("\n" + ("=" * os.get_terminal_size()[0]) + "\n")
    for a in getSearchResultAnswers(r["question_id"]):
        # print(a["question_id"]) # TODO
        print(getAnswerBodyRichMD(a["answer_id"]))
        print("\n...\n")

@app.command()
def version():
    """\
    Print the version.
    """
    print(f"TermOverflow version [aqua]{VERSION}[/aqua]")

@app.command()
def mydevice():
    """\
    Print the device info.
    """
    print("Python version:", os.sys.version)
    print("")
    print("Operating system:", platform.system(), platform.release())
    print("Operating system version:", platform.version())
    print("")
    print("Computer architecture:", platform.machine())

if __name__ == "__main__":
    app()