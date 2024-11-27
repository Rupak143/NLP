def check_agreement(sentence):
    grammar = {
        "S": [["NP", "VP"]],
        "NP": [["Det", "N"]],
        "VP": [["V", "NP"]],
        "Det": [["the"]],
        "N": [["cat"], ["cats"]],
        "V": [["chases"], ["chase"]]
    }
    rules = {"singular": ["cat", "chases"], "plural": ["cats", "chase"]}
    parsed = parse(sentence.split(), ["S"])
    if parsed:
        for word in sentence.split():
            for rule, words in rules.items():
                if word in words:
                    print(f"{word} is {rule}.")
    else:
        print("Sentence is ungrammatical.")

check_agreement("the cats chase")
