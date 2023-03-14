---
title: GetDedupProperties method of the MSFT\_Volume class
description: Gets deduplication properties of the volume.
ms.assetid: 94B6A3CD-7D52-468F-9E6C-54870C97A383
keywords:
- GetDedupProperties method Windows Storage Management API
- GetDedupProperties method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , GetDedupProperties method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Volume.GetDedupProperties
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetDedupProperties method of the MSFT\_Volume class

Gets deduplication properties of the volume.

## Syntax


```mof
UInt32 GetDedupProperties(
  [out] String DedupProperties,
  [out] String ExtendedStatus
);
```



## Parameters

 

*DedupProperties* \[out\]
 

An array of strings containing embedded [**MSFT\_DedupProperties**](msft-dedupproperties.md) objects specifying the deduplication properties of the volume.

 

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
 

**Object Not Found** (8)
 

**Access denied** (40001)
 

**Deduplication feature is not available** (43020)
 

**Deduplication is not enabled for the volume** (43021)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





