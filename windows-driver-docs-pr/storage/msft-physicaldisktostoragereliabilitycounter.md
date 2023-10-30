---
title: MSFT\_PhysicalDiskToStorageReliabilityCounter class
description: Association between a MSFT\_PhysicalDisk object and the corresponding MSFT\_StorageReliabilityCounter object.
ms.assetid: 2900E210-F130-4DCF-B451-7EACFF04B759
keywords:
- MSFT_PhysicalDiskToStorageReliabilityCounter class Windows Storage Management API
- MSFT_PhysicalDiskToStorageReliabilityCounter class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_PhysicalDiskToStorageReliabilityCounter
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_PhysicalDiskToStorageReliabilityCounter class

Association between a [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) object and the corresponding [**MSFT\_StorageReliabilityCounter**](msft-storagereliabilitycounter.md) object.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_PhysicalDiskToStorageReliabilityCounter
{
  MSFT_PhysicalDisk              REF PhysicalDisk;
  MSFT_StorageReliabilityCounter REF StorageReliabilityCounter;
};
```

## Members

The **MSFT\_PhysicalDiskToStorageReliabilityCounter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_PhysicalDiskToStorageReliabilityCounter** class has these properties.

 

[**PhysicalDisk**](msft-physicaldisk.md)
   

Data type: **[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

The physical disk object.

 

[**StorageReliabilityCounter**](msft-storagereliabilitycounter.md)
   

Data type: **[**MSFT\_StorageReliabilityCounter**](msft-storagereliabilitycounter.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

The storage reliability counter object.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
 

[**MSFT\_StorageReliabilityCounter**](msft-storagereliabilitycounter.md)
 

 

 





