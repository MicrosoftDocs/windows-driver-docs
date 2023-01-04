---
title: MSFT\_StorageProviderToStorageSubSystem class
description: Association between StorageProvider and StorageSubSystem.
ms.assetid: 0be0f434-3d17-4075-86db-58b11ef15544
keywords:
- MSFT_StorageProviderToStorageSubSystem class Windows Storage Management API
- MSFT_StorageProviderToStorageSubSystem class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageProviderToStorageSubSystem
- MSFT_StorageProviderToStorageSubSystem.StorageProvider
- MSFT_StorageProviderToStorageSubSystem.StorageSubSystem
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageProviderToStorageSubSystem class

Association between [**StorageProvider**](msft-storageprovider.md) and [**StorageSubSystem**](msft-storagesubsystem.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageProviderToStorageSubSystem
{
  MSFT_StorageProvider  REF StorageProvider;
  MSFT_StorageSubSystem REF StorageSubSystem;
};
```

## Members

The **MSFT\_StorageProviderToStorageSubSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageProviderToStorageSubSystem** class has these properties.

 

**StorageProvider**
   

Data type: **MSFT\_StorageProvider**
 

Access type: Read-only
 

Qualifiers: **Key**
 

The storage provider.

 

**StorageSubSystem**
   

Data type: **MSFT\_StorageSubSystem**
 

Access type: Read-only
 

Qualifiers: **Key**
 

The storage subsystem.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageProvider**](msft-storageprovider.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





