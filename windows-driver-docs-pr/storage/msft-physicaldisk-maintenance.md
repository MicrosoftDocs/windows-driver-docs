---
title: Maintenance Method of the MSFT_PhysicalDisk Class
description: Allows a user to perform certain maintenance tasks on the physical disk while it is part of a concrete pool.
ms.assetid: 99730040-46E2-4886-A0FE-4C2D8980DC87
keywords:
- Maintenance method Windows Storage Management API
- Maintenance method Windows Storage Management API , MSFT_PhysicalDisk class
- MSFT_PhysicalDisk class Windows Storage Management API , Maintenance method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_PhysicalDisk.Maintenance
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Maintenance method of the MSFT\_PhysicalDisk class

Allows a user to perform certain maintenance tasks on the physical disk while it is part of a concrete pool.

## Syntax


```mof
UInt32 Maintenance(
  [in]  Boolean EnableIndication,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*EnableIndication* \[in\]
 

If **TRUE**, this instructs the physical disk to enable its indication LED. The indication LED should remain enabled until a second call to **Maintenance** is made with this parameter specified as **FALSE**.

This parameter is required and cannot be NULL.

 

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
 

 

 





