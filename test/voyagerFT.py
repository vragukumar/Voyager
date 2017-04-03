#!/usr/bin/python
import unittest, logging
import sys, time
from voyagerTest import VoyagerTest
from voyagerBaseSuite import VoyagerTestSuiteBase

logging.basicConfig(stream=sys.stderr)
log = logging.getLogger('VoyagerSuite')
log.setLevel(logging.DEBUG)

class VoyagerXponderGlobalTests(VoyagerTestSuiteBase):
    def suite1(self):
        '''
        @TEST
        @DESCRIPTION: Validate that inventory information of the AC400 optical module can be read
        @STEP: Query state/DWDMModules and verify AC400 inventory
        @EXPECT: VendorName set to Acacia Comm Inc.
        @EXPECT: VendorPartNum set to AC400-001-00H
        @EXPECT: VendorDateCode set to 20160527
        @EXPECT: ModuleHWVersion set to 48.49
        '''
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('verifyAC400Inventory'))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite2(self):
        '''
        @TEST
        @DESCRIPTION: Validate that inventory information of the Tomahawk ASIC can be read
        @STEP: Query state/AsicGlobals and verify ASIC inventory
        @EXPECT: VendorId set to 14e4 
        @EXPECT: PartNumber set to b960
        @EXPECT: RevisionId set to 12
        '''
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('verifyAsicInventory'))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite3(self):
        '''
        @TEST
        @DESCRIPTION: Validate that the transponder can be configured to be in InServiceWire/InServiceOversub/InServiceRegen/PacketOptical/OutOfService modes
        @STEP: Set transponder mode to be InServiceWire
        @STEP: Query and verify current transponder mode is InServiceWire
        @STEP: Set transponder mode to be InServiceRegen
        @STEP: Query and verify current transponder mode is InServiceRegen
        @STEP: Set transponder mode to be InServiceOverSub
        @STEP: Query and verify current transponder mode is InServiceOverSub
        @STEP: Set transponder mode to be InServicePacketOptical
        @STEP: Query and verify current transponder mode is InServicePacketOptical
        @STEP: Set transponder mode to be InServicePacketOptical
        @STEP: Query and verify current transponder mode is InServicePacketOptical
        @STEP: Set transponder mode to be OutOfService
        @STEP: Query and verify current transponder mode is OutOfService
        @EXPECT: Transponder mode in config/XponderGlobal must match value in state/XponderGlobal
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        mode = 'InServiceRegen'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        mode = 'InServiceOverSub'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        mode = 'InServicePacketOptical'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        mode = 'OutOfService'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite4(self):
        '''
        @TEST
        @DESCRIPTION: Validate asic configuration when transponder is in InServiceWire mode 
        @STEP: Set transponder mode to be InServiceWire
        @STEP: Read vlan configuration 
        @EXPECT: VlanId: 2, UntagIntfList: ["fpPort1","fpPort13"] should be present
        @EXPECT: VlanId: 3, UntagIntfList: ["fpPort2","fpPort14"] should be present
        @EXPECT: VlanId: 4, UntagIntfList: ["fpPort3","fpPort15"] should be present
        @EXPECT: VlanId: 5, UntagIntfList: ["fpPort4","fpPort16"] should be present
        @EXPECT: VlanId: 6, UntagIntfList: ["fpPort5","fpPort17"] should be present
        @EXPECT: VlanId: 7, UntagIntfList: ["fpPort6","fpPort18"] should be present
        @EXPECT: VlanId: 8, UntagIntfList: ["fpPort7","fpPort19"] should be present
        @EXPECT: VlanId: 9, UntagIntfList: ["fpPort8","fpPort20"] should be present
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite5(self):
        '''
        @TEST
        @DESCRIPTION: Validate asic configuration when transponder is in InServiceOverSub mode 
        @STEP: Set transponder mode to be InServiceOverSub
        @STEP: Read vlan configuration 
        @EXPECT: VlanId: 2, IntfList: ["fpPort13"], UntagIntfList: ["fpPort1"] should be present
        @EXPECT: VlanId: 3, IntfList: ["fpPort14"], UntagIntfList: ["fpPort2"] should be present
        @EXPECT: VlanId: 4, IntfList: ["fpPort15"], UntagIntfList: ["fpPort3"] should be present
        @EXPECT: VlanId: 5, IntfList: ["fpPort16"], UntagIntfList: ["fpPort4"] should be present
        @EXPECT: VlanId: 6, IntfList: ["fpPort17"], UntagIntfList: ["fpPort5"] should be present
        @EXPECT: VlanId: 7, IntfList: ["fpPort18"], UntagIntfList: ["fpPort6"] should be present
        @EXPECT: VlanId: 8, IntfList: ["fpPort19"], UntagIntfList: ["fpPort7"] should be present
        @EXPECT: VlanId: 9, IntfList: ["fpPort20"], UntagIntfList: ["fpPort8"] should be present
        @EXPECT: VlanId: 10, IntfList: ["fpPort15"], UntagIntfList: ["fpPort9"] should be present
        @EXPECT: VlanId: 11, IntfList: ["fpPort16"], UntagIntfList: ["fpPort10"] should be present
        @EXPECT: VlanId: 12, IntfList: ["fpPort17"], UntagIntfList: ["fpPort11"] should be present
        @EXPECT: VlanId: 13, IntfList: ["fpPort18"], UntagIntfList: ["fpPort12"] should be present
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceOverSub'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceOverSubCfg'))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite6(self):
        '''
        @TEST
        @DESCRIPTION: Validate asic configuration when transponder is in OutOfService mode 
        @STEP: Set transponder mode to be OutOfService 
        @STEP: Read vlan configuration 
        @EXPECT: All applied vlan configuration from InServiceOverSub mode should be removed 
        '''
        suite = unittest.TestSuite()
        mode = 'OutOfService'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyOutOfServiceCfg'))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite7(self):
        '''
        @TEST
        @DESCRIPTION: Validate Xponder description can be set
        @STEP: Set xponder description to 'Voyager-233'
        @STEP: Validate xponder description is set correctly
        @EXPECT: XponderDescription in state/XponderGlobals must be set to 'Voyager-233'
        '''
        suite = unittest.TestSuite()
        desc = 'Voyager-233'
        suite.addTest(VoyagerTest('updateXponderGlobalDescription', attrs = {'XponderId':0, 'XponderDescription':desc}))
        suite.addTest(VoyagerTest('verifyXponderGlobalDescription', attrs = {'XponderId':0, 'XponderDescription':desc}))
        unittest.TextTestRunner(failfast=True).run(suite)

class VoyagerDWDMModuleTests(VoyagerTestSuiteBase):
    def suite1(self):
        '''
        @TEST
        @DESCRIPTION: Validate AC400 automatic turn up
        @STEP: Set AdminState to UP on DWDMModule
        @EXPECT: ModuleState in state/DWDMModules must be set to READY
        '''
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('updateDWDMModule', attrs = {'ModuleId':0, 'AdminState':'UP'}))
        suite.addTest(VoyagerTest('verifyDWDMModuleState', attrs = {'ModuleId':0, 'ModuleState':'READY'}))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite2(self):
        '''
        @TEST
        @DESCRIPTION: Validate AC400 automatic turn down 
        @STEP: Set AdminState to DOWN on DWDMModule
        @EXPECT: ModuleState in state/DWDMModules must be set to LOW POWER
        '''
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('updateDWDMModule', attrs = {'ModuleId':0, 'AdminState':'DOWN'}))
        suite.addTest(VoyagerTest('verifyDWDMModuleState', attrs = {'ModuleId':0, 'ModuleState':'LOW POWER'}))
        unittest.TextTestRunner(failfast=True).run(suite)

class VoyagerDWDMModuleNwIntfTests(VoyagerTestSuiteBase):
    def suite1(self):
        '''
        @TEST
        @DESCRIPTION: Validate that state and configuration can be queried for all Network Interfaces
        @STEP: Read config/DWDMModuleNwIntfs 
        @STEP: Read state/DWDMModuleNwIntfs 
        @EXPECT: Both reads above should list entries for NwIntfId 0 and NwIntfId 1
        '''
        pass
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('verifyNWIntfCfgInventory'))
        suite.addTest(VoyagerTest('verifyNWIntfStateInventory'))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite2(self):
        '''
        @TEST
        @DESCRIPTION: Validate Tx power can be set on AC400 network interfaces
        @STEP: Set Tx power value on NwIntf 0
        @STEP: Set Tx power value on NwIntf 1
        @STEP: Read Rx power value on Nw intf 0
        @STEP: Read Rx power value on NwIntf 1 
        @EXPECT: RxPower read in state/DWDMModuleNwIntf should be within 30% deviation of TxPower
        '''
        pass
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('updateDWDMModuleNwIntf', attrs = {'ModuleId':0, 'NwIntfId':0, 'TxPower':2}))
        suite.addTest(VoyagerTest('updateDWDMModuleNwIntf', attrs = {'ModuleId':0, 'NwIntfId':1, 'TxPower':3}))
        suite.addTest(VoyagerTest('verifyNwIntfState', attrs = {'ModuleId':0, 'NwIntfId':1, 'RxPower':2, 'RxPwrDev':1}))
        suite.addTest(VoyagerTest('verifyNwIntfState', attrs = {'ModuleId':0, 'NwIntfId':0, 'RxPower':3, 'RxPwrDev':1}))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite3(self):
        '''
        @TEST
        @DESCRIPTION: Validate Tx channel number can be set on AC400 network interfaces
        @STEP: Read CurrentBER value on NwIntf 1
        @STEP: Set Tx Channel number to be 45 on NwIntf 0
        @STEP: Read CurrentBER value on NwIntf 1
        @EXPECT: Initially Tx channels match on both NwIntf, hence CurrentBER will read > 0
        @EXPECT: Setting NwIntf 0 to channel 45, causes loss of sync, resulting in CurrentBER < 0
        '''
        pass
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('verifyPeerNwIntfIsOperational', attrs = {'ModuleId':0, 'NwIntfId':1}))
        suite.addTest(VoyagerTest('updateDWDMModuleNwIntf', attrs = {'ModuleId':0, 'NwIntfId':0, 'ChannelNumber':45}))
        suite.addTest(VoyagerTest('verifyPeerNwIntfIsNotOperational', attrs = {'ModuleId':0, 'NwIntfId':1}))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite4(self):
        '''
        @TEST
        @DESCRIPTION: Validate modulation format can be modified on AC400 network interfaces
        @STEP: Read CurrentBER value on NwIntf 1
        @STEP: Set modulation format on NwIntf 0 to be QPSK 
        @STEP: Read CurrentBER value on NwIntf 1
        @EXPECT: Initial modulation formats on both NWIntf should be 16QAM, hence CurrentBER will read > 0
        @EXPECT: Setting NwIntf 0 to QPSK results in loss of sync, hence CurrentBER will read < 0 
        '''
        pass
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('verifyPeerNwIntfIsOperational', attrs = {'ModuleId':0, 'NwIntfId':1}))
        suite.addTest(VoyagerTest('updateDWDMModuleNwIntf', attrs = {'ModuleId':0, 'NwIntfId':0, 'ModFmt':'QPSK'}))
        suite.addTest(VoyagerTest('verifyPeerNwIntfIsNotOperational', attrs = {'ModuleId':0, 'NwIntfId':1}))
        unittest.TextTestRunner(failfast=True).run(suite)

    def suite5(self):
        '''
        @TEST
        @DESCRIPTION: Validate FEC mode can be modified on AC400 network interfaces
        @STEP: Read CurrentBER value on NwIntf 1
        @STEP: Set FEC mode on NwIntf 0 to be 15%SDFEC 
        @STEP: Read CurrentBER value on NwIntf 1
        @EXPECT: Initial FEC mode on both NwIntf should be 25%OvrHeadSDFEC, hence CurrentBER will read > 0
        @EXPECT: Setting NwIntf 0 to 15%SDFEC results in loss of sync, hence CurrentBER will read < 0 
        '''
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('verifyPeerNwIntfIsOperational', attrs = {'ModuleId':0, 'NwIntfId':1}))
        suite.addTest(VoyagerTest('updateDWDMModuleNwIntf', attrs = {'ModuleId':0, 'NwIntfId':0, 'FECMode':'15%SDFEC'}))
        suite.addTest(VoyagerTest('verifyPeerNwIntfIsNotOperational', attrs = {'ModuleId':0, 'NwIntfId':1}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite6(self):
        '''
        @TEST
        @DESCRIPTION: Validate that differential encoding setting can be modified on AC400 network interfaces
        @STEP: Read CurrentBER value on NwIntf 1
        @STEP: Set DiffEncoding to True on NwIntf 0
        @STEP: Read RxPower and CurrentBER value on NwIntf 1
        @EXPECT: Initial DiffEncoding setting on both NWIntf should be False, hence CurrentBER will read > 0
        @EXPECT: Setting DiffEncoding to True on NwIntf 0 results in loss of sync, hence CurrentBER will read < 0 
        '''
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('verifyPeerNwIntfIsOperational', attrs = {'ModuleId':0, 'NwIntfId':1}))
        suite.addTest(VoyagerTest('updateDWDMModuleNwIntf', attrs = {'ModuleId':0, 'NwIntfId':0, 'DiffEncoding':True}))
        suite.addTest(VoyagerTest('verifyPeerNwIntfIsNotOperational', attrs = {'ModuleId':0, 'NwIntfId':1}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite7(self):
        '''
        @TEST
        @DESCRIPTION: Validate that PM data can be read for BER on AC400 network interfaces
        @STEP: Read CurrentBER value from state/DWDMModuleNwintfs 
        @STEP: Read MinBEROverPMInterval value from state/DWDMModuleNwintfs 
        @STEP: Read AvgBEROverPMInterval value from state/DWDMModuleNwintfs 
        @STEP: Read MaxBEROverPMInterval value from state/DWDMModuleNwintfs 
        @EXPECT: BER values read at each step must read > 0 
        '''
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('verifyNwIntfBERValuesAreValid', attrs = {'ModuleId':0, 'NwIntfId':0}))
        suite.addTest(VoyagerTest('verifyNwIntfBERValuesAreValid', attrs = {'ModuleId':0, 'NwIntfId':1}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

class VoyagerDWDMModuleClntIntfTests(VoyagerTestSuiteBase):
    def suite1(self):
        '''
        @TEST
        @DESCRIPTION: Validate that state and configuration can be queried for all Client Interfaces
        @STEP: Read config/DWDMModuleClntIntfs 
        @STEP: Read state/DWDMModuleClntIntfs 
        @EXPECT: Both reads above should list entries for ClintIntfId 0,1,2 and 3
        '''
        suite = unittest.TestSuite()
        suite.addTest(VoyagerTest('verifyClntIntfCfgInventory'))
        suite.addTest(VoyagerTest('verifyClntIntfStateInventory'))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite2(self):
        '''
        @TEST
        @DESCRIPTION: Validate host electrical parameters can be configured for each client interface 
        @STEP: For each client interface read HostTxEqLfCtle, HostTxEqCtle, HostTxEqDfe
        @STEP: For each client interface set HostTxEqLfCtle = 3, HostTxEqCtle = 4, HostTxEqDfe = 5
        @STEP: For each client interface read HostTxEqLfCtle, HostTxEqCtle, HostTxEqDfe
        @EXPECT: Initial values read for HostTxEqLfCtle, HostTxEqCtle, HostTxEqDfe should be 2, 19, 3 respectively
        @EXPECT: Subsequent read after write yields HostTxEqLfCtle = 3, HostTxEqCtle = 4, HostTxEqDfe = 5
        '''
        suite = unittest.TestSuite()
        for clntIntfId in range(0,4):
            suite.addTest(VoyagerTest('verifyDWDMModuleClntIntfElecParams', attrs = {'ModuleId':0, 'ClntIntfId':clntIntfId, 'HostTxEqLfCtle':2, 'HostTxEqCtle':19, 'HostTxEqDfe':3}))
        for clntIntfId in range(0,4):
            suite.addTest(VoyagerTest('updateDWDMModuleClntIntf', attrs = {'ModuleId':0, 'ClntIntfId':clntIntfId, 'HostTxEqLfCtle':3, 'HostTxEqCtle':4, 'HostTxEqDfe':5}))
            suite.addTest(VoyagerTest('verifyDWDMModuleClntIntfElecParams', attrs = {'ModuleId':0, 'ClntIntfId':clntIntfId, 'HostTxEqLfCtle':3, 'HostTxEqCtle':4, 'HostTxEqDfe':5}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

class VoyagerFCAPSTests(VoyagerTestSuiteBase):
    def suite1(self):
        '''
        @TEST
        @DESCRIPTION: Validate switching ASIC related events are generated in the Voyager system 
        @STEP: Configure the transponder to be in InServiceWire mode 
        @STEP: Set AdminState to UP on fpPort1 on Voyager unit 2 
        @STEP: Set AdminState to UP on fpPort49 on the traffic generator 
        @STEP: Read all events logged by the Voyager system
        @EXPECT: PortOperStateUp event should be generated for fpPort1
        '''
        #FIXME: FlexSDK lacking events support, enable test case when FlexSDK support is enhanced
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('configPortsAndReadEvents', attrs = {'LocalPort':'fpPort1', 'RemotePort':'fpPort49', 'PortAdminState':'UP'}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass


    def suite2(self):
        '''
        @TEST
        @DESCRIPTION: Validate AC400 related events are generated in the Voyager system 
        @STEP: Configure the transponder to be in InServiceWire mode 
        @STEP: Set AdminState to UP for AC400 module 1 on Voyager unit 2 
        @STEP: Set TxPower to -30 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
        @STEP: Read all events logged by the Voyager system
        @EXPECT: RxLOS event should be generated for ModuleId 1, NwIntfId 1
        '''
        #FIXME: FlexSDK lacking events support, enable test case when FlexSDK support is enhanced
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('configTxPowerAndReadEvents', attrs = {'ModuleId':0, 'NwIntfId':0, 'TxPower':-30}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite3(self):
        '''
        @TEST
        @DESCRIPTION: Validate switching ASIC related faults are generated in the Voyager system 
        @STEP: Configure the transponder to be in InServiceWire mode 
        @STEP: Set AdminState to UP on fpPort49 on the traffic generator 
        @STEP: Set AdminState to DOWN on fpPort49 on the traffic generator to bring the link down 
        @STEP: Read all faults logged by the Voyager system
        @EXPECT: PortOperStateDown fault should be generated for fpPort1
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('configPortsAndReadFaults', attrs = {'LocalPort':'fpPort1', 'RemotePort':'fpPort49', 'PortAdminState':'UP'}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite4(self):
        '''
        @TEST
        @DESCRIPTION: Validate AC400 related faults are generated in the Voyager system 
        @STEP: Configure the transponder to be in InServiceWire mode 
        @STEP: Set TxPower to -30 dBm for ModuleId 0 NwIntfId 0 on Voyager unit 2 
        @STEP: Read all faults logged by the Voyager system
        @EXPECT: RxLOS fault should be generated for ModuleId 0, NwIntfId 1
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('configTxPowerAndReadFaults', attrs = {'ModuleId':0, 'NwIntfId':0, 'TxPower':-30, 'PeerNwIntfId':1}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite5(self):
        '''
        @TEST
        @DESCRIPTION: Validate switching ASIC related alarms are generated in the Voyager system 
        @STEP: Configure the transponder to be in InServiceWire mode 
        @STEP: Set AdminState to UP on fpPort1 on Voyager unit 2 
        @STEP: Set AdminState to UP on fpPort49 on the traffic generator 
        @STEP: Set AdminState to DOWN on fpPort49 on the traffic generator to bring the link down 
        @STEP: Read all alarms logged by the Voyager system
        @EXPECT: PortOperStateDown alarm should be generated for fpPort1
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('configPortsAndReadAlarms', attrs = {'LocalPort':'fpPort1', 'RemotePort':'fpPort49', 'PortAdminState':'UP'}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite6(self):
        '''
        @TEST
        @DESCRIPTION: Validate AC400 related alarms are generated in the Voyager system 
        @STEP: Configure the transponder to be in InServiceWire mode 
        @STEP: Set AdminState to UP for AC400 module 1 on Voyager unit 2 
        @STEP: Set TxPower to -30 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
        @STEP: Read all alarms logged by the Voyager system
        @EXPECT: RxLOS alarm should be generated for ModuleId 1, NwIntfId 1
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('configTxPowerAndReadAlarms', attrs = {'ModuleId':0, 'NwIntfId':0, 'TxPower':-30, 'PeerNwIntfId':1}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite7(self):
        '''
        @TEST
        @DESCRIPTION: Validate switching ASIC related fault resolution in the Voyager system 
        @STEP: Configure the transponder to be in InServiceWire mode 
        @STEP: Set AdminState to UP on fpPort1 on Voyager unit 2 
        @STEP: Set AdminState to UP on fpPort49 on the traffic generator 
        @STEP: Set AdminState to DOWN on fpPort49 on the traffic generator to bring the link down 
        @STEP: Read all faults logged by the Voyager system
        @STEP: Set AdminState to UP on fpPort49 on the traffic generator to bring the link down 
        @STEP: Read all faults logged by the Voyager system
        @EXPECT: PortOperStateDown fault should be generated for fpPort1
        @EXPECT: ResolutionTime/ResolutionReason should be populated
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('configPortsAndReadFaults', attrs = {'LocalPort':'fpPort1', 'RemotePort':'fpPort49', 'PortAdminState':'UP'}))
        suite.addTest(VoyagerTest('configPortsAndVerifyFaultResolution', attrs = {'LocalPort':'fpPort1', 'RemotePort':'fpPort49', 'PortAdminState':'UP'}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite8(self):
        '''
        @TEST
        @DESCRIPTION: Validate AC400 related fault resolution in the Voyager system 
        @STEP: Configure the transponder to be in InServiceWire mode 
        @STEP: Set AdminState to UP for AC400 module 1 on Voyager unit 2 
        @STEP: Set TxPower to -30 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
        @STEP: Read all alarms logged by the Voyager system
        @STEP: Set TxPower to -1 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
        @STEP: Read all faults logged by the Voyager system
        @EXPECT: RxLOS fault should be generated for ModuleId 1, NwIntfId 1
        @EXPECT: ResolutionTime/ResolutionReason should be populated
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('configTxPowerAndReadFaults', attrs = {'ModuleId':0, 'NwIntfId':0, 'TxPower':-30, 'PeerNwIntfId':1}))
        suite.addTest(VoyagerTest('configTxPowerAndVerifyFaultResolution', attrs = {'ModuleId':0, 'NwIntfId':0, 'TxPower':-1}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite9(self):
        '''
        @TEST
        @DESCRIPTION: Validate switching ASIC related alarm resolution in the Voyager system 
        @STEP: Configure the transponder to be in InServiceWire mode 
        @STEP: Set AdminState to UP on fpPort1 on Voyager unit 2 
        @STEP: Set AdminState to UP on fpPort49 on the traffic generator 
        @STEP: Set AdminState to DOWN on fpPort49 on the traffic generator to bring the link down 
        @STEP: Read all alarms logged by the Voyager system
        @STEP: Set AdminState to UP on fpPort49 on the traffic generator to bring the link down 
        @STEP: Read all alarms logged by the Voyager system
        @EXPECT: PortOperStateDown alarm should be generated for fpPort1
        @EXPECT: ResolutionTime/ResolutionReason should be populated
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('configPortsAndReadAlarms', attrs = {'LocalPort':'fpPort1', 'RemotePort':'fpPort49', 'PortAdminState':'UP'}))
        suite.addTest(VoyagerTest('configPortsAndVerifyAlarmResolution', attrs = {'LocalPort':'fpPort1', 'RemotePort':'fpPort49', 'PortAdminState':'UP'}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite10(self):
        '''
        @TEST
        @DESCRIPTION: Validate AC400 related alarm resolution in the Voyager system 
        @STEP: Configure the transponder to be in InServiceWire mode 
        @STEP: Set AdminState to UP for AC400 module 1 on Voyager unit 2 
        @STEP: Set TxPower to -30 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
        @STEP: Read all alarms logged by the Voyager system
        @STEP: Set TxPower to -1 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
        @STEP: Read all alarms logged by the Voyager system
        @EXPECT: RxLOS alarm should be generated for ModuleId 1, NwIntfId 1
        @EXPECT: ResolutionTime/ResolutionReason should be populated
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('configTxPowerAndReadFaults', attrs = {'ModuleId':0, 'NwIntfId':0, 'TxPower':-30, 'PeerNwIntfId':1}))
        suite.addTest(VoyagerTest('configTxPowerAndVerifyAlarmResolution', attrs = {'ModuleId':0, 'NwIntfId':0, 'TxPower':-1}))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

    def suite11(self):
        '''
        @TEST
        @DESCRIPTION: Validate performance data related to the switching ASIC can be queried
        @STEP: Configure the transponder to be in InServiceWire mode
        @STEP: Query temperature related PM data for the switching asicd using the endpoint state/asicGlobalPM
        @EXPECT: Non empty list of temperature data should be returned
        '''
        suite = unittest.TestSuite()
        mode = 'InServiceWire'
        suite.addTest(VoyagerTest('configXponderMode', attrs = {'XponderId':0, 'XponderMode':mode}))
        suite.addTest(VoyagerTest('verifyInServiceWireCfg'))
        suite.addTest(VoyagerTest('verifyAsicPMInfo'))
        unittest.TextTestRunner(failfast=True).run(suite)
        pass

class VoyagerTrafficTests(VoyagerTestSuiteBase):
    def suite1(self):
        '''
        @TEST
        @DESCRIPTION: Validate end to end data path connectivity 
        @STEP: Configure Voyager unit 1 to be in InServiceWire mode 
        @STEP: Set AdminState to UP for AC400 module 0 on Voyager unit 1 
        @STEP: Set AdminState to UP, and Speed to 40000, on fpPort1 on Voyager unit 1 
        @STEP: Set AdminState to UP, and Speed to 40000,  on fpPort49 on the traffic generator 
        @STEP: Configure Voyager unit 2 to be in InServiceWire mode 
        @STEP: Set AdminState to UP for AC400 module 0 on Voyager unit 2 
        @STEP: Set AdminState to UP, and Speed to 40000 on fpPort1 on Voyager unit 2 
        @STEP: Set AdminState to UP, and Speed to 40000 on fpPort50 on the traffic generator 
        @STEP: Transmit 10,000 L2 frames egressing fpPort49 on the traffic generator
        @STEP: Transmit 10,000 L2 frames egressing fpPort50 on the traffic generator
        @EXPECT: 10,000 L2 frames must ingress fpPort49 on the traffic generator
        @EXPECT: 10,000 L2 frames must ingress fpPort50 on the traffic generator 
        '''
        pass

def execTestAndGenDoc(testSuite):
    testSuite.run()
    testSuite.writeDoc()

if __name__ == '__main__':
    execTestAndGenDoc(VoyagerXponderGlobalTests())
    execTestAndGenDoc(VoyagerDWDMModuleTests())
    execTestAndGenDoc(VoyagerDWDMModuleNwIntfTests())
    execTestAndGenDoc(VoyagerDWDMModuleClntIntfTests())
    execTestAndGenDoc(VoyagerFCAPSTests())
    execTestAndGenDoc(VoyagerTrafficTests())
