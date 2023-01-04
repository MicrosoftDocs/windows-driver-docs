---
title: MSFT\_StorageNodeToStoragePool class
description: Association between a storage node and a storage pool.
ms.assetid: 701C6089-46CB-4A26-B5A7-83316DFF49B5
keywords:
- MSFT_StorageNodeToStoragePool class Windows Storage Management API
- MSFT_StorageNodeToStoragePool class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageNodeToStoragePool
- MSFT_StorageNodeToStoragePool.StorageNode
- MSFT_StorageNodeToStoragePool.StoragePool
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageNodeToStoragePool class

Association between a storage node and a storage pool.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToStoragePool
{
  MSFT_StorageNode REF StorageNode;
  MSFT_StoragePool REF StoragePool;
};
```

## Members

The **MSFT\_StorageNodeToStoragePool** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToStoragePool** class has these properties.

 

**StorageNode**
   

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StoragePool**
   

Data type: **[**MSFT\_StoragePool**](msft-storagepool.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





