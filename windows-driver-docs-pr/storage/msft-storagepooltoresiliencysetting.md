---
title: MSFT\_StoragePoolToResiliencySetting class
description: Association between StoragePool and ResiliencySetting.
ms.assetid: 8EA9D275-ED5D-4901-B0CD-546247512800
keywords:
- MSFT_StoragePoolToResiliencySetting class Windows Storage Management API
- MSFT_StoragePoolToResiliencySetting class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StoragePoolToResiliencySetting
- MSFT_StoragePoolToResiliencySetting.StoragePool
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StoragePoolToResiliencySetting class

Association between [**StoragePool**](msft-storagepool.md) and [**ResiliencySetting**](msft-resiliencysetting.md)

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StoragePoolToResiliencySetting
{
  MSFT_StoragePool       REF StoragePool;
  MSFT_ResiliencySetting REF ResiliencySetting;
};
```

## Members

The **MSFT\_StoragePoolToResiliencySetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StoragePoolToResiliencySetting** class has these properties.

 

[**ResiliencySetting**](msft-resiliencysetting.md)
   

Data type: **[**MSFT\_ResiliencySetting**](msft-resiliencysetting.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StoragePool**
   

Data type: **[**MSFT\_StoragePool**](msft-storagepool.md)**
 

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

 

[**MSFT\_ResiliencySetting**](msft-resiliencysetting.md)
 

[**MSFT\_StoragePool**](msft-storagepool.md)
 

 

 





