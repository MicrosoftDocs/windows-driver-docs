---
title: SetFriendlyName method of the MSFT\_PhysicalDisk class
description: Sets or changes the friendly name for the physical disk.
ms.assetid: 64A8F43F-6A3F-4956-9C8B-0F3D7FA6F2CE
keywords:
- SetFriendlyName method Windows Storage Management API
- SetFriendlyName method Windows Storage Management API , MSFT_PhysicalDisk class
- MSFT_PhysicalDisk class Windows Storage Management API , SetFriendlyName method
topic_type:
- apiref
api_name:
- MSFT_PhysicalDisk.SetFriendlyName
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetFriendlyName method of the MSFT\_PhysicalDisk class

Sets or changes the friendly name for the physical disk.

## Syntax


```mof
UInt32 SetFriendlyName(
  [in]  String FriendlyName,
  [out] String ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

The friendly name to be set for the physical disk object. This parameter is required and cannot be **NULL**.

 

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
 

 

 





