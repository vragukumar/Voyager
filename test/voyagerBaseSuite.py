import inspect
import json
class VoyagerTestSuiteBase(object):
    DOC_FILE = 'testPlan.json'
    DESC_TAG = 'DESCRIPTION'
    STEP_TAG = 'STEP'
    EXPECT_TAG = 'EXPECT'
    def __init__ (self):
        self.testMethods =  [method for method in dir(self) if callable(getattr(self, method)) and method.startswith('suite')]

    def run (self):
        for method in self.testMethods:
            getattr(self, method)()

    def getDocumentation (self, method):
        docstr = inspect.getdoc(getattr(self, method))
        testInfo = { 'description' : '',
                     'steps' : [],
                     'expect' : [],
                     'result' : 'PASS'}

        for line in docstr.split('@'):
            idx = line.find (self.DESC_TAG + ':') 
            if idx >= 0:
                testInfo['description'] =   [entry for entry in line.lstrip(self.DESC_TAG + ':').split('\n') if entry != '']

            idx = line.find (self.STEP_TAG + ':') 
            if idx >= 0:
                steps  = [entry for entry in line.lstrip(self.STEP_TAG + ':').split('\n') if entry != '']
                testInfo['steps'].extend(steps)

            idx = line.find (self.EXPECT_TAG+ ':') 
            if idx >= 0:
                steps  = [entry for entry in line.lstrip(self.EXPECT_TAG + ':').split('\n') if entry != '']
                testInfo['expect'].extend(steps)
        return testInfo
            
    def writeDoc (self):
        testDocs = {'totalTests' : 0,
                    'tests' : {}
                   }
        with open(self.DOC_FILE, 'a+') as testInfoFd:
            try:
                testDocs = json.load(testInfoFd)
            except:
                pass

        totalTests = testDocs['totalTests'] if 'totalTests' in testDocs else 0

        for method in self.testMethods:
            if 'tests' in  testDocs:
                testcaseName = self.__class__.__name__ + '-' +method
                if not testcaseName in testDocs['tests']:
                    testInfo = {}
                    testInfo ['index'] =  totalTests + 1
                    totalTests += 1
                else:
                    testInfo = testDocs['tests'][testcaseName]
                info = self.getDocumentation(method)
                print info
                testInfo['description'] = info['description']
                testInfo['steps'] = info['steps']
                testInfo['expect'] = info['expect']
                testInfo['result'] = info['result']
                testDocs ['tests'][testcaseName] =  testInfo
        testDocs['totalTests'] = totalTests 

        with open(self.DOC_FILE, 'w') as testInfoFd:
            testInfoFd.write(json.dumps(testDocs, indent=4, sort_keys=True))


