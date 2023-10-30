---
title: CreateReplicationRelationship method of the MSFT\_StorageSubSystem class
description: Creates two replication groups and a replication relationship between them. This method requires the subsystem to support fully discovered replication.
ms.assetid: 354EDEDE-CE2F-4865-9A79-0B664D705649
keywords:
- CreateReplicationRelationship method Windows Storage Management API
- CreateReplicationRelationship method Windows Storage Management API , MSFT_StorageSubSystem interface
- MSFT_StorageSubSystem interface Windows Storage Management API , CreateReplicationRelationship method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystem.CreateReplicationRelationship
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# CreateReplicationRelationship method of the MSFT\_StorageSubSystem class

Creates two replication groups and a replication relationship between them. This method requires the subsystem to support fully discovered replication.

## Syntax


```mof
UInt32 CreateReplicationRelationship(
  [in]  String              FriendlyName,
  [in]  Uint16              SyncType,
  [in]  String              TargetStorageSubsystem,
  [in]  String              SourceReplicationGroupFriendlyName,
  [in]  String              SourceReplicationGroupDescription,
  [in]  String              SourceStorageElements[],
  [in]  String              SourceGroupSettings,
  [in]  String              TargetReplicationGroupFriendlyName,
  [in]  String              TargetReplicationGroupDescription,
  [in]  String              TargetStorageElements[],
  [in]  String              TargetStoragePool,
  [in]  String              TargetStoragePools[],
  [in]  String              TargetGroupSettings,
  [in]  UInt16              RecoveryPointObjective,
  [out] String              SourceGroup,
  [out] String              TargetGroup,
  [out] String              CreatedReplicaPeer,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

A user-relevant name for the relationship between the source and target groups, or between a source element and a target group (that is, one-to-many). If **NULL**, the implementation assigns a name. If the individual target elements require an **ElementName**, the implementation constructs an appropriate **ElementName** using the **RelationshipName**; for example, **RelationshipName** as a prefix followed by a "\_n" sequence number, where n is a number beginning with 1.

 

*SyncType* \[in\]
 

Describes the type of copy that will be made.

 

**DMTF Reserved** (..)
 

**Mirror** (6)
 

**Snapshot** (7)
 

**Clone** (8)
 

**TokenizedClone** (9)
 

**DMTF Reserved** (..)
 

**Vendor Specific** (0x8000..)
   

*TargetStorageSubsystem* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object. This allows the user to specify the replica target subsystem when setting up a relationship with another subsystem.

 

*SourceReplicationGroupFriendlyName* \[in\]
 

The name of the source replication group to be created.

 

*SourceReplicationGroupDescription* \[in\]
 

A description of the purpose of the source replication group.

 

*SourceStorageElements* \[in\]
 

Specifies an array of strings that contain embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects. This is an ordered list of storage objects that are to be a part of the source replication group.

 

*SourceGroupSettings* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) object to be applied to the source replication group.

 

*TargetReplicationGroupFriendlyName* \[in\]
 

The name of the target replication group to be created.

 

*TargetReplicationGroupDescription* \[in\]
 

A description of the purpose of the target replication group.

 

*TargetStorageElements* \[in\]
 

Specifies an array of strings that contain embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects. This is an ordered list of storage objects that are to be a part of the target replication group.

 

*TargetStoragePool* \[in\]
 

A string that contains an embedded [**MSFT\_StoragePool**](msft-storagepool.md) object. This is a storage pool on the target to be used as the source for creating the necessary *TargetStorageElements*. This parameter can be specified in lieu of *TargetStorageElements*.

 

*TargetStoragePools* \[in\]
 

A array of strings containing embedded [**MSFT\_StoragePool**](msft-storagepool.md) objects. The underlying storage for the target elements (the replicas) will be drawn from *TargetStoragePool* if specified. Otherwise the allocation is implementation specific. If target elements are supplied, this parameter shall be **NULL**. If *TargetStoragePools* is supplied, *TargetStoragePool* shall be **NULL**.

 

*TargetGroupSettings* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) object to be applied to the target replication group.

 

*RecoveryPointObjective* \[in\]
 

Indicates the maximum interval in which data might be lost. For synchronous copy operations, *RecoveryPointObjective* is 0. For asynchronous copy operations *RecoveryPointObjective* represents the interval since the most recent transmission of data to the target element.

 

*SourceGroup* \[out\]
 

If the replication groups and relationship are created successfully, this parameter receives a string that contains an embedded [**MSFT\_ReplicationGroup**](msft-replicationgroup.md) object representing the source replication group.

 

*TargetGroup* \[out\]
 

If the replication groups and relationship are created successfully, this parameter receives a string that contains an embedded [**MSFT\_ReplicationGroup**](msft-replicationgroup.md) object representing the target replication group.

 

*CreatedReplicaPeer* \[out\]
 

If the replication groups and relationship are created successfully, this parameter receives a string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object representing the replica peer for the target replication group.

 

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

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





