import sys
log=open('testlogo','a')
from testapi import moreTests, runNextTest ,testName
def testdrive():
    while moreTest():
        try :
            runNextTest()
        except:
            print('Failed',testName(),sys.exc_info()[:2],file=log)
        else:
            print('Passed' ,testName(),file=log)

testdrive()
