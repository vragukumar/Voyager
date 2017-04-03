import unittest, time, json, logging, sys
from voyagerSetup import testSetup
from flexNode import FlexNode
from flexswitchV2 import FlexSwitch

logging.basicConfig(stream=sys.stderr)
log = logging.getLogger("VoyagerTest")
log.setLevel(logging.DEBUG)

resetHw = False

class VoyagerTest(unittest.TestCase):

    def __init__(self, testMethod, attrs = {}):
        self.ModuleId = attrs.get('ModuleId', None)
        self.NwIntfId = attrs.get('NwIntfId', None)
        self.ClntIntfId = attrs.get('ClntIntfId', None)
        self.XponderId = attrs.get('XponderId', None)
        self.XponderMode = attrs.get('XponderMode', None)
        self.AdminState = attrs.get('AdminState', None)
        self.ModuleState =  attrs.get('ModuleState', None)
        self.XponderDescription = attrs.get('XponderDescription', None)
        self.TxPower = attrs.get('TxPower', None)
        self.RxPower = attrs.get('RxPower', None)
        self.RxPwrDev = attrs.get('RxPwrDev', None)
        self.ChannelNumber = attrs.get('ChannelNumber', None)
        self.ModFmt = attrs.get('ModFmt', None)
        self.FECMode = attrs.get('FECMode', None)
        self.DiffEncoding = attrs.get('DiffEncoding', None)
        self.HostTxEqLfCtle = attrs.get('HostTxEqLfCtle', None)
        self.HostTxEqCtle = attrs.get('HostTxEqCtle', None)
        self.HostTxEqDfe = attrs.get('HostTxEqDfe', None)
        self.LocalPort = attrs.get('LocalPort', None)
        self.RemotePort = attrs.get('RemotePort', None)
        self.PortAdminState = attrs.get('PortAdminState', 'DOWN')
        self.PeerNwIntfId = attrs.get('PeerNwIntfId', 1)
        self.InServiceWireVlanCfg = {
                    2 : {
                        "UntagIntfList": ["fpPort1", "fpPort13"],
                        },
                    3 : {
                        "UntagIntfList": ["fpPort2", "fpPort14"],
                        },
                    4 : {
                        "UntagIntfList": ["fpPort3", "fpPort15"],
                        },
                    5 : {
                        "UntagIntfList": ["fpPort4", "fpPort16"],
                        },
                    6 : {
                        "UntagIntfList": ["fpPort5", "fpPort17"],
                        },
                    7 : {
                        "UntagIntfList": ["fpPort6", "fpPort18"],
                        },
                    8 : {
                        "UntagIntfList": ["fpPort7", "fpPort19"],
                        },
                    9 : {
                        "UntagIntfList": ["fpPort8", "fpPort20"],
                        },
                }
        self.InServiceOverSubVlanCfg = {
                    2 : {
                        "IntfList": ["fpPort13"],
                        "UntagIntfList": ["fpPort1"],
                        },
                    3 : {
                        "IntfList": ["fpPort14"],
                        "UntagIntfList": ["fpPort2"],
                        },
                    4 : {
                        "IntfList": ["fpPort15"],
                        "UntagIntfList": ["fpPort3"],
                        },
                    5 : {
                        "IntfList": ["fpPort16"],
                        "UntagIntfList": ["fpPort4"],
                        },
                    6 : {
                        "IntfList": ["fpPort17"],
                        "UntagIntfList": ["fpPort5"],
                        },
                    7 : {
                        "IntfList": ["fpPort18"],
                        "UntagIntfList": ["fpPort6"],
                        },
                    8 : {
                        "IntfList": ["fpPort19"],
                        "UntagIntfList": ["fpPort7"],
                        },
                    9 : {
                        "IntfList": ["fpPort20"],
                        "UntagIntfList": ["fpPort8"],
                        },
                   10 : {
                        "IntfList": ["fpPort15"],
                        "UntagIntfList": ["fpPort9"],
                        },
                   11 : {
                        "IntfList": ["fpPort16"],
                        "UntagIntfList": ["fpPort10"],
                        },
                   12 : {
                        "IntfList": ["fpPort17"],
                        "UntagIntfList": ["fpPort11"],
                        },
                   13 : {
                        "IntfList": ["fpPort18"],
                        "UntagIntfList": ["fpPort12"],
                        },
                }
        self.node = FlexNode(conf = testSetup['SwitchInfo'], waitAfterCofig = False)
        self.restIf = self.node.getRestIf()
        self.trafficGenNode = FlexNode(conf = testSetup['TrafficGenInfo'], waitAfterCofig = False)
        self.trafficGenRestIf = self.trafficGenNode.getRestIf()
        global resetHw 
        resetHw = attrs.get('ResetHw', False)
        super (VoyagerTest, self).__init__(testMethod)

    def setUp(self):
        log.debug('************** Executing SetUp **************')
        global resetHw 
        if resetHw == True:
            self.restIf.updateDWDMModule(ModuleId = 0, AdminState = 'UP')
            for nwIntfId in range(0,2):
                self.restIf.updateDWDMModuleNwIntf(ModuleId = 0, NwIntfId = nwIntfId, TxPower = 1,
                    ChannelNumber = 52, ModulationFmt = '16QAM', FECMode = '25%OvrHeadSDFEC',
                    DiffEncoding = False)
            for clntIntfId in range(0,4):
                self.restIf.updateDWDMModuleClntIntf(ModuleId = 0, ClntIntfId = clntIntfId,
                        HostTxEqLfCtle = 2, HostTxEqCtle = 19, HostTxEqDfe = 3)
        resetHw = False

    def tearDown(self):
        log.debug('************** Executing TearDown **************')

    def verifyAC400Inventory(self):
        #Following constants defined based on actual testbed H/W
        ACACIA_VENDOR_NAME_STR = 'Acacia Comm Inc.'
        ACACIA_VENDOR_PART_NUM = 'AC400-001-00H'
        ACACIA_MODULE_HW_VER = '48.49'
        ACACIA_VENDOR_DATE_CODE = '20160527'
        log.debug('************** Executing VerifyAC400Inventory **************')
        res = self.restIf.getAllDWDMModuleStates()
        for obj in res:
            self.assertEqual(obj['Object']['VendorName'], ACACIA_VENDOR_NAME_STR, 'Vendor name mismatch in AC400 inventory')
            self.assertEqual(obj['Object']['VendorPartNum'], ACACIA_VENDOR_PART_NUM, 'Vendor part number mismatch in AC400 inventory')
            self.assertEqual(obj['Object']['ModuleHWVersion'], ACACIA_MODULE_HW_VER, 'Vendor module HW version mismatch in AC400 inventory')
            self.assertEqual(obj['Object']['VendorDateCode'], ACACIA_VENDOR_DATE_CODE, 'Vendor date code mismatch in AC400 inventory')

    def verifyAsicInventory(self):
        #Following constants defined based on actual testbed H/W
        ASIC_VENDOR_ID = '14e4'
        ASIC_PART_NUM = 'b960'
        ASIC_REV_ID = '12'
        log.debug('************** Executing Verify ASIC Inventory **************')
        res = self.restIf.getAllAsicGlobalStates()
        for obj in res:
            self.assertEqual(obj['Object']['VendorId'], ASIC_VENDOR_ID)
            self.assertEqual(obj['Object']['PartNumber'], ASIC_PART_NUM)
            self.assertEqual(obj['Object']['RevisionId'], ASIC_REV_ID)

    def configXponderMode(self):
        res = self.restIf.updateXponderGlobal(XponderId = self.XponderId, XponderMode = self.XponderMode)

    def verifyXponderMode(self):
        res = self.restIf.getXponderGlobalState(XponderId = self.XponderId)
        result = res.json()
        mode = result['Object']['XponderMode']
        self.assertEqual(mode, self.XponderMode, "XponderMode verification failed : current mode " + mode + " expected mode " + self.XponderMode)

    def updateXponderGlobalDescription(self):
        res = self.restIf.updateXponderGlobal(XponderId = self.XponderId, XponderDescription= self.XponderDescription)

    def verifyXponderGlobalDescription(self):
        res = self.restIf.getXponderGlobalState(XponderId = self.XponderId)
        obj = res.json()
        desc = obj['Object']['XponderDescription']
        self.assertEqual(desc, self.XponderDescription, 'Failed to validate xponder description. Current description - ' + desc + ' Expected -' + self.XponderDescription)

    def verifyInServiceWireCfg(self):
        res = self.restIf.getAllVlans()
        for obj in res:
            vlanId = obj['Object']['VlanId']
            self.assertTrue(self.InServiceWireVlanCfg.has_key(vlanId), "Failure verifying inservice wire cfg, unexpected vlan - " + str(vlanId))
            for port in obj['Object']['UntagIntfList']:
                self.assertTrue(port in self.InServiceWireVlanCfg[vlanId]['UntagIntfList'], "Failure verifying inservice wire cfg, unexpected untagged port member - " + str(port))

    def verifyInServiceOverSubCfg(self):
        res = self.restIf.getAllVlans()
        for obj in res:
            vlanId = obj['Object']['VlanId']
            self.assertTrue(self.InServiceOverSubVlanCfg.has_key(vlanId), "Failure verifying inservice oversub cfg, unexpected vlan - " + str(vlanId))
            for port in obj['Object']['IntfList']:
                self.assertTrue(port in self.InServiceOverSubVlanCfg[vlanId]['IntfList'], "Failure verifying inservice oversub cfg, unexpected tagged port member - " + str(port))
            for port in obj['Object']['UntagIntfList']:
                self.assertTrue(port in self.InServiceOverSubVlanCfg[vlanId]['UntagIntfList'], "Failure verifying inservice oversub cfg, unexpected untagged port member - " + str(port))

    def verifyOutOfServiceCfg(self):
        res = self.restIf.getAllVlans()
        self.assertTrue(len(res) == 0, "Failure verifying OutOfServiceCfg, unexpected vlan configuration exists")

    def updateDWDMModule(self):
        res = self.restIf.updateDWDMModule(ModuleId = self.ModuleId, AdminState = self.AdminState)

    def verifyDWDMModuleState(self):
        success = False
        waitIterCnt = 0
        expectedState = self.ModuleState
        while (waitIterCnt < 10):
            res = self.restIf.getAllDWDMModuleStates()
            for obj in res:
                if obj['Object']['ModuleId'] == self.ModuleId:
                    state = obj['Object']['ModuleState']
                    if state == expectedState:
                        success = True
            if success:
                break
            waitIterCnt += 1
            time.sleep(10)
        self.assertTrue(success, "AC400 module state verification failed, timeout after waiting for 100s. Current module state = " + state)

    def verifyNWIntfCfgInventory(self):
        nwIntfId0Present = False
        nwIntfId1Present = False
        res = self.restIf.getAllDWDMModuleNwIntfs()
        for obj in res:
            if obj['Object']['NwIntfId'] == 0:
                nwIntfId0Present = True
            if obj['Object']['NwIntfId'] == 1:
                nwIntfId1Present = True
        self.assertTrue(nwIntfId0Present and nwIntfId1Present, "Nw Intf config object validation failed")

    def verifyNWIntfStateInventory(self):
        nwIntfId0Present = False
        nwIntfId1Present = False
        res = self.restIf.getAllDWDMModuleNwIntfStates()
        for obj in res:
            if obj['Object']['NwIntfId'] == 0:
                nwIntfId0Present = True
            if obj['Object']['NwIntfId'] == 1:
                nwIntfId1Present = True
        self.assertTrue(nwIntfId0Present and nwIntfId1Present, "Nw Intf state object validation failed")

    def updateDWDMModuleNwIntf(self):
        res = self.restIf.updateDWDMModuleNwIntf(ModuleId = self.ModuleId,
                NwIntfId = self.NwIntfId,
                TxPower = self.TxPower,
                ChannelNumber = self.ChannelNumber,
                ModulationFmt = self.ModFmt,
                FECMode = self.FECMode,
                DiffEncoding = self.DiffEncoding
                )
        if self.TxPower != None:
            #Wait for txpower changes to take effect
            time.sleep(2)

        if ((self.ChannelNumber != None) or (self.ModFmt != None) or
            (self.FECMode != None) or (self.DiffEncoding != None)):
            #Wait for module to become operational again
            self.ModuleState = 'READY'
            self.verifyDWDMModuleState()
        
    def isRxPowerWithinDeviation(self, RxPwr):
        if (RxPwr >= (self.RxPower - self.RxPwrDev)) and (RxPwr <= (self.RxPower + self.RxPwrDev)):
            return True
        else:
            return False

    def verifyNwIntfState(self):
        res = self.restIf.getAllDWDMModuleNwIntfStates()
        for elem in res:
            obj = elem['Object']
            if (obj['ModuleId'] == self.ModuleId) and (obj['NwIntfId'] == self.NwIntfId):
                self.assertTrue(self.isRxPowerWithinDeviation(obj['RxPower']), "NwIntf RxPower not within expected range for NwIntfId " + str(self.NwIntfId) + " Actual RxPower - " + str(obj['RxPower']) + " Expected RxPower - " + str(self.RxPower))
                break

    def verifyPeerNwIntfIsOperational(self):
        #This method validates that the peer NwIntf is transmitting light by reading local BER
        res = self.restIf.getAllDWDMModuleNwIntfStates()
        for elem in res:
            obj = elem['Object']
            if (obj['ModuleId'] == self.ModuleId) and (obj['NwIntfId'] == self.NwIntfId):
                self.assertTrue(obj['CurrentBER'] > 0, "NwIntf " + str(self.NwIntfId) + " is not operational")

    def verifyPeerNwIntfIsNotOperational(self):
        #This method validates that the peer NwIntf is not transmitting light by verifiying local BER < 0
        res = self.restIf.getAllDWDMModuleNwIntfStates()
        for elem in res:
            obj = elem['Object']
            if (obj['ModuleId'] == self.ModuleId) and (obj['NwIntfId'] == self.NwIntfId):
                self.assertTrue(obj['CurrentBER'] < 0, "NwIntf " + str(self.NwIntfId) + " is not operational")

    def verifyNwIntfBERValuesAreValid(self):
        res = self.restIf.getAllDWDMModuleNwIntfStates()
        for elem in res:
            obj = elem['Object']
            if (obj['ModuleId'] == self.ModuleId) and (obj['NwIntfId'] == self.NwIntfId):
                self.assertTrue(obj['CurrentBER'] > 0, "NwIntf " + str(self.NwIntfId) + " invalid BER reading")
                self.assertTrue(obj['MinBEROverPMInterval'] > 0, "NwIntf " + str(self.NwIntfId) + " invalid BER reading")
                self.assertTrue(obj['AvgBEROverPMInterval'] > 0, "NwIntf " + str(self.NwIntfId) + " invalid BER reading")
                self.assertTrue(obj['MaxBEROverPMInterval'] > 0, "NwIntf " + str(self.NwIntfId) + " invalid BER reading")

    def verifyClntIntfCfgInventory(self):
        clntfIntfId0Present = False
        clntfIntfId1Present = False
        res = self.restIf.getAllDWDMModuleClntIntfs()
        for obj in res:
            if obj['Object']['ClntIntfId'] == 0:
                clntfIntfId0Present = True
            if obj['Object']['ClntIntfId'] == 1:
                clntfIntfId1Present = True
        self.assertTrue(clntfIntfId0Present and clntfIntfId1Present, "Clnt Intf config object validation failed")

    def verifyClntIntfStateInventory(self):
        clntfIntfId0Present = False
        clntfIntfId1Present = False
        clntfIntfId2Present = False
        clntfIntfId3Present = False
        res = self.restIf.getAllDWDMModuleClntIntfStates()
        for obj in res:
            if obj['Object']['ClntIntfId'] == 0:
                clntfIntfId0Present = True
            if obj['Object']['ClntIntfId'] == 1:
                clntfIntfId1Present = True
            if obj['Object']['ClntIntfId'] == 2:
                clntfIntfId2Present = True
            if obj['Object']['ClntIntfId'] == 3:
                clntfIntfId3Present = True
        self.assertTrue(clntfIntfId0Present and clntfIntfId1Present and clntfIntfId2Present and clntfIntfId3Present, "Clnt Intf state object validation failed")

    def updateDWDMModuleClntIntf(self):
        res = self.restIf.updateDWDMModuleClntIntf(
                ModuleId = self.ModuleId,
                ClntIntfId = self.ClntIntfId,
                HostTxEqLfCtle = self.HostTxEqLfCtle,
                HostTxEqCtle = self.HostTxEqCtle,
                HostTxEqDfe = self.HostTxEqDfe
                )

    def verifyDWDMModuleClntIntfElecParams(self):
        res = self.restIf.getAllDWDMModuleClntIntfs()
        for elem in res:
            obj = elem['Object']
            if (obj['ModuleId'] == self.ModuleId) and (obj['ClntIntfId'] == self.ClntIntfId):
                self.assertEqual(obj['HostTxEqLfCtle'], self.HostTxEqLfCtle, "HostTxEqLfCtle setting mismatch for clnt intf " + str(self.ClntIntfId))
                self.assertEqual(obj['HostTxEqCtle'], self.HostTxEqCtle, "HostTxEqCtle setting mismatch for clnt intf " + str(self.ClntIntfId))
                self.assertEqual(obj['HostTxEqDfe'], self.HostTxEqDfe, "HostTxEqDfe setting mismatch for clnt intf " + str(self.ClntIntfId))

    def configPortsAndReadEvents(self):
        self.restIf.updatePort(IntfRef = self.LocalPort, AdminState = self.PortAdminState)
        self.trafficGenRestIf.updatePort(IntfRef = self.RemotePort, AdminState = self.PortAdminState)

    def configTxPowerAndReadEvents(self):
        self.updateDWDMModuleNwIntf()

    def configPortsAndReadFaults(self):
        self.restIf.updatePort(IntfRef = self.LocalPort, AdminState = self.PortAdminState)
        self.trafficGenRestIf.updatePort(IntfRef = self.RemotePort, AdminState = self.PortAdminState)
        #Force port down
        self.trafficGenRestIf.updatePort(IntfRef = self.RemotePort, AdminState = 'DOWN')
        time.sleep(1)
        #Read all faults 
        faultFound = False
        res = self.restIf.getAllFaultStates()
        for elem in res:
            obj = elem['Object']
            if (obj['SrcObjKey'].endswith(self.LocalPort) and (obj['EventName'] == 'PortOperStateDown') and
                obj['ResolutionReason'] == 'N/A'):
                faultFound = True
                break
        self.assertTrue(faultFound, "PortOperStateDown fault not found in fault database for port - " + self.LocalPort)

    def configTxPowerAndReadFaults(self):
        self.updateDWDMModuleNwIntf()
        time.sleep(1)
        faultFound = False
        #Read all faults 
        keyStr = 'ModuleId:'+ str(self.ModuleId) + ' NwIntfId:' + str(self.PeerNwIntfId)
        res = self.restIf.getAllFaultStates()
        for elem in res:
            obj = elem['Object']
            if (obj['SrcObjKey'].endswith(keyStr) and (obj['EventName'] == 'RXLOS') and
                obj['ResolutionReason'] == 'N/A'):
                faultFound = True
                break
        self.assertTrue(faultFound, "RXLOS fault not found for ModuleId :" + str(self.ModuleId) + " NwIntfId :" +  str(self.PeerNwIntfId))

    def configPortsAndReadAlarms(self):
        self.restIf.updatePort(IntfRef = self.LocalPort, AdminState = self.PortAdminState)
        self.trafficGenRestIf.updatePort(IntfRef = self.RemotePort, AdminState = self.PortAdminState)
        #Force port down
        self.trafficGenRestIf.updatePort(IntfRef = self.RemotePort, AdminState = 'DOWN')
        #Wait 3 sec for alarm to be generated
        time.sleep(3)
        #Read all alarms 
        faultFound = False
        res = self.restIf.getAllAlarmStates()
        for elem in res:
            obj = elem['Object']
            if (obj['SrcObjKey'].endswith(self.LocalPort) and (obj['EventName'] == 'PortOperStateDown') and
                obj['ResolutionReason'] == 'N/A'):
                faultFound = True
                break
        self.assertTrue(faultFound, "PortOperStateDown alarm not found in fault database for port - " + self.LocalPort)

    def configTxPowerAndReadAlarms(self):
        self.updateDWDMModuleNwIntf()
        #Wait 3 sec for alarm to be generated
        time.sleep(3)
        faultFound = False
        #Read all faults 
        keyStr = 'ModuleId:'+ str(self.ModuleId) + ' NwIntfId:' + str(self.PeerNwIntfId)
        res = self.restIf.getAllFaultStates()
        for elem in res:
            obj = elem['Object']
            if (obj['SrcObjKey'].endswith(keyStr) and (obj['EventName'] == 'RXLOS') and
                obj['ResolutionReason'] == 'N/A'):
                faultFound = True
                break
        self.assertTrue(faultFound, "RXLOS alarm not found for ModuleId :" + str(self.ModuleId) + " NwIntfId :" +  str(self.PeerNwIntfId))

    def configPortsAndVerifyFaultResolution(self):
        self.restIf.updatePort(IntfRef = self.LocalPort, AdminState = self.PortAdminState)
        self.trafficGenRestIf.updatePort(IntfRef = self.RemotePort, AdminState = self.PortAdminState)
        time.sleep(1)
        #Read all faults 
        faultFound = False
        res = self.restIf.getAllFaultStates()
        for elem in res:
            obj = elem['Object']
            if (obj['SrcObjKey'].endswith(self.LocalPort) and (obj['EventName'] == 'PortOperStateDown') and
                obj['ResolutionReason'] != 'N/A'):
                faultFound = True
                break
        self.assertTrue(faultFound, "PortOperStateDown fault not cleared in fault database for port - " + self.LocalPort)

    def configTxPowerAndVerifyFaultResolution(self):
        self.updateDWDMModuleNwIntf()
        faultFound = False
        time.sleep(1)
        #Read all faults 
        keyStr = 'ModuleId:'+ str(self.ModuleId) + ' NwIntfId:' + str(self.PeerNwIntfId)
        res = self.restIf.getAllFaultStates()
        for elem in res:
            obj = elem['Object']
            if (obj['SrcObjKey'].endswith(keyStr) and (obj['EventName'] == 'RXLOS') and
                obj['ResolutionReason'] != 'N/A'):
                faultFound = True
                break
        self.assertTrue(faultFound, "RXLOS fault not cleared for ModuleId :" + str(self.ModuleId) + " NwIntfId :" +  str(self.PeerNwIntfId))

    def configPortsAndVerifyAlarmResolution(self):
        self.restIf.updatePort(IntfRef = self.LocalPort, AdminState = self.PortAdminState)
        self.trafficGenRestIf.updatePort(IntfRef = self.RemotePort, AdminState = self.PortAdminState)
        time.sleep(1)
        #Read all alarms 
        faultFound = False
        res = self.restIf.getAllAlarmStates()
        for elem in res:
            obj = elem['Object']
            if (obj['SrcObjKey'].endswith(self.LocalPort) and (obj['EventName'] == 'PortOperStateDown') and
                obj['ResolutionReason'] != 'N/A'):
                faultFound = True
                break
        self.assertTrue(faultFound, "PortOperStateDown alarm not cleared in fault database for port - " + self.LocalPort)

    def configTxPowerAndVerifyAlarmResolution(self):
        self.updateDWDMModuleNwIntf()
        faultFound = False
        time.sleep(1)
        #Read all faults 
        keyStr = 'ModuleId:'+ str(self.ModuleId) + ' NwIntfId:' + str(self.PeerNwIntfId)
        res = self.restIf.getAllAlarmStates()
        for elem in res:
            obj = elem['Object']
            if (obj['SrcObjKey'].endswith(keyStr) and (obj['EventName'] == 'RXLOS') and
                obj['ResolutionReason'] != 'N/A'):
                faultFound = True
                break
        self.assertTrue(faultFound, "RXLOS alarm not cleared for ModuleId :" + str(self.ModuleId) + " NwIntfId :" +  str(self.PeerNwIntfId))

    def verifyAsicPMInfo(self):
        res = self.restIf.getAllAsicGlobalPMs()
        self.assertTrue(len(res) != 0, "Unable to retrieve PM information for asic")
