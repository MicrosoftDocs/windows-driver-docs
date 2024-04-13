---
title: UnblockAccess Method of the MSFT_FileShare Class
description: Removes specified users from the denied access list for the file share.
ms.assetid: DA0B78BE-571F-4B5E-9120-7321FE2BB977
keywords:
- UnblockAccess method Windows Storage Management API
- UnblockAccess method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , UnblockAccess method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileShare.UnblockAccess
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# UnblockAccess method of the MSFT\_FileShare class

Removes specified users from the denied access list for the file share.

## Syntax


```mof
UInt32 UnblockAccess(
  [in]  String AccountNames[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*AccountNames* \[in\]
 

User accounts to remove from the deny access list for the file share.

 

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
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileShare**](msft-fileshare.md)
 

 

 





