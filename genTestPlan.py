import json

class testPlanDoc (object):
    def __init__ (self, info):
        self.info = info

    def generateDoc (self, fd):
        fd.writelines('**' + ''.join(self.info['description']).lstrip()+ '**')
        fd.writelines('\n\n')
        fd.writelines('- **Test Steps**\n\n')
        for line in self.info['steps']:
            fd.writelines('--' + line)
            fd.writelines('\n\n')
            
        fd.writelines('- **Expected Results**\n')
        fd.writelines('\n\n')
        for line in self.info['expect']:
            fd.writelines('--' + line)
            fd.writelines('\n\n')
        fd.writelines('- **Actual Results**\n')


if __name__ == '__main__':
    with open('testPlan.json') as testFd:
        testInfo =  json.load(testFd)

    testsList = [None] * int(testInfo['totalTests'])
    for testName, testDtls in testInfo['tests'].iteritems():
        testsList [ int (testDtls['index']) -1] = testPlanDoc(testDtls)
    with open('source/testPlan2.rst', 'w+') as testFd:
        testFd.writelines('Test Cases\n')
        testFd.writelines('==========\n')
        testFd.writelines('\n\n')
        for test in testsList:
            test.generateDoc(testFd)
        
