from PcpTuple import PcpTuple
from typing import List

class Sequence:
    def __init__(self, start_tuple : PcpTuple):
        self.pcp_queue : List[PcpTuple] = []
        self.missing : str = ""
        self.more_in_first : bool = True # true => more in first part of tuple

        self.add_tuple(start_tuple)
        # debug:print(f"Sequence made with tuple:{self.pcp_queue[0]}")
        # debug:print(self.first_string)
        # debug:print(self.second_string)

    # this method can be called when a tuple is beeing added to the sequence so that the missing var is updated
    def __add_to_missing(self, pcp_tuple : PcpTuple) -> bool:
        if self.more_in_first:
            first_string = self.missing + pcp_tuple.pcp_tuple[0]
            second_string = pcp_tuple.pcp_tuple[1]
        else:
            first_string = pcp_tuple.pcp_tuple[0]
            second_string = self.missing + pcp_tuple.pcp_tuple[1]
        if len(first_string) < len(second_string):
            self.missing = second_string[len(first_string):]
            self.more_in_first = False
            return False
        elif len(first_string) > len(second_string):
            self.missing = first_string[len(second_string):]
            self.more_in_first = True
            return False
        else:
            return True
            

    def is_appendable(self, pcp_tuple : PcpTuple) -> bool:
        if self.more_in_first:
            concatination = self.missing + pcp_tuple.pcp_tuple[0]
            other_string = pcp_tuple.pcp_tuple[1]
            # debug:print(concatination)
            # debug:print(other_string)
        else:
            concatination = self.missing + pcp_tuple.pcp_tuple[1]
            other_string = pcp_tuple.pcp_tuple[0]
            # debug:print(other_string)
            # debug:print(concatination)

        if len(concatination) <= len(other_string):
            # debug:print(f"is_appendable = {other_string.startswith(concatination)}")
            return other_string.startswith(concatination)
        else:
            # debug:print(f"is_appendable = {concatination.startswith(other_string)}")
            return concatination.startswith(other_string)

    def add_tuple(self, pcp_tuple : PcpTuple):

        self.pcp_queue.append(pcp_tuple)
        return self.__add_to_missing(pcp_tuple) # returns if sequence is over
    
    def copy(self):
        new_seq = Sequence.__new__(Sequence)
        new_seq.pcp_queue = self.pcp_queue.copy()
        new_seq.missing = self.missing
        new_seq.more_in_first = self.more_in_first
        return new_seq
