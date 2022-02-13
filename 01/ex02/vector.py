class InValidVectorTypes(Exception):
    def __str__(self):
        return "Vector elements must be a floats or a lists of floats"


class Vector:
    def __init__(self, arg):
        if isinstance(arg, list):
            try:
                self.__is_valid_vector__(arg)
                self.values = self.__format_vec__(arg)
            except Exception as e:
                print(e)
                exit(1)
        elif isinstance(arg, tuple):
            try:
                self.__is_valid_range__(arg)
                self.values = self.__create_vec_from_range__(*arg)
            except Exception:
                print(Exception)
                exit(1)
        elif isinstance(arg, int):
            self.values = self.__create_vec_from_range__(0, arg)
        else:
            raise Exception("arg type is not valid")

        self.shape = self.__get_vector_shape__()

    def __is_valid_vector__(self, vec):
        elements_type = None
        col_length = 0
        for ele in vec:
            if not isinstance(ele, list) and not isinstance(ele, float):
                raise InValidVectorTypes()
            if not elements_type:
                elements_type = type(ele)
                continue
            if not isinstance(ele, elements_type):
                raise Exception("Can't mix floats with lists")
            if isinstance(ele, list):
                if not all(isinstance(e, float) for e in ele):
                    raise InValidVectorTypes()
                if col_length == 0:
                    col_length = len(ele)
                    continue
                if len(ele) != col_length:
                    raise Exception("Columns must be of the same length")

    def __is_valid_range__(self, _range):
        is_valid = True
        if len(_range) != 2:
            is_valid = False
        if not isinstance(_range[0], int) or not isinstance(_range[1], int):
            is_valid = False
        if _range[0] < 0 or _range[0] > _range[1]:
            is_valid = False

        if not is_valid:
            raise Exception("invalid range")

    def __create_vec_from_range__(self, start, end):
        values = []

        while start < end:
            values.append([float(start)])
            start += 1
        return values

    def __format_vec__(self, values):
        if len(values) == 1 and isinstance(values[0], list):
            return values[0]
        return values

    def __get_vector_shape__(self):
        vec_length = len(self.values)

        if vec_length == 0 or isinstance(self.values[0], float):
            return (1, vec_length)
        else:
            return (vec_length, len(self.values[0]))

    def __do_operation__(self, v1, v2, operation_func):
        if v1.shape != v2.shape:
            raise Exception("vectors not of the same shape")

        is_list_of_floats = isinstance(v1.values[0], float)
        values = []
        for i in range(v1.shape[0]):
            if is_list_of_floats:
                for j in range(v1.shape[1]):
                    val = operation_func(v1.values[i][j], v2.values[i][j])
                    values.append(val)
                continue

            col = []
            for j in range(v1.shape[1]):
                val = operation_func(v1.values[i][j], v2.values[i][j])
                col.append(val)
            values.append(col)

        return Vector(values)

    def __add__(self, other):
        return self.__do_operation__(self, other, lambda a, b: a + b)

    def __radd__(self, other):
        return other.__add__(self)

    def __sub__(self, other):
        return self.__do_operation__(self, other, lambda a, b: a - b)

    def __rsub__(self, other):
        return other.__sub__(self)
