import pytest

@pytest.fixture()
def setup():
    print("this is setup method")
# @pytest.yield_fixture()
# def setup():
#     print("this is executed before test method")
#     yield
#     print("this is executed after test method")



def testMethod1(setup):
    print("This is test method1")

def testMethod2(setup):
    print("This is test method2")