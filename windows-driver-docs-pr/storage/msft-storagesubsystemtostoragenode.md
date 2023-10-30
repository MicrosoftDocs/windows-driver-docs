---
title: MSFT\_StorageSubSystemToStorageNode class
description: Association between a storage subsystem and a storage node.
ms.assetid: E8D27895-90A7-4A61-A1AE-79F82AF9C53E
keywords:
- MSFT_StorageSubSystemToStorageNode class Windows Storage Management API
- MSFT_StorageSubSystemToStorageNode class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToStorageNode
- MSFT_StorageSubSystemToStorageNode.StorageSubSystem
- MSFT_StorageSubSystemToStorageNode.StorageNode
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToStorageNode class

Association between a storage subsystem and a storage node.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToStorageNode
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_StorageNode      REF StorageNode;
};
```

## Members

The **MSFT\_StorageSubSystemToStorageNode** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToStorageNode** class has these properties.

 

**StorageNode**
   

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StorageSubSystem**
   

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

 





