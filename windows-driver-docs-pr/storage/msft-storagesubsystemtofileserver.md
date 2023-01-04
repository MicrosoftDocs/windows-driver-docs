---
title: MSFT\_StorageSubSystemToFileServer class
description: Association between a MSFT\_StorageSubSystem and its MSFT\_FileServer.
ms.assetid: 64B3A267-4286-4D0D-A646-F001074180EE
keywords:
- MSFT_StorageSubSystemToFileServer class Windows Storage Management API
- MSFT_StorageSubSystemToFileServer class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToFileServer
- MSFT_StorageSubSystemToFileServer.StorageSubSystem
- MSFT_StorageSubSystemToFileServer.FileServer
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToFileServer class

Association between a [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and its [**MSFT\_FileServer**](msft-fileserver.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToFileServer
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_FileServer       REF FileServer;
};
```

## Members

The **MSFT\_StorageSubSystemToFileServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToFileServer** class has these properties.

 

**FileServer**
   

Data type: **[**MSFT\_FileServer**](msft-fileserver.md)**
 

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

 

[**MSFT\_FileServer**](msft-fileserver.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





