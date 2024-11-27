def pluralize(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word.endswith(('s', 'x', 'z', 'ch', 'sh')):
        return word + 'es'
    elif word in ['man', 'woman']:
        return word[:-2] + 'en'
    elif word == 'child':
        return 'children'
    elif word == 'foot':
        return 'feet'
    elif word == 'tooth':
        return 'teeth'
    elif word == 'mouse':
        return 'mice'
    else:
        return word + 's'

# Test the FSM
words = ['cat', 'dog', 'box', 'lady', 'man', 'child', 'tooth']
plural_forms = [pluralize(word) for word in words]
print("Plural Forms:", plural_forms)
