---
title: MSFT\_DiskToStorageReliabilityCounter class
description: Association between a MSFT\_Disk object and the corresponding MSFT\_StorageReliabilityCounter object.
ms.assetid: A9B5BF06-4062-4244-9A27-9B4AC5ACEA00
keywords:
- MSFT_DiskToStorageReliabilityCounter class Windows Storage Management API
- MSFT_DiskToStorageReliabilityCounter class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_DiskToStorageReliabilityCounter
- MSFT_DiskToStorageReliabilityCounter.Disk
- MSFT_DiskToStorageReliabilityCounter.StorageReliabilityCounter
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# MSFT\_DiskToStorageReliabilityCounter class

Association between a [**MSFT\_Disk**](msft-disk.md) object and the corresponding [**MSFT\_StorageReliabilityCounter**](msft-storagereliabilitycounter.md) object.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_DiskToStorageReliabilityCounter
{
  MSFT_Disk                      REF Disk;
  MSFT_StorageReliabilityCounter REF StorageReliabilityCounter;
};
```

## Members

The **MSFT\_DiskToStorageReliabilityCounter** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DiskToStorageReliabilityCounter** class has these properties.

 

**Disk**
   

Data type: **[**MSFT\_Disk**](msft-disk.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

The disk object.

 

**StorageReliabilityCounter**
   

Data type: **[**MSFT\_StorageReliabilityCounter**](msft-storagereliabilitycounter.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

The storage reliability counter object.

 

 

 




