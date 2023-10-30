---
title: GrantAccess method of the MSFT\_FileShare class
description: Grants to the specified user accounts the specified access to the file share.
ms.assetid: 9303326E-062D-452A-9E3C-AD9F394A49D4
keywords:
- GrantAccess method Windows Storage Management API
- GrantAccess method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , GrantAccess method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileShare.GrantAccess
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GrantAccess method of the MSFT\_FileShare class

Grants to the specified user accounts the specified access to the file share.

## Syntax


```mof
UInt32 GrantAccess(
  [in]  String AccountNames[],
  [in]  UInt32 AccessRight,
  [out] String ExtendedStatus
);
```



## Parameters

 

*AccountNames* \[in\]
 

User accounts to be granted access to the file share.

 

*AccessRight* \[in\]
 

Access to be granted to the specified user accounts.

 

**Full** (0)
 

**Change** (1)
 

**Read** (2)
   

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
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**The operation is not supported while the cluster is being upgraded.** (40009)
 

**At least one account name needs to be specified.** (58003)
 

**You must specify an access right.** (58004)
 

**The specified user account could not be found.** (58005)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileShare**](msft-fileshare.md)
 

 

 





