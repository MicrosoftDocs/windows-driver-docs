---
title: RemoveInitiatorId Method of the MSFT_MaskingSet Class
description: Removes one or more initiator identifiers from the masking set.
ms.assetid: 1EB34D83-40B8-4174-9AC5-06091EC5A610
keywords:
- RemoveInitiatorId method Windows Storage Management API
- RemoveInitiatorId method Windows Storage Management API , MSFT_MaskingSet class
- MSFT_MaskingSet class Windows Storage Management API , RemoveInitiatorId method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_MaskingSet.RemoveInitiatorId
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# RemoveInitiatorId method of the MSFT\_MaskingSet class

Removes one or more initiator identifiers from the masking set.

Note that the [**MSFT\_InitiatorId**](msft-initiatorid.md) instances themselves should not be deleted from the system.

## Syntax


```mof
UInt32 RemoveInitiatorId(
  [in]  String                  InitiatorIds[],
  [in]  Boolean                 RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String                  ExtendedStatus
);
```



## Parameters

 

*InitiatorIds* \[in\]
 

Array of strings containing initiator identifiers. This parameter is required and cannot be NULL.

 

*RunAsJob* \[in\]
 

This parameter controls the asynchronous behavior the method will follow.

**TRUE** to use the *CreatedStorageJob* out parameter when the request takes a long time to service; otherwise **FALSE**.

If a storage job has been created to track the operation, this method will return 4096 - 'Method Parameters Checked - Job Started'. Note, even if *RunAsJob* is **TRUE**, the method can still return a result if it finishes in sufficient time.

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation (i.e. synchronous unless requested otherwise).

 

*CreatedStorageJob* \[out\]
 

If *RunAsJob* is set to **TRUE** and this method takes a while to execute, this parameter returns a reference to the storage job used to track the long running operation.

 

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
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**The initiator address specified is not valid** (53000)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_MaskingSet**](msft-maskingset.md)
 

 

 





