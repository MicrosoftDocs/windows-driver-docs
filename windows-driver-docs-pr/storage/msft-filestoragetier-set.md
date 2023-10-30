---
title: Set method of the MSFT\_FileStorageTier class
description: Pins a volume or file to a storage tier.
ms.assetid: 9F235321-2013-49F8-91AF-7A6369BB739A
keywords:
- Set method Windows Storage Management API
- Set method Windows Storage Management API , MSFT_FileStorageTier class
- MSFT_FileStorageTier class Windows Storage Management API , Set method
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_FileStorageTier.Set
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# Set method of the MSFT\_FileStorageTier class

Pins a volume or file to a storage tier.

## Syntax


```mof
UInt32 Set(
  [in] String FilePath,
  [in] String DesiredStorageTierFriendlyName,
  [in] String DesiredStorageTierUniqueId,
  [in] String DesiredStorageTier
);
```



## Parameters

 

*FilePath* \[in\]
 

The path of a file.

 

*DesiredStorageTierFriendlyName* \[in\]
 

The friendly name of the desired storage tier.

 

*DesiredStorageTierUniqueId* \[in\]
 

The unique ID of the desired storage tier.

 

*DesiredStorageTier* \[in\]
 

The desired storage tier, an [**MSFT\_StorageTier**](msft-storagetier.md) object.

 

## Remarks

Only one of the input parameters is required to specify the file storage tier.

The actual movement of the file to this tier will happen only when the optimizer runs (or is invoked).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileStorageTier**](msft-filestoragetier.md)
 

 

 





