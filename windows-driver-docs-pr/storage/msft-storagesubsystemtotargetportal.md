---
title: MSFT\_StorageSubSystemToTargetPortal class
description: Association between StorageSubSystem and TargetPortal.
ms.assetid: 40AEE0E9-85C7-4DCA-AE74-17E26399CE08
keywords:
- MSFT_StorageSubSystemToTargetPortal class Windows Storage Management API
- MSFT_StorageSubSystemToTargetPortal class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToTargetPortal
- MSFT_StorageSubSystemToTargetPortal.StorageSubSystem
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToTargetPortal class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**TargetPortal**](msft-targetportal.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToTargetPortal
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_TargetPortal     REF TargetPortal;
};
```

## Members

The **MSFT\_StorageSubSystemToTargetPortal** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToTargetPortal** class has these properties.

 

**StorageSubSystem**
   

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
 

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

 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

[**MSFT\_TargetPortal**](msft-targetportal.md)
 

 

 





