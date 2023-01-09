---
title: BlockAccess method of the MSFT\_FileShare class
description: Denies specified users access to the file share.
ms.assetid: FA3B0467-BE7E-4847-8AA3-BF73E622E83F
keywords:
- BlockAccess method Windows Storage Management API
- BlockAccess method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , BlockAccess method
topic_type:
- apiref
api_name:
- MSFT_FileShare.BlockAccess
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BlockAccess method of the MSFT\_FileShare class

Denies specified users access to the file share.

## Syntax


```mof
UInt32 BlockAccess(
  [in]  String AccountNames[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*AccountNames* \[in\]
 

User accounts to be denied access to the file share.

 

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
 

 

 





