---
title: Resize method of the MSFT\_Partition class
description: Resizes the partition and any associated file system volume to the size specified by the Size parameter.
ms.assetid: 89343280-F14E-47B2-A8F6-28F85B525804
keywords:
- Resize method Windows Storage Management API
- Resize method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , Resize method
topic_type:
- apiref
api_name:
- MSFT_Partition.Resize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resize method of the MSFT\_Partition class

Resizes the partition and any associated file system volume to the size specified by the *Size* parameter.

## Syntax


```mof
UInt32 Resize(
  [in]  UInt64 Size,
  [out] String ExtendedStatus
);
```



## Parameters

 

*Size* \[in\]
 

The new size for the disk. This parameter is required and cannot be zero.

 

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

This method resizes the partition and any associated file system to the size specified by the *Size* parameter. If the size is outside the bounds returned by the [**GetSupportedSize**](msft-partition-getsupportedsizes.md) method, then this method will fail with a well-defined error code. The resize operation is supported only on NTFS-formatted partitions and RAW partitions.

If the specified size is smaller than the original size, this method will move files so that they are as close as possible to the beginning of the partition, to consolidate free space at the end of the partition. It then truncates the file system volume, reducing its size, and then truncates the partition.

In almost all cases, there will be some files that are immovable (that is, cannot be moved). For example, file system and storage driver metadata files are likely to be immovable. For this reason, the amount by which a partition can be shrunk is usually less than the total amount of free space on the partition.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Partition**](msft-partition.md)
 

 

 





