---
title: MSFT\_OffloadDataTransferSetting class
description: Represents the offload data transfer (ODX) settings for a subsystem.
ms.assetid: DCE938F6-8901-409F-9CBB-CAAB1F38F9AA
keywords:
- MSFT_OffloadDataTransferSetting class Windows Storage Management API
- MSFT_OffloadDataTransferSetting class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_OffloadDataTransferSetting
- MSFT_OffloadDataTransferSetting.SupportInterSubsystem
- MSFT_OffloadDataTransferSetting.NumberOfTokensMax
- MSFT_OffloadDataTransferSetting.NumberOfTokensInUse
- MSFT_OffloadDataTransferSetting.OptimalDataTokenSize
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_OffloadDataTransferSetting class

Represents the offload data transfer (ODX) settings for a subsystem.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_OffloadDataTransferSetting : MSFT_StorageObject
{
  Boolean SupportInterSubsystem;
  UInt32  NumberOfTokensMax;
  UInt32  NumberOfTokensInUse;
  UInt32  OptimalDataTokenSize;
};
```

## Members

The **MSFT\_OffloadDataTransferSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_OffloadDataTransferSetting** class has these properties.

 

**NumberOfTokensInUse**
   

Data type: **UInt32**
 

Access type: Read-only
 

The maximum number of tokens in use for the subsystem.

 

**NumberOfTokensMax**
   

Data type: **UInt32**
 

Access type: Read-only
 

The maximum number of tokens available for the subsystem.

 

**OptimalDataTokenSize**
   

Data type: **UInt32**
 

Access type: Read-only
 

The optimal data token size, in bytes.

 

**SupportInterSubsystem**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the subsystem supports transfer of data using tokens across different subsystems.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

 





