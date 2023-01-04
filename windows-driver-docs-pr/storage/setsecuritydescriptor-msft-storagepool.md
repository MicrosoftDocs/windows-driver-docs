---
title: SetSecurityDescriptor method of the MSFT\_StoragePool class
description: Sets or changes the security descriptor that controls access to the storage pool object.
ms.assetid: 443D68E6-A51F-43C6-ABFC-8B9FBEFA9D5A
keywords:
- SetSecurityDescriptor method Windows Storage Management API
- SetSecurityDescriptor method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , SetSecurityDescriptor method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.SetSecurityDescriptor
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetSecurityDescriptor method of the MSFT\_StoragePool class

Sets or changes the security descriptor that controls access to the storage pool object.

## Syntax


```mof
UInt32 SetSecurityDescriptor(
  [in]  String SecurityDescriptor,
  [out] String ExtendedStatus
);
```



## Parameters

 

*SecurityDescriptor* \[in\]
 

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
 

## Remarks

The user must have sufficient privileges to set the security descriptor.

If the call is not made in the context of a user specified in the security descriptor's access control list, this method will fail with **Access Denied**.

If an empty security descriptor is passed to this method, the behavior is left to the specific implementation as long as there is some user context (typically domain administrators) that can access and administer the object.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





