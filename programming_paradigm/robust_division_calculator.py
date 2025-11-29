def safe_divide(numerator, denominator):

    try:
        numerator = float(numerator)
        denominator = float(denominator)
    

        result = numerator / denominator
        return result
    
    except ValueError:
        return "Input not a number"

    except ZeroDivisionError:
        return "Cannot Divide number by 0"