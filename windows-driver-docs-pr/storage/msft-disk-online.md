---
title: Online method of the MSFT\_Disk class
description: Brings the disk online.
ms.assetid: 18F3A556-9BAD-48D8-BFEF-30414B45FFE1
keywords:
- Online method Windows Storage Management API
- Online method Windows Storage Management API , MSFT_Disk class
- MSFT_Disk class Windows Storage Management API , Online method
topic_type:
- apiref
api_name:
- MSFT_Disk.Online
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Online method of the MSFT\_Disk class

Brings the disk online.

## Syntax


```mof
UInt32 Online(
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
 

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation.** (41018)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Disk**](msft-disk.md)
 

 

 





