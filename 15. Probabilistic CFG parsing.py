from nltk import PCFG
from nltk.parse.viterbi import ViterbiParser

grammar = PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.6] | 'cats' [0.4]
    VP -> V NP [0.7] | V [0.3]
    Det -> 'the' [1.0]
    N -> 'cat' [1.0]
    V -> 'chases' [0.5] | 'chase' [0.5]
""")
parser = ViterbiParser(grammar)

sentence = ["the", "cat", "chases"]
for tree in parser.parse(sentence):
    print(tree)
