from flask import Blueprint, jsonify
from utils import numbers

conversions = Blueprint('conversions', __name__)

@conversions.route('/to_roman/<arabic>', methods = ['GET'])
def to_roman(arabic):
    print('this works!')
    #jsonify({'result' : })

@conversions.route('/to_arabic/<roman>', methods = ['GET'])
def to_arabic(roman):
    print('this works')