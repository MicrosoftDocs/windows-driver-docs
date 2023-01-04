---
title: MSFT\_PartitionToVolume class
description: Association between Partition and Volume.
ms.assetid: 739714d6-683a-468f-b404-cb78991383af
keywords:
- MSFT_PartitionToVolume class Windows Storage Management API
- MSFT_PartitionToVolume class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_PartitionToVolume
- MSFT_PartitionToVolume.Partition
- MSFT_PartitionToVolume.Volume
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_PartitionToVolume class

Association between [**Partition**](msft-partition.md) and [**Volume**](msft-volume.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_PartitionToVolume
{
  MSFT_Partition REF Partition;
  MSFT_Volume    REF Volume;
};
```

## Members

The **MSFT\_PartitionToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_PartitionToVolume** class has these properties.

 

**Partition**
   

Data type: **MSFT\_Partition**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**Volume**
   

Data type: **MSFT\_Volume**
 

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

 

[**MSFT\_Partition**](msft-partition.md)
 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





