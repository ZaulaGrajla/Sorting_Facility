import random
from datetime import datetime

from dataclasses import dataclass

destinations = ("Gdansk", "Gdynia", "Sopot", "Rumia","Reda","Wejherowo","Warszawa")
sizes = ("Small", "Medium", "Large")


@dataclass
class Parcels:
    destination: str
    send_time: str
    size: str
    serial_number: int
    sender_name: str = None
    sender_origin: str = None


def __parcel_generator():
    serial_nr = 0
    while True:
        serial_nr += 1
        yield Parcels(random.choice(destinations), str(datetime.now()), random.choice(sizes), serial_nr)


parcel_generator = __parcel_generator()

