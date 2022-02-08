t = (0, 4, 132.42222, 10000, 12345.67)

mod = 'module_' + (str(t[0]) if t[0] > 10 else '0' + str(t[0]))
ex = 'ex_' + (str(t[1]) if t[1] > 10 else '0' + str(t[1]))
float_nb = "{0:.2f}".format(t[2])
print(f'{mod}, {ex} : {"{0:.2f}".format(t[2])}, {t[3]:.2e}, {t[4]:.2e}')
