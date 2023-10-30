---
title: RevokeAccess method of the MSFT\_FileShare class
description: Revokes access to the file share for specified users.
ms.assetid: D6835291-A93F-4510-9B2D-71B0AABFEDFF
keywords:
- RevokeAccess method Windows Storage Management API
- RevokeAccess method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , RevokeAccess method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileShare.RevokeAccess
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# RevokeAccess method of the MSFT\_FileShare class

Revokes access to the file share for specified users.

## Syntax


```mof
UInt32 RevokeAccess(
  [in]  String AccountNames[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*AccountNames* \[in\]
 

User accounts for which to revoke access to the file share.

 

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
 

 

 





