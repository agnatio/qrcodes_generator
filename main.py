from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import os
from io import BytesIO
from qr_gen import (
    QRCodeGenerator,
)  # Make sure qr_gen.py is in the same directory or properly installed

app = FastAPI()

dir_path = os.path.dirname(os.path.realpath(__file__))

templates = Jinja2Templates(directory=os.path.join(dir_path, "templates"))


# mount static folder

static_folder = os.path.join(dir_path, "static")
app.mount("/static", StaticFiles(directory=static_folder), name="static")


@app.get("/", response_class=HTMLResponse)
def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/generate_qr_code")
def generate_qr_code(data: str):
    qr = QRCodeGenerator(data)
    qr_bytes = qr.get_qr_code_bytes()
    return StreamingResponse(BytesIO(qr_bytes), media_type="image/png")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
