---
title: MSFT\_InitiatorPort class
description: Represents a Host Bus Adapter (HBA) initiator port on the host computer.
ms.assetid: FFD445F4-3A34-4681-B38E-6E84C0E5DF06
keywords:
- MSFT_InitiatorPort class Windows Storage Management API
- MSFT_InitiatorPort class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_InitiatorPort
- MSFT_InitiatorPort.ObjectId
- MSFT_InitiatorPort.PortAddress
- MSFT_InitiatorPort.NodeAddress
- MSFT_InitiatorPort.InstanceName
- MSFT_InitiatorPort.AlternatePortAddress
- MSFT_InitiatorPort.AlternateNodeAddress
- MSFT_InitiatorPort.PortType
- MSFT_InitiatorPort.ConnectionType
- MSFT_InitiatorPort.OtherConnectionTypeDescription
- MSFT_InitiatorPort.OperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_InitiatorPort class

Represents a Host Bus Adapter (HBA) initiator port on the host computer.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_InitiatorPort
{
  String ObjectId;
  String PortAddress;
  String NodeAddress;
  String InstanceName;
  String AlternatePortAddress[];
  String AlternateNodeAddress[];
  UInt16 PortType;
  UInt16 ConnectionType;
  String OtherConnectionTypeDescription;
  UInt16 OperationalStatus[];
};
```

## Members

The **MSFT\_InitiatorPort** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_InitiatorPort** class has these methods.



| Method                                                      | Description                                              |
|:------------------------------------------------------------|:---------------------------------------------------------|
| [**SetNodeAddress**](msft-initiatorport-setnodeaddress.md) | Sets the node address for the initiator port. |



 

### Properties

The **MSFT\_InitiatorPort** class has these properties.

 

**AlternateNodeAddress**
   

Data type: **String** array
 

Access type: Read-only
 

A list of alternate node addresses for the initiator.

 

**AlternatePortAddress**
   

Data type: **String** array
 

Access type: Read-only
 

A list of alternate port addresses for the initiator.

 

**ConnectionType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The connection type.

You can specify a predefined connection type or a custom connection type. To specify a predefined connection type, use a value other than **Other**.

To specify a custom connection type, use **Other** and specify a non-NULL value for the **OtherConnectionTypeDescription** property.

 

**Other** (0)
 

**Fibre Channel** (1)
 

**iSCSI** (2)
 

**SAS** (3)
 

 

**InstanceName**
   

Data type: **String**
 

Access type: Read-only
 

The instance name for the initiator.

 

**NodeAddress**
   

Data type: **String**
 

Access type: Read-only
 

The node address for the initiator.

 

**ObjectId**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: **Key**
 

The object identifier for the initiator.

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array of values that denote the current status of the initiator port.

You can specify a predefined status or a custom status. To specify a predefined status, use a value other than **Other**.

To specify a custom status, use **Other** and specify a non-NULL value for the **OtherOperationalStatusDescription** property.

 

**Unknown** (1)
 

**Operational** (2)
 

**User Offline** (3)
 

**Bypassed** (4)
 

**In diagnostics mode** (5)
 

**Link Down** (6)
 

**Port Error** (7)
 

**Loopback** (8)
 

 

**OtherConnectionTypeDescription**
   

Data type: **String**
 

Access type: Read-only
 

A string representation of the vendor-defined connection type. This property should be set only if the value of the **ConnectionType** property is **Other**.

 

**PortAddress**
   

Data type: **String**
 

Access type: Read-only
 

The port address for the initiator.

 

**PortType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The port type for the initiator.

 

**Unknown** (1)
 

**Other** (2)
 

**Not present** (3)
 

**Fabric** (5)
 

**Public Loop** (6)
 

**FL Port** (7)
 

**Fabric Port** (8)
 

**Fabric expansion port** (9)
 

**Generic Fabric Port** (10)
 

**Private Loop** (20)
 

**Point to Point** (21)
 

**SAS** (30)
 

**SATA** (31)
 

**SAS Expander** (32)
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





