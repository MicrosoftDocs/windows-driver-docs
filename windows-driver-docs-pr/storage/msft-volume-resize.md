---
title: Resize method of the MSFT\_Volume class
description: Resizes the volume.
ms.assetid: 9676FA96-D1FA-4435-87DE-72703B54D538
keywords:
- Resize method Windows Storage Management API
- Resize method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , Resize method
topic_type:
- apiref
api_name:
- MSFT_Volume.Resize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resize method of the MSFT\_Volume class

Resizes the volume.

## Syntax


```mof
UInt32 Resize(
  [in]  UInt64              Size,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*Size* \[in\]
 

Total size, in bytes, to which the volume is to be resized.

 

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
 

**Not enough available capacity** (40000)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





