---
title: SetNodeAddress method of the MSFT\_InitiatorPort class
description: Sets the node address for an iSCSI initiator port by passing an IQN as the node address string.
ms.assetid: 0F1A5F3C-3064-44EE-A8D2-0A6E735CDE5A
keywords:
- SetNodeAddress method Windows Storage Management API
- SetNodeAddress method Windows Storage Management API , MSFT_InitiatorPort class
- MSFT_InitiatorPort class Windows Storage Management API , SetNodeAddress method
topic_type:
- apiref
api_name:
- MSFT_InitiatorPort.SetNodeAddress
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetNodeAddress method of the MSFT\_InitiatorPort class

Sets the node address for an iSCSI initiator port by passing an IQN as the node address string.

## Syntax


```mof
UInt32 SetNodeAddress(
  [in]  String NodeAddress,
  [out] String ExtendedStatus
);
```



## Parameters

 

*NodeAddress* \[in\]
 

The node address. This parameter is required.

 

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
 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_InitiatorPort**](msft-initiatorport.md)
 

 

 





