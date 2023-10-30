---
title: GetDiagnosticInfo method of the MSFT\_StorageSubSystem class
description: Gets the diagnostic information of the storage subsystem.
ms.assetid: F0ED1A8C-3F20-460C-8D60-1461332C75AA
keywords:
- GetDiagnosticInfo method Windows Storage Management API
- GetDiagnosticInfo method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , GetDiagnosticInfo method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystem.GetDiagnosticInfo
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetDiagnosticInfo method of the MSFT\_StorageSubSystem class

Gets the diagnostic information of the storage subsystem.

## Syntax


```mof
UInt32 GetDiagnosticInfo(
  [in]  String  DestinationPath,
  [in]  UInt32  TimeSpan,
  [in]  String  ActivityId,
  [in]  Boolean IncludeOperationalLog,
  [in]  Boolean IncludeDiagnosticLog,
  [in]  Boolean IncludeLiveDump,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*DestinationPath* \[in\]
  

*TimeSpan* \[in\]
  

*ActivityId* \[in\]
  

*IncludeOperationalLog* \[in\]
  

*IncludeDiagnosticLog* \[in\]
  

*IncludeLiveDump* \[in\]
  

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
 

 

 





