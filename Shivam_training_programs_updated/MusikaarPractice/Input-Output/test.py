with open('test.txt', 'r+') as rf:
    with open('test2.txt', 'r+') as wf:
        for i in rf:
            wf.write(i)
            print(wf.read())


print("done")

