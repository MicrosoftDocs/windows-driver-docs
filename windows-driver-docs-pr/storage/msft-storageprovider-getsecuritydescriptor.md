---
title: GetSecurityDescriptor method of the MSFT\_StorageProvider class
description: Retrieves the security descriptor that controls access to the storage provider object instance.
ms.assetid: 2D3278D3-C8F4-4EBE-B432-F0CCDB56A877
keywords:
- GetSecurityDescriptor method Windows Storage Management API
- GetSecurityDescriptor method Windows Storage Management API , MSFT_StorageProvider class
- MSFT_StorageProvider class Windows Storage Management API , GetSecurityDescriptor method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageProvider.GetSecurityDescriptor
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetSecurityDescriptor method of the MSFT\_StorageProvider class

Retrieves the security descriptor that controls access to the storage provider object instance.

## Syntax


```mof
UInt32 GetSecurityDescriptor(
  [out] String SecurityDescriptor,
  [out] String ExtendedStatus
);
```



## Parameters

 

*SecurityDescriptor* \[out\]
 

A Security Descriptor Definition Language (SDDL) formatted string describing the access control list of the object.

 

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

 

[**MSFT\_StorageProvider**](msft-storageprovider.md)
 

 

 





