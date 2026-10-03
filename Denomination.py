def no_notes(a):
    Q = [500, 200, 100, 50, 20, 10]
    X = 0
    for i in range(6):
        q = Q[i]
        x = a//q
        print("Notes of {} = {}".format(q, x))
        a = a%q
amount = int(input("Enter Totle Amount"))
no_notes(amount)