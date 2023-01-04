---
title: MSFT\_StorageEnclosure class
description: Represents a storage enclosure.
ms.assetid: 617DA7A7-E594-42C0-AD69-F95E55BC0D4B
keywords:
- MSFT_StorageEnclosure class Windows Storage Management API
- MSFT_StorageEnclosure class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageEnclosure
- MSFT_StorageEnclosure.DeviceId
- MSFT_StorageEnclosure.FriendlyName
- MSFT_StorageEnclosure.FirmwareVersion
- MSFT_StorageEnclosure.NumberOfSlots
- MSFT_StorageEnclosure.PowerSupplyOperationalStatus
- MSFT_StorageEnclosure.FanOperationalStatus
- MSFT_StorageEnclosure.TemperatureSensorOperationalStatus
- MSFT_StorageEnclosure.VoltageSensorOperationalStatus
- MSFT_StorageEnclosure.CurrentSensorOperationalStatus
- MSFT_StorageEnclosure.IOControllerOperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageEnclosure class

Represents a storage enclosure.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageEnclosure : MSFT_StorageFaultDomain
{
  String DeviceId;
  String FriendlyName;
  String FirmwareVersion;
  UInt32 NumberOfSlots;
  UInt16 PowerSupplyOperationalStatus[];
  UInt16 FanOperationalStatus[];
  UInt16 TemperatureSensorOperationalStatus[];
  UInt16 VoltageSensorOperationalStatus[];
  UInt16 CurrentSensorOperationalStatus[];
  UInt16 IOControllerOperationalStatus[];
};
```

## Members

The **MSFT\_StorageEnclosure** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageEnclosure** class has these methods.



| Method                                                           | Description                                                                                  |
|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**GetVendorData**](msft-storageenclosure-getvendordata.md)     | Returns the vendor-specific data from an enclosure.                               |
| [**IdentifyElement**](msft-storageenclosure-identifyelement.md) | Permits a user to perform identification tasks on the enclosure and its elements. |



 

### Properties

The **MSFT\_StorageEnclosure** class has these properties.

 

**CurrentSensorOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array containing the operational status of each current sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
|  **Unknown** 0                                                          | The operational status of the element is unknown.                 |
|  **OK** 2                                                                                                   | The element is present and working, with no issues detected.      |
|  **Degraded** 3                                                      | The element detects a non-critical issue.                         |
|  **Error** 6                                                                  | The element detects a critical issue.                             |
|  **Non-Recoverable Error** 7  | The element detects a non-recoverable issue.                      |
|  **Not Installed** 0xD009                             | The element is not present.                                       |
|  **Not Available** 0xD00A                             | The element is present but has problems that make it unavailable. |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                              |
|  **Not Supported** 0xD00C                             | The element is not supported.                                     |



 

 

**DeviceId**
   

Data type: **String**
 

Access type: Read-only
 

An address or other identifier that uniquely names the enclosure.

 

**FanOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array containing the operational status of each fan of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
|  **Unknown** 0                                                          | The operational status of the element is unknown.                 |
|  **OK** 2                                                                                                   | The element is present and working, with no issues detected.      |
|  **Degraded** 3                                                      | The element detects a non-critical issue.                         |
|  **Error** 6                                                                  | The element detects a critical issue.                             |
|  **Non-Recoverable Error** 7  | The element detects a non-recoverable issue.                      |
|  **Not Installed** 0xD009                             | The element is not present.                                       |
|  **Not Available** 0xD00A                             | The element is present but has problems that make it unavailable. |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                              |
|  **Not Supported** 0xD00C                             | The element is not supported.                                     |



 

 

**FirmwareVersion**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A string representation of the enclosure's firmware version.

 

**FriendlyName**
   

Data type: **String**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

A user-friendly string representing the name of the enclosure.

 

**IOControllerOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array containing the operational status of each IO controller module of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
|  **Unknown** 0                                                          | The operational status of the element is unknown.                 |
|  **OK** 2                                                                                                   | The element is present and working, with no issues detected.      |
|  **Degraded** 3                                                      | The element detects a non-critical issue.                         |
|  **Error** 6                                                                  | The element detects a critical issue.                             |
|  **Non-Recoverable Error** 7  | The element detects a non-recoverable issue.                      |
|  **Not Installed** 0xD009                             | The element is not present.                                       |
|  **Not Available** 0xD00A                             | The element is present but has problems that make it unavailable. |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                              |
|  **Not Supported** 0xD00C                             | The element is not supported.                                     |



 

 

**NumberOfSlots**
   

Data type: **UInt32**
 

Access type: Read-only
 

Qualifiers: [**Required**](/windows/win32/wmisdk/standard-qualifiers)
 

Number of slots hosted within the enclosure.

 

**PowerSupplyOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array containing the operational status of each power supply module of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
|  **Unknown** 0                                                          | The operational status of the element is unknown.                 |
|  **OK** 2                                                                                                   | The element is present and working, with no issues detected.      |
|  **Degraded** 3                                                      | The element detects a non-critical issue.                         |
|  **Error** 6                                                                  | The element detects a critical issue.                             |
|  **Non-Recoverable Error** 7  | The element detects a non-recoverable issue.                      |
|  **Not Installed** 0xD009                             | The element is not present.                                       |
|  **Not Available** 0xD00A                             | The element is present but has problems that make it unavailable. |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                              |
|  **Not Supported** 0xD00C                             | The element is not supported.                                     |



 

 

**TemperatureSensorOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array containing the operational status of each temperature sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
|  **Unknown** 0                                                          | The operational status of the element is unknown.                 |
|  **OK** 2                                                                                                   | The element is present and working, with no issues detected.      |
|  **Degraded** 3                                                      | The element detects a non-critical issue.                         |
|  **Error** 6                                                                  | The element detects a critical issue.                             |
|  **Non-Recoverable Error** 7  | The element detects a non-recoverable issue.                      |
|  **Not Installed** 0xD009                             | The element is not present.                                       |
|  **Not Available** 0xD00A                             | The element is present but has problems that make it unavailable. |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                              |
|  **Not Supported** 0xD00C                             | The element is not supported.                                     |



 

 

**VoltageSensorOperationalStatus**
   

Data type: **UInt16** array
 

Access type: Read-only
 

An array containing the operational status of each voltage sensor of the enclosure.



| Value                                                                                                                                                                                                                                                                               | Meaning                                                                      |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
|  **Unknown** 0                                                          | The operational status of the element is unknown.                 |
|  **OK** 2                                                                                                   | The element is present and working, with no issues detected.      |
|  **Degraded** 3                                                      | The element detects a non-critical issue.                         |
|  **Error** 6                                                                  | The element detects a critical issue.                             |
|  **Non-Recoverable Error** 7  | The element detects a non-recoverable issue.                      |
|  **Not Installed** 0xD009                             | The element is not present.                                       |
|  **Not Available** 0xD00A                             | The element is present but has problems that make it unavailable. |
|  **No Access Allowed** 0xD00B             | No access is allowed to the element.                              |
|  **Not Supported** 0xD00C                             | The element is not supported.                                     |



 

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8.1 \[desktop apps only\]                                              |
| Minimum supported server | Windows Server 2012 R2 \[desktop apps only\]                                   |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)
 

 

