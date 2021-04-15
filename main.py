# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# from model import predict

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*'],
#     allow_methods=['*']
# )

# class StockIn(BaseModel):
# 	email: str

# class StockOut(StockIn):
# 	res: dict

# # ROUTES
# @app.post('/predict', response_model = StockOut, status_code = 200)
# def predict_spam(payload: StockIn):

# 	email = payload.email

# 	prediction_value = predict(email)

# 	if prediction_value == 1:
# 		return "Spam"
# 	else:
# 		if prediction_value == 0:
# 			return "Not Spam"
# 		else:
# 			raise HTTPException(status_code = 400, detail = "Model not found.")