from PcpTuple import PcpTuple
from queue import Queue
import copy

class Sequence:
    def __init__(self, start_tuple : PcpTuple):
        self.pcp_queue : Queue[PcpTuple] = Queue()
        self.add_tuple(start_tuple)
        self.missing : str = ""
        self.first_string : str = "" 
        self.second_string : str = "" 
        self.more_in_first : bool = True # true => more in first part of tuple

    # this method can be called when a tuple is beeing added to the sequence so that the missing var is updated
    def __add_to_missing(self, pcp_tuple : PcpTuple) -> bool:
        self.first_string = self.first_string + pcp_tuple[0]
        self.second_string = self.second_string + pcp_tuple[1]
        if len(self.first_string) == len(self.second_string):
            return True
        elif len (self.first_string) > len(self.second_string):
            self.more_in_first = True
            self.missing = self.first_string[len(self.second_string):]
        else:
            self.more_in_first = False
            self.missing = second_string[len(first_string):]
        return False

    def is_appendable(self, pcp_tuple : PcpTuple) -> bool:
        if self.more_in_first:
            concatination = self.missing + pcp_tuple[1]
            other_string = pcp_tuple[0]
        else:
            concatination = self.missing + pcp_tuple[0]
            other_string = pcp_tuple[1]
        shorter, longer = sorted((concatination, other_string), key=len)
        return longer.startswith(shorter)

    def add_tuple(self, pcp_tuple : PcpTuple):
        self.pcp_queue.put(pcp_tuple)
        return self.__add_to_missing(pcp_tuple) # returns if sequence is over
    
