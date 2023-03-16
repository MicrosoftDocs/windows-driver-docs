---
title: GetSupportedFileSystems method of the MSFT\_Volume class
description: Retrieves the names of file systems that are supported on the volume.
ms.assetid: AE1FF69D-E373-46AA-8AB0-11883C782B87
keywords:
- GetSupportedFileSystems method Windows Storage Management API
- GetSupportedFileSystems method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , GetSupportedFileSystems method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Volume.GetSupportedFileSystems
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetSupportedFileSystems method of the MSFT\_Volume class

Retrieves the names of file systems that are supported on the volume.

## Syntax


```mof
UInt32 GetSupportedFileSystems(
  [out] String SupportedFileSystems[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*SupportedFileSystems* \[out\]
 

An array of strings containing the names of file systems that are supported on the volume.

 

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

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





