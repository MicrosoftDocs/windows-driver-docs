---
title: GetSupportedSize method of the MSFT\_StorageTier class
description: Returns the supported sizes for a new storage tier.
ms.assetid: 6D88653E-0F32-42A3-9B14-7E13CBABE1D7
keywords:
- GetSupportedSize method Windows Storage Management API
- GetSupportedSize method Windows Storage Management API , MSFT_StorageTier class
- MSFT_StorageTier class Windows Storage Management API , GetSupportedSize method
topic_type:
- apiref
api_name:
- MSFT_StorageTier.GetSupportedSize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedSize method of the MSFT\_StorageTier class

Returns the supported sizes for a new storage tier. These sizes can be returned in one or both of the following ways: in an array of all supported sizes; or through a minimum, increment, and maximum.

## Syntax


```mof
UInt32 GetSupportedSize(
  [in]  String ResiliencySettingName,
  [out] UInt64 SupportedSizes[],
  [out] UInt64 TierSizeMin,
  [out] UInt64 TierSizeMax,
  [out] UInt64 TierSizeDivisor,
  [out] String ExtendedStatus
);
```



## Parameters

 

*ResiliencySettingName* \[in\]
 

The name of the resiliency setting to use to determine the supported sizes. Note that the sizes returned may vary depending on the resiliency setting.

 

*SupportedSizes* \[out\]
 

The supported sizes for the storage tier, one size per array element. This parameter may be NULL if the number of supported sizes is large, but is useful for storage tiers that only support a small number of tier sizes.

 

*TierSizeMin* \[out\]
 

The minimum supported size of a sequence of sizes specified by the minimum, increment and maximum.

 

*TierSizeMax* \[out\]
 

The maximum supported size of a sequence of sizes specified by the minimum, increment and maximum.

 

*TierSizeDivisor* \[out\]
 

The increment, in bytes, between support sizes. For example: if the minimum supported size is 10 GB, the maximum is 20 GB, and this parameter is 2 GB, then the supported sizes for this pool would be 10 GB, 12 GB, 14 GB, 16 GB, 18 GB, and 20 GB.

 

*ExtendedStatus* \[out\]
 

Extended error information from the storage provider in a [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object. The information is implementation-specific.

 

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
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageTier**](msft-storagetier.md)
 

 

 





