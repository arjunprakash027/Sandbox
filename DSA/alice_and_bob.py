def locate_card(cards,query):
    position = 0

    while True:
        if cards[position] == query:
            return position
        
        position += 1

        if position == len(cards):
            return -1

cards = [13,11,10,7,4,3,1]
query = 7
output = 3

result = locate_card(cards,query)

test = {
    "input": {
        "cards": [13,11,10,7,4,3,1],
        "query": 7
    },
    "output": 3
}

print(locate_card(**test["input"]) == test["output"])


def locate_card_binary(cards,query):
    lo,hi = 0, len(cards)-1

    while lo <= hi:
        mid = (lo+hi) // 2
        mid_number = cards[mid]

        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1

    return -1 

print(locate_card_binary(**test["input"]) == test["output"])