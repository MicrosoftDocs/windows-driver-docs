---
title: RemoveMember method of the MSFT\_ReplicationGroup class
description: Remove members from this replication group.
ms.assetid: 52BED6E0-FCB3-49D9-9766-78B191DEB0C2
keywords:
- RemoveMember method Windows Storage Management API
- RemoveMember method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , RemoveMember method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationGroup.RemoveMember
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# RemoveMember method of the MSFT\_ReplicationGroup class

Remove members from this replication group.

## Syntax


```mof
UInt32 RemoveMember(
  [in]  String StorageObjects[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*StorageObjects* \[in\]
 

An array of strings containing embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects specifying the storage objects to remove from the group.

 

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
 

 

 





