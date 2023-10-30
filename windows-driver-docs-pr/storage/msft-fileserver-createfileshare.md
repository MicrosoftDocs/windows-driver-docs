---
title: CreateFileShare method of the MSFT\_FileServer class
description: Creates a file share on the file server.
ms.assetid: 0567E773-D3C4-4BE8-83AA-2929A8064F45
keywords:
- CreateFileShare method Windows Storage Management API
- CreateFileShare method Windows Storage Management API , MSFT_FileServer class
- MSFT_FileServer class Windows Storage Management API , CreateFileShare method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileServer.CreateFileShare
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# CreateFileShare method of the MSFT\_FileServer class

Creates a file share on the file server.

## Syntax


```mof
UInt32 CreateFileShare(
  [in]  String              Name,
  [in]  String              Description,
  [in]  String              SourceVolume,
  [in]  String              VolumeRelativePath,
  [in]  Boolean             ContinuouslyAvailable,
  [in]  Boolean             EncryptData,
  [in]  UInt16              FileSharingProtocol,
  [out] String              CreatedFileShare,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*Name* \[in\]
 

A semi-unique (scoped to the owning file server), human-readable string used to identify the file share.

 

*Description* \[in\]
 

A user settable description of the file share. This field can be used to store extra free-form information, such as notes or details about the intended usage.

 

*SourceVolume* \[in\]
 

A string that contains an embedded [**MSFT\_Volume**](msft-volume.md) object specifying the volume on which the share is to be created.

 

*VolumeRelativePath* \[in\]
 

The volume relative path of an existing directory to share. If this parameter is not provided, an empty share will be created.

 

*ContinuouslyAvailable* \[in\]
 

If **TRUE**, the share will be continuously available.

 

*EncryptData* \[in\]
 

If **TRUE**, the share data will be encrypted during transport.

 

*FileSharingProtocol* \[in\]
 

The file sharing protocol to be used by the share if the server supports more than one protocol.

 

**NFS** (2)
 

**CIFS(SMB)** (3)
   

*CreatedFileShare* \[out\]
 

This parameter receives a string that contains an embedded [**MSFT\_FileShare**](msft-fileshare.md) object representing the new file share.

 

*CreatedStorageJob* \[out\]
 

Returns a reference to the storage job object used to track the long-running operation.

 

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
 

**Method Parameters Checked - Job Started** (4096)
 

**Size Not Supported** (4097)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**The requested access path is already in use.** (42002)
 

**The access path is not valid.** (42007)
 

**You must specify a name for this file share.** (58000)
 

**You must specify a sharing protocol for this file share.** (58001)
 

**You must specify a volume for this file share.** (58002)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileServer**](msft-fileserver.md)
 

 

 





