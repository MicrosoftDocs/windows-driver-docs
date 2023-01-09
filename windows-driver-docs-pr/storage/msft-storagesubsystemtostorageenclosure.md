---
title: MSFT\_StorageSubSystemToStorageEnclosure class
description: Association between StorageSubSystem and StorageEnclosure.
ms.assetid: 787A2FC9-A215-4F76-936E-709D5BC0FD30
keywords:
- MSFT_StorageSubSystemToStorageEnclosure class Windows Storage Management API
- MSFT_StorageSubSystemToStorageEnclosure class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToStorageEnclosure
- MSFT_StorageSubSystemToStorageEnclosure.StorageSubSystem
- MSFT_StorageSubSystemToStorageEnclosure.StorageEnclosure
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToStorageEnclosure class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**StorageEnclosure**](msft-storageenclosure.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToStorageEnclosure
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_StorageEnclosure REF StorageEnclosure;
};
```

## Members

The **MSFT\_StorageSubSystemToStorageEnclosure** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToStorageEnclosure** class has these properties.

 

**StorageEnclosure**
   

Data type: **[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers)
 

 

**StorageSubSystem**
   

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers)
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)
 

 

