from flask import Flask

app = Flask(__name__, static_url_path="/")


def page(file_name):
    with open(f"..{file_name}", encoding="utf-8") as file:
        return file.read()


pages = {
    "index": page("index.html"),
    "kanobu": page("kanobu.html"),
    "timer": page("timer.html"),
    "404": page("404.html"),
    "lorem": page("lorem.html"),
    "test": page("test.html"),
    "ligatures": page("ligatures.html")
}
