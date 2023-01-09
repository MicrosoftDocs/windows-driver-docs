---
title: MSFT\_TargetPort class
description: Represents a target port.
ms.assetid: 00D10838-331D-4145-9040-2F96A85324EB
keywords:
- MSFT_TargetPort class Windows Storage Management API
- MSFT_TargetPort class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_TargetPort
- MSFT_TargetPort.FriendlyName
- MSFT_TargetPort.PortAddress
- MSFT_TargetPort.NodeAddress
- MSFT_TargetPort.StorageControllerId
- MSFT_TargetPort.Role
- MSFT_TargetPort.UsageRestriction
- MSFT_TargetPort.HealthStatus
- MSFT_TargetPort.OperationalStatus
- MSFT_TargetPort.OtherOperationalStatusDescription
- MSFT_TargetPort.ConnectionType
- MSFT_TargetPort.OtherConnectionTypeDescription
- MSFT_TargetPort.LinkTechnology
- MSFT_TargetPort.OtherLinkTechnology
- MSFT_TargetPort.Speed
- MSFT_TargetPort.MaxSpeed
- MSFT_TargetPort.NetworkAddresses
- MSFT_TargetPort.PortNumbers
- MSFT_TargetPort.PortType
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_TargetPort class

Represents a target port.

A target port is an endpoint in a storage subsystem with associated properties for showing and hiding virtual disks. Fibre Channel, Serial Attached SCSI, and iSCSI ports within a storage subsystem controller are all examples of target ports.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_TargetPort : MSFT_StorageObject
{
  String FriendlyName;
  String PortAddress;
  String NodeAddress;
  String StorageControllerId;
  UInt16 Role;
  UInt16 UsageRestriction;
  UInt16 HealthStatus;
  UInt16 OperationalStatus[];
  String OtherOperationalStatusDescription;
  UInt16 ConnectionType;
  String OtherConnectionTypeDescription;
  UInt16 LinkTechnology;
  String OtherLinkTechnology;
  UInt64 Speed;
  UInt64 MaxSpeed;
  String NetworkAddresses[];
  UInt16 PortNumbers[];
  UInt16 PortType;
};
```

## Members

The **MSFT\_TargetPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_TargetPort** class has these properties.

 

**ConnectionType**
   

Data type: **UInt16**
 

Access type: Read-only
 



| Value                                                                        | Meaning                  |
|------------------------------------------------------------------------------|--------------------------|
|  1  | Other         |
|  2  | Fibre Channel |
|  3  | Parallel SCSI |
|  4  | SSA           |
|  5  | IEEE 1394     |
|  6  | RDMA          |
|  7  | iSCSI         |
|  8  | SAS           |
|  9  | ADT           |



 

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-friendly name for the target port.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The health status of the target port.

 

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>**Healthy** (0)
 

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>**Warning** (1)
 

<span id="Unhealthy_"></span><span id="unhealthy_"></span><span id="UNHEALTHY_"></span>**Unhealthy** (2 )
 

 

**LinkTechnology**
   

Data type: **UInt16**
 

Access type: Read-only
 

The link technology of the target port.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
 

<span id="Ethernet"></span><span id="ethernet"></span><span id="ETHERNET"></span>**Ethernet** (2)
 

<span id="IB"></span><span id="ib"></span>**IB** (3)
 

<span id="FC"></span><span id="fc"></span>**FC** (4)
 

<span id="FDDI"></span><span id="fddi"></span>**FDDI** (5)
 

<span id="ATM"></span><span id="atm"></span>**ATM** (6)
 

<span id="Token_Ring"></span><span id="token_ring"></span><span id="TOKEN_RING"></span>**Token Ring** (7)
 

<span id="Frame_Relay"></span><span id="frame_relay"></span><span id="FRAME_RELAY"></span>**Frame Relay** (8)
 

<span id="Infrared"></span><span id="infrared"></span><span id="INFRARED"></span>**Infrared** (9)
 

<span id="BlueTooth"></span><span id="bluetooth"></span><span id="BLUETOOTH"></span>**BlueTooth** (10)
 

<span id="Wireless_LAN"></span><span id="wireless_lan"></span><span id="WIRELESS_LAN"></span>**Wireless LAN** (11)
 

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
 

 

**MaxSpeed**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("bits/sec")
 

The maximum speed of the target port, in bits per second.

 

**NetworkAddresses**
   

Data type: **String** array
 

Access type: Read-only
 

An array of strings that represent the various network addresses for the target port.

The type and format of these addresses are specified in the PortType property.

 

**NodeAddress**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The node address.

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

An array of values that denote the operational status of the target port.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
 

<span id="OK"></span><span id="ok"></span>**OK** (2)
 

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (3)
 

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>**Stressed** (4)
 

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>**Predictive Failure** (5)
 

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>**Error** (6)
 

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>**Non-Recoverable Error** (7)
 

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>**Starting** (8)
 

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>**Stopping** (9)
 

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped** (10)
 

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>**In Service** (11)
 

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>**No Contact** (12)
 

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>**Lost Communication** (13)
 

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>**Aborted** (14)
 

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>**Dormant** (15)
 

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>**Supporting Entity in Error** (16)
 

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>**Completed** (17)
 

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>**Power Mode** (18)
 

<span id="Microsoft_Reserved"></span><span id="microsoft_reserved"></span><span id="MICROSOFT_RESERVED"></span>**Microsoft Reserved** (..)
 

 

**OtherConnectionTypeDescription**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the vendor-defined connection type. Relevant only if the **ConnectionType** property is **Other.**

 

**OtherLinkTechnology**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the vendor-defined link technology. Relevant only if the **LinkTechnology** property is **Other**.

 

**OtherOperationalStatusDescription**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the vendor-defined status. Relevant only if the **OperationalStatus** array contains **Other.**

 

**PortAddress**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The port identifier or address.

For Fibre Channel networks, this property should be the World-Wide Name (WWN) for the port, formatted as a hexadecimal string (16 characters long), with the most significant byte first. For example, a WWN address of 01:23:45:67:89:AB:CD:EF should be represented as 0123456789ABCDEF.

For iSCSI networks, this field should be the IQN.

 

**PortNumbers**
   

Data type: **UInt16** array
 

Access type: Read-only
 

A list of port numbers for the target port.

 

**PortType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The specific mode that is currently enabled for the port. If the port is logged in, this will be the negotiated port type. Otherwise, the configured port type will be reported.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
 

<span id="N"></span><span id="n"></span>**N** (10)
 

<span id="NL"></span><span id="nl"></span>**NL** (11)
 

<span id="F_NL"></span><span id="f_nl"></span>**F/NL** (12)
 

<span id="NX"></span><span id="nx"></span>**NX** (13)
 

<span id="E"></span><span id="e"></span>**E** (14)
 

<span id="F"></span><span id="f"></span>**F** (15)
 

<span id="FL"></span><span id="fl"></span>**FL** (16)
 

<span id="B"></span><span id="b"></span>**B** (17)
 

<span id="G"></span><span id="g"></span>**G** (18)
 

<span id="10BaseT"></span><span id="10baset"></span><span id="10BASET"></span>**10BaseT** (50)
 

<span id="10-100BaseT"></span><span id="10-100baset"></span><span id="10-100BASET"></span>**10-100BaseT** (51)
 

<span id="100BaseT"></span><span id="100baset"></span><span id="100BASET"></span>**100BaseT** (52)
 

<span id="1000BaseT"></span><span id="1000baset"></span><span id="1000BASET"></span>**1000BaseT** (53)
 

<span id="2500BaseT"></span><span id="2500baset"></span><span id="2500BASET"></span>**2500BaseT** (54)
 

<span id="10GBaseT"></span><span id="10gbaset"></span><span id="10GBASET"></span>**10GBaseT** (55)
 

<span id="10GBase-CX4"></span><span id="10gbase-cx4"></span><span id="10GBASE-CX4"></span>**10GBase-CX4** (56)
 

<span id="SAS"></span><span id="sas"></span>**SAS** (94)
 

<span id="100Base-FX"></span><span id="100base-fx"></span><span id="100BASE-FX"></span>**100Base-FX** (100)
 

<span id="100Base-SX"></span><span id="100base-sx"></span><span id="100BASE-SX"></span>**100Base-SX** (101)
 

<span id="1000Base-SX"></span><span id="1000base-sx"></span><span id="1000BASE-SX"></span>**1000Base-SX** (102)
 

<span id="1000Base-LX"></span><span id="1000base-lx"></span><span id="1000BASE-LX"></span>**1000Base-LX** (103)
 

<span id="1000Base-CX"></span><span id="1000base-cx"></span><span id="1000BASE-CX"></span>**1000Base-CX** (104)
 

<span id="10GBase-SR"></span><span id="10gbase-sr"></span><span id="10GBASE-SR"></span>**10GBase-SR** (105)
 

<span id="10GBase-SW"></span><span id="10gbase-sw"></span><span id="10GBASE-SW"></span>**10GBase-SW** (106)
 

<span id="10GBase-LX4"></span><span id="10gbase-lx4"></span><span id="10GBASE-LX4"></span>**10GBase-LX4** (107)
 

<span id="10GBase-LR"></span><span id="10gbase-lr"></span><span id="10GBASE-LR"></span>**10GBase-LR** (108)
 

<span id="10GBase-LW"></span><span id="10gbase-lw"></span><span id="10GBASE-LW"></span>**10GBase-LW** (109)
 

<span id="10GBase-ER"></span><span id="10gbase-er"></span><span id="10GBASE-ER"></span>**10GBase-ER** (110)
 

<span id="10GBase-EW"></span><span id="10gbase-ew"></span><span id="10GBASE-EW"></span>**10GBase-EW** (111)
 

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (112..15999)
 

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>**Vendor Reserved** (16000..65535)
 

 

**Role**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The role of this controller port. For iSCSI, this port must act as either a target or an initiator endpoint. Other transports allow a port to act as both an initiator and a target.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Initiator"></span><span id="initiator"></span><span id="INITIATOR"></span>**Initiator** (1)
 

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>**Target** (2)
 

<span id="Both_Initiator_and_Target"></span><span id="both_initiator_and_target"></span><span id="BOTH_INITIATOR_AND_TARGET"></span>**Both Initiator and Target** (3)
 

 

**Speed**
   

Data type: **UInt64**
 

Access type: Read-only
 

Qualifiers: [**Units**](/windows/win32/wmisdk/standard-qualifiers) ("bits/sec")
 

The current speed (bandwidth) of the port, in bits per second. For ports that vary in bandwidth, or for those where no accurate estimation can be made, this property should contain the nominal bandwidth for the port.

 

**StorageControllerId**
   

Data type: **String**
 

Access type: Read-only
 

The identifier of the controller to which this port belongs.

 

**UsageRestriction**
   

Data type: **UInt16**
 

Access type: Read-only
 

The usage restriction of the target port.

In some circumstances, a target port may be identifiable as a front-end or back-end port. For example, a storage array might have back-end ports to communicate with physical disks, and front-end ports to communicate with hosts. If there is no restriction on the use of the port, then the value should be set to **Not restricted**.

 

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
 

<span id="Front-end_only"></span><span id="front-end_only"></span><span id="FRONT-END_ONLY"></span>**Front-end only** (2)
 

<span id="Back-end_only"></span><span id="back-end_only"></span><span id="BACK-END_ONLY"></span>**Back-end only** (3)
 

<span id="Not_restricted"></span><span id="not_restricted"></span><span id="NOT_RESTRICTED"></span>**Not restricted** (4)
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

