"""Imports"""
import time
import sys
import argparse
from Organizer import Organizer
from PcpTuple import PcpTuple
from Sequence import Sequence

"""Universal variables"""
pcp_list : list[PcpTuple] = []
FIRST_SOLUTION = False
organizer = Organizer()

def intro_text():
    for i in range (4):
        sys.stdout.write('\rloading |')
        time.sleep(0.1)
        sys.stdout.write('\rloading /')
        time.sleep(0.1)
        sys.stdout.write('\rloading -')
        time.sleep(0.1)
        sys.stdout.write('\rloading \\')
        time.sleep(0.1)
    sys.stdout.write('\r')

    print("Hello, let us introduce ourselves. Our names are Sonic, Lizzy, Danin and Amonymos. " \
    "We are bored cs students. That's why we decied to write this programm to return a solution/solutions " \
    "to the PCP Problem.")
    #time.sleep(4)
    if(FIRST_SOLUTION):
        print("You chose to stop after the first solution. Wise choice.")
    else:
        print("Seems like you really like to test the limits. You decided not to add the --first_solution " \
        "flag when starting the program meaning this program might run forever...")
    #time.sleep(3)
    print("Now it is your turn to act. To add a tuple please write a blank space between the elements then press Enter. " \
    " When you are done simply enter # once.")
    


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
    parser = argparse.ArgumentParser(prog="pcp_solver")
    parser.add_argument("--first-solution", action="store_true",
                        help="Stop after the first solution")
    args = parser.parse_args()
    global FIRST_SOLUTION
    FIRST_SOLUTION = args.first_solution

    intro_text()

    tuple_count = 1
    while(True):
        input_message = input(f"Please enter the {tuple_count}. tuple:")
        if input_message == '#': break
        try:
            x,y = input_message.split(' ')
            pcp_list.append(PcpTuple(tuple_count,(x,y)))
            print(f"debug:{pcp_list[0]}")
            tuple_count += 1
        except:
            print("Your last input is incorrect, please check your input and try again")
    print("All tuples are entered, calculating...")
    """for i in range (tuple_count-1):
         print(f"debug: {pcp_list[i]}")"""
    init_organizer()
    while not (organizer.queue.empty()):
        focused_sequence = organizer.pull_first()
        for temp in pcp_list:
            if focused_sequence.is_appendable(temp):
                new_sequence = focused_sequence
                if new_sequence.add_tuple(temp):
                    print("Solution Sequence:", end=" ")
                    for i in new_sequence.queue:
                        printf(i.id, end = " ")
                    if parser.first_solution:
                        return
                else: 
                    organizer.append(new_sequence)


if __name__ == "__main__":
    main()
