---
title: CreateSnapshot method of the MSFT\_VirtualDisk class
description: Creates a new virtual disk that is a shadow copy of the existing virtual disk.
ms.assetid: 320B1576-614B-4590-BEA1-371E2B5BCBBA
keywords:
- CreateSnapshot method Windows Storage Management API
- CreateSnapshot method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , CreateSnapshot method
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk.CreateSnapshot
api_location:
- dbdaoint.h
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateSnapshot method of the MSFT\_VirtualDisk class

Creates a new virtual disk that is a shadow copy of the existing virtual disk.

## Syntax


```mof
UInt32 CreateSnapshot(
  [in]  String              FriendlyName,
  [in]  String              TargetStoragePoolName,
  [in]  Boolean             RunAsJob,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              CreatedVirtualDisk,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

The desired name of the shadow copy virtual disk.

This parameter is required and cannot be **NULL**.

 

*TargetStoragePoolName* \[in\]
 

The storage pool that should be used to hold the created snapshot. If this parameter is not set, this method will default to using the same storage pool that contains the source virtual disk.

 

*RunAsJob* \[in\]
 

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

 

*CreatedStorageJob* \[out\]
 

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

 

*CreatedVirtualDisk* \[out\]
 

If the virtual disk is created successfully, this parameter receives a string that contains an embedded [**MSFT\_VirtualDisk**](msft-virtualdisk.md) object.

 

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
 

**Not enough free space** (40000)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**This operation is not supported on primordial storage pools.** (48000)
 

**The storage pool is reserved for special usage only.** (48001)
 

**The specified storage pool could not be found.** (48005)
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| Header                   |  Dbdaoint.h      |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





