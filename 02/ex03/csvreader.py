class CsvReader():
    def __init__(
            self, filename=None, sep=',', header=False,
            skip_top=0, skip_bottom=0):
        try:
            file = open(filename, 'r')
            lines = list(filter(lambda e: len(e), file.read().split('\n')))
            self.file = file

            self.error = self.__is_data_corrupted__(lines, sep)
            if self.error:
                return

            self.__parse_data__(lines, sep, header, skip_top, skip_bottom)

        except Exception:
            self.error = True

    def __parse_data__(self, lines, sep, header, skip_top, skip_bottom):
        self.header = None
        if header:
            self.header = lines[0].split(sep)
            self.header = list(map(lambda e: e.strip('" '), self.header))

        skip_top += int(header)
        lines = lines[skip_top:-skip_bottom]

        data = list(map(lambda l: l.split(sep), lines))
        data = list(map(lambda l: list(map(lambda e: e.strip('" '), l)), data))
        self.data = data

    def __is_data_corrupted__(self, lines, sep):
        fileds_nb = 0
        lines_len = 0

        for li in lines:
            if fileds_nb == 0:
                fileds_nb = len(li.split(sep))
                continue
            if len(li.split(sep)) != fileds_nb:
                return True

            if lines_len == 0:
                lines_len = len(li)
                continue
            if len(li) != lines_len:
                return True

        return False

    def __enter__(self):
        return self if not self.error else None

    def __exit__(self, *_args):
        try:
            self.file.close()
        except Exception:
            pass

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header


with CsvReader(1, header=True, skip_top=2, skip_bottom=2) as file:
    if file is None:
        print("ERROR")
        exit(1)

    data = file.getdata()
    header = file.getheader()
    print('Header:', header)
    print(f'Rocords({len(data)}):')
    for d in data:
        print(d)
