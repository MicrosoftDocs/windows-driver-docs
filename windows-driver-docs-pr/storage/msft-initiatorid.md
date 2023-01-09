---
title: MSFT\_InitiatorId class
description: Represents an initiator identifier.
ms.assetid: 446877F7-C9A3-40D5-A17E-D3DBBF341B9B
keywords:
- MSFT_InitiatorId class Windows Storage Management API
- MSFT_InitiatorId class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_InitiatorId
- MSFT_InitiatorId.InitiatorAddress
- MSFT_InitiatorId.Type
- MSFT_InitiatorId.HostType
- MSFT_InitiatorId.OtherHostTypeDescription
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_InitiatorId class

Represents an initiator identifier.

This object represents the storage subsystem's view of an initiator port. This is used in conjunction with a target port to establish which initiator port is allowed access to the subsystem's virtual disks.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_InitiatorId : MSFT_StorageObject
{
  String InitiatorAddress;
  UInt16 Type;
  UInt16 HostType[];
  String OtherHostTypeDescription[];
};
```

## Members

The **MSFT\_InitiatorId** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_InitiatorId** class has these methods.



| Method                                                | Description                                                |
|:------------------------------------------------------|:-----------------------------------------------------------|
| [**DeleteObject**](msft-initiatorid-deleteobject.md) | Deletes an instance of an initiator identifier. |



 

### Properties

The **MSFT\_InitiatorId** class has these properties.

 

**HostType**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

An array of values specifying the operating system, version, driver, and other host environment factors.

 

**Unknown** (0)
 

**Other** (1)
 

**Standard** (2)
 

**Solaris** (3)
 

**HPUX** (4)
 

**OpenVMS** (5)
 

**Tru64** (6)
 

**Netware** (7)
 

**Sequent** (8)
 

**AIX** (9)
 

**DGUX** (10)
 

**Dynix** (11)
 

**Irix** (12)
 

**Cisco iSCSI Storage Router** (13)
 

**Linux** (14)
 

**Microsoft Windows** (15)
 

**OS400** (16)
 

**TRESPASS** (17)
 

**HI-UX** (18)
 

**VMware ESXi** (19)
 

**Microsoft Windows Server 2008** (20)
 

**Microsoft Windows Server 2003** (21)
 

**Microsoft Reserved** (22..32767)
 

**Vendor Specific** (32768..65535)
 

 

**InitiatorAddress**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The address or unique identifier for the corresponding initiator port.

 

**OtherHostTypeDescription**
   

Data type: **String** array
 

Access type: Read-only
 

Qualifiers: [**ArrayType**](/windows/win32/wmisdk/standard-qualifiers) ( "Indexed" ), [**ModelCorrespondence {"CIM\_StorageClientSettingData.ClientTypes"}**](/windows/win32/wmisdk/standard-qualifiers)
 

If the corresponding entry in the **HostType** array is **Other**, the entry in this property contains a string describing the host operating system information.

If the corresponding entry in the **HostType** array is not **Other**, the entry in this property allows variations or qualifications of **ClientTypes** for example, different versions of Solaris.

 

**Type**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The type of identifier that is used in the **InitiatorAddress** property.

 

**Other** (1)
 

**PortWWN** (2)
 

**NodeWWN** (3)
 

**HostName** (4)
 

**iSCSI Name** (5)
 

**SwitchWWN** (6)
 

**SASAddress** (7)
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

