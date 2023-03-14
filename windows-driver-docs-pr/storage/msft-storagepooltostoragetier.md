---
title: MSFT\_StoragePoolToStorageTier class
description: Association between a storage pool and storage tiers in that pool.
ms.assetid: 39B3D9AA-56FA-49ED-8EF2-E85947F382E0
keywords:
- MSFT_StoragePoolToStorageTier class Windows Storage Management API
- MSFT_StoragePoolToStorageTier class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StoragePoolToStorageTier
- MSFT_StoragePoolToStorageTier.StoragePool
- MSFT_StoragePoolToStorageTier.StorageTier
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StoragePoolToStorageTier class

Association between a storage pool and storage tiers in that pool.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StoragePoolToStorageTier
{
  MSFT_StoragePool REF StoragePool;
  MSFT_StorageTier REF StorageTier;
};
```

## Members

The **MSFT\_StoragePoolToStorageTier** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StoragePoolToStorageTier** class has these properties.

 

**StoragePool**
   

Data type: **[**MSFT\_StoragePool**](msft-storagepool.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StorageTier**
   

Data type: **[**MSFT\_StorageTier**](msft-storagetier.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





