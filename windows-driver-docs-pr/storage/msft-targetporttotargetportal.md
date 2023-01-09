---
title: MSFT\_TargetPortToTargetPortal class
description: Association between TargetPort and TargetPortal.
ms.assetid: 83174B58-7A06-4431-8453-CA948CD900D4
keywords:
- MSFT_TargetPortToTargetPortal class Windows Storage Management API
- MSFT_TargetPortToTargetPortal class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_TargetPortToTargetPortal
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_TargetPortToTargetPortal class

Association between [**TargetPort**](msft-targetport.md) and [**TargetPortal**](msft-targetportal.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_TargetPortToTargetPortal
{
  MSFT_TargetPort   REF TargetPort;
  MSFT_TargetPortal REF TargetPortal;
};
```

## Members

The **MSFT\_TargetPortToTargetPortal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_TargetPortToTargetPortal** class has these properties.

 

[**TargetPort**](msft-targetport.md)
   

Data type: **[**MSFT\_TargetPort**](msft-targetport.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

[**TargetPortal**](msft-targetportal.md)
   

Data type: **[**MSFT\_TargetPortal**](msft-targetportal.md)**
 

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

 

[**MSFT\_TargetPort**](msft-targetport.md)
 

[**MSFT\_TargetPortal**](msft-targetportal.md)
 

 

 





