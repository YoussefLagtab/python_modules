class Evaluator:

    @staticmethod
    def zip_evaluate(words, coef):
        if len(words) != len(coef):
            return -1

        result = 0
        for w, c in zip(words, coef):
            result += len(w) * c

        return result

    @staticmethod
    def enumerate_evaluate(words, coef):
        if len(words) != len(coef):
            return -1

        result = 0
        for i, w in enumerate(words):
            result += len(w) * coef[i]

        return result
