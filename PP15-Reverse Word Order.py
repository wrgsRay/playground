if __name__ == '__main__':
    def rstring(sentence):
        lst = sentence.split()
        newlst = list()
        for i in reversed(lst):
            newlst.append(i)
        return ' '.join(x for x in newlst if x)

    userstring = input('Give me a sentence and I will reverse it for you')
    print(rstring(userstring))

