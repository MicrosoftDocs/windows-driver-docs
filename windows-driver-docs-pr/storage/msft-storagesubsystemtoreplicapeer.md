---
title: MSFT\_StorageSubSystemToReplicaPeer class
description: Association between an MSFT\_StorageSubSystem and MSFT\_ReplicaPeer.
ms.assetid: F0DA41D9-7EFE-4526-918A-183110D1E309
keywords:
- MSFT_StorageSubSystemToReplicaPeer class Windows Storage Management API
- MSFT_StorageSubSystemToReplicaPeer class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToReplicaPeer
- MSFT_StorageSubSystemToReplicaPeer.StorageSubSystem
- MSFT_StorageSubSystemToReplicaPeer.ReplicaPeer
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToReplicaPeer class

Association between an [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_ReplicaPeer**](msft-replicapeer.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToReplicaPeer
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_ReplicaPeer      REF ReplicaPeer;
};
```

## Members

The **MSFT\_StorageSubSystemToReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToReplicaPeer** class has these properties.

 

**ReplicaPeer**
   

Data type: **[**MSFT\_ReplicaPeer**](msft-replicapeer.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StorageSubSystem**
   

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
 

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

 

[**MSFT\_ReplicaPeer**](msft-replicapeer.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





