"""Imports"""
import argparse
import Organizer
import PcpTuple
import Sequence

"""Universal variables"""
pcp_list = []
first_solution = False


def init_organizer():
    # TODO: fill the organizer
    return

def main():
    """Main entry point of the program."""
    parser = argparse(prog = 'pcp_solver')
    parser.add_argument(
        "--input",
        type = str,
        help = "A String off the input list to run the pcp solver on"
    )
    parser.add_argument("--first_solution")
    args = parser.parse_args()

    # Validate input
    if not args.input:
        parser.error("For the program to work there has to be an input in form --input <(x_1,y_1),...,(x_n,y_n)>")
    pass

    # Check if the script should terminate after one solution
    if args.first_solution:
        first_solution = True


if __name__ == "__main__":
    main()