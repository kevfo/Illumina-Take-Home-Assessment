from flask import Blueprint, jsonify
from utils import numbers

conversions = Blueprint('conversions', __name__)

@conversions.route('/to_roman/<arabic>', methods = ['POST'])
def to_roman(arabic):
    print(arabic)
    result = numbers.convert(str(arabic), 'roman')
    return(jsonify({'result' : result}))

@conversions.route('/to_arabic/<roman>', methods = ['POST'])
def to_arabic(roman):
    print(roman)
    result = numbers.convert(roman, 'arabic')
    return(jsonify({'result' : result}))