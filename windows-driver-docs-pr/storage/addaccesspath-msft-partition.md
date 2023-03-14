---
title: AddAccessPath method of the MSFT\_Partition class
description: Adds a mount path or drive letter assignment to the partition.
ms.assetid: d692d4f5-c912-48ec-98a6-9c72ac6e75f6
keywords:
- AddAccessPath method Windows Storage Management API
- AddAccessPath method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , AddAccessPath method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Partition.AddAccessPath
api_location:
- vds.h
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# AddAccessPath method of the MSFT\_Partition class

Adds a mount path or drive letter assignment to the partition.

## Syntax


```mof
UInt32 AddAccessPath(
  [in]  String  AccessPath,
  [in]  Boolean AssignDriveLetter,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*AccessPath* \[in\]
 

Specifies the access path, which is a user-mode path that can be used to open the partition. An access path can be a drive letter (for example, "C:" or "C:\\") or a path to an empty directory on an NTFS volume. The access path string does not require a trailing backslash.

 

*AssignDriveLetter* \[in\]
 

If **TRUE**, the next available drive letter will be assigned to the partition.

 

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
 

**There are not enough resources to complete the operation.** (40002)
 

**The requested access path is already in use.** (42002)
 

**Cannot assign access paths to hidden partitions.** (42004)
 

**The access path is not valid.** (42007)
 

## Remarks

This method adds a mount path or drive letter assignment to the partition. The *AccessPath* and *AssignDriveLetter* parameters are mutually exclusive, and will result in an Invalid Parameter error if both are specified at once. This method adds the access path by creating a mounted folder (also called a volume mount point). Note that mounted folders are supported only on NTFS formatted partitions. This method returns an error if the path specified in *AccessPath* is a folder that is already in use (even if the directory is empty) or if it contains a path to a non-empty directory.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| Header                   |  Vds.h           |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Partition**](msft-partition.md)
 

 

 





