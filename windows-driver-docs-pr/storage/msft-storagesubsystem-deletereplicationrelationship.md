---
title: DeleteReplicationRelationship method of the MSFT\_StorageSubSystem class
description: Deletes a replication relationship between groups. The groups themselves are deleted if they have no more relationships with other groups. The method is only available on subsystems that support fully discovered replication.
ms.assetid: FCACCFF1-A80C-4B51-888A-90E31760C067
keywords:
- DeleteReplicationRelationship method Windows Storage Management API
- DeleteReplicationRelationship method Windows Storage Management API , MSFT_StorageSubSystem interface
- MSFT_StorageSubSystem interface Windows Storage Management API , DeleteReplicationRelationship method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.DeleteReplicationRelationship
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteReplicationRelationship method of the MSFT\_StorageSubSystem class

Deletes a replication relationship between groups. The groups themselves are deleted if they have no more relationships with other groups. The method is only available on subsystems that support fully discovered replication.

## Syntax


```mof
UInt32 DeleteReplicationRelationship(
  [in]  String              SourceReplicationGroup,
  [in]  String              TargetGroupReplicaPeer,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*SourceReplicationGroup* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicationGroup**](msft-replicationgroup.md) object, specifying the source replication group.

 

*TargetGroupReplicaPeer* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object, specifying the target replication group.

 

*CreatedStorageJob* \[out\]
 

Returns a reference to the storage job object used to track the long-running operation.

 

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

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





