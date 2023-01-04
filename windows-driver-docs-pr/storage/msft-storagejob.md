---
title: MSFT\_StorageJob class
description: Represents a storage job.
ms.assetid: 71DC2B71-3F39-488F-B9D0-01E65354BF7C
keywords:
- MSFT_StorageJob class Windows Storage Management API
- MSFT_StorageJob class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageJob
- MSFT_StorageJob.Name
- MSFT_StorageJob.Description
- MSFT_StorageJob.ElapsedTime
- MSFT_StorageJob.ErrorCode
- MSFT_StorageJob.ErrorDescription
- MSFT_StorageJob.JobState
- MSFT_StorageJob.JobStatus
- MSFT_StorageJob.LocalOrUtcTime
- MSFT_StorageJob.OperationalStatus
- MSFT_StorageJob.StatusDescriptions
- MSFT_StorageJob.PercentComplete
- MSFT_StorageJob.StartTime
- MSFT_StorageJob.TimeBeforeRemoval
- MSFT_StorageJob.TimeOfLastStateChange
- MSFT_StorageJob.TimeSubmitted
- MSFT_StorageJob.DeleteOnCompletion
- MSFT_StorageJob.IsBackgroundTask
- MSFT_StorageJob.RecoveryAction
- MSFT_StorageJob.OtherRecoveryAction
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageJob class

Represents a storage job.

The following syntax is simplified from Managed Object Format (MOF) code.

Storage jobs represent long running operations on a storage subsystem. These operations can be initiated in either of the following ways:

-   By users, through the various management interfaces defined by this MOF.
-   Automatically, by intelligent storage subsystems.

## Syntax

``` syntax
class MSFT_StorageJob : MSFT_StorageObject
{
  String   Name;
  String   Description;
  Datetime ElapsedTime;
  UInt16   ErrorCode;
  String   ErrorDescription;
  UInt16   JobState;
  String   JobStatus;
  UInt16   LocalOrUtcTime;
  UInt16   OperationalStatus[];
  String   StatusDescriptions[];
  UInt16   PercentComplete;
  Datetime StartTime;
  Datetime TimeBeforeRemoval;
  Datetime TimeOfLastStateChange;
  Datetime TimeSubmitted;
  Boolean  DeleteOnCompletion;
  Boolean  IsBackgroundTask;
  UInt16   RecoveryAction;
  String   OtherRecoveryAction;
};
```

## Members

The **MSFT\_StorageJob** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageJob** class has these methods.



| Method                                                           | Description                                                                                                        |
|:-----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------|
| [**GetExtendedStatus**](msft-storagejob-getextendedstatus.md)   | Retrieves extended status information for an unsuccessful storage job.                                  |
| [**RequestStateChange**](msft-storagejob-requeststatechange.md) | Requests that the state of the job be changed to the value specified in the *RequestedState* parameter. |



 

### Properties

The **MSFT\_StorageJob** class has these properties.

 

**DeleteOnCompletion**
   

Data type: **Boolean**
 

Access type: Read-only
 

If **TRUE**, the storage job will be deleted automatically after a short time interval.

 

**Description**
   

Data type: **String**
 

Access type: Read-only
 

A textual description of the operation that the storage job is tracking.

 

**ElapsedTime**
   

Data type: **Datetime**
 

Access type: Read-only
 

If the job is still executing, this property indicates how long it has been executing. If the job is complete, it is the total execution time.

 

**ErrorCode**
   

Data type: **UInt16**
 

Access type: Read-only
 

If the operation that this storage job was tracking has failed, the provider sets this property to an error code defined by the method that invoked the operation. If this storage job was tracking a background task, the error code can be set to any valid storage management error code as defined in the value map below. If there was no error, this property must be set to **Success**. This property should be **NULL** until the operation has completed.

 

**ErrorDescription**
   

Data type: **String**
 

Access type: Read-only
 

A free-form string that contains the vendor's error description.

 

**IsBackgroundTask**
   

Data type: **Boolean**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

If **TRUE**, this storage job represents an automated background task initiated by the storage subsystem. For all user- or management-initiated operations, this value should be set to **FALSE**.

 

**JobState**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

The state of the job.

 

**New** (2)
 

**Starting** (3)
 

**Running** (4)
 

**Suspended** (5)
 

**Shutting Down** (6)
 

**Completed** (7)
 

**Terminated** (8)
 

**Killed** (9)
 

**Exception** (10)
 

**Service** (11)
 

**Query Pending** (12)
 

**Microsoft Reserved** (13..32767)
 

**Vendor Reserved** (32768..65535)
 

 

**JobStatus**
   

Data type: **String**
 

Access type: Read-only
 

A free-form string that represents the status of the job. The primary status is reflected in the **OperationalStatus** property. **JobStatus** provides additional, implementation-specific details.

 

**LocalOrUtcTime**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: **Values** ( "Local Time", "UTC Time" ), **ValueMap** ("1", "2")
 

Indicates whether the time values in the **RunStartInterval** and **UntilTime** properties represent local time or UTC time. Time values are synchronized worldwide by setting this property to **UTC Time**.

 

**Name**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A system-defined name for the storage job.

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Indicates the current status of each storage subsystem that is participating in the storage job.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0                                                                               | The operational status is unknown.                                                                                                                                                             |
|  **Other** 1                                                                                       | A vendor-specific **OperationalStatus** is specified in the **OtherOperationalStatusDescription** property.                                                                                    |
|  **OK**  2                                                                                                                     | The storage subsystem is responding to commands and is in a normal operating state.                                                                                                            |
|  **Degraded** 3                                                                           | The storage subsystem is responding to commands, but is not running in an optimal operating state.                                                                                             |
|  **Stressed** 4                                                                           | The storage subsystem is functioning, but needs attention. For example, it may be overloaded or overheated.                                                                                    |
|  **Predictive Failure** 5                                   | The storage subsystem is functioning, but it is likely to fail in the near future.                                                                                                             |
|  **Error** 6                                                                                       | An error has occurred.                                                                                                                                                                         |
|  **Non-Recoverable Error** 7                       | A nonrecoverable error has occurred.                                                                                                                                                           |
|  **Starting** 8                                                                           | The storage subsystem is in the process of starting.                                                                                                                                           |
|  **Stopping** 9                                                                           | The storage subsystem is in the process of stopping.                                                                                                                                           |
|  **Stopped** 10                                                                              | The storage subsystem was stopped or shut down in a clean and orderly fashion.                                                                                                                 |
|  **In Service** 11                                                                  | The storage subsystem is being configured, maintained, cleaned, or otherwise administered.                                                                                                     |
|  **No Contact** 12                                                                  | The storage provider is aware of the storage subsystem, but has never been able to communicate with it.                                                                                        |
|  **Lost Communication** 13                                  | The storage provider is aware of the storage subsystem and has communicated with it in the past, but is currently unable to communicate with it.                                               |
|  **Aborted** 14                                                                              | The storage subsystem was stopped abruptly and might require configuration or maintenance.                                                                                                     |
|  **Dormant** 15                                                                              | The storage provider is able to contact the storage subsystem, but the storage subsystem is not currently active.                                                                              |
|  **Supporting Entity in Error** 16  | This value indicates that another device or connection that the storage subsystem depends on might need attention. It does not necessarily indicate trouble with the storage subsystem itself. |
|  **Completed** 17                                                                      | The storage subsystem has completed an operation. This value should be combined with "OK", "Error", or "Degraded", depending on the outcome of the operation.                                  |
|  **Power Mode** 18                                                                  | This value is reserved for system use.                                                                                                                                                         |
|  **DMTF Reserved** ..                                                      | Values between 18 and 0x8000 (exclusive) are reserved for DMTF.                                                                                                                                |
|  **Vendor Reserved** 0x8000..                                        | Values greater than or equal to 0x8000 are reserved for vendors.                                                                                                                               |



 

 

**OtherRecoveryAction**
   

Data type: **String**
 

Access type: Read-only
 

A vendor-specific recovery action to be taken for an unsuccessfully run job. This property should only be set if the **RecoveryAction** is set to **Other**.

 

**PercentComplete**
   

Data type: **UInt16**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers), [**Units**](/windows/win32/wmisdk/standard-qualifiers) (Percentage)
 

The percentage of the job that has completed at the time that this value is requested.

 

**RecoveryAction**
   

Data type: **UInt16**
 

Access type: Read-only
 

Describes the recovery action to be taken for an unsuccessfully run job. One of the following values.



| Value                                                                                                                                                                                                                                                                                   | Meaning                                                                              |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
|  **Unknown** 0                                                              | The desired recovery action is unknown.                                   |
|  **Other** 1                                                                      | The recovery action is specified in the **OtherRecoveryAction** property. |
|  **Do Not Continue** 2                              | Stop executing the storage job and appropriately update its status.       |
|  **Continue With Next Job** 3  | Continue with the next job in the queue.                                  |
|  **Re-run Job** 4                                                  | Rerun the job.                                                            |



 

 

**StartTime**
   

Data type: **Datetime**
 

Access type: Read-only
 

The time when the job was started.

 

**StatusDescriptions**
   

Data type: **String** array
 

Access type: Read-only
 

Descriptions of the **OperationalStatus** values. For example, if **Stopping** is a value in **OperationalStatus**, the corresponding array element of **StatusDescriptions** may explain why an object is being stopped.

 

**TimeBeforeRemoval**
   

Data type: **Datetime**
 

Access type: Read-only
 

The amount of time, in seconds, that the job is retained after it has finished executing, either succeeding or failing in that execution. The job must remain in existence for some period of time regardless of the value of the **DeleteOnCompletion** property.

 

**TimeOfLastStateChange**
   

Data type: **Datetime**
 

Access type: Read-only
 

The time when the state of the job last changed. If the state of the job has not changed and this property does not have a value, it must be set to zero. If a state change was requested, but it was rejected or has not yet been processed, the value of this property must not be updated.

 

**TimeSubmitted**
   

Data type: **Datetime**
 

Access type: Read-only
 

The time when the job was submitted for execution. A value of all zeros indicates that the owning element is not capable of reporting a date and time. Therefore, the **ScheduledStartTime** and **StartTime** are reported as intervals relative to the time their values are requested.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

