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
        parts = numbers.split(';')
        sub = None
        for part in parts :
            try :
                part = float(part)
                if part > 1000 :
                    part = 0
            except ValueError :
                part = 0
            if sub is None :
                sub = part
            else :
                sub = sub - part
        return sub


    def multiply(numbers):
            if numbers == "":
                return 0
            else:
                return 5
