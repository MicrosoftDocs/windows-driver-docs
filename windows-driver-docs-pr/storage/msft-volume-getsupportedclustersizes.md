---
title: GetSupportedClusterSizes method of the MSFT\_Volume class
description: Retrieves the supported cluster sizes for the volume.
ms.assetid: 5D1AE94F-37BB-4B0C-B98E-F19D95D69143
keywords:
- GetSupportedClusterSizes method Windows Storage Management API
- GetSupportedClusterSizes method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , GetSupportedClusterSizes method
topic_type:
- apiref
api_name:
- MSFT_Volume.GetSupportedClusterSizes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetSupportedClusterSizes method of the MSFT\_Volume class

Retrieves the supported cluster sizes for the volume.

## Syntax


```mof
UInt32 GetSupportedClusterSizes(
  [in]  String FileSystem,
  [out] UInt32 SupportedClusterSizes[],
  [out] String ExtendedStatus
);
```



## Parameters

 

*FileSystem* \[in\]
 

The volume's file system. One of the following:

-   "ExFAT"
-   "FAT"
-   "FAT32"
-   "NTFS"
-   "ReFS"

 

*SupportedClusterSizes* \[out\]
 

An array of values specifying the supported cluster sizes for the volume.

 

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
 

 

 





