---
title: SetAttributes method of the MSFT\_Partition class
description: Sets various attributes and properties of the partition.
ms.assetid: 203396F7-2F2B-4121-B415-21BFE036074F
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_Partition class
- MSFT_Partition class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_Partition.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_Partition class

Sets various attributes and properties of the partition.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean IsReadOnly,
  [in]  Boolean NoDefaultDriveLetter,
  [in]  Boolean IsActive,
  [in]  Boolean IsHidden,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*IsReadOnly* \[in\]
 

If **TRUE**, the partition will be made read-only. If **FALSE**, the partition will be made writable.

 

*NoDefaultDriveLetter* \[in\]
 

If **TRUE**, the operating system does not assign a drive letter automatically when the partition is discovered. This is only honored for GPT disks and is assumed to be **FALSE** for MBR disks. This attribute is useful in storage area network (SAN) environments.

 

*IsActive* \[in\]
 

**TRUE** if the partition is an MBR partition that is active and can be used to start the system. This parameter is only relevant for MBR disks.

 

*IsHidden* \[in\]
 

**TRUE** if the partition is not detected by the mount manager. As a result, the partition does not receive a drive letter, does not receive a volume GUID path, does not host volume mount points, and is not enumerated by calls to [**FindFirstVolume**](/windows/win32/api/fileapi/nf-fileapi-findfirstvolumew) and [**FindNextVolume**](/windows/win32/api/fileapi/nf-fileapi-findnextvolumew). This ensures that applications such as disk defragmenter do not access the partition. The Volume Shadow Copy Service (VSS) uses this attribute on its shadow copies.

 

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
 

**In Use** (6)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

**The disk has not been initialized.** (41000)
 

**The disk is offline.** (41003)
 

**A parameter is not valid for this type of partition.** (41006)
 

**The operation is not allowed on a system or critical partition.** (42010)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Partition**](msft-partition.md)
 

 

