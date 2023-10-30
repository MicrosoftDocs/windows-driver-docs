---
title: MSFT\_StorageSubSystemToVolume class
description: Association between an MSFT\_StorageSubSystem and MSFT\_Volume.
ms.assetid: EA89DCE7-39BE-4BEC-9C27-2C267595010D
keywords:
- MSFT_StorageSubSystemToVolume class Windows Storage Management API
- MSFT_StorageSubSystemToVolume class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToVolume
- MSFT_StorageSubSystemToVolume.StorageSubSystem
- MSFT_StorageSubSystemToVolume.Volume
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToVolume class

Association between an [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_Volume**](msft-volume.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToVolume
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_Volume           REF Volume;
};
```

## Members

The **MSFT\_StorageSubSystemToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToVolume** class has these properties.

 

**StorageSubSystem**
   

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
 

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

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

[**MSFT\_Volume**](msft-volume.md)
 

 

 





