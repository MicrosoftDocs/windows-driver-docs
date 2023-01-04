---
title: SetFileSystemLabel method of the MSFT\_Volume class
description: Sets the file system label for the volume.
ms.assetid: BD93DE04-A779-49DC-8764-75A98F8B8AF8
keywords:
- SetFileSystemLabel method Windows Storage Management API
- SetFileSystemLabel method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , SetFileSystemLabel method
topic_type:
- apiref
api_name:
- MSFT_Volume.SetFileSystemLabel
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetFileSystemLabel method of the MSFT\_Volume class

Sets the file system label for the volume.

## Syntax


```mof
UInt32 SetFileSystemLabel(
  [in]  String FileSystemLabel,
  [out] String ExtendedStatus
);
```



## Parameters

 

*FileSystemLabel* \[in\]
 

The file system label.

 

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

 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





