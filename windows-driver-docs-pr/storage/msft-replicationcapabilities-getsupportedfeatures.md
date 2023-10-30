---
title: GetSupportedFeatures method of the MSFT\_ReplicationCapabilities class
description: Returns, for a given ReplicationType, the supported features.
ms.assetid: 0DA00822-1931-47CA-874E-6192895F5124
keywords:
- GetSupportedFeatures method Windows Storage Management API
- GetSupportedFeatures method Windows Storage Management API , MSFT_ReplicationCapabilities class
- MSFT_ReplicationCapabilities class Windows Storage Management API , GetSupportedFeatures method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationCapabilities.GetSupportedFeatures
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetSupportedFeatures method of the MSFT\_ReplicationCapabilities class

Returns, for a given *ReplicationType*, the supported features.

## Syntax


```mof
UInt32 GetSupportedFeatures(
  [in]  UInt16 ReplicationType,
  [out] UInt16 Features[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*ReplicationType* \[in\]
 

A value representing the replication type. This must be in the enumeration [**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md).SupportedReplicationTypes.

 

*Features* \[out\]
 

An array of supported features.

 

**Replication groups** (2)
 

**Multi-hop element replication** (3)
 

**Multi-hop elements must have same SyncType** (4)
 

**Multi-hop requires advance notice** (5)
 

**Requires full discovery of target ComputerSystem** (6)
 

**Service suspends source I/O when necessary** (7)
 

**Targets allocated from any storage pool** (8)
 

**Targets allocated from shared storage pool** (9)
 

**Targets allocated from exclusive storage pool** (10)
 

**Targets allocated from multiple storage pools** (11)
 

**Targets require reserved elements** (12)
 

**Target is associated to SynchronizationAspect** (13)
 

**Source is associated to SynchronizationAspect** (14)
 

**Error recovery from Broken state Automatic** (15)
 

**Target must remain associated to source** (16)
 

**Remote resource requires remote CIMOM** (17)
 

**Synchronized clone target detaches automatically** (18)
 

**Reverse Roles operation requires read only source** (19)
 

**Reverse Roles operation requires subsequent resync** (20)
 

**Restore operation requires subsequent fracture** (21)
 

**Resync operation requires subsequent activate** (22)
 

**Copy operation requires offline source** (23)
 

**Adjustable CopyPriority** (24)
 

**Source requires reserved element** (25)
 

**Supports undiscovered resources** (26)
 

**Restore operation requires subsequent detach** (27)
 

**Target element can be added to collections** (28)
 

**Reverse Roles operation requires Synchronized state** (29)
 

**Reverse Roles operation requires Fractured state** (30)
 

**Reverse Roles operation requires Split state** (31)
 

**Reverse Roles operation requires FailedOver state** (32)
 

**Reverse Roles operation requires Suspended state** (33)
 

**Provider can manage remote source** (34)
 

**Provider can manage remote target** (35)
 

**Supports temporary ReplicationEntity** (36)
 

**Supports persistent ReplicationEntity** (37)
 

**ReplicationEntity supports embedded instance** (38)
 

**TargetElement shall not be supplied** (39)
 

**TargetPool shall not be supplied** (40)
 

**TargetGoal shall not be supplied** (41)
 

**Provider can create remote elements** (42)
 

**Creating remote elements requires TargetPool** (43)
 

**Local targets allocated from sources resource pool** (44)
 

**Supports SynchronizationAspect** (45)
 

**Accepts foreign object paths** (46)
 

**Failover operation requires subsequent fracture** (47)
 

**Failover operation requires subsequent split** (48)
 

**Restore operation requires subsequent resume** (49)
 

**GetPeerSystems can return access points** (50)
 

**Client can supply target ElementName** (51)
 

**Reverse Roles operation does not change CopyState** (52)
 

**Failover operation requires subsequent failback** (53)
 

**Planned Failover operation requires fractured state** (54)
 

**Target element requires resource pool reserved for replication** (55)
 

**DMTF Reserved** (..)
 

**Vendor Specific** (0x8000..0xFFFF)
   

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
 

**In Use** (6)
 

**DMTF Reserved** (..)
 

**Vendor Specific** (0x8000..)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md)
 

 

 





