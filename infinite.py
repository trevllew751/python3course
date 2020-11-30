def current_beat():
    beats = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(beats):
            i = 0
        yield beats[i]
        i += 1


counter = current_beat()
for i in range(20):
    print(next(counter))

