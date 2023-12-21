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
        sub = 0
        if (";" in numbers) :
            sub = 1
        try :
            sub = int(numbers)
        except ValueError :
            pass
        return sub
            
