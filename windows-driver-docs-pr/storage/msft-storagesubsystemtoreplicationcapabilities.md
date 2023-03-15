---
title: MSFT\_StorageSubSystemToReplicationCapabilities class
description: Association between an MSFT\_StorageSubSystem and MSFT\_ReplicationCapabilities.
ms.assetid: 73AC3F3F-645B-4D0C-AA7E-2CAAB47E27D8
keywords:
- MSFT_StorageSubSystemToReplicationCapabilities class Windows Storage Management API
- MSFT_StorageSubSystemToReplicationCapabilities class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToReplicationCapabilities
- MSFT_StorageSubSystemToReplicationCapabilities.StorageSubSystem
- MSFT_StorageSubSystemToReplicationCapabilities.ReplicationCapabilities
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToReplicationCapabilities class

Association between an [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToReplicationCapabilities
{
  MSFT_StorageSubSystem        REF StorageSubSystem;
  MSFT_ReplicationCapabilities REF ReplicationCapabilities;
};
```

## Members

The **MSFT\_StorageSubSystemToReplicationCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToReplicationCapabilities** class has these properties.

 

**ReplicationCapabilities**
   

Data type: **[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)**
 

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

 

[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





