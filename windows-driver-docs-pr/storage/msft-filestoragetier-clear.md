---
title: Clear method of the MSFT\_FileStorageTier class
description: Unpins a volume or file from a storage tier.
ms.assetid: 771004D8-8D11-4B34-8CF4-F6DF785C6634
keywords:
- Clear method Windows Storage Management API
- Clear method Windows Storage Management API , MSFT_FileStorageTier class
- MSFT_FileStorageTier class Windows Storage Management API , Clear method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileStorageTier.Clear
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Clear method of the MSFT\_FileStorageTier class

Unpins a volume or file from a storage tier.

## Syntax


```mof
UInt32 Clear(
  [in] String FilePath
);
```



## Parameters

 

*FilePath* \[in\]
 

The path of a file to unpin.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileStorageTier**](msft-filestoragetier.md)
 

 

 





