---
title: SetDescription method of the MSFT\_PhysicalDisk class
description: Sets or changes the description for the physical disk.
ms.assetid: 2BD6A32E-DE02-4632-98E4-123EF9A7EDD5
keywords:
- SetDescription method Windows Storage Management API
- SetDescription method Windows Storage Management API , MSFT_PhysicalDisk class
- MSFT_PhysicalDisk class Windows Storage Management API , SetDescription method
topic_type:
- apiref
api_name:
- MSFT_PhysicalDisk.SetDescription
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetDescription method of the MSFT\_PhysicalDisk class

Sets or changes the description for the physical disk.

## Syntax


```mof
UInt32 SetDescription(
  [in]  String Description,
  [out] String ExtendedStatus
);
```



## Parameters

 

*Description* \[in\]
 

A free-form, user settable description for the physical disk. This parameter is required and cannot be NULL.

 

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
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
 

 

 





