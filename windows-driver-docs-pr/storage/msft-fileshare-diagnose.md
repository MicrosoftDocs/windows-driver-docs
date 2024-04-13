---
title: Diagnose Method of the MSFT_FileShare Class
description: Performs a diagnostic on the file share, returning any actionable results.
ms.assetid: 2BBE9751-7B3F-4A32-8CA5-041C826FB421
keywords:
- Diagnose method Windows Storage Management API
- Diagnose method Windows Storage Management API , MSFT_FileShare class
- MSFT_FileShare class Windows Storage Management API , Diagnose method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileShare.Diagnose
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Diagnose method of the MSFT\_FileShare class

Performs a diagnostic on the file share, returning any actionable results.

## Syntax


```mof
UInt32 Diagnose(
  [out] String DiagnoseResults[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*DiagnoseResults* \[out\]
 

An array of strings containing embedded [**MSFT\_StorageDiagnoseResult**](msft-storagediagnoseresult.md) objects specifying the actionable results of the diagnostic.

 

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
 

**Failed to communicate with cluster health resource.** (59000)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileShare**](msft-fileshare.md)
 

 

 





