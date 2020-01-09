import parcels
from time import sleep


class Sender:
    def __init__(self, name, origin):
        self.name = name
        self.origin = origin

    def prepare_parcel(self):
        sleep(0.1)  # it takes some time to prepare parcel...
        new_package = next(parcels.parcel_generator)
        new_package.sender_name, new_package.sender_origin = self.name, self.origin
        return new_package

    def prepare_parcels(self, n):
        return [self.prepare_parcel() for _ in range(n)]
