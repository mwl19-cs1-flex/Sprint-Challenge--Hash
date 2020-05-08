#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    for i in tickets:
        Ticket(i[0], i[1])

    # if ticket.source is 'None"
    # it is the start of the trip
    # if ticket.destination is none
    # it is the end of the trip

    return route
