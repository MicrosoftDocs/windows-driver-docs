---
title: StartDiagnosticLog method of the MSFT\_StorageSubSystem class
description: Starts a diagnostic log for the storage subsystem.
ms.assetid: C3A6500C-E0E4-48D5-AB81-788AACD0AB9C
keywords:
- StartDiagnosticLog method Windows Storage Management API
- StartDiagnosticLog method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , StartDiagnosticLog method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.StartDiagnosticLog
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StartDiagnosticLog method of the MSFT\_StorageSubSystem class

Starts a diagnostic log for the storage subsystem.

## Syntax


```mof
UInt32 StartDiagnosticLog(
  [in]  UInt16 Level,
  [in]  UInt64 MaxLogSize,
  [out] String ExtendedStatus
);
```



## Parameters

 

*Level* \[in\]
  

*MaxLogSize* \[in\]
 

This value is in units of megabytes.

 

*ExtendedStatus* \[out\]
 

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

 

## Return value

See [Storage Management API Common Return Codes](storage-management-api-common-return-codes.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





