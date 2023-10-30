---
title: SetDescription method of the MSFT\_FileShare class
description: Allows a user to set the description field of the file share.
ms.assetid: 09CEA9ED-198E-4163-8981-8B164BDB8E34
keywords:
- SetDescription method Windows Storage Management API
- SetDescription method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , SetDescription method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileShare.SetDescription
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetDescription method of the MSFT\_FileShare class

Allows a user to set the description field of the file share.

## Syntax


```mof
UInt32 SetDescription(
  [in]  String Description,
  [out] String ExtendedStatus
);
```



## Parameters

 

*Description* \[in\]
 

A user settable description of the file share. This field can be used to store extra free-form information, such as notes or details about the intended usage.

 

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
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileShare**](msft-fileshare.md)
 

 

 





