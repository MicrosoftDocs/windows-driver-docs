---
title: GetSupportedSize method of the MSFT\_Partition class
description: Retrieves the minimum and maximum sizes that the partition can be resized to using the Resize method.
ms.assetid: 8BE1F2BF-AFA8-4AC3-BFB0-54723F605E95
keywords:
- GetSupportedSize method Windows Storage Management API
- GetSupportedSize method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , GetSupportedSize method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Partition.GetSupportedSize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetSupportedSize method of the MSFT\_Partition class

Retrieves the minimum and maximum sizes that the partition can be resized to using the [**Resize**](msft-partition-resize.md) method.

## Syntax


```mof
UInt32 GetSupportedSize(
  [out] UInt64 SizeMin,
  [out] UInt64 SizeMax,
  [out] String ExtendedStatus
);
```



## Parameters

 

*SizeMin* \[out\]
 

The minimum size that this partition can become, in bytes. If this method is run multiple times, this value can change slightly depending on the placement of various temporary files.

 

*SizeMax* \[out\]
 

The maximum partition size that this partition can become, in bytes.

 

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
 

**Size Not Supported** (4097)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot shrink a partition containing a volume with errors.** (42008)
 

**Cannot resize a partition containing an unknown file system.** (42009)
 

## Remarks

The minimum size is determined by Disk Defragmenter and takes into account the location of immovable files (that is, files that cannot be moved). The maximum size is determined by adding the size of any free extents immediately after the current partition.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Partition**](msft-partition.md)
 

 

 





