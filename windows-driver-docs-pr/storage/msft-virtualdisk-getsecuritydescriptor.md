---
title: GetSecurityDescriptor method of the MSFT\_VirtualDisk class
description: Retrieves the security descriptor that controls access to the virtual disk object instance.
ms.assetid: 430EAAFF-96B4-45E4-9D4F-0713B4094B5B
keywords:
- GetSecurityDescriptor method Windows Storage Management API
- GetSecurityDescriptor method Windows Storage Management API , MSFT_VirtualDisk class
- MSFT_VirtualDisk class Windows Storage Management API , GetSecurityDescriptor method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_VirtualDisk.GetSecurityDescriptor
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# GetSecurityDescriptor method of the MSFT\_VirtualDisk class

Retrieves the security descriptor that controls access to the virtual disk object instance.

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
 

**Not enough free space** (40000)
 

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

 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





