spam = ['apples', 'bananas', 'tofu', 'cats', 'aaaaa', True]
for i in range(len(spam)):
    if i < len(spam) - 1:
        print(str(spam[i]), end=", ")
    else:
        print("and " + str(spam[i]))
