---
title: SetAttributes method of the MSFT\_FileShare class
description: Allows the user to update or set various attributes on the file share.
ms.assetid: 24327F54-8EBE-4872-93C6-0041193BA3BC
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileShare.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_FileShare class

Allows the user to update or set various attributes on the file share. Note that not all parameters must be specified, and only those given will be updated.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean EncryptData,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*EncryptData* \[in\]
 

If **TRUE**, the share data will be encrypted during transport.

 

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
 

**This operation is not supported on primordial storage pools.** (48000)
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

**The number of thin provisioning alert thresholds specified exceeds the limit for this storage pool.** (48009)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileShare**](msft-fileshare.md)
 

 

 





