---
title: IdentifyElement method of the MSFT\_StorageEnclosure class
description: Permits a user to perform identification tasks on the enclosure and its elements.
ms.assetid: 9993C05C-28A4-4AB8-8860-ADE5D3032AF3
keywords:
- IdentifyElement method Windows Storage Management API
- IdentifyElement method Windows Storage Management API , MSFT_StorageEnclosure class
- MSFT_StorageEnclosure class Windows Storage Management API , IdentifyElement method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageEnclosure.IdentifyElement
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# IdentifyElement method of the MSFT\_StorageEnclosure class

Permits a user to perform identification tasks on the enclosure and its elements.

## Syntax


```mof
HRESULT IdentifyElement(
  [in]  Boolean Enable,
  [in]  UInt32  SlotNumber[],
  [out] String  ExtendedStatus
);
```



## Parameters

 

*Enable* \[in\]
 

If **TRUE**, this instructs the enclosure to enable its identification LED on the specified element(s). The identification LED should remain enabled until a second call to **IdentifyElement** on the same element is made with this parameter set to FALSE.

This parameter is required and cannot be NULL.

 

*SlotNumber* \[in\]
 

An array of slot numbers on which to enable or disable the identification LED.

 

*ExtendedStatus* \[out\]
 

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

 

## Return value

This method can return one of these values.



| Return value                                                                     | Description                                                              |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------|
|  0      | Success.                                                      |
|  1      | Not supported.                                                |
|  2      | Unspecified error.                                            |
|  3      | Timeout.                                                      |
|  4      | Failed.                                                       |
|  5      | Invalid parameter.                                            |
|  40001  | Access denied.                                                |
|  40002  | There are not enough resources to complete the operation.     |
|  46000  | Cannot connect to the storage provider.                       |
|  46001  | The storage provider cannot connect to the storage subsystem. |
|  55000  | One or more slot numbers provided are not valid.              |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)
 

 

 





