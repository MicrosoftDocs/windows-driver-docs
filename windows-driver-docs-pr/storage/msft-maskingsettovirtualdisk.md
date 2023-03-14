---
title: MSFT\_MaskingSetToVirtualDisk class
description: Association between MaskingSet and VirtualDisk.
ms.assetid: 4E5328D1-655B-45A5-9D76-A2042377F7F1
keywords:
- MSFT_MaskingSetToVirtualDisk class Windows Storage Management API
- MSFT_MaskingSetToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_MaskingSetToVirtualDisk
- MSFT_MaskingSetToVirtualDisk.MaskingSet
- MSFT_MaskingSetToVirtualDisk.VirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_MaskingSetToVirtualDisk class

Association between [**MaskingSet**](msft-maskingset.md) and [**VirtualDisk**](msft-virtualdisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_MaskingSetToVirtualDisk
{
  MSFT_MaskingSet  REF MaskingSet;
  MSFT_VirtualDisk REF VirtualDisk;
};
```

## Members

The **MSFT\_MaskingSetToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MaskingSetToVirtualDisk** class has these properties.

 

**MaskingSet**
   

Data type: **MSFT\_MaskingSet**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**VirtualDisk**
   

Data type: **MSFT\_VirtualDisk**
 

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
 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





