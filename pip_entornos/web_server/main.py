import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
@app.get('/')
def get_list():
    return [
        1,2,3,4,5,6,7,8,9,10
    ]



@app.get('/Contact', response_class=HTMLResponse)
def get_list():
    return """
    <html>
        <head>
            <title>FastAPI</title>
        </head>
        <body>
            <h1>FastAPI</h1>
            <p>FastAPI</p>
        </body>
    </html>
    
"""

def run():
    store.get_categories()

if __name__ == '__main__':
    run()