"""Imports"""
import time
import sys
import argparse
import Organizer
from PcpTuple import PcpTuple
import Sequence

"""Universal variables"""
pcp_list : list[PcpTuple] = []
FIRST_SOLUTION = False

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
    # TODO: fill the organizer
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
    for i in range (tuple_count-1):
        print(f"debug: {pcp_list[i]}")

if __name__ == "__main__":
    main()