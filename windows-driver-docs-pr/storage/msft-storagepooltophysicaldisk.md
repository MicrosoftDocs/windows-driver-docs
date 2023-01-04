---
title: MSFT\_StoragePoolToPhysicalDisk class
description: Association between StoragePool and PhysicalDisk.Primordial storage pools should retain their association to all physical disks that originated from that pool.
ms.assetid: aadef48f-76c7-4aa5-86e7-2ffdceb7f048
keywords:
- MSFT_StoragePoolToPhysicalDisk class Windows Storage Management API
- MSFT_StoragePoolToPhysicalDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StoragePoolToPhysicalDisk
- MSFT_StoragePoolToPhysicalDisk.StoragePool
- MSFT_StoragePoolToPhysicalDisk.PhysicalDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StoragePoolToPhysicalDisk class

Association between [**StoragePool**](msft-storagepool.md) and [**PhysicalDisk**](msft-physicaldisk.md).

Primordial storage pools should retain their association to all physical disks that originated from that pool. This means that if a physical disk has been added to a concrete pool, the disk should have an association with both its concrete and primordial pools.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StoragePoolToPhysicalDisk
{
  MSFT_StoragePool  REF StoragePool;
  MSFT_PhysicalDisk REF PhysicalDisk;
};
```

## Members

The **MSFT\_StoragePoolToPhysicalDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StoragePoolToPhysicalDisk** class has these properties.

 

**PhysicalDisk**
   

Data type: **[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StoragePool**
   

Data type: **[**MSFT\_StoragePool**](msft-storagepool.md)**
 

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
 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





