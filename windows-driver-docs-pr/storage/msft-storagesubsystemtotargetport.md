---
title: MSFT\_StorageSubSystemToTargetPort class
description: Association between StorageSubSystem and TargetPort.
ms.assetid: 70E186A0-7FBB-4EFB-ADAA-7EE7068DCF6F
keywords:
- MSFT_StorageSubSystemToTargetPort class Windows Storage Management API
- MSFT_StorageSubSystemToTargetPort class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToTargetPort
- MSFT_StorageSubSystemToTargetPort.StorageSubSystem
- MSFT_StorageSubSystemToTargetPort.TargetPort
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToTargetPort class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**TargetPort**](msft-targetport.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToTargetPort
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_TargetPort       REF TargetPort;
};
```

## Members

The **MSFT\_StorageSubSystemToTargetPort** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToTargetPort** class has these properties.

 

**StorageSubSystem**
   

Data type: **MSFT\_StorageSubSystem**
 

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

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

[**MSFT\_TargetPort**](msft-targetport.md)
 

 

 





