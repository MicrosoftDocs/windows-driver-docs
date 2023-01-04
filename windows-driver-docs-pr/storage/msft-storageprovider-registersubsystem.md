---
title: RegisterSubsystem method of the MSFT\_StorageProvider class
description: Registers a subsystem to be managed by this provider.
ms.assetid: 0C882319-FC92-4C79-A89C-F16C6439A221
keywords:
- RegisterSubsystem method Windows Storage Management API
- RegisterSubsystem method Windows Storage Management API , MSFT_StorageProvider class
- MSFT_StorageProvider class Windows Storage Management API , RegisterSubsystem method
topic_type:
- apiref
api_name:
- MSFT_StorageProvider.RegisterSubsystem
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RegisterSubsystem method of the MSFT\_StorageProvider class

Registers a subsystem to be managed by this provider. Note that the subsystem must be compatible with the provider software.

## Syntax


```mof
UInt32 RegisterSubsystem(
  [in]  String ComputerName,
  [in]  String Credential,
  [out] String ExtendedStatus
);
```



## Parameters

 

*ComputerName* \[in\]
 

Name of the computer where the subsystem resides.

 

*Credential* \[in\]
 

Credential providing access to the computer.

 

*ExtendedStatus* \[out\]
 

Extended error information from the storage provider in a [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object. The information is implementation-specific.

 

## Return value

 

**Success** (0)
 

**Not Supported** (1)
 

**Unspecified Error** (2)
 

**Timeout** (3)
 

**Failed** (4)
 

**Invalid Parameter** (5)
 

**In use** (6)
 

**Access denied** (40001)
 

**There are not enough resources to complete the operation.** (40002)
 

**Cannot connect to the storage provider.** (46000)
 

**The storage provider cannot connect to the storage subsystem.** (46001)
 

**Cannot register/unregister the storage subsystem on local host.** (46004)
 

**This subsystem is already registered.** (46006)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageProvider**](msft-storageprovider.md)
 

 

 





