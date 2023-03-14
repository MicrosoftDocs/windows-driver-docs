---
title: GetSupportedGroupFeatures method of the MSFT\_ReplicationCapabilities class
description: Returns, for a given ReplicationType, the supported group features.
ms.assetid: A7037D94-1196-4F10-9084-F797A75C7C8D
keywords:
- GetSupportedGroupFeatures method Windows Storage Management API
- GetSupportedGroupFeatures method Windows Storage Management API , MSFT_ReplicationCapabilities class
- MSFT_ReplicationCapabilities class Windows Storage Management API , GetSupportedGroupFeatures method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationCapabilities.GetSupportedGroupFeatures
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetSupportedGroupFeatures method of the MSFT\_ReplicationCapabilities class

Returns, for a given *ReplicationType*, the supported group features.

## Syntax


```mof
UInt32 GetSupportedGroupFeatures(
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

 

**One-to-many replication** (2)
 

**Many-to-many groups** (3)
 

**Consistency enabled for all groups** (4)
 

**Empty replication groups allowed** (5)
 

**Source group must have more than one element** (6)
 

**Composite groups** (7)
 

**Multihop element replication** (8)
 

**Multi-hop elements must have same SyncType** (9)
 

**Group can only have one single relationship active** (10)
 

**Source element can be removed from group** (11)
 

**Target element can be removed from group** (12)
 

**Group can be temporary** (13)
 

**Group is nameable** (14)
 

**Supports target element count** (15)
 

**Synchronized clone target detaches automatically** (16)
 

**Reverse Roles operation requires read only source** (17)
 

**Reverse Roles operation requires subsequent resync** (18)
 

**Restore operation requires subsequent fracture** (19)
 

**Resync operation requires subsequent activate** (20)
 

**Copy operation requires offline source** (21)
 

**Restore operation requires subsequent detach** (22)
 

**Element can be member of multiple groups** (23)
 

**Elements of group can be mix of thin and thick** (24)
 

**TokenizedClone ConsistentPointInTime** (25)
 

**Target elements can be added to collections** (26)
 

**Reverse Roles operation requires Synchronized state** (27)
 

**Reverse Roles operation requires Fractured state** (28)
 

**Reverse Roles operation requires Split state** (29)
 

**Reverse Roles operation requires FailedOver state** (30)
 

**Reverse Roles operation requires Suspended state** (31)
 

**Provider can manage remote source group** (32)
 

**Provider can manage remote target group** (33)
 

**TargetGroup shall not be supplied** (34)
 

**TargetPool shall not be supplied** (35)
 

**TargetSettingGoal shall not be supplied** (36)
 

**Provider can create remote target group** (37)
 

**Provider can create local target group** (38)
 

**Provider must create remote group** (39)
 

**Creating remote elements requires TargetPool** (40)
 

**Target group shall be supplied** (41)
 

**CreateGroupReplica only accepts empty groups** (42)
 

**One replication group per storage pool** (43)
 

**Supports ConsistencyExempt when adding to group** (44)
 

**Add or Remove to group requires Fractured state** (45)
 

**Add or Remove to group requires Split state** (46)
 

**Add or Remove to group requires Suspended state** (47)
 

**Add or Remove to group requires FailedOver state** (48)
 

**Supports SynchronizationAspect of replication group** (49)
 

**No element level StorageSynchronized** (50)
 

**Accepts foreign object paths** (51)
 

**Failover operation requires subsequent fracture** (52)
 

**Failover operation requires subsequent split** (53)
 

**Restore operation requires subsequent resume** (54)
 

**One consistent async per RemoteReplicationCollection** (55)
 

**Client can supply RelationshipName** (56)
 

**Implementation decides group member order** (57)
 

**Reverse Roles operation does not change CopyState** (58)
 

**Failover operation requires subsequent failback** (59)
 

**Planned Failover operation requires split state** (60)
 

**Planned Failover operation requires fractured state** (61)
 

**Target element requires resource pool reserved for replication** (62)
 

**AddSyncPair requires Synchronized mirror pair** (63)
 

**Provider can create remote elements using TargetPools** (64)
 

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
 

 

 





