---
title: GetExtendedStatus Method of the MSFT_StorageJob Class
description: Retrieves extended status information for an unsuccessful storage job.
ms.assetid: 75B8C19E-F25D-4201-B895-24B8B0587E4A
keywords:
- GetExtendedStatus method Windows Storage Management API
- GetExtendedStatus method Windows Storage Management API , MSFT_StorageJob class
- MSFT_StorageJob class Windows Storage Management API , GetExtendedStatus method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageJob.GetExtendedStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetExtendedStatus method of the MSFT\_StorageJob class

Retrieves extended status information for an unsuccessful storage job.

## Syntax


```mof
UInt32 GetExtendedStatus(
  [out] String ExtendedStatus
);
```



## Parameters

 

*ExtendedStatus* \[out\]
 

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageJob**](msft-storagejob.md)
 

 

 





