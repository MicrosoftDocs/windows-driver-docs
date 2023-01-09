---
title: Get method of the MSFT\_StorageSetting class
description: Retrieves the current state of all storage settings for the computer.
ms.assetid: 044A260C-65A0-462B-8C2D-1553E17493D0
keywords:
- Get method Windows Storage Management API
- Get method Windows Storage Management API , MSFT_StorageSetting class
- MSFT_StorageSetting class Windows Storage Management API , Get method
topic_type:
- apiref
api_name:
- MSFT_StorageSetting.Get
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the MSFT\_StorageSetting class

Retrieves the current state of all storage settings for the computer.

## Syntax


```mof
UInt32 Get(
  [out] String StorageSettings
);
```



## Parameters

 

*StorageSettings* \[out\]
 

A string that contains an embedded instance of the [**MSFT\_StorageSetting**](msft-storagesetting.md) class that contains the storage settings.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageSetting**](msft-storagesetting.md)
 

 

 





