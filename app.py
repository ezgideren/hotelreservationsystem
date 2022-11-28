import models
from fastapi import FastAPI
from pydantic import BaseModel
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

reservations = {
	1: {
		"name": "Ezgi",
		"surname": "Ozdemir",
		"age": "26",
		"room": "a12b34"
	}
}

@app.get("/")
def root():
	return 

@app.get("/hotels/{hotel_name}")
def read_hotels(hotel_name: str):
	return {"hotel_name": hotel_name}

@app.get("/hotels/{hotel_name}/room/{room_id}")
def read_rooms(hotel_name:str, room_id):
	return{"hotel_name": hotel_name, "room_id": room_id}

@app.get("/reservation/{reservation_id}")
def read_reservation(reservation_id: int):
	return{"reservation_id": reservation_id}

#Query paramater by name from reservations list
@app.get("/reservation-by-name")
def get_reservation(name: str):
	for reservation_id in reservations:
		if reservations[reservation_id]["name"] == name:
			return reservations[reservation_id]
	return {"Data" : "Not Found"}

#Query paramater str has default value none so this query parameter is optional.
@app.get("/reservation-by-surname")
def get_reservation(surname: str = None):
	for reservation_id in reservations:
		if reservations[reservation_id]["surname"] == surname:
			return reservations[reservation_id]
	return {"Data" : "Not Found"}

@app.post("/register")
def create_acc(account_request: AccountRequest):
	return{}