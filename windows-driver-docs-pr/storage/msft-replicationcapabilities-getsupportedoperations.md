---
title: GetSupportedOperations Method of the MSFT_ReplicationCapabilities Class
description: Returns, for a given ReplicationType, the supported operations on a storage synchronized association that can be supplied to the ModifyReplicaSynchronization operation.
ms.assetid: 6D3911FC-CA5B-418D-878F-6630871C3B90
keywords:
- GetSupportedOperations method Windows Storage Management API
- GetSupportedOperations method Windows Storage Management API , MSFT_ReplicationCapabilities class
- MSFT_ReplicationCapabilities class Windows Storage Management API , GetSupportedOperations method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationCapabilities.GetSupportedOperations
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetSupportedOperations method of the MSFT\_ReplicationCapabilities class

Returns, for a given *ReplicationType*, the supported operations on a storage synchronized association that can be supplied to the **ModifyReplicaSynchronization** operation.

## Syntax


```mof
UInt32 GetSupportedOperations(
  [in]  UInt16 ReplicationType,
  [out] UInt16 SupportedOperations[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*ReplicationType* \[in\]
 

A value representing the replication type. This must be in the enumeration [**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md).SupportedReplicationTypes.

 

*SupportedOperations* \[out\]
 

An array of supported operations.

 

**Abort** (2)
 

**Activate Consistency** (3)
 

**Activate** (4)
 

**AddSyncPair** (5)
 

**Deactivate Consistency** (6)
 

**Deactivate** (7)
 

**Detach** (8)
 

**Dissolve** (9)
 

**Failover** (10)
 

**Failback** (11)
 

**Fracture** (12)
 

**RemoveSyncPair** (13)
 

**Resync Replica** (14)
 

**Restore from Replica** (15)
 

**Resume** (16)
 

**Reset To Sync** (17)
 

**Reset To Async** (18)
 

**Return To ResourcePool** (19)
 

**Reverse Roles** (20)
 

**Split** (21)
 

**Suspend** (22)
 

**Unprepare** (23)
 

**Prepare** (24)
 

**Reset To Adaptive** (25)
 

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
 

 

 





