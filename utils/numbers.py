'''
Contains several helper functions and constants to help convert between roman and arabic numerals.
'''

ARABIC_TO_ROMAN = {1 : 'I', 5 : 'V', 10 : 'X', 50 : 'L', 100 : 'C', 500 : 'D', 1000 : 'M'}
ROMAN_TO_ARABIC = dict(list(map(lambda x : x[::-1], list(ARABIC_TO_ROMAN.items()))))

def convert(number: str, to: str) -> str:
    '''
    Given a number and a mode, convert it to the specified
    number system:
    '''
    try:
        number = number.upper()
        if to == 'roman':
            result, number = '', int(number)
            while number > 0:
                if number >= 1000:
                    result += 'M'
                    number -= 1000
                elif number >= 900:
                    result += 'CM'
                    number -= 900
                elif number >= 500:
                    result += 'D'
                    number -= 500
                elif number >= 400:
                    result += 'CD'
                    number -= 400
                elif number >= 100:
                    result += 'C'
                    number -= 100
                elif number >= 90:
                    result += 'XC'
                    number -= 90
                elif number >= 50:
                    result += 'L'
                    number -= 50
                elif number >= 40:
                    result += 'XL'
                    number -= 40
                elif number >= 10:
                    result += 'X'
                    number -= 10
                elif number == 9:
                    result += 'IX'
                    number -= 9
                elif number >= 5:
                    result += 'V'
                    number -= 5
                elif number >= 4:
                    result += 'IV'
                    number -= 4
                else:
                    result += 'I'
                    number -= 1
            return(result)
        elif to == 'arabic':
            result, index = 0, 0
            while index < len(number):
                num1 = ROMAN_TO_ARABIC[number[index]]
                if index + 1 < len(number):
                    num2 = ROMAN_TO_ARABIC[number[index + 1]]
                    if num1 >= num2:
                        result += num1
                        index += 1
                    else:
                        result += (num2 - num1)
                        index += 2
                else:
                    result += num1
                    index += 1
            return(str(result))
    except Exception as e:
        return('???')
