from fastapi import FastAPI

app = FastAPI()


reservations = {}

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