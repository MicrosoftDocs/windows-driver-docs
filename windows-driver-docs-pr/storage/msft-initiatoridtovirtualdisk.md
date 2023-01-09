---
title: MSFT\_InitiatorIdToVirtualDisk class
description: Association between InitiatorId and VirtualDisk.
ms.assetid: A0E84922-4D13-4934-8F00-2C2809062713
keywords:
- MSFT_InitiatorIdToVirtualDisk class Windows Storage Management API
- MSFT_InitiatorIdToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_InitiatorIdToVirtualDisk
- MSFT_InitiatorIdToVirtualDisk.InitiatorId
- MSFT_InitiatorIdToVirtualDisk.VirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_InitiatorIdToVirtualDisk class

Association between [**InitiatorId**](msft-initiatorid.md) and [**VirtualDisk**](msft-virtualdisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_InitiatorIdToVirtualDisk
{
  MSFT_InitiatorId REF InitiatorId;
  MSFT_VirtualDisk REF VirtualDisk;
};
```

## Members

The **MSFT\_InitiatorIdToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_InitiatorIdToVirtualDisk** class has these properties.

 

**InitiatorId**
   

Data type: **[**MSFT\_InitiatorId**](msft-initiatorid.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**VirtualDisk**
   

Data type: **[**MSFT\_VirtualDisk**](msft-virtualdisk.md)**
 

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

 

[**MSFT\_InitiatorId**](msft-initiatorid.md)
 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





