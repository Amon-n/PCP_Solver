"""Imports"""
import time
import sys
from Organizer import Organizer
from PcpTuple import PcpTuple
from Sequence import Sequence

"""Universal variables"""
pcp_list : list[PcpTuple] = []
FIRST_SOLUTION = False
organizer = Organizer()

def init_organizer():
    for temp_pcp_tuple in pcp_list:
        temp_tuple = temp_pcp_tuple.pcp_tuple
        #find the length of the shorter element
        elem_length = min(len(temp_tuple[0]),len(temp_tuple[1]))
        if temp_tuple[0][:elem_length] == temp_tuple[1][:elem_length]:
            new_sequence = Sequence(temp_pcp_tuple)
            organizer.append(new_sequence)
    
    organizer.set_start_seq() # The amount of Start sequences is set here
    print(f"There are {organizer.start_seq} possible tuples to begin with...")
    return

def main():
    """Main entry point of the program."""

    print("To add a tuple please write a blank space between the elements then press Enter. " \
    " When you are done simply enter # once.")

    tuple_count = 1
    while(True):
        input_message = input(f"Please enter the {tuple_count}. tuple:")
        if input_message == '#': break
        try:
            x,y = input_message.split(' ')
            pcp_list.append(PcpTuple(tuple_count,(x,y)))
            print(f"Tuple:{pcp_list[tuple_count - 1]}")
            tuple_count += 1
        except:
            print("Your last input is incorrect, please check your input and try again")
    print("All tuples are entered, calculating...")

    init_organizer()

    while not (organizer.queue.empty()):
        focused_sequence = organizer.pull_first()
        print(f"We have reached a sequence lenth of {len(focused_sequence.pcp_queue)}", end="\r")
        # still hast to be fixed:print(f"Options: {len(organizer.queue)}", end="\r")
        for temp in pcp_list:
            # debug:print(f"checking with Tuple{temp}")

            if focused_sequence.is_appendable(temp):
                new_sequence = focused_sequence.copy()
                if new_sequence.add_tuple(temp):
                    print("Solution Sequence:", end=" ")
                    for i in new_sequence.pcp_queue:
                        print(i.id, end = ",")
                    return
                else: 
                    organizer.append(new_sequence)
    print("There is no solution to your Problem")


if __name__ == "__main__":
    main()
