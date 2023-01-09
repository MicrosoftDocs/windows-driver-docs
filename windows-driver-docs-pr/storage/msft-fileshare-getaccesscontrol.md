---
title: GetAccessControlEntries method of the MSFT\_FileShare class
description: Gets the access control entries for specified accounts.
ms.assetid: 252AD23C-4951-4C1D-A9FD-42E35A2ED81F
keywords:
- GetAccessControlEntries method Windows Storage Management API
- GetAccessControlEntries method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , GetAccessControlEntries method
topic_type:
- apiref
api_name:
- MSFT_FileShare.GetAccessControlEntries
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetAccessControlEntries method of the MSFT\_FileShare class

Gets the access control entries for specified accounts.

## Syntax


```mof
UInt32 GetAccessControlEntries(
  [out] String AccessControlEntries[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*AccessControlEntries* \[out\]
 

An array of strings containing embedded [**MSFT\_FileShareAccessControlEntry**](msft-fileshareaccesscontrolentry.md) objects specifying the access control entries for the share.

 

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
 

 

 





