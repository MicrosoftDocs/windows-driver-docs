---
title: Format method of the MSFT\_Volume class
description: Formats the volume.
ms.assetid: 007dd46a-4812-4273-beaa-74fbe9520c7d
keywords:
- Format method Windows Storage Management API
- Format method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , Format method
topic_type:
- apiref
api_name:
- MSFT_Volume.Format
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Format method of the MSFT\_Volume class

Formats the volume.

## Syntax


```mof
UInt32 Format(
  [in]  String  FileSystem,
  [in]  String  FileSystemLabel,
  [in]  UInt32  AllocationUnitSize,
  [in]  Boolean Full,
  [in]  Boolean Force,
  [in]  Boolean Compress,
  [in]  Boolean ShortFileNameSupport,
  [in]  Boolean SetIntegrityStreams,
  [in]  Boolean UseLargeFRS,
  [in]  Boolean DisableHeatGathering,
  [out] String  FormattedVolume,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*FileSystem* \[in\]
 

The file system to apply to the volume. One of the following:

-   "ExFAT"
-   "FAT"
-   "FAT32"
-   "NTFS"
-   "ReFS"

 

*FileSystemLabel* \[in\]
 

The file system label for the volume.

 

*AllocationUnitSize* \[in\]
 

The allocation unit size, in bytes.

 

*Full* \[in\]
 

**TRUE** for a full format, or **FALSE** for a quick format.

 

*Force* \[in\]
 

**TRUE** to force the format operation; otherwise, **FALSE**.

 

*Compress* \[in\]
 

**TRUE** to compress the volume; otherwise, **FALSE**. Leave undefined if *FileSystem* is set to  ReFS .

 

*ShortFileNameSupport* \[in\]
 

**TRUE** if the volume should support short names; otherwise, **FALSE**. Leave undefined if *FileSystem* is set to  ReFS .

 

*SetIntegrityStreams* \[in\]
 

**TRUE** to set integrity streams. Leave undefined unless *FileSystem* is set to  ReFS .

 

*UseLargeFRS* \[in\]
 

**TRUE** to use large FRS; otherwise, **FALSE**. Leave undefined if *FileSystem* is set to  ReFS .

 

*DisableHeatGathering* \[in\]
 

**TRUE** to disable heat gathering; otherwise, **FALSE**.

 

*FormattedVolume* \[out\]
 

Receives a [**MSFT\_Volume**](msft-volume.md) object that represents the formatted volume.

 

*ExtendedStatus* \[out\]
 

Contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

 

## Return value

 

**Success** (0)
 

**Not Supported** (1)
 

**Unspecified Error** (2)
 

**Timeout** (3)
 

**Failed** (4)
 

**Invalid Parameter** (5)
 

**This command is not supported on x86 running in x64 environment.** (7)
 

**Access Denied** (40001)
 

**An unexpected I/O error has occured** (40004)
 

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation.** (40018)
 

**The operation is not allowed on a system or critical partition.** (42010)
 

**The specified cluster size is invalid** (43000)
 

**The specified file system is not supported** (43001)
 

**The volume cannot be quick formatted** (43002)
 

**The number of clusters exceeds 32 bits** (43003)
 

**The specified UDF version is not supported** (43004)
 

**The cluster size must be a multiple of the disk's physical sector size** (43005)
 

**Cannot perform the requested operation when the drive is read only** (43006)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





