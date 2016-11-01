Test Plan 
==========
              
    **Document Number: TBD**


   **Document Revision History**

   +---------------+---------------------+---------------+---------------+
   | **Version**   |   **Comment**       |  **Author**   |    **Date**   |
   +---------------+---------------------+---------------+---------------+
   |  v1.0         |   Initial version   |   SnapRoute   |   10/22/2016  |
   +---------------+---------------------+---------------+---------------+
   |  v1.1         |  Revised test cases |   SnapRoute   |   10/25/2016  |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+


   **Document Approval History**

   +---------------+---------------------+---------------+---------------+
   | **Version**   |   **Comment**       |  **Author**   |    **Date**   |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
    
|   
|   
|   
|
|

==================
Voyager Test Setup
==================

    
|   
|   
|   

.. image:: VoyagerTestSetup.jpg


**Description**


  The diagram above depicts the Voyager testbed setup. The testbed utilizes a 40G switch as a traffic source.
  Voyager unit 1 and Voyager unit 2 have, AC400 module 0, NW interface id 0 connected to each other.

  Given the above topology, bidirectional traffic flows can be setup originating from port 49/50 on the traffic
  generator, switched by the Voyager units 1/2 and terminating at the traffic generator.

  The test setup also provides for running traffic loopback tests. Voyager unit 2 has network interfaces 0 and 1
  looped back on AC400 module 1.

  Additionally, Voyager unit 1 has only one AC400 module, while Voyager unit 2 is fully populated with 2 AC400
  modules. This provides for test coverage, ensuring full functionality is available even if only 1 AC400 module
  is present in the transponder system.

|   
|   
|   
|   
|   
|   
==========
Test Cases
==========



Test Case : 1
-------------

**Validate that state and configuration can be queried for all Network Interfaces**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Read config/DWDMModuleNwIntfs 
    * -   Read state/DWDMModuleNwIntfs 

**Expected Results**
    *  Both reads above should list entries for NwIntfId 0 and NwIntfId 1


**Actual Results**
    PASS


Test Case : 2
-------------

**Validate that inventory information of the AC400 optical module can be read**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Query state/DWDMModules and verify AC400 inventory

**Expected Results**
    *  VendorName set to Acacia Comm Inc.
    *  VendorPartNum set to AC400-001-00H
    *  VendorDateCode set to 20160527
    *  ModuleHWVersion set to 48.49


**Actual Results**
    PASS


Test Case : 3
-------------

**Validate that inventory information of the Tomahawk ASIC can be read**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Query state/AsicGlobals and verify ASIC inventory

**Expected Results**
    *  VendorId set to 14e4 
    *  PartNumber set to b960
    *  RevisionId set to 12


**Actual Results**
    PASS


Test Case : 4
-------------

**Validate that the transponder can be configured to be in InServiceWire/InServiceOversub/InServiceRegen/PacketOptical/OutOfService modes**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set transponder mode to be InServiceWire
    * -   Query and verify current transponder mode is InServiceWire
    * -   Set transponder mode to be InServiceRegen
    * -   Query and verify current transponder mode is InServiceRegen
    * -   Set transponder mode to be InServiceOverSub
    * -   Query and verify current transponder mode is InServiceOverSub
    * -   Set transponder mode to be InServicePacketOptical
    * -   Query and verify current transponder mode is InServicePacketOptical
    * -   Set transponder mode to be InServicePacketOptical
    * -   Query and verify current transponder mode is InServicePacketOptical
    * -   Set transponder mode to be OutOfService
    * -   Query and verify current transponder mode is OutOfService

**Expected Results**
    *  Transponder mode in config/XponderGlobal must match value in state/XponderGlobal


**Actual Results**
    PASS


Test Case : 5
-------------

**Validate asic configuration when transponder is in InServiceWire mode**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set transponder mode to be InServiceWire
    * -   Read vlan configuration 

**Expected Results**
    *  VlanId: 2, UntagIntfList: ["fpPort1","fpPort13"] should be present
    *  VlanId: 3, UntagIntfList: ["fpPort2","fpPort14"] should be present
    *  VlanId: 4, UntagIntfList: ["fpPort3","fpPort15"] should be present
    *  VlanId: 5, UntagIntfList: ["fpPort4","fpPort16"] should be present
    *  VlanId: 6, UntagIntfList: ["fpPort5","fpPort17"] should be present
    *  VlanId: 7, UntagIntfList: ["fpPort6","fpPort18"] should be present
    *  VlanId: 8, UntagIntfList: ["fpPort7","fpPort19"] should be present
    *  VlanId: 9, UntagIntfList: ["fpPort8","fpPort20"] should be present


**Actual Results**
    PASS


Test Case : 6
-------------

**Validate asic configuration when transponder is in InServiceOverSub mode**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set transponder mode to be InServiceOverSub
    * -   Read vlan configuration 

**Expected Results**
    *  VlanId: 2, IntfList: ["fpPort13"], UntagIntfList: ["fpPort1"] should be present
    *  VlanId: 3, IntfList: ["fpPort14"], UntagIntfList: ["fpPort2"] should be present
    *  VlanId: 4, IntfList: ["fpPort15"], UntagIntfList: ["fpPort3"] should be present
    *  VlanId: 5, IntfList: ["fpPort16"], UntagIntfList: ["fpPort4"] should be present
    *  VlanId: 6, IntfList: ["fpPort17"], UntagIntfList: ["fpPort5"] should be present
    *  VlanId: 7, IntfList: ["fpPort18"], UntagIntfList: ["fpPort6"] should be present
    *  VlanId: 8, IntfList: ["fpPort19"], UntagIntfList: ["fpPort7"] should be present
    *  VlanId: 9, IntfList: ["fpPort20"], UntagIntfList: ["fpPort8"] should be present
    *  VlanId: 10, IntfList: ["fpPort15"], UntagIntfList: ["fpPort9"] should be present
    *  VlanId: 11, IntfList: ["fpPort16"], UntagIntfList: ["fpPort10"] should be present
    *  VlanId: 12, IntfList: ["fpPort17"], UntagIntfList: ["fpPort11"] should be present
    *  VlanId: 13, IntfList: ["fpPort18"], UntagIntfList: ["fpPort12"] should be present


**Actual Results**
    PASS


Test Case : 7
-------------

**Validate AC400 automatic turn up**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set AdminState to UP on DWDMModule

**Expected Results**
    *  ModuleState in state/DWDMModules must be set to READY


**Actual Results**
    PASS


Test Case : 8
-------------

**Validate AC400 automatic turn down**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set AdminState to DOWN on DWDMModule

**Expected Results**
    *  ModuleState in state/DWDMModules must be set to LOW POWER


**Actual Results**
    PASS


Test Case : 9
-------------

**Validate asic configuration when transponder is in OutOfService mode**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set transponder mode to be OutOfService 
    * -   Read vlan configuration 

**Expected Results**
    *  All applied vlan configuration from InServiceOverSub mode should be removed 


**Actual Results**
    PASS


Test Case : 10
--------------

**Validate Xponder description can be set**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set xponder description to 'Voyager-233'
    * -   Validate xponder description is set correctly

**Expected Results**
    *  XponderDescription in state/XponderGlobals must be set to 'Voyager-233'


**Actual Results**
    PASS


Test Case : 11
--------------

**Validate Tx power can be set on AC400 network interfaces**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set Tx power value on NwIntf 0
    * -   Read Rx power value on NwIntf 1 
    * -   Set Tx power value on NwIntf 1
    * -   Read Rx power value on Nw intf 0

**Expected Results**
    *  RxPower read in state/DWDMModuleNwIntf should be within 20% deviation of TxPower


**Actual Results**
    PASS


Test Case : 12
--------------

**Validate Tx channel number can be set on AC400 network interfaces**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Read current Tx Channel number on both network interfaces 
    * -   Read RxPower and CurrentBER value on NwIntf 1
    * -   Set Tx Channel number to be 48 on NwIntf 0
    * -   Read RxPower and CurrentBER value on NwIntf 1

**Expected Results**
    *  Initially Tx channels match on both NwIntf, hence CurrentBER will read > 0
    *  Setting NwIntf 0 to channel 48, causes loss of sync, resulting in CurrentBER < 0


**Actual Results**
    PASS


Test Case : 13
--------------

**Validate modulation format can be modified on AC400 network interfaces**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Read current modulation format on both network interfaces 
    * -   Read RxPower and CurrentBER value on NwIntf 1
    * -   Set modulation format on NwIntf 0 to be QPSK 
    * -   Read RxPower and CurrentBER value on NwIntf 1

**Expected Results**
    *  Initial modulation formats on both NWIntf should be 16QAM, hence CurrentBER will read > 0
    *  Setting NwIntf 0 to QPSK results in loss of sync, hence CurrentBER will read < 0 


**Actual Results**
    PASS


Test Case : 14
--------------

**Validate FEC mode can be modified on AC400 network interfaces**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Read current FEC mode on both network interfaces 
    * -   Read RxPower and CurrentBER value on NwIntf 1
    * -   Set FEC mode on NwIntf 0 to be 15%SDFEC 
    * -   Read RxPower and CurrentBER value on NwIntf 1

**Expected Results**
    *  Initial FEC mode on both NwIntf should be 25%OvrHeadSDFEC, hence CurrentBER will read > 0
    *  Setting NwIntf 0 to 15%SDFEC results in loss of sync, hence CurrentBER will read < 0 


**Actual Results**
    PASS


Test Case : 15
--------------

**Validate that differential encoding setting can be modified on AC400 network interfaces**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Read current DiffEncoding setting on both network interfaces 
    * -   Read RxPower and CurrentBER value on NwIntf 1
    * -   Set DiffEncoding to True on NwIntf 0
    * -   Read RxPower and CurrentBER value on NwIntf 1

**Expected Results**
    *  Initial DiffEncoding setting on both NWIntf should be False, hence CurrentBER will read > 0
    *  Setting DiffEncoding to True on NwIntf 0 results in loss of sync, hence CurrentBER will read < 0 


**Actual Results**
    PASS


Test Case : 16
--------------

**Validate that PM data can be read for BER on AC400 network interfaces**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Read CurrentBER value from state/DWDMModuleNwintfs 
    * -   Read MinBEROverPMInterval value from state/DWDMModuleNwintfs 
    * -   Read AvgBEROverPMInterval value from state/DWDMModuleNwintfs 
    * -   Read MaxBEROverPMInterval value from state/DWDMModuleNwintfs 

**Expected Results**
    *  BER values read at each step must read > 0 


**Actual Results**
    PASS


Test Case : 17
--------------

**Validate that state and configuration can be queried for all Client Interfaces**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Read config/DWDMModuleClntIntfs 
    * -   Read state/DWDMModuleClntIntfs 

**Expected Results**
    *  Both reads above should list entries for ClintIntfId 0,1,2 and 3


**Actual Results**
    PASS


Test Case : 18
--------------

**Validate host electrical parameters can be configured for each client interface**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   For each client interface read HostTxEqLfCtle, HostTxEqCtle, HostTxEqDfe
    * -   For each client interface set HostTxEqLfCtle = 3, HostTxEqCtle = 4, HostTxEqDfe = 5
    * -   For each client interface read HostTxEqLfCtle, HostTxEqCtle, HostTxEqDfe

**Expected Results**
    *  Initial values read for HostTxEqLfCtle, HostTxEqCtle, HostTxEqDfe are all 0
    *  Subsequent read after write yields HostTxEqLfCtle = 3, HostTxEqCtle = 4, HostTxEqDfe = 5


**Actual Results**
    PASS


Test Case : 19
--------------

**Validate switching ASIC related events are generated in the Voyager system**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure the transponder to be in InServiceWire mode 
    * -   Set AdminState to UP on fpPort1 on Voyager unit 2 
    * -   Set AdminState to UP on fpPort49 on the traffic generator 
    * -   Read all events logged by the Voyager system

**Expected Results**
    *  PortOperStateUp event should be generated for fpPort1


**Actual Results**
    PASS


Test Case : 20
--------------

**Validate AC400 related alarm resolution in the Voyager system**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure the transponder to be in InServiceWire mode 
    * -   Set AdminState to UP for AC400 module 1 on Voyager unit 2 
    * -   Set TxPower to -30 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
    * -   Set TxPower to -1 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
    * -   Read all alarms logged by the Voyager system

**Expected Results**
    *  RxLOS alarm should be generated for ModuleId 1, NwIntfId 1, and the ResolutionTime/ResolutionReason should be populated


**Actual Results**
    PASS


Test Case : 21
--------------

**Validate AC400 related events are generated in the Voyager system**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure the transponder to be in InServiceWire mode 
    * -   Set AdminState to UP for AC400 module 1 on Voyager unit 2 
    * -   Set TxPower to -30 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
    * -   Read all events logged by the Voyager system

**Expected Results**
    *  RxLOS event should be generated for ModuleId 1, NwIntfId 1


**Actual Results**
    PASS


Test Case : 22
--------------

**Validate switching ASIC related faults are generated in the Voyager system**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure the transponder to be in InServiceWire mode 
    * -   Set AdminState to UP on fpPort1 on Voyager unit 2 
    * -   Set AdminState to UP on fpPort49 on the traffic generator 
    * -   Set AdminState to DOWN on fpPort49 on the traffic generator to bring the link down 
    * -   Read all faults logged by the Voyager system

**Expected Results**
    *  PortOperStateDown fault should be generated for fpPort1


**Actual Results**
    PASS


Test Case : 23
--------------

**Validate AC400 related faults are generated in the Voyager system**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure the transponder to be in InServiceWire mode 
    * -   Set AdminState to UP for AC400 module 1 on Voyager unit 2 
    * -   Set TxPower to -30 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
    * -   Read all faults logged by the Voyager system

**Expected Results**
    *  RxLOS fault should be generated for ModuleId 1, NwIntfId 1


**Actual Results**
    PASS


Test Case : 24
--------------

**Validate switching ASIC related alarms are generated in the Voyager system**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure the transponder to be in InServiceWire mode 
    * -   Set AdminState to UP on fpPort1 on Voyager unit 2 
    * -   Set AdminState to UP on fpPort49 on the traffic generator 
    * -   Set AdminState to DOWN on fpPort49 on the traffic generator to bring the link down 
    * -   Read all alarms logged by the Voyager system

**Expected Results**
    *  PortOperStateDown alarm should be generated for fpPort1


**Actual Results**
    PASS


Test Case : 25
--------------

**Validate AC400 related alarms are generated in the Voyager system**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure the transponder to be in InServiceWire mode 
    * -   Set AdminState to UP for AC400 module 1 on Voyager unit 2 
    * -   Set TxPower to -30 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
    * -   Read all alarms logged by the Voyager system

**Expected Results**
    *  RxLOS alarm should be generated for ModuleId 1, NwIntfId 1


**Actual Results**
    PASS


Test Case : 26
--------------

**Validate switching ASIC related fault resolution in the Voyager system**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure the transponder to be in InServiceWire mode 
    * -   Set AdminState to UP on fpPort1 on Voyager unit 2 
    * -   Set AdminState to UP on fpPort49 on the traffic generator 
    * -   Set AdminState to DOWN on fpPort49 on the traffic generator to bring the link down 
    * -   Set AdminState to UP on fpPort49 on the traffic generator to bring the link down 
    * -   Read all faults logged by the Voyager system

**Expected Results**
    *  PortOperStateDown fault should be generated for fpPort1, and the ResolutionTime/ResolutionReason should be populated


**Actual Results**
    PASS


Test Case : 27
--------------

**Validate AC400 related fault resolution in the Voyager system**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure the transponder to be in InServiceWire mode 
    * -   Set AdminState to UP for AC400 module 1 on Voyager unit 2 
    * -   Set TxPower to -30 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
    * -   Set TxPower to -1 dBm for ModuleId 1 NwIntfId 0 on Voyager unit 2 
    * -   Read all faults logged by the Voyager system

**Expected Results**
    *  RxLOS fault should be generated for ModuleId 1, NwIntfId 1, and the ResolutionTime/ResolutionReason should be populated


**Actual Results**
    PASS


Test Case : 28
--------------

**Validate switching ASIC related alarm resolution in the Voyager system**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure the transponder to be in InServiceWire mode 
    * -   Set AdminState to UP on fpPort1 on Voyager unit 2 
    * -   Set AdminState to UP on fpPort49 on the traffic generator 
    * -   Set AdminState to DOWN on fpPort49 on the traffic generator to bring the link down 
    * -   Set AdminState to UP on fpPort49 on the traffic generator to bring the link down 
    * -   Read all alarms logged by the Voyager system

**Expected Results**
    *  PortOperStateDown alarm should be generated for fpPort1, and the ResolutionTime/ResolutionReason should be populated


**Actual Results**
    PASS


Test Case : 29
--------------

**Validate end to end data path connectivity**

.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Configure Voyager unit 1 to be in InServiceWire mode 
    * -   Set AdminState to UP for AC400 module 0 on Voyager unit 1 
    * -   Set AdminState to UP, and Speed to 40000, on fpPort1 on Voyager unit 1 
    * -   Set AdminState to UP, and Speed to 40000,  on fpPort49 on the traffic generator 
    * -   Configure Voyager unit 2 to be in InServiceWire mode 
    * -   Set AdminState to UP for AC400 module 0 on Voyager unit 2 
    * -   Set AdminState to UP, and Speed to 40000 on fpPort1 on Voyager unit 2 
    * -   Set AdminState to UP, and Speed to 40000 on fpPort50 on the traffic generator 
    * -   Transmit 10,000 L2 frames egressing fpPort49 on the traffic generator
    * -   Transmit 10,000 L2 frames egressing fpPort50 on the traffic generator

**Expected Results**
    *  10,000 L2 frames must ingress fpPort49 on the traffic generator
    *  10,000 L2 frames must ingress fpPort50 on the traffic generator 


**Actual Results**
    PASS
|
|
|
|
|

========================
        Appendix
========================
    

   **Test plan execution summary**

   +---------------+---------------------+---------------+---------------+
   | **Version**   |   **Comment**       |  **Author**   |    **Date**   |
   +---------------+---------------------+---------------+---------------+
   |  1.0.0.168    | All tests passed    |  Snaproute    |  10/25/2016   |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+
   |               |                     |               |               |
   +---------------+---------------------+---------------+---------------+

