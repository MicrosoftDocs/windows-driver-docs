---
title: SetAttributes method of the MSFT\_StorageSubSystem class
description: Sets the SupportsAutomaticObjectClustering field of the storage subsystem object instance.
ms.assetid: 226BCD54-EA3A-4917-9688-7293C1C049EA
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_StorageSubSystem class
- MSFT_StorageSubSystem class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystem.SetAttributes
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# SetAttributes method of the MSFT\_StorageSubSystem class

Sets the **SupportsAutomaticObjectClustering** field of the storage subsystem object instance.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  Boolean AutomaticClusteringEnabled,
  [out] String  ExtendedStatus
);
```



## Parameters

 

*AutomaticClusteringEnabled* \[in\]
 

**TRUE** to enable automatic object clustering; otherwise, **FALSE**. This parameter is required and cannot be **NULL**.

 

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
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





