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
        SendersData=namedtuple("Senders_Data","Name Origin")
        return [SendersData(sender.name, sender.origin) for sender in self.my_senders]


def day_simulation():
    my_senders = SortingFacilitySenders()

    wiesiek = my_senders.add_new_sender("Wiesiek", "Daszyna")
    mariola = my_senders.add_new_sender("Mariola", "Pcim")
    zenek = my_senders.add_new_sender("Zenek", "Grażynowo")
    janusz = my_senders.add_new_sender("Janusz", "Cebulandia-Zdrój")



    my_sorting_facility=sorting_facility.SortingFacility()

    week=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    day=random.choice(week)

    my_sorting_facility.start_day()
    print(f"Today is {day}.","\n_________________________________________________\n")
    time.sleep(1)

    print("Here are some senders' info:\n")
    pprint(my_senders.get_senders_info())

    print("\nThe senders are sending their parcels now...")
    time.sleep(1)

    for sender in my_senders.senders:

        amount_of_parcels=random.randint(1,5)
        new_parcels=sender.prepare_parcels(amount_of_parcels)
        print(f"\n{sender.name} sends on {day} {amount_of_parcels} parcel(s).")

        my_sorting_facility.take_parcels_from_sender(new_parcels)
    print('\n_________________________________________________\n')
    print(f"Here is total amount of parcels from {day}:\n")
    counter=0
    for destination, parcels in my_sorting_facility.parcels_sorted_by_destination.items():
        print("Destination:",destination)
        print("Total number of parcels:",len(parcels))
        print('\n')
        counter+=len(parcels)

    print('\n_________________________________________________\n')

    print(f'On {day} there were {counter} parcels sent.')

    print('\n_________________________________________________\n')

    start_again=input("Do you want to start another random day simulation?\nPress y for Yes.\n")
    if start_again=='y':
        print('\n')
        day_simulation()


if __name__ == '__main__':
    day_simulation()

