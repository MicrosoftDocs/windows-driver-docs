---
title: MSFT\_StorageFaultDomainToStorageFaultDomain class
description: Association between an MSFT\_StorageFaultDomain object and its ancestor or descendent MSFT\_StorageFaultDomain objects.
ms.assetid: A45632F0-7607-49F8-BB6C-FF1043A9E173
keywords:
- MSFT_StorageFaultDomainToStorageFaultDomain class Windows Storage Management API
- MSFT_StorageFaultDomainToStorageFaultDomain class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageFaultDomainToStorageFaultDomain
- MSFT_StorageFaultDomainToStorageFaultDomain.SourceStorageFaultDomain
- MSFT_StorageFaultDomainToStorageFaultDomain.TargetStorageFaultDomain
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageFaultDomainToStorageFaultDomain class

Association between an [**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md) object and its ancestor or descendent **MSFT\_StorageFaultDomain** objects.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageFaultDomainToStorageFaultDomain
{
  MSFT_StorageFaultDomain REF SourceStorageFaultDomain;
  MSFT_StorageFaultDomain REF TargetStorageFaultDomain;
};
```

## Members

The **MSFT\_StorageFaultDomainToStorageFaultDomain** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageFaultDomainToStorageFaultDomain** class has these properties.

 

**SourceStorageFaultDomain**
   

Data type: **[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**TargetStorageFaultDomain**
   

Data type: **[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)**
 

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
 

 

 





