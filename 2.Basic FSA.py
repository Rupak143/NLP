def fsa_match_end_ab(string):
    # Initial state
    state = 0
    
    # Transition rules
    for char in string:
        if state == 0 and char == 'a':
            state = 1
        elif state == 1 and char == 'b':
            state = 2
        elif char == 'a':  # Reset if 'a' appears again
            state = 1
        else:
            state = 0
    
    # Final state is 2
    return state == 2

# Test the FSA
strings = ["cab", "abc", "ab", "abab", "aaa"]
for s in strings:
    print(f"'{s}': {'Accepted' if fsa_match_end_ab(s) else 'Rejected'}")
