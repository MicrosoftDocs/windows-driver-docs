---
title: MSFT\_StorageSubSystemToInitiatorId class
description: Association between StorageSubSystem and InitiatorId.
ms.assetid: C7F30596-DEA8-4179-8C2B-0F8F65248CF9
keywords:
- MSFT_StorageSubSystemToInitiatorId class Windows Storage Management API
- MSFT_StorageSubSystemToInitiatorId class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToInitiatorId
- MSFT_StorageSubSystemToInitiatorId.StorageSubSystem
- MSFT_StorageSubSystemToInitiatorId.InitiatorId
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToInitiatorId class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**InitiatorId**](msft-initiatorid.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToInitiatorId
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_InitiatorId      REF InitiatorId;
};
```

## Members

The **MSFT\_StorageSubSystemToInitiatorId** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToInitiatorId** class has these properties.

 

**InitiatorId**
   

Data type: **MSFT\_InitiatorId**
 

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

 

[**MSFT\_InitiatorId**](msft-initiatorid.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





