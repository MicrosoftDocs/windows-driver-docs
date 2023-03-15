---
title: MSFT\_VirtualDiskToReplicaPeer class
description: Association between replicated virtual disks (MSFT\_VirtualDisk to MSFT\_ReplicaPeer).
ms.assetid: 751166F2-07D4-4E69-AE8D-38EAFAF78DE3
keywords:
- MSFT_VirtualDiskToReplicaPeer class Windows Storage Management API
- MSFT_VirtualDiskToReplicaPeer class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_VirtualDiskToReplicaPeer
- MSFT_VirtualDiskToReplicaPeer.VirtualDisk
- MSFT_VirtualDiskToReplicaPeer.ReplicaPeer
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_VirtualDiskToReplicaPeer class

Association between replicated virtual disks ([**MSFT\_VirtualDisk**](msft-virtualdisk.md) to [**MSFT\_ReplicaPeer**](msft-replicapeer.md))

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_VirtualDiskToReplicaPeer : MSFT_Synchronized
{
  MSFT_VirtualDisk REF VirtualDisk;
  MSFT_ReplicaPeer REF ReplicaPeer;
};
```

## Members

The **MSFT\_VirtualDiskToReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VirtualDiskToReplicaPeer** class has these properties.

 

**ReplicaPeer**
   

Data type: **[**MSFT\_ReplicaPeer**](msft-replicapeer.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**VirtualDisk**
   

Data type: **[**MSFT\_VirtualDisk**](msft-virtualdisk.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Synchronized**](msft-synchronized.md)
 

[**MSFT\_ReplicaPeer**](msft-replicapeer.md)
 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





