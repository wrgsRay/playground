if __name__ == '__main__':
    a = [5, 10, 15, 20, 25]

    def listends(lst):
        if type(lst) == list:
            newlst = list()
            newlst.append(lst[0])
            newlst.append(lst[-1])
            return newlst
        else:
            return 'Error'

    print(listends(a))
