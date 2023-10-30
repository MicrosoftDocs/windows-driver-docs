---
title: MSFT\_StorageEvent class
description: Base class for representing storage events.
ms.assetid: 77338A5C-7AF6-4C78-80E1-AF557B60CA46
keywords:
- MSFT_StorageEvent class Windows Storage Management API
- MSFT_StorageEvent class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageEvent
- MSFT_StorageEvent.SourceObjectId
- MSFT_StorageEvent.SourceClassName
- MSFT_StorageEvent.SourceNamespace
- MSFT_StorageEvent.SourceServer
- MSFT_StorageEvent.Description
- MSFT_StorageEvent.EventTime
- MSFT_StorageEvent.PerceivedSeverity
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageEvent class

Base class for representing storage events.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Indication, Abstract]
class MSFT_StorageEvent
{
  String   SourceObjectId;
  String   SourceClassName;
  String   SourceNamespace;
  String   SourceServer;
  String   Description;
  Datetime EventTime;
  UInt16   PerceivedSeverity;
};
```

## Members

The **MSFT\_StorageEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageEvent** class has these properties.

 

**Description**
   

Data type: **String**
 

Access type: Read-only
 

A brief description of the event, provided by the storage subsystem.

 

**EventTime**
   

Data type: **Datetime**
 

Access type: Read-only
 

The date and time in which the event that triggered this event occurred.

 

**PerceivedSeverity**
   

Data type: **UInt16**
 

Access type: Read-only
 

The perceived severity of the event from the notifier's point of view.

One of the following values.



| Value                                                                                                                                                                                                                                                                           | Meaning                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
|  **Unknown** 0                                                      | The severity is unknown or indeterminate.                         |
|  **Information** 2                                      | The event is for informative purposes.                            |
|  **Degraded/Warning** 3                  | Action may be required by the user.                               |
|  **Minor** 4                                                              | Action is needed, but the situation is not serious at this time.  |
|  **Major** 5                                                              | Immediate action is needed.                                       |
|  **Critical** 6                                                  | Immediate action is needed and the scope of the issue is broad.   |
|  **Fatal/NonRecoverable** 7  | An error has occured, but it is too late to take remedial action. |
|  **Microsoft Reserved** ..         | This value is reserved for system use.                            |



 

 

**SourceClassName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The class of the object that caused the event. For example, if the object causing the event is a storage pool, this property should be set to "MSFT\_StoragePool" (not the vendor-derived class).

 

**SourceNamespace**
   

Data type: **String**
 

Access type: Read-only
 

The source namespace of the object that caused the event.

 

**SourceObjectId**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**ModelCorrespondence {"MSFT\_StorageObject.ObjectId"}**](/windows/win32/wmisdk/standard-qualifiers)
 

The object that caused the event.

 

**SourceServer**
   

Data type: **String**
 

Access type: Read-only
 

The source server of the object that caused the event.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageAlertEvent**](msft-storagealertevent.md)
 

[**MSFT\_StorageArrivalEvent**](msft-storagearrivalevent.md)
 

[**MSFT\_StorageDepartureEvent**](msft-storagedepartureevent.md)
 

[**MSFT\_StorageModificationEvent**](msft-storagemodificationevent.md)
 

 

