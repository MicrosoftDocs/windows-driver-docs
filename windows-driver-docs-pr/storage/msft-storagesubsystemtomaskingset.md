---
title: MSFT\_StorageSubSystemToMaskingSet class
description: Association between StorageSubSystem and MaskingSet.
ms.assetid: 38E7838B-E9CB-4FDF-9952-A4DB47F57FE0
keywords:
- MSFT_StorageSubSystemToMaskingSet class Windows Storage Management API
- MSFT_StorageSubSystemToMaskingSet class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToMaskingSet
- MSFT_StorageSubSystemToMaskingSet.StorageSubSystem
- MSFT_StorageSubSystemToMaskingSet.MaskingSet
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToMaskingSet class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**MaskingSet**](msft-maskingset.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToMaskingSet
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_MaskingSet       REF MaskingSet;
};
```

## Members

The **MSFT\_StorageSubSystemToMaskingSet** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToMaskingSet** class has these properties.

 

**MaskingSet**
   

Data type: **MSFT\_MaskingSet**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StorageSubSystem**
   

Data type: **MSFT\_StorageSubSystem**
 

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

 

[**MSFT\_MaskingSet**](msft-maskingset.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





