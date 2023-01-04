---
title: MSFT\_StorageSubSystemToStoragePool class
description: Association between StorageSubSystem and StoragePool.
ms.assetid: 8fa2f262-3ffd-4bcb-b6a6-628e7d3fbe63
keywords:
- MSFT_StorageSubSystemToStoragePool class Windows Storage Management API
- MSFT_StorageSubSystemToStoragePool class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToStoragePool
- MSFT_StorageSubSystemToStoragePool.StorageSubSystem
- MSFT_StorageSubSystemToStoragePool.StoragePool
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToStoragePool class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**StoragePool**](msft-storagepool.md)

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToStoragePool
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_StoragePool      REF StoragePool;
};
```

## Members

The **MSFT\_StorageSubSystemToStoragePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToStoragePool** class has these properties.

 

**StoragePool**
   

Data type: **MSFT\_StoragePool**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StorageSubSystem**
   

Data type: **MSFT\_StorageSubSystem**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





