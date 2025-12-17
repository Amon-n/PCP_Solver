from PcpTuple import PcpTuple
from typing import List

class Sequence:
    def __init__(self, start_tuple : PcpTuple):
        self.pcp_queue : List[PcpTuple] = []
        self.missing : str = ""
        self.first_string : str = "" 
        self.second_string : str = "" 
        self.more_in_first : bool = True # true => more in first part of tuple

        self.add_tuple(start_tuple)


    # this method can be called when a tuple is beeing added to the sequence so that the missing var is updated
    def __add_to_missing(self, pcp_tuple : PcpTuple) -> bool:
        self.first_string = self.first_string + pcp_tuple.pcp_tuple[0]
        self.second_string = self.second_string + pcp_tuple.pcp_tuple[1]
        if len(self.first_string) == len(self.second_string):
            return True
        elif len (self.first_string) > len(self.second_string):
            self.more_in_first = True
            self.missing = self.first_string[len(self.second_string):]
        else:
            self.more_in_first = False
            self.missing = self.second_string[len(self.first_string):]
        return False

    def is_appendable(self, pcp_tuple : PcpTuple) -> bool:
        if self.more_in_first:
            concatination = self.missing + pcp_tuple.pcp_tuple[1]
            other_string = pcp_tuple.pcp_tuple[0]
        else:
            concatination = self.missing + pcp_tuple.pcp_tuple[0]
            other_string = pcp_tuple.pcp_tuple[1]
        if len(concatination) <= len(other_string):
            return other_string.startswith(concatination)
        else:
            return concatination.startswith(other_string)

    def add_tuple(self, pcp_tuple : PcpTuple):
        self.pcp_queue.append(pcp_tuple)
        return self.__add_to_missing(pcp_tuple) # returns if sequence is over
    
    def copy(self):
        new_seq = Sequence.__new__(Sequence)
        new_seq.pcp_queue = self.pcp_queue.copy()
        new_seq.missing = self.missing
        new_seq.first_string = self.first_string
        new_seq.second_string = self.second_string
        new_seq.more_in_first = self.more_in_first
        return new_seq
