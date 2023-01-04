---
title: MSFT\_FileServerToFileShare class
description: Association between a MSFT\_FileServer and its MSFT\_FileShare objects.
ms.assetid: 9A76E1EA-50B1-49F2-8B0D-BB444CC89188
keywords:
- MSFT_FileServerToFileShare class Windows Storage Management API
- MSFT_FileServerToFileShare class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_FileServerToFileShare
- MSFT_FileServerToFileShare.FileServer
- MSFT_FileServerToFileShare.FileShare
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_FileServerToFileShare class

Association between a [**MSFT\_FileServer**](msft-fileserver.md) and its [**MSFT\_FileShare**](msft-fileshare.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_FileServerToFileShare
{
  MSFT_FileServer REF FileServer;
  MSFT_FileShare  REF FileShare;
};
```

## Members

The **MSFT\_FileServerToFileShare** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FileServerToFileShare** class has these properties.

 

**FileServer**
   

Data type: **[**MSFT\_FileServer**](msft-fileserver.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**FileShare**
   

Data type: **[**MSFT\_FileShare**](msft-fileshare.md)**
 

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
 

[**MSFT\_FileShare**](msft-fileshare.md)
 

 

 





