---
title: SetAttributes method of the MSFT\_PhysicalDisk class
description: Updates the attributes of the physical disk.
ms.assetid: 8A7194B5-345D-43F1-933D-6061C7107D80
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_PhysicalDisk class
- MSFT_PhysicalDisk class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_PhysicalDisk.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_PhysicalDisk class

Updates the attributes of the physical disk.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  UInt16 MediaType,
  [out] String ExtendedStatus
);
```



## Parameters

 

*MediaType* \[in\]
 

The media type of the physical disk.



| Value                                                                                                | Meaning                |
|------------------------------------------------------------------------------------------------------|------------------------|
|  **0**  | Unspecified |
|  **3**  | HDD         |
|  **4**  | SSD         |
|  **5**  | SCM         |



 

 

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
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
 

 

 





