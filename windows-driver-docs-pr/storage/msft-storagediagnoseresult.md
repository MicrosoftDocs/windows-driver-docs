---
title: MSFT\_StorageDiagnoseResult class
description: Represents the result of a diagnose method call on a storage object.
ms.assetid: 6C164BE2-2B7B-404B-A254-1FBBB9FAE579
keywords:
- MSFT_StorageDiagnoseResult class Windows Storage Management API
- MSFT_StorageDiagnoseResult class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageDiagnoseResult
- MSFT_StorageDiagnoseResult.FaultId
- MSFT_StorageDiagnoseResult.FaultType
- MSFT_StorageDiagnoseResult.FaultingObjectDescription
- MSFT_StorageDiagnoseResult.FaultingObjectLocation
- MSFT_StorageDiagnoseResult.FaultingObject
- MSFT_StorageDiagnoseResult.Reason
- MSFT_StorageDiagnoseResult.RecommendedActions
- MSFT_StorageDiagnoseResult.PerceivedSeverity
- MSFT_StorageDiagnoseResult.EventTime
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageDiagnoseResult class

Represents the result of a diagnose method call on a storage object.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageDiagnoseResult
{
  String                 FaultId;
  String                 FaultType;
  String                 FaultingObjectDescription;
  String                 FaultingObjectLocation;
  MSFT_StorageObject REF FaultingObject;
  String                 Reason;
  String                 RecommendedActions[];
  UInt16                 PerceivedSeverity;
  Datetime               EventTime;
};
```

## Members

The **MSFT\_StorageDiagnoseResult** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageDiagnoseResult** class has these properties.

 

**EventTime**
   

Data type: **Datetime**
 

Access type: Read-only
 

Denotes the date and time of the incident. **Null** if the time is unknown.

 

**FaultId**
   

Data type: **String**
 

Access type: Read-only
 

A unique identifier for the fault.

 

**FaultingObject**
   

Data type: **[**MSFT\_StorageObject**](msft-storageobject.md)**
 

Access type: Read-only
 

Reference to the Storage Management API instance of the object that has faulted.

 

**FaultingObjectDescription**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The description of the object that triggered the fault.

 

**FaultingObjectLocation**
   

Data type: **String**
 

Access type: Read-only
 

The location of the object that triggered the fault.

 

**FaultType**
   

Data type: **String**
 

Access type: Read-only
 

A string that uniquely identifies the type of fault.

 

**PerceivedSeverity**
   

Data type: **UInt16**
 

Access type: Read-only
 

Denotes the perceived severity of the event from the notifier's point of view. One of the following values;



| Value                                                                                                                                                                                                                                                                           | Meaning                                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
|  **Unknown** 0                                                      | The severity is unknown or indeterminate.                          |
|  **Information** 2                                      | The event is for informative purposes.                             |
|  **Degraded/Warning** 3                  | Action may be required by the user.                                |
|  **Minor** 4                                                              | Action is needed, but the situation is not serious at this time.   |
|  **Major** 5                                                              | Immediate action is needed.                                        |
|  **Critical** 6                                                  | Immediate action is needed and the scope of the issue is broad.    |
|  **Fatal/NonRecoverable** 7  | An error has occurred, but it is too late to take remedial action. |



 

 

**Reason**
   

Data type: **String**
 

Access type: Read-only
 

The formatted message describing the reason for the fault.

 

**RecommendedActions**
   

Data type: **String** array
 

Access type: Read-only
 

Free form descriptions of the recommended actions to take to resolve the cause of the fault.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



 

