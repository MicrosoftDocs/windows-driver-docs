---
title: MSFT\_MaskingSet class
description: Represents a masking set.
ms.assetid: 2B745820-9347-414A-8D33-36C8DB97385D
keywords:
- MSFT_MaskingSet class Windows Storage Management API
- MSFT_MaskingSet class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_MaskingSet
- MSFT_MaskingSet.FriendlyName
- MSFT_MaskingSet.Name
- MSFT_MaskingSet.HostType
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_MaskingSet class

Represents a masking set.

A masking set is a collection of virtual disks, target ports, and initiator IDs that are used for bulk [**Show**](msft-virtualdisk-show.md) and [**Hide**](msft-virtualdisk-hide.md) operations. When a resource is added to a masking set, it is made available for access to all other resources in the masking set. For example, adding a virtual disk object to a masking set will allow all initiator IDs in the masking set to access the virtual disk object.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_MaskingSet : MSFT_StorageObject
{
  String FriendlyName;
  String Name;
  UInt16 HostType;
};
```

## Members

The **MSFT\_MaskingSet** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_MaskingSet** class has these methods.



| Method                                                                 | Description                                                                |
|:-----------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**AddInitiatorId**](msft-maskingset-addinitiatorid.md)               | Adds one or more initiator identifiers to the masking set.      |
| [**AddTargetPort**](msft-maskingset-addtargetport.md)                 | Adds one or more target ports to the masking set.               |
| [**AddVirtualDisk**](msft-maskingset-addvirtualdisk.md)               | Adds one or more virtual disks to the masking set.              |
| [**DeleteObject**](msft-maskingset-deleteobject.md)                   | Deletes the masking set instance.                               |
| [**GetSecurityDescriptor**](msft-maskingset-getsecuritydescriptor.md) | Retrieves the security descriptor for the masking set instance. |
| [**RemoveInitiatorId**](msft-maskingset-removeinitiatorid.md)         | Removes one or more initiator identifiers from the masking set. |
| [**RemoveTargetPort**](msft-maskingset-removetargetport.md)           | Removes one or more target ports from the masking set.          |
| [**RemoveVirtualDisk**](msft-maskingset-removevirtualdisk.md)         | Removes one or more virtual disks from the masking set.         |
| [**SetFriendlyName**](msft-maskingset-setfriendlyname.md)             | Sets the friendly name for the masking set.                     |
| [**SetSecurityDescriptor**](msft-maskingset-setsecuritydescriptor.md) | Sets the security descriptor for the masking set object.        |



 

### Properties

The **MSFT\_MaskingSet** class has these properties.

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-friendly name for the masking set. It is specified when the masking set is created, and it can be changed using the [**SetFriendlyName**](msft-maskingset-setfriendlyname.md) method.

 

**HostType**
   

Data type: **UInt16**
 

Access type: Read-only
 

The host operating system or other host environmental factors that may influence the behavior that the storage system should have when showing a virtual disk to an initiator.

 

**Unknown** (0)
 

**Other** (1)
 

**Standard** (2)
 

**Solaris** (3)
 

**HPUX**
 

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
 

 

**Name**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-friendly system-defined name for the masking set. This name is unique within the scope of the owning storage subsystem.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

