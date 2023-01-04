---
title: SetAttributes method of the MSFT\_Volume class
description: Sets or changes the volume attributes.
ms.assetid: 526F2E01-6E34-4891-ACF9-A8A87FDF0271
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_Volume.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_Volume class

Sets or changes the volume attributes.

Only one attribute can be set or changed.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean EnableVolumeScrub,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*EnableVolumeScrub* \[in\]
 

Specifies whether the automatic data integrity scanner should repair files.

**TRUE** if files on this volume will be scrubbed, or **FALSE** otherwise.

 

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
 

**This setting may not be changed due to the group policy setting** (43015)
 

**This setting may not be changed due to the global registry setting** (43016)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





