---
title: GetSupportedGroupCopyStates method of the MSFT\_ReplicationCapabilities class
description: Returns, for a given ReplicationType, the supported replication group copy states.
ms.assetid: 47DA6025-D1F6-4840-883E-EBA63C5E37D0
keywords:
- GetSupportedGroupCopyStates method Windows Storage Management API
- GetSupportedGroupCopyStates method Windows Storage Management API , MSFT_ReplicationCapabilities class
- MSFT_ReplicationCapabilities class Windows Storage Management API , GetSupportedGroupCopyStates method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_ReplicationCapabilities.GetSupportedGroupCopyStates
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetSupportedGroupCopyStates method of the MSFT\_ReplicationCapabilities class

Returns, for a given *ReplicationType*, the supported replication group copy states.

## Syntax


```mof
UInt32 GetSupportedGroupCopyStates(
  [in]  UInt16 ReplicationType,
  [out] UInt16 SupportedCopyStates[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*ReplicationType* \[in\]
 

A value representing the replication type. This must be in the enumeration [**MSFT\_ReplicationCapabilities**](msft-replicationcapabilities.md).SupportedReplicationTypes.

 

*SupportedCopyStates* \[out\]
 

The supported copy states. One of the following values.



| Value                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Initialized** 2                               | The link to enable replication is established, and the source and target have been associated. However, the copy operation has not started.                                  |
|  **Unsynchronized** 3                   | Not all of the source data has been copied to the target.                                                                                                                    |
|  **Synchronized** 4                           | All of the source data has been copied to the target.                                                                                                                        |
|  **Broken** 5                                                   | The relationship is nonfunctional due to errors in the source, the target, the path between the two, or space constraints.                                                   |
|  **Fractured** 6                                       | The target is split from the source.                                                                                                                                         |
|  **Split** 7                                                       | The target was gracefully (or systematically) split from the source in a way that ensures consistency.                                                                       |
|  **Inactive** 8                                           | The copy operation has stopped. Writes to the source will not be sent to the target.                                                                                         |
|  **Suspended** 9                                       | Data flow between the source and target has stopped. Writes to the source are held until the association is resumed.                                                         |
|  **Failedover** 10                                  | Reads from and writes to the target have failed. The source is not reachable.                                                                                                |
|  **Prepared** 11                                          | Initialization is completed, and the copy operation has started. However, the data flow has not started.                                                                     |
|  **Aborted** 12                                              | The copy operation was aborted. Use the Resync Replica operation to restart the copy operation.                                                                              |
|  **Skewed** 13                                                  | The target has been modified and is no longer synchronized with the source or the point-in-time view.                                                                        |
|  **Mixed** 14                                                      | Applies to the *CopyState* of *GroupSynchronized*. It indicates that the *StorageSynchronized* associations of the elements in the groups have different *CopyState* values. |
|  **Not Applicable** 15                  | The target does not have a replication state.                                                                                                                                |
|  **Microsoft Reserved** ..  | This value is reserved for system use.                                                                                                                                       |
|  **Vendor Specific** 0x8000..        | These values are reserved for vendors.                                                                                                                                       |



 

 

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
 

 

 





