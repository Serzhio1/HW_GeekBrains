def thesaurus(*args):
    for i in args:
        first_letter = i[0]
        if first_letter in handlist:
            handlist[first_letter] += [i]
        else:
            handlist[first_letter] = [i]
    return handlist

handlist = {
}
print(thesaurus('Игорь', 'Ира', 'Маша', 'Петя'))
