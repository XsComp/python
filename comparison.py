def sum_of_five(a=1, b=2, c=3, d=4, e=5):
    return a + b + c + d + e

def comparison(x:int, y:int) -> str:
    if x < y:
        return "smaller than"
    elif x > y:
        return "greater than"
    else:
        return "equal to"
