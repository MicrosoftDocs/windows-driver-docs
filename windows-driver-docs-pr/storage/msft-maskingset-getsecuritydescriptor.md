---
title: GetSecurityDescriptor Method of the MSFT_MaskingSet Class
description: Retrieves the security descriptor that controls access to the masking set object instance.
ms.assetid: 8738053D-3852-4EB9-9297-48428030CFEF
keywords:
- GetSecurityDescriptor method Windows Storage Management API
- GetSecurityDescriptor method Windows Storage Management API , MSFT_MaskingSet class
- MSFT_MaskingSet class Windows Storage Management API , GetSecurityDescriptor method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_MaskingSet.GetSecurityDescriptor
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetSecurityDescriptor method of the MSFT\_MaskingSet class

Retrieves the security descriptor that controls access to the masking set object instance.

## Syntax


```mof
UInt32 GetSecurityDescriptor(
  [out] String SecurityDescriptor,
  [out] String ExtendedStatus
);
```



## Parameters

 

*SecurityDescriptor* \[out\]
 

A Security Descriptor Definition Language (SDDL) formatted string describing the access control list of the object. This parameter is required and cannot be NULL.

 

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
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_MaskingSet**](msft-maskingset.md)
 

 

 





