from typing import List

def linear_search(cards: List[int], query: int)-> int:
    """_Given a list of sorted integers in descending order, find the postion of a given number_

    Args:
        cards (List[int]): _A sorted list of intgers in descending order_
        query (int): _Number whose position in the list is to be determined_

    Returns:
        int: _Position of given number or -1 if number not found_
    """
    position: int = 0

    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

def main()-> None:
    cards: List[int] = list(map(int,input("List integers in descending order separated by whitespace: ").split(" ")))
    query: int = int(input("Query: "))
    position: int = linear_search(cards=cards, query=query)
    print(f"The position of {query} is {position}")

if __name__ == "__main__":
    main()