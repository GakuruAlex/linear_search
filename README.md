# Linear Search #

## Problem Statement ##

Search for position of a given number in a sorted list in descending order.

### Input ###

Cards: A list of numbers sorted in decreasing order i.e

    cards = [24,16,13,11,9,8,5,2]

Query: Number whose position in the list is to be determined e.g 2


### Output ###

The position of the given number in the list i.e 7 (position of 2 in above list , counting from 0)


## Test Cases ##

### Possible Variations ###

1) Number is at the end of the list

2) Number is somewhere in the middle of the list

3) Number is at the beggining of the list 

4) List is empty

5) Number doesnt exist in the list

6) List with only one number

7) Number is repeated in the list

8) List contains repeating numbers

    tests = [
        
        {
            "input":{
                "cards":[24, 16, 13, 11, 9, 8, 5, 2],
                "query": 2
            },
            "output": 7
        },

        {
            "input":{
                    "cards":[24, 17, 10, 11, 9, 8, 4],
                    "query": 24
                },
                "output": 0
        },

        {
            "input":{
                    "cards":[20, 18, 17, 15, 8, 4, 2, 1, 0],
                    "query": 8
                },
                "output":4
        },
        {
            "input":{
                "cards":[],
                "query": 4
            },
            "output": -1
        
        },
        {
            "input":{
                "cards":[2],
                "query":2
            },
            "output":0
        },
        {
            "input":{
                "cards": [9,8, 8, 6, 5, 4, 2, 0],
                "query": 8
                },
                "output": 1
        }
    ]
# Assumption #

List of numbers is sorted in descending order.

Query is an integer.

List contains only integers.

# Time Complexity #

Time taken for the worst case scenario i.e number located at the end of the list.

    O(n)