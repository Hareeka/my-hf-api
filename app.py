from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# 1. Initialize the FastAPI application
app = FastAPI()

# 2. Define the input schema for the API request body
# Expects a JSON payload with a 'text' field.
class InputText(BaseModel):
    text: str

# 3. Load the model globally (runs once at startup)
# This uses a simple, small sentiment model from the Hub.
# If you have your own fine-tuned model, replace "sentiment-analysis" 
# with your model's name (e.g., "your-username/your-fine-tuned-model").
try:
    model = pipeline("sentiment-analysis")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


# 4. Define the API prediction endpoint at /predict
@app.post("/predict")
def predict(data: InputText):
    if model is None:
        return {"error": "Model failed to load during startup. Check logs."}, 500
        
    # Run the prediction
    output = model(data.text)[0] 
    
    return {
        "text": data.text,
        "label": output['label'], 
        "score": float(output['score'])
    }

# 5. Optional: Root endpoint for health check
@app.get("/")
def read_root():
    return {"status": "Model API is running."}