'''Assignment 4

This assignment covers your proficiency with Python's data structures.
It engages your ability to manipulate and evaluate data stored in lists and dictionaries.
'''

def relationship_status(from_member, to_member, social_graph):
    '''
    Item 1.
    Relationship Status. 20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Write your code below this line
    does_from_member_follow = False
    does_to_member_follow = False
    for i in social_graph[from_member]["following"]:
        if i == to_member:
             does_from_member_follow = True
    for i in social_graph[to_member]["following"]:
        if i == from_member:
              does_to_member_follow = True

    if does_from_member_follow and not does_to_member_follow:
        return "follower"
    elif does_to_member_follow and not does_from_member_follow:
        return "followed by"
    elif does_from_member_follow and does_to_member_follow:
        return "friends"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''
    Item 2.
    Tic Tac Toe. 20 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Write your code below this line
    verticals = [[], [], [], [], [], []]
    horizontals =[[], [], [], [], [], []]
    diagonals = [[], []]

    for i in range(len(board)):
        diagonals[0].append(board[i][i])
        diagonals[1].append(board[i][len(board) - 1 - i])
        for j in range(len(board)):
            horizontals[i].append(board[i][j])
            verticals[i].append(board[j][i])

    for i in verticals:
        if len(set(i)) == 1:
            return i[0]

    for i in horizontals:
        if len(set(i)) == 1:
            return i[0]

    for i in diagonals:
        if len(set(i)) == 1:
            return i[0]

    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    '''
    Item 3.
    ETA. 25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "assignment-4-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Write your code below this line
legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
    }
}

def eta(first_stop, second_stop, route_map):
    if first_stop == 'upd':
        if second_stop == 'admu':
            return route_map[('upd', 'admu')]['travel_time_mins']
        elif second_stop == 'dlsu':
            return route_map[('upd', 'admu')]['travel_time_mins'] + route_map[('admu', 'dlsu')]['travel_time_mins']
    elif first_stop == 'admu':
        if second_stop == 'dlsu':
            return route_map[('admu', 'dlsu')]['travel_time_mins']
        elif second_stop == 'upd':
            return route_map[('admu', 'dlsu')]['travel_time_mins'] + route_map[('dlsu', 'upd')]['travel_time_mins']
    elif first_stop == 'dlsu':
        if second_stop == 'upd':
            return route_map[('dlsu', 'upd')]['travel_time_mins']
        elif second_stop == 'admu':
            return route_map[('dlsu', 'upd')]['travel_time_mins'] + route_map[('upd', 'admu')]['travel_time_mins']