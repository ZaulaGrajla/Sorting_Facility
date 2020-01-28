import itertools
import time
from collections import defaultdict, Counter
from dataclasses import astuple
from day_simulation import line
from functools import wraps
from pprint import pprint
import datetime


class SortingFacility:

    def __init__(self):
        self.parcels_sorted_by_destination = defaultdict(list)

    def start_day(self):
        self.parcels_sorted_by_destination = defaultdict(list)
        print("Welcome to sorting facility! Let's send some parcels.")
        time.sleep(1)

    def take_parcels_from_sender(self, new_parcels):
        time.sleep(2)
        self.sort_parcels(new_parcels)

    def sort_parcels(self, new_parcels):
        print(len(new_parcels), 'new parcel(s) in sorting facility.')
        new_parcels = sorted(new_parcels, key=lambda x: x.destination)
        for destination, group in itertools.groupby(new_parcels, lambda y: y.destination):
            line()
            for parcel in group:
                self.parcels_sorted_by_destination[destination].append(parcel)
            self.log_parcels()

    def log_parcels(self):
        print(f'Data of all parcels in sorting facility at {datetime.datetime.now().strftime("%H:%M:%S")}:\n')
        time.sleep(2)
        pprint(self.parcels_sorted_by_destination)
        time.sleep(2)

        line()
        print('Parcels sorted by destination:\n')
        for destination, parcels in self.parcels_sorted_by_destination.items():
            parcel_counter = Counter()

            for one_parcel in parcels:
                parcel_counter[one_parcel.size] += 1
            time.sleep(1)
            print("Destination", destination, ":\n",
                  [{"Size": size, "Amount": amount} for size, amount in parcel_counter.items()])
