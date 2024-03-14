'''
Contains several helper functions and constants to help convert between roman and arabic numerals.
'''

ARABIC_TO_ROMAN = {1 : 'I', 4 : 'IV', 5 : 'V', 9 : 'IX', 40 : 'XL', 50 : 'L', 90 : 'XC', 100 : 'C', 400 : 'CD',
                   500 : 'D', 900 : 'CM', 1000 : 'M'}
ROMAN_TO_ARABIC = dict(list(map(lambda x : x[::-1], list(ARABIC_TO_ROMAN.items()))))

def convert(number: str, to: str) -> str:
    '''
    Given a number and a mode, convert it to the specified
    number system:
    '''
    try:
        if to == 'roman':
            result, number = '', int(number)
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
            elif number >= 9:
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
                num1 = ROMAN_TO_ARABIC(number[index])
                if index + 1 < len(number):
                    num2 = ROMAN_TO_ARABIC(number[index + 1])
                    if num1 >= num2:
                        result += num1
                        index += 1
                    else:
                        res += (num2 - num1)
                        i += 2
                else:
                    result += num1
                    index += 1
            return(result)
    except Exception as e:
        print(f'The following error ocurred: "{e}"')
