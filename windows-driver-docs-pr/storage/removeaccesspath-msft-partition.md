---
title: RemoveAccessPath method of the MSFT\_Partition class
description: Remove the access path from the partition.
ms.assetid: 0238bfe6-2e36-44e2-81ee-04bfa159ef47
keywords:
- RemoveAccessPath method Windows Storage Management API
- RemoveAccessPath method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , RemoveAccessPath method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_Partition.RemoveAccessPath
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# RemoveAccessPath method of the MSFT\_Partition class

Remove the access path from the partition.

## Syntax


```mof
UInt32 RemoveAccessPath(
  [in]  String AccessPath,
  [out] String ExtendedStatus
);
```



## Parameters

 

*AccessPath* \[in\]
 

Specifies the access path, which is a user-mode path that can be used to open the partition. An access path can be a drive letter (for example, "C:" or "C:\\") or a path to an empty directory on an NTFS volume. The access path string does not require a trailing backslash.

This parameter is required and cannot be **NULL**.

 

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
 

**Cannot remove a volume GUID path.** (42005)
 

**Cannot remove the drive letter of a boot or paging file partition.** (42006)
 

**The access path is not valid.** (42007)
 

## Remarks

This method removes the access path from the partition even if the access path is in use.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Partition**](msft-partition.md)
 

 

 





