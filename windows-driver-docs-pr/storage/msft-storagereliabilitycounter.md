---
title: MSFT\_StorageReliabilityCounter class
description: The MSFT\_StorageReliabilityCounter class provides reliability statistics or counters reported by a storage device.
ms.assetid: A64126B3-0399-47A3-95E3-0755EE34C2C4
keywords:
- MSFT_StorageReliabilityCounter class Windows Storage Management API
- MSFT_StorageReliabilityCounter class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageReliabilityCounter
- MSFT_StorageReliabilityCounter.DeviceId
- MSFT_StorageReliabilityCounter.Temperature
- MSFT_StorageReliabilityCounter.TemperatureMax
- MSFT_StorageReliabilityCounter.ReadErrorsTotal
- MSFT_StorageReliabilityCounter.ReadErrorsCorrected
- MSFT_StorageReliabilityCounter.ReadErrorsUncorrected
- MSFT_StorageReliabilityCounter.WriteErrorsTotal
- MSFT_StorageReliabilityCounter.WriteErrorsCorrected
- MSFT_StorageReliabilityCounter.WriteErrorsUncorrected
- MSFT_StorageReliabilityCounter.ManufactureDate
- MSFT_StorageReliabilityCounter.StartStopCycleCount
- MSFT_StorageReliabilityCounter.StartStopCycleCountMax
- MSFT_StorageReliabilityCounter.LoadUnloadCycleCount
- MSFT_StorageReliabilityCounter.LoadUnloadCycleCountMax
- MSFT_StorageReliabilityCounter.Wear
- MSFT_StorageReliabilityCounter.PowerOnHours
- MSFT_StorageReliabilityCounter.ReadLatencyMax
- MSFT_StorageReliabilityCounter.WriteLatencyMax
- MSFT_StorageReliabilityCounter.FlushLatencyMax
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StorageReliabilityCounter class

The **MSFT\_StorageReliabilityCounter** class provides reliability statistics or counters reported by a storage device.

This information is dynamic and should be obtained from the storage device whenever needed.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageReliabilityCounter : MSFT_StorageObject
{
  String DeviceId;
  UInt8  Temperature;
  UInt8  TemperatureMax;
  UInt64 ReadErrorsTotal;
  UInt64 ReadErrorsCorrected;
  UInt64 ReadErrorsUncorrected;
  UInt64 WriteErrorsTotal;
  UInt64 WriteErrorsCorrected;
  UInt64 WriteErrorsUncorrected;
  String ManufactureDate;
  UInt32 StartStopCycleCount;
  UInt32 StartStopCycleCountMax;
  UInt32 LoadUnloadCycleCount;
  UInt32 LoadUnloadCycleCountMax;
  UInt8  Wear;
  UInt16 PowerOnHours;
  UInt64 ReadLatencyMax;
  UInt64 WriteLatencyMax;
  UInt64 FlushLatencyMax;
};
```

## Members

The **MSFT\_StorageReliabilityCounter** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageReliabilityCounter** class has these methods.



| Method                                                | Description                           |
|:------------------------------------------------------|:--------------------------------------|
| [**Reset**](msft-storagereliabilitycounter-reset.md) | Resets reliability values. |



 

### Properties

The **MSFT\_StorageReliabilityCounter** class has these properties.

 

**DeviceId**
   

Data type: **String**
 

Access type: Read-only
 

An identifier that uniquely names the associated storage device. When associated with an [**MSFT\_PhysicalDisk**](msft-physicaldisk.md), it will be the same as its **DeviceId** member. When associated with an [**MSFT\_Disk**](msft-disk.md), it will be the same as its **Number** field.

 

**FlushLatencyMax**
   

Data type: **UInt64**
 

Access type: Read-only
 

Maximum latency experienced by a flush request, in milliseconds. A value greater than 10 seconds may indicate a problem with the disk or the HBA.

 

**LoadUnloadCycleCount**
   

Data type: **UInt32**
 

Access type: Read-only
 

The number of load-unload cycles that were performed by the storage device.

 

**LoadUnloadCycleCountMax**
   

Data type: **UInt32**
 

Access type: Read-only
 

The maximum number of load-unload cycles that can be performed by the storage device in normal operation.

 

**ManufactureDate**
   

Data type: **String**
 

Access type: Read-only
 

The year and week when the storage device was manufactured.

 

**PowerOnHours**
   

Data type: **UInt16**
 

Access type: Read-only
 

The number of hours that the storage device has been powered on since it was manufactured.

 

**ReadErrorsCorrected**
   

Data type: **UInt64**
 

Access type: Read-only
 

The number of read errors that were corrected by the storage device.

 

**ReadErrorsTotal**
   

Data type: **UInt64**
 

Access type: Read-only
 

The total number of read errors that were encountered by the storage device.

 

**ReadErrorsUncorrected**
   

Data type: **UInt64**
 

Access type: Read-only
 

The number of read errors that were not corrected by the storage device.

 

**ReadLatencyMax**
   

Data type: **UInt64**
 

Access type: Read-only
 

Maximum latency experienced by a read request, in milliseconds. A value greater than 10 seconds may indicate a problem with the disk or the HBA.

 

**StartStopCycleCount**
   

Data type: **UInt32**
 

Access type: Read-only
 

The number of start-stop cycles that were performed by the storage device.

 

**StartStopCycleCountMax**
   

Data type: **UInt32**
 

Access type: Read-only
 

The maximum number of start-stop cycles that can be performed by the storage device in normal operation.

 

**Temperature**
   

Data type: **UInt8**
 

Access type: Read-only
 

The current temperature of the storage device in degrees Celsius.

 

**TemperatureMax**
   

Data type: **UInt8**
 

Access type: Read-only
 

The maximum temperature in degrees Celsius at which the storage device is capable of normal operation.

 

**Wear**
   

Data type: **UInt8**
 

Access type: Read-only
 

The storage device wear indicator, in percentage. At 100 percent, the estimated wear limit will have been reached.

 

**WriteErrorsCorrected**
   

Data type: **UInt64**
 

Access type: Read-only
 

The number of write errors that were corrected by the storage device.

 

**WriteErrorsTotal**
   

Data type: **UInt64**
 

Access type: Read-only
 

The total number of write errors that were encountered by the storage device.

 

**WriteErrorsUncorrected**
   

Data type: **UInt64**
 

Access type: Read-only
 

The number of write errors that were not corrected by the storage device.

 

**WriteLatencyMax**
   

Data type: **UInt64**
 

Access type: Read-only
 

Maximum latency experienced by a write request, in milliseconds. A value greater than 10 seconds may indicate a problem with the disk or the HBA.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 \[desktop apps only\]                                                |
| Minimum supported server | Windows Server 2012 \[desktop apps only\]                                      |
| Namespace                | Root\\Microsoft\\Windows\\Storage                                              |
| MOF                      |  Storagewmi.mof  |



## See also

 

[**MSFT\_StorageObject**](msft-storageobject.md)
 

[**MSFT\_DiskToStorageReliabilityCounter**](msft-disktostoragereliabilitycounter.md)
 

[**MSFT\_PhysicalDiskToStorageReliabilityCounter**](msft-physicaldisktostoragereliabilitycounter.md)
 

 

 





