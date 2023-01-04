---
title: SetAttributes method of the MSFT\_StorageTier class
description: Updates or sets various attributes on the storage tier.
ms.assetid: C949619B-0197-45C0-B3A1-9E7ECCE6D272
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_StorageTier class
- MSFT_StorageTier class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_StorageTier.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_StorageTier class

Updates or sets various attributes on the storage tier. Note that not all parameters need be specified, and only those given will be updated.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  UInt16 MediaType,
  [out] String ExtendedStatus
);
```



## Parameters

 

*MediaType* \[in\]
 

The media type of the storage tier.



| Value                                                                                                | Meaning        |
|------------------------------------------------------------------------------------------------------|----------------|
| <span id="3"></span> **3**  | HDD |
| <span id="4"></span> **4**  | SSD |



 

 

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
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**The storage pool could not complete the operation because its configuration is read-only.** (48007)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageTier**](msft-storagetier.md)
 

 

 





