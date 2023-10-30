---
title: MSFT\_StorageAlertEvent class
description: Represents a storage alert event.
ms.assetid: 3DB2E42D-28BA-418C-8494-1C6FDCF44B98
keywords:
- MSFT_StorageAlertEvent class Windows Storage Management API
- MSFT_StorageAlertEvent class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageAlertEvent
- MSFT_StorageAlertEvent.AlertType
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageAlertEvent class

Represents a storage alert event.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Indication]
class MSFT_StorageAlertEvent : MSFT_StorageEvent
{
  UInt16 AlertType;
};
```

## Members

The **MSFT\_StorageAlertEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageAlertEvent** class has these properties.

 

**AlertType**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The alert type.



| Value                                                                                                                                         | Meaning                                        |
|-----------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
|  **1**                                           | Thin provisioning threshold reached |
|  **...**                                       | Microsoft Reserved                  |
|  **0x8000..**  | Vendor Specific                     |



 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageEvent**](msft-storageevent.md)
 

 

