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
        try :
            sub = int(parts[0])
        except ValueError :
            sub = 0
        for part in parts[1:] :
            sub = int(sub) - int(part)
        return sub
            
