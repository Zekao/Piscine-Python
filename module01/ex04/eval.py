class Evaluator:
    
    @staticmethod
    def zip_evaluate(coeffs, words):
        if (len(coeffs) != len(words)):
            return (-1)
        else:
            return sum(coeffs * len(word) for word, coeffs in zip(words, coeffs))
    
    @staticmethod
    def enumerate_evaluate(coeffs, words):
        if (len(coeffs) != len(words)):
            return (-1)
        else:
            return sum(coeffs[i] * len(word) for i, word in enumerate(words))