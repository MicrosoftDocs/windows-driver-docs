---
title: MSFT\_ReplicationGroupToReplicaPeer class
description: Association between replicated groups (MSFT\_ReplicationGroup to MSFT\_ReplicaPeer).
ms.assetid: 57DC1776-987F-491E-A063-B17824E02496
keywords:
- MSFT_ReplicationGroupToReplicaPeer class Windows Storage Management API
- MSFT_ReplicationGroupToReplicaPeer class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationGroupToReplicaPeer
- MSFT_ReplicationGroupToReplicaPeer.ReplicationGroup
- MSFT_ReplicationGroupToReplicaPeer.ReplicaPeer
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_ReplicationGroupToReplicaPeer class

Association between replicated groups ([**MSFT\_ReplicationGroup**](msft-replicationgroup.md) to [**MSFT\_ReplicaPeer**](msft-replicapeer.md)).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_ReplicationGroupToReplicaPeer : MSFT_Synchronized
{
  MSFT_ReplicationGroup REF ReplicationGroup;
  MSFT_ReplicaPeer      REF ReplicaPeer;
};
```

## Members

The **MSFT\_ReplicationGroupToReplicaPeer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_ReplicationGroupToReplicaPeer** class has these properties.

 

**ReplicaPeer**
   

Data type: **[**MSFT\_ReplicaPeer**](msft-replicapeer.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**ReplicationGroup**
   

Data type: **[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)**
 

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
 

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
 

[**MSFT\_ReplicaPeer**](msft-replicapeer.md)
 

 

 





