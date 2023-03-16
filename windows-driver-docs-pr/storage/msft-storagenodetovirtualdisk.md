---
title: MSFT\_StorageNodeToVirtualDisk class
description: Association between a storage node and a virtual disk.
ms.assetid: 7A193FBD-6435-4CF3-86D3-FAEEB755C21F
keywords:
- MSFT_StorageNodeToVirtualDisk class Windows Storage Management API
- MSFT_StorageNodeToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageNodeToVirtualDisk
- MSFT_StorageNodeToVirtualDisk.StorageNode
- MSFT_StorageNodeToVirtualDisk.VirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageNodeToVirtualDisk class

Association between a storage node and a virtual disk.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToVirtualDisk
{
  MSFT_StorageNode REF StorageNode;
  MSFT_VirtualDisk REF VirtualDisk;
};
```

## Members

The **MSFT\_StorageNodeToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToVirtualDisk** class has these properties.

 

**StorageNode**
   

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**VirtualDisk**
   

Data type: **[**MSFT\_VirtualDisk**](msft-virtualdisk.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





