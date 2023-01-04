---
title: CreateReplicationGroup method of the MSFT\_StorageSubSystem class
description: Creates a replication group on a storage subsystem.
ms.assetid: B6B5CCB3-1B4B-4323-8BE9-145112A5FD70
keywords:
- CreateReplicationGroup method Windows Storage Management API
- CreateReplicationGroup method Windows Storage Management API , MSFT_StorageSubSystem interface
- MSFT_StorageSubSystem interface Windows Storage Management API , CreateReplicationGroup method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.CreateReplicationGroup
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateReplicationGroup method of the MSFT\_StorageSubSystem class

Creates a replication group on a storage subsystem.

## Syntax


```mof
UInt32 CreateReplicationGroup(
  [in]  String              FriendlyName,
  [in]  String              Description,
  [in]  String              StorageElements[],
  [in]  String              ReplicationSettings[],
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              CreatedReplicationGroup,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

Allows the user to specify the *FriendlyName* when the replication group is created. A *FriendlyName* is expected to be descriptive, but it is not required to be unique.

Note that some storage subsystems do not allow setting a friendly name during replication group creation. If a subsystem doesn't support this, replication group creation will still succeed, but the replication group may have a different name assigned to it.

This parameter is required and cannot be NULL.

 

*Description* \[in\]
 

A description of the purpose of the replication group.

This parameter is required and cannot be NULL.

 

*StorageElements* \[in\]
 

An array of strings that contain embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects. These storage objects must be of the same type as the source elements to be replicated. The ordering in this array determines the consistency ordering of the element replicas.

 

*ReplicationSettings* \[in\]
 

An array of strings that contain embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) objects to be configured on each storage element.

 

*CreatedStorageJob* \[out\]
 

Returns a reference to the storage job object used to track the long-running operation.

 

*CreatedReplicationGroup* \[out\]
 

If the replication group is created successfully, this parameter receives a string that contains an embedded [**MSFT\_ReplicationGroup**](msft-replicationgroup.md) object.

 

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
 

 

 





