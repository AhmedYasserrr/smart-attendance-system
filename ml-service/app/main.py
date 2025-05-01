import cv2
import numpy as np
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse
from recognition import Recognition

app = FastAPI()
recognition_srv = Recognition()


@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1> Welcome to ML Service API </h1>"


@app.post("/recognize")
async def recognize(file: UploadFile = File(...)):
    try:
        img = await process_uploaded_image(file)

        results = recognition_srv.find(img)
        return JSONResponse(content={"results": results})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/save")
async def save(file: UploadFile = File(...), name: str = "unknown"):
    try:
        img = await process_uploaded_image(file)

        saved_path = recognition_srv.save(img, name)
        return JSONResponse(
            content={"message": "Image saved successfully", "path": saved_path}
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


async def process_uploaded_image(file: UploadFile):
    try:
        contents = await file.read()
        np_array = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Invalid image format")
        return img
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing image: {str(e)}")
