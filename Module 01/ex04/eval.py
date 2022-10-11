

class Evaluator():
    def zip_evaluate(coefs, words):
        if (not isinstance(words, list) or not all(isinstance(elem, str) for elem in words)):
            return -1
        if (not isinstance(coefs, list) or not all(isinstance(elem, float) for elem in coefs)):
            return -1
        if (len(words) != len(coefs)):
            return -1
        return sum([len(word) * coef for (word, coef) in zip(words, coefs)])

    def enumerate_evaluate(coefs, words):
        if (not isinstance(words, list) or not all(isinstance(elem, str) for elem in words)):
            return -1
        if (not isinstance(coefs, list) or not all(isinstance(elem, float) for elem in coefs)):
            return -1
        if (len(words) != len(coefs)):
            return -1
        return sum([len(word) * coefs[idx] for (idx, word) in enumerate(words)])
