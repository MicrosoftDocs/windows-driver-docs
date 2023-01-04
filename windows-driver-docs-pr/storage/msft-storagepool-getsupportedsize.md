---
title: GetSupportedSize method of the MSFT\_StoragePool class
description: Retrieves the supported virtual disk sizes that can be created in the storage pool.
ms.assetid: C993C168-910B-4151-9B24-7A72807939F0
keywords:
- GetSupportedSize method Windows Storage Management API
- GetSupportedSize method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , GetSupportedSize method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.GetSupportedSize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedSize method of the MSFT\_StoragePool class

Retrieves the supported virtual disk sizes that can be created in the storage pool.

These sizes can be returned in either or both of the following ways:

-   As an array of all supported sizes in the *SupportedSizes* parameter.
-   As a range defined by the *VirtualDiskSizeMin*, *VirtualDiskSizeMax*, and *VirtualDiskSizeDivisor* parameters.

## Syntax


```mof
UInt32 GetSupportedSize(
  [in]  String ResiliencySettingName,
  [out] UInt64 SupportedSizes[],
  [out] UInt64 VirtualDiskSizeMin,
  [out] UInt64 VirtualDiskSizeMax,
  [out] UInt64 VirtualDiskSizeDivisor,
  [out] String ExtendedStatus
);
```



## Parameters

 

*ResiliencySettingName* \[in\]
 

The name of the resiliency setting that should be used when determining the supported sizes. Note that the sizes returned may be different depending on the resiliency setting.

 

*SupportedSizes* \[out\]
 

An array of all of the supported sizes, in bytes, that are supported by the storage pool. This parameter can be **NULL** if the number of supported sizes is large, but is useful for storage pools that only support a select number of virtual disk sizes.

 

*VirtualDiskSizeMin* \[out\]
 

The minimum virtual disk size, in bytes, for a virtual disk created in the storage pool.

 

*VirtualDiskSizeMax* \[out\]
 

The maximum virtual disk size, in bytes, for a virtual disk created in the storage pool.

 

*VirtualDiskSizeDivisor* \[out\]
 

Specifies the multiplier that must be used when determining a virtual disk size. Any size specified in a creation or modification operation must be a multiple of this value.

For example: If the minimum supported size is 10 GB, and this parameter is 2 GB, the supported sizes for this pool would be 10 GB, 12 GB, 14 GB, and so on, until the maximum supported size is reached.

 

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
 

**Cache out of date** (40003)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

## Remarks

The values that this method returns should reflect the current state of the storage pool and its available storage capacity. All values returned in *SupportedSizes* must be multiples of *VirtualDiskSizeDivisor*.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





