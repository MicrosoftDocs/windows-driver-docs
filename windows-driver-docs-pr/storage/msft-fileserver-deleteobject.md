---
title: DeleteObject method of the MSFT\_FileServer class
description: Deletes the file server. If the file server contains any file shares, these shares must be removed first.
ms.assetid: 81C51A89-AB40-4125-919E-EFADB101AC83
keywords:
- DeleteObject method Windows Storage Management API
- DeleteObject method Windows Storage Management API , MSFT_FileServer class
- MSFT_FileServer class Windows Storage Management API , DeleteObject method
topic_type:
- apiref
api_name:
- MSFT_FileServer.DeleteObject
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteObject method of the MSFT\_FileServer class

Deletes the file server. If the file server contains any file shares, these shares must be removed first.

## Syntax


```mof
UInt32 DeleteObject(
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

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
 

**Method Parameters Checked - Job Started** (4096)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**This operation is not supported on local file servers.** (58000)
 

**The file server could not complete the operation because its health or operational status does not permit it.** (58006)
 

**The file server could not complete the operation because its configuration is read-only.** (58007)
 

**The file server contains virtual disks.** (58008)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileServer**](msft-fileserver.md)
 

 

 





