---
title: CreateReplica method of the MSFT\_VirtualDisk class
description: Creates a replication relationship between virtual disks.
ms.assetid: F2453003-BE50-4B12-ACDA-03B44D3803FF
keywords:
- CreateReplica method Windows Storage Management API
- CreateReplica method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , CreateReplica method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_VirtualDisk.CreateReplica
api_location:
- adojet.h
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# CreateReplica method of the MSFT\_VirtualDisk class

Creates a replication relationship between virtual disks.

## Syntax


```mof
UInt32 CreateReplica(
  [in]  String              FriendlyName,
  [in]  String              TargetStorageSubsystem,
  [in]  String              TargetVirtualDiskObjectId,
  [in]  String              TargetStoragePoolObjectId,
  [in]  UInt16              RecoveryPointObjective,
  [in]  String              ReplicationSettings,
  [in]  UInt16              SyncType,
  [out] String              CreatedReplicaPeer,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

An end-user relevant name for the element being created. If **NULL**, then a system supplied default name can be used.

 

*TargetStorageSubsystem* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object specifying the replica target machine.

 

*TargetVirtualDiskObjectId* \[in\]
 

Specifies the virtual disk target on the target machine.

 

*TargetStoragePoolObjectId* \[in\]
 

A storage pool on the target to be used as the source for creating the target virtual disk. This parameter is ignored if a target virtual disk is specified.

 

*RecoveryPointObjective* \[in\]
 

Indicates the maximum interval in which data might be lost. For synchronous copy operations, *RecoveryPointObjective* is 0. For asynchronous copy operations *RecoveryPointObjective* represents the interval since the most recent transmission of data to the target element.

 

*ReplicationSettings* \[in\]
 

A string that contains an embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) object to be applied.

 

*SyncType* \[in\]
 

The type of copy that will be made. One of the following values:



| Value                                                                                                                                                                                                                                                              | Meaning                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span> **DMTF Reserved** ..                | This value is reserved for system use.                |
| <span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span> **Mirror** 6                                             | Create and maintain a copy of the source.             |
| <span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span> **Snapshot** 7                                     | Create a volume shadow copy of the source.            |
| <span id="Clone"></span><span id="clone"></span><span id="CLONE"></span> **Clone** 8                                                 | Create a point-in-time, full copy of the source.      |
| <span id="TokenizedClone"></span><span id="tokenizedclone"></span><span id="TOKENIZEDCLONE"></span> **TokenizedClone** 9             | Create a point-in-time, tokenized copy of the source. |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span> **DMTF Reserved** ..                | This value is reserved for system use.                |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span> **Vendor Specific** 0x8000..  | These values are reserved for vendors.                |



 

 

*CreatedReplicaPeer* \[out\]
 

If the relationship is created successfully, this parameter receives a string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object representing the replica peer for the target.

 

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

 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





