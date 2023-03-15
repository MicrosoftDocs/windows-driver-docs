---
title: Set method of the MSFT\_FileIntegrity class
description: Sets the file integrity state for the specified file.
ms.assetid: 19ADB940-56F2-44C1-BC9A-77869930B5DB
keywords:
- Set method Windows Storage Management API
- Set method Windows Storage Management API , MSFT_FileIntegrity class
- MSFT_FileIntegrity class Windows Storage Management API , Set method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileIntegrity.Set
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Set method of the MSFT\_FileIntegrity class

Sets the file integrity state for the specified file.

## Syntax


```mof
UInt32 Set(
  [in]  String  FileName,
  [in]  Boolean Enable,
  [in]  Boolean Enforce,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*FileName* \[in\]
 

The file to set the integrity information for.

 

*Enable* \[in\]
 

Specifies whether integrity streams are enabled for this file.

 

*Enforce* \[in\]
 

Specifies whether integrity streams are enforced for this file.

 

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
 

 

 





