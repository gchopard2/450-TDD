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
        parts = numbers.split(';')
        product = None
        for part in parts:
            try:
                part = float(part)
            except ValueError:
                part = 1  # Treat non-numeric values as 1 for multiplication
            if product is None:
                product = part
            else:
                product = product * part
        return product