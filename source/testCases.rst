==========
Test Cases
==========



Test Case : 1
-------------

 Validate Tx power can be set on AC400 network interfaces
.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set Tx power value on Nw intf 0
    * -   Read Rx power value on Nw intf 1 
    * -   Set Tx power value on Nw intf 1 and verify Rx power value on Nw intf 0

**Expected Results**


**Actual Results**
    PASS


Test Case : 2
-------------

 Validate that inventory information of the AC400 optical module can be read
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

 Validate that inventory information of the Tomahawk ASIC can be read
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

 Validate that the transponder can be configured to be in InWire/Oversub/Regen/PacketOptical modes
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


**Actual Results**
    PASS


Test Case : 5
-------------

 Validate asic configuration for all supported transponder modes
.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set transponder mode to be InServiceWire
    * -   Validate vlan and port configuration matches
    * -   Set transponder mode to be InServiceOverSub
    * -   Validate vlan and port configuration matches
    * -   Set transponder mode to be OutOfService
    * -   Validate that all Vlan configuration is removed

**Expected Results**


**Actual Results**
    PASS


Test Case : 6
-------------

 Validate Xponder description can be set
.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set xponder description
    * -   Validate xponder description is set correctly

**Expected Results**


**Actual Results**
    PASS


Test Case : 7
-------------

 Validate AC400 automatic turn up and turn down
.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set AdminState to UP on DWDMModule
    * -   Validate module turns up to READY state
    * -   Set AdminState to DOWN on DWDMModule
    * -   Validate module turns LOW POWER state

**Expected Results**


**Actual Results**
    PASS


Test Case : 8
-------------

 Validate AC400 automatic turn up and turn down
.. list-table:: 
    :header-rows: 1

    * -  Test Execution Steps
    * -   Set AdminState to DOWN on DWDMModule
    * -   Validate module turns down to LOW POWER state
    * -   Set AdminState to UP on DWDMModule
    * -   Validate module turns up to READY state

**Expected Results**


**Actual Results**
    PASS
