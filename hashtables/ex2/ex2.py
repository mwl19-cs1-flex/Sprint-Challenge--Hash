#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    route = []
    t = {}

    # Loads the ticket into the hash table
    for ticket in tickets:
        t[ticket.source] = ticket.destination

    # Sets the value of the item in T[key="NONE"] to variable
    current_ticket = t['NONE']
    # Appends value to route
    route.append(current_ticket)

    # While this value is not a string of NONE
    while t[current_ticket] != 'NONE':
        # for each value of each key in t
        for item in t:
            # if the value of current ticket is equal to the key value
            if t[current_ticket] == item:
                # add the route of the item
                route.append(item)
                # set the current ticket to the item
                current_ticket = item
            else:
                pass
    # need to append the last route to it
    route.append(t[current_ticket])
    
    return route

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
result = reconstruct_trip(tickets, 3)