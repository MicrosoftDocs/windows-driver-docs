---
title: MSFT\_StorageSubSystemToPartition class
description: Association between MSFT\_StorageSubSystem and MSFT\_Partition.
ms.assetid: 57565912-703D-4213-A53A-3A9A5D5EF46F
keywords:
- MSFT_StorageSubSystemToPartition class Windows Storage Management API
- MSFT_StorageSubSystemToPartition class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToPartition
- MSFT_StorageSubSystemToPartition.StorageSubSystem
- MSFT_StorageSubSystemToPartition.Partition
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToPartition class

Association between [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_Partition**](msft-partition.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToPartition
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_Partition        REF Partition;
};
```

## Members

The **MSFT\_StorageSubSystemToPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToPartition** class has these properties.

 

**Partition**
   

Data type: **[**MSFT\_Partition**](msft-partition.md)**
 

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

 

[**MSFT\_Partition**](msft-partition.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





