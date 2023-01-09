---
title: GetAccessPaths method of the MSFT\_Partition class
description: Retrieves all mount points and drive letters that can be used to access the partition.
ms.assetid: a7c0e34e-b9f3-40ce-b81d-b4a46dc9c0ec
keywords:
- GetAccessPaths method Windows Storage Management API
- GetAccessPaths method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , GetAccessPaths method
topic_type:
- apiref
api_name:
- MSFT_Partition.GetAccessPaths
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetAccessPaths method of the MSFT\_Partition class

Retrieves all mount points and drive letters that can be used to access the partition.

## Syntax


```mof
UInt32 GetAccessPaths(
  [out] String AccessPaths[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*AccessPaths* \[out\]
 

An array of all the various mount points for the partition. This list includes drive letters, in addition to mounted folders.

 

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

 

[**MSFT\_Partition**](msft-partition.md)
 

 

 





