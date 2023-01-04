---
title: MSFT\_StoragePoolToVolume class
description: Association between MSFT\_StoragePool and MSFT\_Volume. This association should only exist for concrete pools.
ms.assetid: E8A036AD-47E1-47CF-A382-E7FC4DB671CB
keywords:
- MSFT_StoragePoolToVolume class Windows Storage Management API
- MSFT_StoragePoolToVolume class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StoragePoolToVolume
- MSFT_StoragePoolToVolume.StoragePool
- MSFT_StoragePoolToVolume.Volume
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StoragePoolToVolume class

Association between [**MSFT\_StoragePool**](msft-storagepool.md) and [**MSFT\_Volume**](msft-volume.md). This association should only exist for concrete pools.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StoragePoolToVolume
{
  MSFT_StoragePool REF StoragePool;
  MSFT_Volume      REF Volume;
};
```

## Members

The **MSFT\_StoragePoolToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StoragePoolToVolume** class has these properties.

 

**StoragePool**
   

Data type: **[**MSFT\_StoragePool**](msft-storagepool.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**Volume**
   

Data type: **[**MSFT\_Volume**](msft-volume.md)**
 

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

 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





