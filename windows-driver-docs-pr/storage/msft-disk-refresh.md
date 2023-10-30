---
title: Refresh method of the MSFT\_Disk class
description: Refreshes the cached disk layout information.
ms.assetid: 4BFE5289-DA95-4ED7-993E-496E97D9695A
keywords:
- Refresh method Windows Storage Management API
- Refresh method Windows Storage Management API , MSFT_Disk class
- MSFT_Disk class Windows Storage Management API , Refresh method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Disk.Refresh
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Refresh method of the MSFT\_Disk class

Refreshes the cached disk layout information.

## Syntax


```mof
UInt32 Refresh(
  [out] String ExtendedStatus
);
```



## Parameters

 

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
 

**Disk is in use** (6)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**The disk has not been initialized.** (41000)
 

**The disk is offline.** (41003)
 

## Remarks

This method is useful when the backing disk has changed size (if the backing data store is a VHD or a virtual disk).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Disk**](msft-disk.md)
 

 

 





