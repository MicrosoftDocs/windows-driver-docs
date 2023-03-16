---
title: MSFT\_VirtualDiskToDisk class
description: Association between VirtualDisk and Disk.
ms.assetid: 661e8d56-ac91-4b94-a951-8577b7a26d2e
keywords:
- MSFT_VirtualDiskToDisk class Windows Storage Management API
- MSFT_VirtualDiskToDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_VirtualDiskToDisk
- MSFT_VirtualDiskToDisk.VirtualDisk
- MSFT_VirtualDiskToDisk.Disk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_VirtualDiskToDisk class

Association between [**VirtualDisk**](msft-virtualdisk.md) and [**Disk**](msft-disk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_VirtualDiskToDisk
{
  MSFT_VirtualDisk REF VirtualDisk;
  MSFT_Disk        REF Disk;
};
```

## Members

The **MSFT\_VirtualDiskToDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VirtualDiskToDisk** class has these properties.

 

**Disk**
   

Data type: **MSFT\_Disk**
 

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

 

[**MSFT\_Disk**](msft-disk.md)
 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





