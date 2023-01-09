---
title: Get method of the MSFT\_FileIntegrity class
description: Retrieves the file integrity information for the specified file.
ms.assetid: C376D77A-1AB6-4000-AB5E-814104B9751B
keywords:
- Get method Windows Storage Management API
- Get method Windows Storage Management API , MSFT_FileIntegrity class
- MSFT_FileIntegrity class Windows Storage Management API , Get method
topic_type:
- apiref
api_name:
- MSFT_FileIntegrity.Get
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the MSFT\_FileIntegrity class

Retrieves the file integrity information for the specified file.

## Syntax


```mof
UInt32 Get(
  [in]  FileName String,
  [out] String   FileIntegrity,
  [out] String   ExtendedStatus
);
```



## Parameters

 

*String* \[in\]
 

The file to get the integrity information for.

 

*FileIntegrity* \[out\]
 

A string that contains an embedded [**MSFT\_FileIntegrity**](msft-fileintegrity.md) object that contains the file integrity information.

 

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
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileIntegrity**](msft-fileintegrity.md)
 

 

 





