Test Cases
==========


**Validate Rx power based on Tx power setting**

- **Test Steps**

-- Set Tx power value on Nw intf 0 and verify Rx power value on Nw intf 1

-- Set Tx power value on Nw intf 1 and verify Rx power value on Nw intf 0

- **Expected Results**


--

- **Actual Results**
**Validate that inventory information of various Voyager subsytems can be read**

- **Test Steps**

-- Query SystemStatus and determine if system is ready

-- Query state/DWDMModules and verify AC400 inventory

-- Query state/AsicGlobals and verify ASIC inventory

- **Expected Results**


- **Actual Results**
**Validate that the transponder can be configured to be in InWire/Oversub/Regen/PacketOptical modes**

- **Test Steps**

-- Set transponder mode to be InServiceWire

-- Query and verify current transponder mode is InServiceWire

-- Set transponder mode to be InServiceRegen

-- Query and verify current transponder mode is InServiceRegen

-- Set transponder mode to be InServiceOverSub

-- Query and verify current transponder mode is InServiceOverSub

-- Set transponder mode to be InServicePacketOptical

-- Query and verify current transponder mode is InServicePacketOptical

-- Set transponder mode to be InServicePacketOptical

-- Query and verify current transponder mode is InServicePacketOptical

-- Set transponder mode to be OutOfService

-- Query and verify current transponder mode is OutOfService

- **Expected Results**


- **Actual Results**
**Validate asic configuration for all supported transponder modes**

- **Test Steps**

-- Set transponder mode to be InServiceWire

-- Validate vlan and port configuration matches

-- Set transponder mode to be InServiceOverSub

-- Validate vlan and port configuration matches

-- Set transponder mode to be OutOfService

-- Validate that all Vlan configuration is removed

- **Expected Results**


--

- **Actual Results**
**Validate Xponder description can be set**

- **Test Steps**

-- Set xponder description

-- Validate xponder description is set correctly

- **Expected Results**


--

- **Actual Results**
