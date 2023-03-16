---
title: SetAttributes method of the MSFT\_StorageProvider class
description: Sets the attributes of the provider.
ms.assetid: 649B08C0-CC46-4A93-8037-47CACBC1AD4E
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_StorageProvider class
- MSFT_StorageProvider class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageProvider.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_StorageProvider class

Sets the attributes of the provider.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  UInt16 RemoteSubsystemCacheMode,
  [out] String ExtendedStatus
);
```



## Parameters

 

*RemoteSubsystemCacheMode* \[in\]
 

The caching mode to set. A value of 3 enables caching for all the registered remote subsystems. A value of 2 disables caching for all the registered remote subsystems. This method only affects the remote registered subsystems; local subsystem requests are reported directly with no caching.



| Value                                                                                                | Meaning                     |
|------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="2"></span> **2**  | Disabled         |
| <span id="3"></span> **3**  | Manual-Discovery |



 

 

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
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageProvider**](msft-storageprovider.md)
 

 

 





