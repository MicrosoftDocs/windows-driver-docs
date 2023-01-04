---
title: MSFT\_StorageSubSystemToVirtualDisk class
description: Association between StorageSubSystem and VirtualDisk.
ms.assetid: 2fb7838f-e8c7-4fb4-83f1-4746a2bb3642
keywords:
- MSFT_StorageSubSystemToVirtualDisk class Windows Storage Management API
- MSFT_StorageSubSystemToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToVirtualDisk
- MSFT_StorageSubSystemToVirtualDisk.StorageSubSystem
- MSFT_StorageSubSystemToVirtualDisk.VirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToVirtualDisk class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**VirtualDisk**](msft-virtualdisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToVirtualDisk
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_VirtualDisk      REF VirtualDisk;
};
```

## Members

The **MSFT\_StorageSubSystemToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToVirtualDisk** class has these properties.

 

**StorageSubSystem**
   

Data type: **MSFT\_StorageSubSystem**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**VirtualDisk**
   

Data type: **MSFT\_VirtualDisk**
 

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

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





