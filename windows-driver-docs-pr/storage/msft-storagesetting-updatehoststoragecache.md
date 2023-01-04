---
title: UpdateHostStorageCache method of the MSFT\_StorageSetting class
description: Updates the internal cache of software objects (that is, Disks, Partitions, Volumes) for the storage setting.
ms.assetid: A4B49108-44F2-4BD0-A642-9A0755DCFC81
keywords:
- UpdateHostStorageCache method Windows Storage Management API
- UpdateHostStorageCache method Windows Storage Management API , MSFT_StorageSetting class
- MSFT_StorageSetting class Windows Storage Management API , UpdateHostStorageCache method
topic_type:
- apiref
api_name:
- MSFT_StorageSetting.UpdateHostStorageCache
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UpdateHostStorageCache method of the MSFT\_StorageSetting class

Updates the internal cache of software objects (that is, Disks, Partitions, Volumes) for the storage setting. This is useful if there was extensive change to the storage layout exposed to that computer.

## Syntax


```mof
UInt32 UpdateHostStorageCache();
```



## Parameters

This method has no parameters.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageSetting**](msft-storagesetting.md)
 

 

 





