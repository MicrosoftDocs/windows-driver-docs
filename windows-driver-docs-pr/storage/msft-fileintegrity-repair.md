---
title: Repair method of the MSFT\_FileIntegrity class
description: Repairs the data for the specified file.
ms.assetid: 09FF3AEB-4BD2-4A53-B46D-B3B84CAB02A5
keywords:
- Repair method Windows Storage Management API
- Repair method Windows Storage Management API , MSFT_FileIntegrity class
- MSFT_FileIntegrity class Windows Storage Management API , Repair method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileIntegrity.Repair
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Repair method of the MSFT\_FileIntegrity class

Repairs the data for the specified file.

## Syntax


```mof
UInt32 Repair(
  [in]  String FileName,
  [out] String ExtendedStatus
);
```



## Parameters

 

*FileName* \[in\]
 

The file to repair.

 

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

 

[**MSFT\_FileIntegrity**](msft-fileintegrity.md)
 

 

 





