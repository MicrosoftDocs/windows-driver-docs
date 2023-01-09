---
title: UnregisterSubsystem method of the MSFT\_StorageProvider class
description: Unregisters a subsystem. The provider will no longer manage this subsystem.
ms.assetid: AD78886B-F238-4FFA-94AC-512606393066
keywords:
- UnregisterSubsystem method Windows Storage Management API
- UnregisterSubsystem method Windows Storage Management API , MSFT_StorageProvider class
- MSFT_StorageProvider class Windows Storage Management API , UnregisterSubsystem method
topic_type:
- apiref
api_name:
- MSFT_StorageProvider.UnregisterSubsystem
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UnregisterSubsystem method of the MSFT\_StorageProvider class

Unregisters a subsystem. The provider will no longer manage this subsystem.

## Syntax


```mof
UInt32 UnregisterSubsystem(
  [in]  String  Subsystem,
  [in]  String  StorageSubSystemUniqueId,
  [in]  Boolean Force,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*Subsystem* \[in\]
 

The subsystem to unregister, an [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object.

 

*StorageSubSystemUniqueId* \[in\]
 

Unique identifier of the storage subsystem.

 

*Force* \[in\]
 

**TRUE** to force the unregister operation when the subsystem is registered with the credentials of a different user; otherwise, **FALSE**.

 

*ExtendedStatus* \[out\]
 

Extended error information from the storage provider in a [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object. The information is implementation-specific.

 

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
 

**Cannot register/unregister the storage subsystem on local host.** (46004)
 

**The storage subsystem is not registered.** (46005)
 

**This subsystem is already registered with another user's credentials. Use the -Force flag to remove the existing registration and add a new one anyway.** (46007)
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageProvider**](msft-storageprovider.md)
 

 

 





