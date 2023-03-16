---
title: MSFT\_StorageSubSystemToStorageFaultDomain class
description: Association between MSFT\_StorageSubSystem and MSFT\_StorageFaultDomain.
ms.assetid: 6A53CF61-FFD7-4657-8B88-BD97BC80C075
keywords:
- MSFT_StorageSubSystemToStorageFaultDomain class Windows Storage Management API
- MSFT_StorageSubSystemToStorageFaultDomain class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToStorageFaultDomain
- MSFT_StorageSubSystemToStorageFaultDomain.StorageSubSystem
- MSFT_StorageSubSystemToStorageFaultDomain.StorageFaultDomain
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToStorageFaultDomain class

Association between [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageSubSystemToStorageFaultDomain
{
  MSFT_StorageSubSystem   REF StorageSubSystem;
  MSFT_StorageFaultDomain REF StorageFaultDomain;
};
```

## Members

The **MSFT\_StorageSubSystemToStorageFaultDomain** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToStorageFaultDomain** class has these properties.

 

**StorageFaultDomain**
   

Data type: **[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StorageSubSystem**
   

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
 

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

 

[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





