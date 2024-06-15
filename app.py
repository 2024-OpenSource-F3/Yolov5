from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import torch
from PIL import Image
from io import BytesIO

app = FastAPI()

# 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt')

def transform_image(image_bytes):
    img = Image.open(BytesIO(image_bytes))
    return img

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = await file.read()
    img = transform_image(image)
    results = model(img)
    print(results)
    return JSONResponse(results.pandas().xyxy[0].to_dict(orient="records"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4740)
