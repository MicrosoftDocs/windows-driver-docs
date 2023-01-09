---
title: StopDiagnosticLog method of the MSFT\_StorageSubSystem class
description: Stops the diagnostic log for the storage subsystem.
ms.assetid: 3D5D7A2B-C052-4834-AF7D-6432F407F647
keywords:
- StopDiagnosticLog method Windows Storage Management API
- StopDiagnosticLog method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , StopDiagnosticLog method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.StopDiagnosticLog
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StopDiagnosticLog method of the MSFT\_StorageSubSystem class

Stops the diagnostic log for the storage subsystem.

## Syntax


```mof
UInt32 StopDiagnosticLog(
  [out] String ExtendedStatus
);
```



## Parameters

 

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
 

 

 





