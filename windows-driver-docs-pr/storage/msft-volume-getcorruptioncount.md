---
title: GetCorruptionCount method of the MSFT\_Volume class
description: Retrieves the corruption count for the volume.
ms.assetid: 30F417D9-A4E3-49A3-A86E-79AFF5CC9D1C
keywords:
- GetCorruptionCount method Windows Storage Management API
- GetCorruptionCount method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , GetCorruptionCount method
topic_type:
- apiref
api_name:
- MSFT_Volume.GetCorruptionCount
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetCorruptionCount method of the MSFT\_Volume class

Retrieves the corruption count for the volume.

## Syntax


```mof
UInt32 GetCorruptionCount(
  [out] UInt32 CorruptionCount,
  [out] String ExtendedStatus
);
```



## Parameters

 

*CorruptionCount* \[out\]
 

The corruption count for the volume.

 

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
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





