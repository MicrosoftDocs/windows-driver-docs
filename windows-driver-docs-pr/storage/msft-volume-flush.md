---
title: Flush method of the MSFT\_Volume class
description: Flushes the cached data in the volume's file system to disk.
ms.assetid: 25E48B8F-65C7-46D5-BFFE-6573133148EB
keywords:
- Flush method Windows Storage Management API
- Flush method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , Flush method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Volume.Flush
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Flush method of the MSFT\_Volume class

Flushes the cached data in the volume's file system to disk.

## Syntax


```mof
UInt32 Flush();
```



## Parameters

This method has no parameters.

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
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





