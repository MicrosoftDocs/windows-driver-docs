---
title: MSFT\_TargetPortToVirtualDisk class
description: Association between TargetPort and VirtualDisk.
ms.assetid: EF675F41-FD41-4C95-97AD-6189ACF4032A
keywords:
- MSFT_TargetPortToVirtualDisk class Windows Storage Management API
- MSFT_TargetPortToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_TargetPortToVirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_TargetPortToVirtualDisk class

Association between [**TargetPort**](msft-targetport.md) and [**VirtualDisk**](msft-virtualdisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_TargetPortToVirtualDisk
{
  MSFT_TargetPort  REF TargetPort;
  MSFT_VirtualDisk REF VirtualDisk;
};
```

## Members

The **MSFT\_TargetPortToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_TargetPortToVirtualDisk** class has these properties.

 

[**TargetPort**](msft-targetport.md)
   

Data type: **[**MSFT\_TargetPort**](msft-targetport.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

[**VirtualDisk**](msft-virtualdisk.md)
   

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

 

[**MSFT\_TargetPort**](msft-targetport.md)
 

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
 

 

 





