---
title: AddMember method of the MSFT\_ReplicationGroup class
description: Adds members to this replication group.
ms.assetid: 1E6A5089-40BB-4401-AC4D-7A266FB18C46
keywords:
- AddMember method Windows Storage Management API
- AddMember method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , AddMember method
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup.AddMember
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AddMember method of the MSFT\_ReplicationGroup class

Adds members to this replication group.

## Syntax


```mof
UInt32 AddMember(
  [in]  String StorageObjects[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*StorageObjects* \[in\]
 

An array of strings containing embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects specifying the storage objects to add to the group.

 

*ExtendedStatus* \[out\]
 

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

 

## Return value

 

**Success** (0)
 

**Not Supported** (1)
 

**Unspecified Error** (2)
 

**Timeout** (3)
 

**Failed** (4)
 

**Invalid Parameter** (5)
 

**Object Not Found** (8)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**The operation is not supported while the cluster is being upgraded.** (40009)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
 

 

 





