---
title: MSFT\_StorageSubSystemToFileShare class
description: Association between an MSFT\_StorageSubSystem and its MSFT\_FileShare objects.
ms.assetid: 4BED3526-1DAA-4A20-97B5-BBC558FD10CF
keywords:
- MSFT_StorageSubSystemToFileShare class Windows Storage Management API
- MSFT_StorageSubSystemToFileShare class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToFileShare
- MSFT_StorageSubSystemToFileShare.StorageSubSystem
- MSFT_StorageSubSystemToFileShare.FileShare
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToFileShare class

Association between an [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and its [**MSFT\_FileShare**](msft-fileshare.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToFileShare
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_FileShare        REF FileShare;
};
```

## Members

The **MSFT\_StorageSubSystemToFileShare** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToFileShare** class has these properties.

 

**FileShare**
   

Data type: **[**MSFT\_FileShare**](msft-fileshare.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StorageSubSystem**
   

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_FileShare**](msft-fileshare.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





