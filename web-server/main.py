import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/")
def get_list():
    return [1, 2, 3, 4]

@app.get('/items/', response_class=HTMLResponse)
async def get_list():
    return """<html>
    <h1>Hola mundo</h1>
    <p>Esto es un párrafo</p>
    </html>"""


def run():
    store.get_categories()



if __name__ == '__main__':
    run()