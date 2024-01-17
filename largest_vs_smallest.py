#here i am creating the shortest and the longest functions
#the len key counts the letters in each string
def shortest(strings):
    return min(strings, key=len)

def longest(strings):
    return max(strings, key=len)

strings_list = ["Ronaldo", "Rooney", "Beckham", "Cantona", "Van Nistelrooy"]
shortest_result = shortest(strings_list)
longest_result = longest(strings_list)

print("Shortest string:", shortest_result)
print("Longest string:", longest_result)