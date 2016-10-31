import json
import rst

class testPlanDoc (object):
    def __init__ (self, info):
        self.info = info

    def generateDoc (self, doc):
        para = rst.Paragraph('\n')
        doc.add_child(para)
        sec = rst.Section('Test Case : ' + str(self.info['index']), 2)
        doc.add_child(sec)
        desc = self.info['description'][0].lstrip()
        desc = desc.rstrip()
        para = rst.Paragraph('**' + desc + '**\n\n')
        doc.add_child(para)
        tbl = rst.Table(header = ['Test Execution Steps'])
        for line in self.info['steps']:
            row = []
            row.append(line)
            tbl.add_item(row)
        doc.add_child(tbl)
        para = rst.Paragraph('\n**Expected Results**\n')
        doc.add_child(para)
        bList = rst.Bulletlist()
        for line in self.info['expect']:
            bList.add_item(line)
        doc.add_child(bList)
        para = rst.Paragraph('\n**Actual Results**\n')
        doc.add_child(para)
        para = rst.Paragraph('    PASS\n')
        doc.add_child(para)

if __name__ == '__main__':
    with open('testPlan.json') as testFd:
        testInfo =  json.load(testFd)

    testsList = [None] * int(testInfo['totalTests'])
    for testName, testDtls in testInfo['tests'].iteritems():
        testsList[int(testDtls['index'])-1] = testPlanDoc(testDtls)

    doc = rst.Document('Test Cases')
    for test in testsList:
        test.generateDoc(doc)
    with open('source/testCases.rst', 'w+') as testFd:
        testFd.writelines(doc.get_rst())
