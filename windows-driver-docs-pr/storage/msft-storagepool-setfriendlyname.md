---
title: SetFriendlyName method of the MSFT\_StoragePool class
description: Sets the friendly name for the storage pool.
ms.assetid: 6FD041BB-0554-4E20-896E-4E54DB287384
keywords:
- SetFriendlyName method Windows Storage Management API
- SetFriendlyName method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , SetFriendlyName method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.SetFriendlyName
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetFriendlyName method of the MSFT\_StoragePool class

Sets the friendly name for the storage pool.

## Syntax


```mof
UInt32 SetFriendlyName(
  [in]  String FriendlyName,
  [out] String ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

The friendly name to be set for the storage pool. This parameter is required and cannot be NULL.

 

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
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





