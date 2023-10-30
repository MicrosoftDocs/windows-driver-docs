---
title: MSFT\_StorageSubSystemToDisk class
description: Association between MSFT\_StorageSubSystem and MSFT\_Disk.
ms.assetid: 3028CC6E-0F50-4E50-AE91-0ACD063CE21C
keywords:
- MSFT_StorageSubSystemToDisk class Windows Storage Management API
- MSFT_StorageSubSystemToDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToDisk
- MSFT_StorageSubSystemToDisk.StorageSubSystem
- MSFT_StorageSubSystemToDisk.Disk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToDisk class

Association between [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_Disk**](msft-disk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToDisk
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_Disk             REF Disk;
};
```

## Members

The **MSFT\_StorageSubSystemToDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToDisk** class has these properties.

 

**Disk**
   

Data type: **[**MSFT\_Disk**](msft-disk.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StorageSubSystem**
   

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
 

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

 

[**MSFT\_Disk**](msft-disk.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





