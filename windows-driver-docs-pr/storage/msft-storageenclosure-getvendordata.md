---
title: GetVendorData method of the MSFT\_StorageEnclosure class
description: Returns the vendor-specific data from an enclosure.
ms.assetid: 1CBBC9A4-73D1-4B4C-A164-7D9D40285709
keywords:
- GetVendorData method Windows Storage Management API
- GetVendorData method Windows Storage Management API , MSFT_StorageEnclosure class
- MSFT_StorageEnclosure class Windows Storage Management API , GetVendorData method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageEnclosure.GetVendorData
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetVendorData method of the MSFT\_StorageEnclosure class

Returns the vendor-specific data from an enclosure.

## Syntax


```mof
HRESULT GetVendorData(
  [in]  UInt16 PageNumber,
  [out] String VendorData,
  [out] String ExtendedStatus
);
```



## Parameters

 

*PageNumber* \[in\]
 

The page number for which vendor data is requested.

 

*VendorData* \[out\]
 

The vendor-specific data ("page 04h", for example) from an enclosure.

 

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



 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)
 

 

 





