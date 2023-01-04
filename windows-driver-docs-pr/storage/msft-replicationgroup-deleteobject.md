---
title: DeleteObject method of the MSFT\_ReplicationGroup class
description: Deletes an empty replication group.
ms.assetid: B0439C17-741B-43ED-99C1-B2A1CE99E267
keywords:
- DeleteObject method Windows Storage Management API
- DeleteObject method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , DeleteObject method
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup.DeleteObject
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteObject method of the MSFT\_ReplicationGroup class

Deletes an empty replication group. If the group contains any replicas, these replicas must be removed first.

## Syntax


```mof
UInt32 DeleteObject(
  [out] String ExtendedStatus
);
```



## Parameters

 

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
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**The operation is not supported while the cluster is being upgraded.** (40009)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**This operation is not supported on primordial storage pools.** (48000)
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

**The replication group contains replicas.** (57000)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
 

 

 





