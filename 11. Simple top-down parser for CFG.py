grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased"], ["saw"]]
}

def parse(tokens, symbol):
    if not tokens:
        return symbol == []
    if not symbol:
        return False
    rule = symbol[0]
    if rule in grammar:
        for prod in grammar[rule]:
            if parse(tokens, prod + symbol[1:]):
                return True
    elif tokens[0] == rule:
        return parse(tokens[1:], symbol[1:])
    return False

tokens = ["the", "cat", "chased", "the", "dog"]
print(parse(tokens, ["S"]))
