import curses
from time import sleep, time as now


def ft_progress(listy):
    curses.setupterm()

    bar_len = 50
    length = len(listy)

    remaining_time = 0
    elapsed_time = 0
    starting_time = now()

    for index, ele in enumerate(listy):
        items = index + 1
        remaining_time = '%.2f' %\
            ((now() - starting_time) / items * (length - items))
        elapsed_time = '%.2f' % (now() - starting_time)
        p_format = 'ETA: {}s [{}%] [{}{}] {}/{} | elapsed time {}s'
        progress = int(index * bar_len / length)
        progress_str = '=' * progress
        spaces_str = ''
        if items != length:
            spaces_str += '>' + ' ' * (bar_len - progress - 1)
        elapsed_percent = int(items * 100 / length)
        p_info = [remaining_time, elapsed_percent, progress_str]
        p_info += [spaces_str, items, length, elapsed_time]

        print(curses.tigetstr('el').decode(), end='')
        print(p_format.format(*p_info))
        if items != length:
            print(curses.tigetstr('cuu1').decode(), end='')

        yield ele
