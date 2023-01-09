---
title: SetFriendlyName method of the MSFT\_StorageTier class
description: Renames the storage tier.
ms.assetid: B4DD1630-AA13-46DD-8106-5662173A4E30
keywords:
- SetFriendlyName method Windows Storage Management API
- SetFriendlyName method Windows Storage Management API , MSFT_StorageTier class
- MSFT_StorageTier class Windows Storage Management API , SetFriendlyName method
topic_type:
- apiref
api_name:
- MSFT_StorageTier.SetFriendlyName
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetFriendlyName method of the MSFT\_StorageTier class

Renames the storage tier.

## Syntax


```mof
UInt32 SetFriendlyName(
  [in]  String FriendlyName,
  [out] String ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

The friendly name of the storage tier, defined by the user.

 

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
 

 

 





