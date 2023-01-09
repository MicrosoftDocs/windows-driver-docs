---
title: CreateFileServer method of the MSFT\_StorageSubSystem class
description: Creates a file server on a storage subsystem.
ms.assetid: 60B1D607-A675-484C-8893-2B0F332A5094
keywords:
- CreateFileServer method Windows Storage Management API
- CreateFileServer method Windows Storage Management API , MSFT_StorageSubSystem interface
- MSFT_StorageSubSystem interface Windows Storage Management API , CreateFileServer method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.CreateFileServer
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateFileServer method of the MSFT\_StorageSubSystem class

Creates a file server on a storage subsystem.

## Syntax


```mof
UInt32 CreateFileServer(
  [in]  String              FriendlyName,
  [in]  UInt16              FileSharingProtocols[],
  [in]  String              HostNames[],
  [out] String              CreatedFileServer,
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

 

*FriendlyName* \[in\]
 

Allows the user to specify the *FriendlyName* when the file server is created. A *FriendlyName* is expected to be descriptive, but it is not required to be unique.

Note that some storage subsystems do not allow setting a friendly name during file server creation. If a subsystem doesn't support this, file server creation will still succeed, but the file server may have a different name assigned to it.

 

*FileSharingProtocols* \[in\]
 

The file sharing protocols supported by the file server.

 

**NFS** (2)
 

**SMB** (3)
   

*HostNames* \[in\]
 

The host name associated with each protocol specified in *FileSharingProtocols*.

 

*CreatedFileServer* \[out\]
 

If the file server is created successfully, this parameter receives a string that contains an embedded [**MSFT\_FileServer**](msft-fileserver.md) object.

 

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
 

**Object Not Found** (8)
 

**Method Parameters Checked - Job Started** (4096)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cache out of date** (40003)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





