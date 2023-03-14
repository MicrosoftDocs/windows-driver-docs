---
title: SetReplicationRelationship method of the MSFT\_ReplicationGroup class
description: Modifies the relationship between replication groups.
ms.assetid: AEA4DB91-51E2-4F47-BC45-D58C82580AAA
keywords:
- SetReplicationRelationship method Windows Storage Management API
- SetReplicationRelationship method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , SetReplicationRelationship method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationGroup.SetReplicationRelationship
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetReplicationRelationship method of the MSFT\_ReplicationGroup class

Modifies the relationship between replication groups.

## Syntax


```mof
UInt32 SetReplicationRelationship(
  [in]  UInt16 Operation,
  [in]  String TargetGroup,
  [in]  String SourceStorageObjects[],
  [in]  String TargetStorageObjects[],
  [in]  String SyncPairs[],
  [out] String CreatedReplicaPeer,
  [out] String ExtendedStatus
);
```



## Parameters

 

*Operation* \[in\]
 

One of the following values:

 

**Abort** (2)
 

**ActivateConsistency** (3)
 

**Activate** (4)
 

**AddSyncPair** (5)
 

**DeactivateConsistency** (6)
 

**Deactivate** (7)
 

**Detach** (8)
 

**Dissolve** (9)
 

**Failover** (10)
 

**Failback** (11)
 

**Fracture** (12)
 

**RemoveSyncPair** (13)
 

**ResyncReplica** (14)
 

**RestoreFromReplica** (15)
 

**Resume** (16)
 

**ResetToSync** (17)
 

**ResetToAsync** (18)
 

**ReturnToResourcePool** (19)
 

**ReverseRoles** (20)
 

**Split** (21)
 

**Suspend** (22)
 

**Unprepare** (23)
   

*TargetGroup* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object specifying the replica peer for the target group.

 

*SourceStorageObjects* \[in\]
 

An array of strings containing embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects specifying source objects by Id to be replicated. Consistency ordering is based on the order of objects in this array.

 

*TargetStorageObjects* \[in\]
 

An array of strings containing embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects specifying target objects by Id to be replicated. Consistency ordering is based on the order of objects in this array.

 

*SyncPairs* \[in\]
 

An array of strings containing embedded [**MSFT\_Synchronized**](msft-synchronized.md) objects specifying the element replicas for **AddSyncPair** or **RemoveSyncPair**.

 

*CreatedReplicaPeer* \[out\]
 

This parameter receives a string that contains an embedded [**MSFT\_Synchronized**](msft-synchronized.md) object representing the association between the replication groups.

 

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
 

**Method Parameters Checked - Job Started** (4096)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**The operation is not supported while the cluster is being upgraded.** (40009)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
 

 

 





