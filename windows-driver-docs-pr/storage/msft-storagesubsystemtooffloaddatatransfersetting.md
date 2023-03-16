---
title: MSFT\_StorageSubSystemToOffloadDataTransferSetting class
description: Association between StorageSubSystem and OffloadDataTransferSetting.
ms.assetid: 63E7794B-BD92-47AD-A1C3-0FF57B80AC2B
keywords:
- MSFT_StorageSubSystemToOffloadDataTransferSetting class Windows Storage Management API
- MSFT_StorageSubSystemToOffloadDataTransferSetting class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageSubSystemToOffloadDataTransferSetting
- MSFT_StorageSubSystemToOffloadDataTransferSetting.StorageSubSystem
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageSubSystemToOffloadDataTransferSetting class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**OffloadDataTransferSetting**](msft-offloaddatatransfersetting.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToOffloadDataTransferSetting
{
  MSFT_StorageSubSystem           REF StorageSubSystem;
  MSFT_OffloadDataTransferSetting REF OffloadDataTransferSetting;
};
```

## Members

The **MSFT\_StorageSubSystemToOffloadDataTransferSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToOffloadDataTransferSetting** class has these properties.

 

[**OffloadDataTransferSetting**](msft-offloaddatatransfersetting.md)
   

Data type: **[**MSFT\_OffloadDataTransferSetting**](msft-offloaddatatransfersetting.md)**
 

Access type: Read-only
 

Qualifiers: **Key**
 

 

**StorageSubSystem**
   

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
 

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

 

[**MSFT\_OffloadDataTransferSetting**](msft-offloaddatatransfersetting.md)
 

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
 

 

 





