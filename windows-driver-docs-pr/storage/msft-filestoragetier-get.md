---
title: Get method of the MSFT\_FileStorageTier class
description: Gets tier information for pinned files.
ms.assetid: 5EC4BA2D-159F-4CE4-995C-1690A1DAF3F4
keywords:
- Get method Windows Storage Management API
- Get method Windows Storage Management API , MSFT_FileStorageTier class
- MSFT_FileStorageTier class Windows Storage Management API , Get method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileStorageTier.Get
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Get method of the MSFT\_FileStorageTier class

Gets tier information for pinned files.

## Syntax


```mof
UInt32 Get(
  [in]  String FilePath,
  [in]  Char16 VolumeDriveLetter,
  [in]  String VolumePath,
  [in]  String Volume,
  [out] String FileStorageTier[]
);
```



## Parameters

 

*FilePath* \[in\]
 

The path of the file.

 

*VolumeDriveLetter* \[in\]
 

The drive letter that identifies the drive where the file resides.

 

*VolumePath* \[in\]
 

The volume path.

 

*Volume* \[in\]
 

The volume, an [**MSFT\_Volume**](msft-volume.md) object.

 

*FileStorageTier* \[out\]
 

The tier information, an array of [**MSFT\_FileStorageTier**](msft-filestoragetier.md) objects.

 

## Remarks

Only one of the input parameters is required to specify the file storage tier.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileStorageTier**](msft-filestoragetier.md)
 

 

 





