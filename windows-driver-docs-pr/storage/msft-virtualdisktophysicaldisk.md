---
title: MSFT\_VirtualDiskToPhysicalDisk class
description: Association between VirtualDisk and PhysicalDisk.A virtual disk and a physical disk are associated when the virtual disk has data residing on the physical disk.
ms.assetid: F2B91FCD-81BF-44D8-B6D1-CDECC765726F
keywords:
- MSFT_VirtualDiskToPhysicalDisk class Windows Storage Management API
- MSFT_VirtualDiskToPhysicalDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_VirtualDiskToPhysicalDisk
- MSFT_VirtualDiskToPhysicalDisk.VirtualDisk
- MSFT_VirtualDiskToPhysicalDisk.PhysicalDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_VirtualDiskToPhysicalDisk class

Association between [**VirtualDisk**](msft-virtualdisk.md) and [**PhysicalDisk**](msft-physicaldisk.md).

A virtual disk and a physical disk are associated when the virtual disk has data residing on the physical disk.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_VirtualDiskToPhysicalDisk
{
  MSFT_VirtualDisk  REF VirtualDisk;
  MSFT_PhysicalDisk REF PhysicalDisk;
};
```

## Members

The **MSFT\_VirtualDiskToPhysicalDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VirtualDiskToPhysicalDisk** class has these properties.

 

**PhysicalDisk**
   

Data type: **[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**VirtualDisk**
   

Data type: **[**MSFT\_VirtualDisk**](msft-virtualdisk.md)**
 

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

 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

[**MSFT\_PhysicalDisk**](msft-physicaldisk.md)
 

 

 





