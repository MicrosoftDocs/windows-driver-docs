---
title: SetWriteCache method of the MSFT\_PhysicalDisk class
description: Allows the physical disk's write cache to be enabled or disabled.
ms.assetid: 1DBA8B0E-0C31-471C-B90B-89C1B07CF7F3
keywords:
- SetWriteCache method Windows Storage Management API
- SetWriteCache method Windows Storage Management API , MSFT_PhysicalDisk class
- MSFT_PhysicalDisk class Windows Storage Management API , SetWriteCache method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_PhysicalDisk.SetWriteCache
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetWriteCache method of the MSFT\_PhysicalDisk class

Allows the physical disk's write cache to be enabled or disabled.

## Syntax


```mof
UInt32 SetWriteCache(
  [in]  Boolean WriteCacheEnabled,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*WriteCacheEnabled* \[in\]
 

Specifies whether the physical disk's write cache should be enabled or disabled.

 

*ExtendedStatus* \[out\]
 

Contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

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
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
 

 

 





