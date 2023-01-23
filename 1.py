def master_yoda(my_sentence):
    a = my_sentence.split()
    b = len(a)
    new_sentence = ''
    for i in range(b - 1, 0, -1):
        new_sentence = new_sentence + a[b - 1]
    return new_sentence

