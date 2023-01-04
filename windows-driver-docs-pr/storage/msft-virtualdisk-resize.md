---
title: Resize method of the MSFT\_VirtualDisk class
description: Resizes a virtual disk.
ms.assetid: 6672EB31-A5CE-49E0-8F4F-6874BC95F0DD
keywords:
- Resize method Windows Storage Management API
- Resize method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , Resize method
topic_type:
- apiref
api_name:
- MSFT_VirtualDisk.Resize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resize method of the MSFT\_VirtualDisk class

Resizes a virtual disk.

## Syntax


```mof
UInt32 Resize(
  [in, out] UInt64              Size,
  [in]      Boolean             RunAsJob,
  [out]     MSFT_StorageJob REF CreatedStorageJob,
  [out]     String              ExtendedStatus
);
```



## Parameters

 

*Size* \[in, out\]
 

On input, this parameter is the requested new size, in bytes, for the virtual disk.

On output, this parameter receives actual new size of the virtual disk after the resize operation.

This parameter is required.

 

*RunAsJob* \[in\]
 

If **TRUE**, this method uses the *CreatedStorageJob* parameter when the request is taking a long time to service. If a storage job has been created to track the operation, this method will return **Method Parameters Checked - Job Started**.

> [!Note]  
> Even if *RunAsJob* is **TRUE**, this method can still return a result if it has finished in sufficient time.

 

If **FALSE** or **NULL**, this method will follow default WMI asynchronous behavior as determined by the client's method for invocation. In other words, it is synchronous unless requested otherwise.

 

*CreatedStorageJob* \[out\]
 

If *RunAsJob* is set to **TRUE** and this method takes a long time to execute, this parameter receives a reference to the storage job object that is used to track the long-running operation.

 

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
 

**Size Not Supported** (4097)
 

**Not enough free space** (40000)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**The storage pool could not complete the operation because its health or operational status does not permit it.** (48006)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

**The virtual disk could not complete the operation because another computer controls its configuration.** (50002)
 

**The virtual disk could not complete the operation because its health or operational status does not permit it.** (50003)
 

## Remarks

The new size must be in the range of valid values given by the [**GetSupportedSize**](msft-storagepool-getsupportedsize.md) method of the [**MSFT\_StoragePool**](msft-storagepool.md) object.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





