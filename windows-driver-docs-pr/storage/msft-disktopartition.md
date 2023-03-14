---
title: MSFT\_DiskToPartition class
description: Association between Disk and Partition.
ms.assetid: 6d293eea-3c40-414d-bb05-c59a37ccb1e7
keywords:
- MSFT_DiskToPartition class Windows Storage Management API
- MSFT_DiskToPartition class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_DiskToPartition
- MSFT_DiskToPartition.Disk
- MSFT_DiskToPartition.Partition
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_DiskToPartition class

Association between [**Disk**](msft-disk.md) and [**Partition**](msft-partition.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_DiskToPartition
{
  MSFT_Disk      REF Disk;
  MSFT_Partition REF Partition;
};
```

## Members

The **MSFT\_DiskToPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DiskToPartition** class has these properties.

 

**Disk**
   

Data type: **[**MSFT\_Disk**](msft-disk.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**Partition**
   

Data type: **[**MSFT\_Partition**](msft-partition.md)**
 

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
 

[**MSFT\_Partition**](msft-partition.md)
 

 

 





