---
title: CreateReplica method of the MSFT\_ReplicationGroup class
description: Creates a replication relationship between replication groups.
ms.assetid: 785C38FF-635A-4146-ABBC-8C28027B24A4
keywords:
- CreateReplica method Windows Storage Management API
- CreateReplica method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , CreateReplica method
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup.CreateReplica
api_location:
- adojet.h
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateReplica method of the MSFT\_ReplicationGroup class

Creates a replication relationship between replication groups.

## Syntax


```mof
UInt32 CreateReplica(
  [in]           String              FriendlyName,
  [in]           String              TargetStorageSubsystem,
  [in]           String              TargetGroupObjectId,
  [in, optional] String              TargetStoragePoolObjectId,
  [in, optional] UInt32              RecoveryPointObjective,
  [in]           String              ReplicationSettings,
  [in]           UInt16              SyncType,
  [out]          String              CreatedReplicaPeer,
  [out]          MSFT_StorageJob REF CreatedStorageJob,
  [out]          String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

An end-user relevant name for the element being created. If **NULL**, then a system-supplied default name can be used. The value will be stored in the **FriendlyName** property for the created element.

 

*TargetStorageSubsystem* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object specifying the replica target subsystem.

 

*TargetGroupObjectId* \[in\]
 

Specifies the replication group target on the target machine.

 

*TargetStoragePoolObjectId* \[in, optional\]
 

A storage pool on the target to be used as the source for creating the necessary target storage elements. This parameter is ignored if the target group contains any elements.

 

*RecoveryPointObjective* \[in, optional\]
 

Indicates the maximum interval in which data might be lost. For synchronous copy operations, *RecoveryPointObjective* is 0. For asynchronous copy operations *RecoveryPointObjective* represents the interval since the most recent transmission of data to the target element.

 

*ReplicationSettings* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) object to be applied.

 

*SyncType* \[in\]
 

The type of copy that will be made. One of the following values:



| Value                                                                                                                                                                                                                                                              | Meaning                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
|  **DMTF Reserved** ..                | This value is reserved for system use.                |
|  **Mirror** 6                                             | Create and maintain a copy of the source.             |
|  **Snapshot** 7                                     | Create a volume shadow copy of the source.            |
|  **Clone** 8                                                 | Create a point-in-time, full copy of the source.      |
|  **TokenizedClone** 9             | Create a point-in-time, tokenized copy of the source. |
|  **DMTF Reserved** ..                | This value is reserved for system use.                |
|  **Vendor Specific** 0x8000..  | These values are reserved for vendors.                |



 

 

*CreatedReplicaPeer* \[out\]
 

This parameter receives a string that contains an embedded [**MSFT\_Synchronized**](msft-synchronized.md) object representing the association between the replication groups.

 

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
| Header                   |  Adojet.h        |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
 

 

 





