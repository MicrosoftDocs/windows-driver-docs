---
title: SetReplicationRelationship method of the MSFT\_VirtualDisk class
description: Sets the replication relationship between virtual disks.
ms.assetid: FF87D964-498E-4413-BC33-CCC1E6A5AF0F
keywords:
- SetReplicationRelationship method Windows Storage Management API
- SetReplicationRelationship method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , SetReplicationRelationship method
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk.SetReplicationRelationship
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetReplicationRelationship method of the MSFT\_VirtualDisk class

Sets the replication relationship between virtual disks.

## Syntax


```mof
UInt32 SetReplicationRelationship(
  [in]  UInt16              Operation,
  [in]  String              VirtualDiskReplicaPeer,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*Operation* \[in\]
 

One of the following values:

 

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>**Abort** (2)
 

<span id="ActivateConsistency"></span><span id="activateconsistency"></span><span id="ACTIVATECONSISTENCY"></span>**ActivateConsistency** (3)
 

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>**Activate** (4)
 

<span id="AddSyncPair"></span><span id="addsyncpair"></span><span id="ADDSYNCPAIR"></span>**AddSyncPair** (5)
 

<span id="DeactivateConsistency"></span><span id="deactivateconsistency"></span><span id="DEACTIVATECONSISTENCY"></span>**DeactivateConsistency** (6)
 

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>**Deactivate** (7)
 

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>**Detach** (8)
 

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>**Dissolve** (9)
 

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>**Failover** (10)
 

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>**Failback** (11)
 

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>**Fracture** (12)
 

<span id="RemoveSyncPair"></span><span id="removesyncpair"></span><span id="REMOVESYNCPAIR"></span>**RemoveSyncPair** (13)
 

<span id="ResyncReplica"></span><span id="resyncreplica"></span><span id="RESYNCREPLICA"></span>**ResyncReplica** (14)
 

<span id="RestoreFromReplica"></span><span id="restorefromreplica"></span><span id="RESTOREFROMREPLICA"></span>**RestoreFromReplica** (15)
 

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>**Resume** (16)
 

<span id="ResetToSync"></span><span id="resettosync"></span><span id="RESETTOSYNC"></span>**ResetToSync** (17)
 

<span id="ResetToAsync"></span><span id="resettoasync"></span><span id="RESETTOASYNC"></span>**ResetToAsync** (18)
 

<span id="ReturnToResourcePool"></span><span id="returntoresourcepool"></span><span id="RETURNTORESOURCEPOOL"></span>**ReturnToResourcePool** (19)
 

<span id="ReverseRoles"></span><span id="reverseroles"></span><span id="REVERSEROLES"></span>**ReverseRoles** (20)
 

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>**Split** (21)
 

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>**Suspend** (22)
 

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>**Unprepare** (23)
   

*VirtualDiskReplicaPeer* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object specifying the replica peer for the target virtual disk.

 

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

 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





