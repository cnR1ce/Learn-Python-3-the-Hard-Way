from nose.tools import *
from ex48.parser import *
from ex48.lexicon import *
from copy import deepcopy



def test_peek():
	'test function peek'
	test_list = scan('bear go to the door')
	result = peek(test_list)
	expected_value = 'noun'
	assert_equal(result, expected_value)

def test_match():
	'test function match'
	test_list_1 = scan('bear go to the door')
	test_list_2 = scan('bear go to the door')
	result_1 = match(test_list_1, 'noun')
	expected_value_1 = ('noun','bear')
	result_2 = match(test_list_2,'verb')
	expected_value_2 = None
	result_3 = match(scan(''), ' ')
	expected_value_3 = None
	assert_equal(result_1, expected_value_1)
	assert_equal(result_2, expected_value_2)
	assert_equal(result_3, expected_value_3)


def test_skip():
	'test function skip'
	test_list_1 = scan('bear go to the door')
	test_list_2 = scan('bear go to the door')
	skip(test_list_1, 'noun')
	result = test_list_1
	test_list_2.pop(0)
	expected_value = test_list_2
	assert_equal(result, expected_value)

def test_parse_verb():
	'test function parse_verb'

	#Condition 1
	test_list_1 = scan('go to the door')
	expected_value_1 = scan('go').pop(0)
	result_1 = parse_verb(test_list_1)
	assert_equal(result_1, expected_value_1)

	#Condition 2
	test_list_2 = scan('bear go to the door')
	assert_raises(ParserError, parse_verb, test_list_2)

