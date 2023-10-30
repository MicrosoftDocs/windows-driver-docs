---
title: MSFT\_StorageFaultDomain class
description: Common base class for all storage fault domain objects.
ms.assetid: 662C4D52-AE58-4922-BB01-0470B5B3F3C3
keywords:
- MSFT_StorageFaultDomain class Windows Storage Management API
- MSFT_StorageFaultDomain class Windows Storage Management API , described
topic_type:
- apiref
ms.topic: reference
api_name:
- MSFT_StorageFaultDomain
- MSFT_StorageFaultDomain.Manufacturer
- MSFT_StorageFaultDomain.Model
- MSFT_StorageFaultDomain.SerialNumber
- MSFT_StorageFaultDomain.PhysicalLocation
- MSFT_StorageFaultDomain.HealthStatus
- MSFT_StorageFaultDomain.OperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.date: 05/31/2018
---

# MSFT\_StorageFaultDomain class

Common base class for all storage fault domain objects.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageFaultDomain : MSFT_StorageObject
{
  String Manufacturer;
  String Model;
  String SerialNumber;
  String PhysicalLocation;
  UInt16 HealthStatus;
  UInt16 OperationalStatus[];
};
```

## Members

The **MSFT\_StorageFaultDomain** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageFaultDomain** class has these properties.

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

The health status of the object.



| Value                                                                                                                                                                                                                               | Meaning                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
|  **Healthy** 0          | The object is in a good state. There has been no reported read or write packet loss.          |
|  **Warning** 1          | The object may be failing some read requests, but there have been no reported write failures. |
|  **Unhealthy** 2  | The object is failing read and write requests, or is no longer responding to any commands.    |
|  **Unknown** 5          | The health status is unknown.                                                                 |



 

 

**Manufacturer**
   

Data type: **String**
 

Access type: Read-only
 

The name of the company responsible for the hardware backing the fault domain object. For [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) it must match the disk's SCSI inquiry data.

 

**Model**
   

Data type: **String**
 

Access type: Read-only
 

Represents the model number of the hardware. For [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) it must match the disk's SCSI inquiry data.

 

**OperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array of values that specify the operational status of the object.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  **Unknown** 0                                                                               | The operational status of the object is unknown.                                                                                                                               |
|  **Other** 1                                                                                       | A vendor-specific operational status has been specified.                                                                                                                       |
|  **OK** 2                                                                                                                        | The object is responding to commands and is in a normal operating state.                                                                                                       |
|  **Degraded** 3                                                                           | The object is responding to commands but is not running in an optimal operating state.                                                                                         |
|  **Stressed** 4                                                                           | The object is functioning but needs attention. For example, it might be overloaded or overheated.                                                                              |
|  **Predictive Failure** 5                                   | The object is functioning nominally, but a failure in the near future is predicted.                                                                                            |
|  **Error** 6                                                                                       | An error has occurred.                                                                                                                                                         |
|  **Non-Recoverable Error** 7                       | A nonrecoverable error has occurred.                                                                                                                                           |
|  **Starting** 8                                                                           | The object is in the process of starting.                                                                                                                                      |
|  **Stopping** 9                                                                           | The object is in the process of stopping.                                                                                                                                      |
|  **Stopped** 10                                                                              | The object was stopped or shut down in a clean and orderly fashion.                                                                                                            |
|  **In Service** 11                                                                  | The object is being configured, maintained, cleaned, or otherwise administered.                                                                                                |
|  **No Contact** 12                                                                  | The storage provider has knowledge of the object but has never been able to establish communication with it.                                                                   |
|  **Lost Communication** 13                                  | The object is known to exist and has been contacted successfully in the past but is currently unreachable.                                                                     |
|  **Aborted** 14                                                                              | Similar to **Stopped**, except that the object stopped abruptly and may require configuration or maintenance.                                                                  |
|  **Dormant** 15                                                                              | The object is reachable, but it is inactive.                                                                                                                                   |
|  **Supporting Entity in Error** 16  | This status value does not necessarily indicate trouble with the object, but it does indicate that another device or connection that the object depends on may need attention. |
|  **Completed** 17                                                                      | The object has completed an operation. This status value should be combined with **OK**, **Error**, or **Degraded**, depending on the outcome of the operation                 |
|  **Power Mode** 18                                                                  | This value is reserved for system use.                                                                                                                                         |
|  **Relocating** 19                                                                  | The object is in the process of relocating.                                                                                                                                    |
|  **Microsoft Reserved** ..                                  | This value is reserved for system use.                                                                                                                                         |
|  **Failed Media** 0xD004                                                      |                                                                                                                                                                                           |
|  **Split** 0xD005                                                                                  |                                                                                                                                                                                           |
|  **Stale Metadata** 0xD006                                              |                                                                                                                                                                                           |
|  **IO Error** 0xD007                                                                      |                                                                                                                                                                                           |
|  **Unrecognized Metadata** 0xD008                  |                                                                                                                                                                                           |
|  **Microsoft Reserved** 0xD009..                            | This value is reserved for system use.                                                                                                                                         |



 

 

**PhysicalLocation**
   

Data type: **String**
 

Access type: Read-only
 

A free-form string indicating where the hardware is located.

 

**SerialNumber**
   

Data type: **String**
 

Access type: Read-only
 

Represents the serial number of the hardware. For [**MSFT\_PhysicalDisk**](msft-physicaldisk.md) it must match the disk's SCSI inquiry data.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 10 \[desktop apps only\]                                               |
| Minimum supported server | Windows Server 2016 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

 

 





