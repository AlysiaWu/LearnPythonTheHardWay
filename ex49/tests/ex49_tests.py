from nose.tools import *
from ex49.throwExceptionModule import *

def test_TestException():
	ex49C = Ex49Class()
	result = ex49C.testException(0)
	assert_equal(result, 'pass')
	assert_raises(ZxwException, ex49C.testException, 1)