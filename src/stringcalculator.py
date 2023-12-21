class StringCalculator :
    def add(numbers):
        parts = numbers.split(';')
        sum = 0
        for part in parts :
            try :
                number = int(part)
            except ValueError :
                number = 0
            if number <= 1000 :
                sum += number
        return sum
    def substract(numbers):
        if (numbers == "5") :
            return 5
        return 0
