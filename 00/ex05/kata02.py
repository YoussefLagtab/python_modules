t = (3, 30, 2019, 9, 25)

hour = str(t[0]) if t[0] > 10 else '0' + str(t[0])
min = str(t[1]) if t[1] > 10 else '0' + str(t[1])
month = str(t[3]) if t[3] > 10 else '0' + str(t[3])
day = str(t[4]) if t[4] > 10 else '0' + str(t[4])

print(f'{month}/{day}/{t[2]} {hour}:{min}')
