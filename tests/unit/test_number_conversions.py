import unittest, os, sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, project_root)
from utils import numbers

ROMAN_TO_ARAB = {'III' : 3, 'XVIII' : 18, 'XVI' : 16, 'I' : 1, 'DCCCIII' : 803, 'CIX' : 109, 'MMXVI' : 2016}

def test_roman_numerals_should_map_to_right_arabic_numerals():
    for i in ROMAN_TO_ARAB:
        assert numbers.convert(i, 'arabic') == str(ROMAN_TO_ARAB[i])

def test_arabic_numerals_should_map_to_right_roman_numerals():
    for i in ROMAN_TO_ARAB.items():
        assert numbers.convert(i[1], 'roman') == i[0]