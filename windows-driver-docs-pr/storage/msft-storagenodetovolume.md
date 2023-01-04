---
title: MSFT\_StorageNodeToVolume class
description: Association between MSFT\_StorageNode and MSFT\_Volume.
ms.assetid: 7C19ED8C-34E7-409D-AF09-62C1FE49D7D7
keywords:
- MSFT_StorageNodeToVolume class Windows Storage Management API
- MSFT_StorageNodeToVolume class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageNodeToVolume
- MSFT_StorageNodeToVolume.StorageNode
- MSFT_StorageNodeToVolume.Volume
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageNodeToVolume class

Association between [**MSFT\_StorageNode**](msft-storagenode.md) and [**MSFT\_Volume**](msft-volume.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToVolume
{
  MSFT_StorageNode REF StorageNode;
  MSFT_Volume      REF Volume;
};
```

## Members

The **MSFT\_StorageNodeToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToVolume** class has these properties.

 

**StorageNode**
   

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
 

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

 

[**MSFT\_StorageNode**](msft-storagenode.md)
 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





