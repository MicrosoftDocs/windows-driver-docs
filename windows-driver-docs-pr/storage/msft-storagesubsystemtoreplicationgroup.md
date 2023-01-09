---
title: MSFT\_StorageSubSystemToReplicationGroup class
description: Association between a MSFT\_StorageSubSystem and MSFT\_ReplicationGroup.
ms.assetid: FBADE666-2039-4C76-ACBC-E5804EFFF11C
keywords:
- MSFT_StorageSubSystemToReplicationGroup class Windows Storage Management API
- MSFT_StorageSubSystemToReplicationGroup class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToReplicationGroup
- MSFT_StorageSubSystemToReplicationGroup.StorageSubSystem
- MSFT_StorageSubSystemToReplicationGroup.ReplicationGroup
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToReplicationGroup class

Association between a [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_ReplicationGroup**](msft-replicationgroup.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToReplicationGroup
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_ReplicationGroup REF ReplicationGroup;
};
```

## Members

The **MSFT\_StorageSubSystemToReplicationGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToReplicationGroup** class has these properties.

 

**ReplicationGroup**
   

Data type: **[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)**
 

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

 

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





