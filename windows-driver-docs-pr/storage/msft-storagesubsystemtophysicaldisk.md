---
title: MSFT\_StorageSubSystemToPhysicalDisk class
description: Association between StorageSubSystem and PhysicalDisk.
ms.assetid: a5340475-0b88-4f74-b721-bf32dc7ab398
keywords:
- MSFT_StorageSubSystemToPhysicalDisk class Windows Storage Management API
- MSFT_StorageSubSystemToPhysicalDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToPhysicalDisk
- MSFT_StorageSubSystemToPhysicalDisk.StorageSubSystem
- MSFT_StorageSubSystemToPhysicalDisk.PhysicalDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToPhysicalDisk class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**PhysicalDisk**](msft-physicaldisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToPhysicalDisk
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_PhysicalDisk     REF PhysicalDisk;
};
```

## Members

The **MSFT\_StorageSubSystemToPhysicalDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToPhysicalDisk** class has these properties.

 

**PhysicalDisk**
   

Data type: **MSFT\_PhysicalDisk**
 

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

 

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





