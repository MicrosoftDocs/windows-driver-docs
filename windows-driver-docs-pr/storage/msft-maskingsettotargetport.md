---
title: MSFT\_MaskingSetToTargetPort class
description: Association between MaskingSet and TargetPort.
ms.assetid: CBB7BA43-8506-474C-BE1B-58326AAECD8F
keywords:
- MSFT_MaskingSetToTargetPort class Windows Storage Management API
- MSFT_MaskingSetToTargetPort class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_MaskingSetToTargetPort
- MSFT_MaskingSetToTargetPort.MaskingSet
- MSFT_MaskingSetToTargetPort.TargetPort
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_MaskingSetToTargetPort class

Association between [**MaskingSet**](msft-maskingset.md) and [**TargetPort**](msft-targetport.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_MaskingSetToTargetPort
{
  MSFT_MaskingSet REF MaskingSet;
  MSFT_TargetPort REF TargetPort;
};
```

## Members

The **MSFT\_MaskingSetToTargetPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MaskingSetToTargetPort** class has these properties.

 

**MaskingSet**
   

Data type: **MSFT\_MaskingSet**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**TargetPort**
   

Data type: **MSFT\_TargetPort**
 

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
 

[**MSFT\_TargetPort**](msft-targetport.md)
 

 

 





