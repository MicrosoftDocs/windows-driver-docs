---
title: GetAttributes method of the MSFT\_Volume class
description: Retrieves the volume attributes.
ms.assetid: 82CA68FB-0394-4816-A8EA-510D8D926B1E
keywords:
- GetAttributes method Windows Storage Management API
- GetAttributes method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , GetAttributes method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Volume.GetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetAttributes method of the MSFT\_Volume class

Retrieves the volume attributes.

Only one attribute can be retrieved.

## Syntax


```mof
UInt32 GetAttributes(
  [out] Boolean VolumeScrubEnabled
);
```



## Parameters

 

*VolumeScrubEnabled* \[out\]
 

Indicates whether the automatic data integrity scanner should scrub files.

**TRUE** if files on this volume will be scrubbed, or **FALSE** otherwise.

 

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
 

 

 





