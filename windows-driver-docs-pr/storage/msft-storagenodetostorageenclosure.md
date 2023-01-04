---
title: MSFT\_StorageNodeToStorageEnclosure class
description: Association between StorageNode and StorageEnclosure.
ms.assetid: 1EC3975C-618B-4DE0-B1CC-B6B63D1936BE
keywords:
- MSFT_StorageNodeToStorageEnclosure class Windows Storage Management API
- MSFT_StorageNodeToStorageEnclosure class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageNodeToStorageEnclosure
- MSFT_StorageNodeToStorageEnclosure.StorageNode
- MSFT_StorageNodeToStorageEnclosure.StorageEnclosure
- MSFT_StorageNodeToStorageEnclosure.HealthStatus
- MSFT_StorageNodeToStorageEnclosure.PowerSupplyOperationalStatus
- MSFT_StorageNodeToStorageEnclosure.FanOperationalStatus
- MSFT_StorageNodeToStorageEnclosure.TemperatureSensorOperationalStatus
- MSFT_StorageNodeToStorageEnclosure.VoltageSensorOperationalStatus
- MSFT_StorageNodeToStorageEnclosure.CurrentSensorOperationalStatus
- MSFT_StorageNodeToStorageEnclosure.IOControllerOperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageNodeToStorageEnclosure class

Association between [**StorageNode**](msft-storagenode.md) and [**StorageEnclosure**](msft-storageenclosure.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToStorageEnclosure
{
  MSFT_StorageNode      REF StorageNode;
  MSFT_StorageEnclosure REF StorageEnclosure;
  UInt16                    HealthStatus;
  UInt16                    PowerSupplyOperationalStatus[];
  UInt16                    FanOperationalStatus[];
  UInt16                    TemperatureSensorOperationalStatus[];
  UInt16                    VoltageSensorOperationalStatus[];
  UInt16                    CurrentSensorOperationalStatus[];
  UInt16                    IOControllerOperationalStatus[];
};
```

## Members

The **MSFT\_StorageNodeToStorageEnclosure** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToStorageEnclosure** class has these properties.

 

**CurrentSensorOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

**Starting in Windows 10:** An array containing the operational status of each current sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
|  **Unknown** 0                                                          |                                                                        |
|  **OK** 2                                                                                                   | The element is present and working with no issues detected. |
|  **Degraded** 3                                                      | The element detected one or more non-critical issues.       |
|  **Error** 6                                                                  | The element detected one or more critical issues.           |
|  **Non-Recoverable Error** 7  | The element detected one or more non-recoverable issues.    |
|  **Not Installed** 0xD009                             | The element is not present.                                 |
|  **Not Available** 0xD00A                             | The element is present but has problems.                    |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                        |
|  **Not Reported** 0xD00C                                 |                                                                        |



 

 

**FanOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

**Starting in Windows 10:** An array containing the operational status of each fan of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
|  **Unknown** 0                                                          |                                                                        |
|  **OK** 2                                                                                                   | The element is present and working with no issues detected. |
|  **Degraded** 3                                                      | The element detected one or more non-critical issues.       |
|  **Error** 6                                                                  | The element detected one or more critical issues.           |
|  **Non-Recoverable Error** 7  | The element detected one or more non-recoverable issues.    |
|  **Not Installed** 0xD009                             | The element is not present.                                 |
|  **Not Available** 0xD00A                             | The element is present but has problems.                    |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                        |
|  **Not Reported** 0xD00C                                 |                                                                        |



 

 

**HealthStatus**
   

Data type: **UInt16**
 

Access type: Read-only
 

**Starting in Windows 10:** Denotes the current health status of the enclosure.

 

**Healthy** (0)
 

**Warning** (1)
 

**Unhealthy** (2)
 

**Unknown** (5)
 

 

**IOControllerOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

**Starting in Windows 10:** An array containing the operational status of each controller of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
|  **Unknown** 0                                                          |                                                                        |
|  **OK** 2                                                                                                   | The element is present and working with no issues detected. |
|  **Degraded** 3                                                      | The element detected one or more non-critical issues.       |
|  **Error** 6                                                                  | The element detected one or more critical issues.           |
|  **Non-Recoverable Error** 7  | The element detected one or more non-recoverable issues.    |
|  **Not Installed** 0xD009                             | The element is not present.                                 |
|  **Not Available** 0xD00A                             | The element is present but has problems.                    |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                        |
|  **Not Reported** 0xD00C                                 |                                                                        |



 

 

**PowerSupplyOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

**Starting in Windows 10:** An array containing the operational status of each power supply of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
|  **Unknown** 0                                                          |                                                                        |
|  **OK** 2                                                                                                   | The element is present and working with no issues detected. |
|  **Degraded** 3                                                      | The element detected one or more non-critical issues.       |
|  **Error** 6                                                                  | The element detected one or more critical issues.           |
|  **Non-Recoverable Error** 7  | The element detected one or more non-recoverable issues.    |
|  **Not Installed** 0xD009                             | The element is not present.                                 |
|  **Not Available** 0xD00A                             | The element is present but has problems.                    |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                        |
|  **Not Reported** 0xD00C                                 |                                                                        |



 

 

**StorageEnclosure**
   

Data type: **[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers)
 

 

**StorageNode**
   

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
 

Access type: Read-only
 

Qualifiers: [**Key**](/windows/win32/wmisdk/standard-qualifiers)
 

 

**TemperatureSensorOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

**Starting in Windows 10:** An array containing the operational status of each temperature sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
|  **Unknown** 0                                                          |                                                                        |
|  **OK** 2                                                                                                   | The element is present and working with no issues detected. |
|  **Degraded** 3                                                      | The element detected one or more non-critical issues.       |
|  **Error** 6                                                                  | The element detected one or more critical issues.           |
|  **Non-Recoverable Error** 7  | The element detected one or more non-recoverable issues.    |
|  **Not Installed** 0xD009                             | The element is not present.                                 |
|  **Not Available** 0xD00A                             | The element is present but has problems.                    |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                        |
|  **Not Reported** 0xD00C                                 |                                                                        |



 

 

**VoltageSensorOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

**Starting in Windows 10:** An array containing the operational status of each voltage sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
|  **Unknown** 0                                                          |                                                                        |
|  **OK** 2                                                                                                   | The element is present and working with no issues detected. |
|  **Degraded** 3                                                      | The element detected one or more non-critical issues.       |
|  **Error** 6                                                                  | The element detected one or more critical issues.           |
|  **Non-Recoverable Error** 7  | The element detected one or more non-recoverable issues.    |
|  **Not Installed** 0xD009                             | The element is not present.                                 |
|  **Not Available** 0xD00A                             | The element is present but has problems.                    |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                        |
|  **Not Reported** 0xD00C                                 |                                                                        |



 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageNode**](msft-storagenode.md)
 

[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)
 

 

