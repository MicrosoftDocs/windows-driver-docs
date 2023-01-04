---
title: MSFT\_MaskingSetToInitiatorId class
description: Association between MaskingSet and InitiatorId.
ms.assetid: 8D2D62DE-D7DB-4E22-9704-017B586988BE
keywords:
- MSFT_MaskingSetToInitiatorId class Windows Storage Management API
- MSFT_MaskingSetToInitiatorId class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_MaskingSetToInitiatorId
- MSFT_MaskingSetToInitiatorId.MaskingSet
- MSFT_MaskingSetToInitiatorId.InitiatorId
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_MaskingSetToInitiatorId class

Association between [**MaskingSet**](msft-maskingset.md) and [**InitiatorId**](msft-initiatorid.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_MaskingSetToInitiatorId
{
  MSFT_MaskingSet  REF MaskingSet;
  MSFT_InitiatorId REF InitiatorId;
};
```

## Members

The **MSFT\_MaskingSetToInitiatorId** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MaskingSetToInitiatorId** class has these properties.

 

**InitiatorId**
   

Data type: **MSFT\_InitiatorId**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**MaskingSet**
   

Data type: **MSFT\_MaskingSet**
 

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
 

[**MSFT\_MaskingSet**](msft-maskingset.md)
 

 

 





