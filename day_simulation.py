import datetime
import random
from pprint import pprint
import time
import sorting_facility
from collections import namedtuple
from sender import Sender


class SortingFacilitySenders():

    def __init__(self):
        self.my_senders = []

    @property
    def senders(self):
        return self.my_senders

    def add_new_sender(self, name, origin):
        new_sender = Sender(name, origin)
        self.my_senders.append(new_sender)
        return new_sender

    def get_senders_info(self):
        SendersData = namedtuple("Senders_Data", "Name Origin")
        return [SendersData(sender.name, sender.origin) for sender in self.my_senders]


def line():
    print(70 * '_', end='\n')


def day_simulation():
    start = datetime.datetime.now()
    my_senders = SortingFacilitySenders()

    random_names = ["Zenon", "Grazyna", "Pacek", "Lacek", "Janusz", "Mariola"]
    random_places = ["Daszyna", "Pcim", "Bystra", "Ciechocinek", "Pruszcz", "Cebulowo"]

    for _ in range(5):
        my_senders.add_new_sender(random.choice(random_names), random.choice(random_places))

    my_sorting_facility = sorting_facility.SortingFacility()

    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = random.choice(week)

    my_sorting_facility.start_day()
    print(f"Today is {day}.")
    if day == "Sunday":
        line()
        print("We don't work on Sundays...")
        line()
        once_again()
    line()
    time.sleep(1)

    print("Here are some senders' info:\n")
    pprint(my_senders.get_senders_info())

    print("\nThe senders are sending their parcels now...")
    time.sleep(1)

    for sender in my_senders.senders:
        amount_of_parcels = random.randint(1, 10)
        new_parcels = sender.prepare_parcels(amount_of_parcels)
        print(f"\n{sender.name} sends on {day} {amount_of_parcels} parcel(s).")

        my_sorting_facility.take_parcels_from_sender(new_parcels)
    line()
    print(f"Here is total amount of parcels from {day}:\n")
    counter = 0
    for destination, parcels in my_sorting_facility.parcels_sorted_by_destination.items():
        time.sleep(1)
        print("Destination:", destination)
        print("Total number of parcels:", len(parcels))
        print('\n')
        counter += len(parcels)

    line()

    time.sleep(1)
    stop = datetime.datetime.now()
    time_wasted = stop - start
    print(f"Day simulation on {day} took only {time_wasted}. That wasn't so bad, ay?")
    print(f'On {day} there were {counter} parcels sent.')

    line()
    once_again()


def once_again():
    start_again = input("Do you want to start another random day simulation?\nPress y for Yes.\n")
    if start_again == 'y':
        print('\n')
        day_simulation()


if __name__ == '__main__':
    day_simulation()
