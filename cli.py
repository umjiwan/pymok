from omok import omok

om = omok()
count = 1

while True:
    stone = 1 if count % 2 else 2
    print(om.board)
    x, y = input("x y : ").split(" ")
    event = om.put(int(x), int(y), stone)
    if not event:
        count += 1
    elif event == "end":
        print(om.board)
        break
        