---
title: Energy Meter Interface
description: Energy Meter Interface
keywords:
- Energy Metering and Budgeting WDK , interface
- Energy Meter Interface WDK
- PMI WDK Energy Meter
ms.date: 11/17/2017
ms.localizationpriority: medium
---

# Energy Meter Interface

Starting in Windows 10, drivers  can implement the Energy Metering Interface (EMI) to expose energy consumption data to clients. This interface consists of a set of standardized IOCTLs for clients to get energy data as well as data about the metering hardware and the hardware being metered. 

On-board energy meters periodically measure voltage and current on a rail, calculate a power product, and integrate the total energy consumed over time. These meters are distinct from the existing [Power Meter Interface](https://docs.microsoft.com/windows-hardware/drivers/powermeter/power-meter-interface) concept because power meters have a global averaging interval. Energy meters allow multiple consumers to determine average power over different intervals according to their needs by returning total energy consumption up to the present.  

The EMI interface provides the conduit for energy data to be consumed by interested client applications and services.  Clients calculate energy consumed since their last query by subtracting the previous values from the latest values, and optionally convert to average power by simple division. 

## Discovering devices that implement EMI

Clients discover devices that support the EMI through calls to [SetupDiEnumDeviceInterfaces](https://msdn.microsoft.com/library/windows/hardware/ff551015.aspx) and [SetupDiGetDeviceInterfaceDetail](https://msdn.microsoft.com/library/windows/hardware/ff551120.aspx). One instance of an EMI device interface is created for each energy metering device that is EMI-compliant and is present in the system. 

The GUID for the EMI device interface is **{45BD8344-7ED6-49cf-A440-C276C933B053}**, as defined in emi.h. Code can alternatively use GUID_DEVICE_ENERGY_METER to specify this GUID. 

## Using the EMI interface

Client code typically interacts with the EMI using the following process:

1. Call [IOCTL_EMI_GET_VERSION](https://msdn.microsoft.com/library/windows/hardware/dn957440.aspx) and verify the EMI interface version supported by the device in the returned [EMI_VERSION](https://msdn.microsoft.com/library/windows/hardware/dn957430.aspx) value. In Windows 10, devices can support EMI_VERSION_V1. In Windows 10 Version 1809, devices can also support EMI_VERSION_V2. Future operating system releases may introduce later versions. 

2. Call IOCTL_EMI_GET_METADATA_SIZE to get size of the EMI metadata. 

3. Allocate a buffer of the required EMI metadata size and call [IOCTL_EMI_GET_METADATA](https://msdn.microsoft.com/library/windows/hardware/dn957436.aspx). Verify that the returned EMI_MEASUREMENT_UNIT is EmiMeasurementUnitPicowattHours. Releases after Windows 10 may define additional unit types. 

4. To measure total energy consumption, call [IOCTL_EMI_GET_MEASUREMENT](https://msdn.microsoft.com/library/windows/hardware/dn957434.aspx). The AbsoluteEnergy value in the returned [EMI_MEASUREMENT_DATA](https://msdn.microsoft.com/library/windows/hardware/dn957426.aspx) is the total accumulated energy in picowatt-hours with some arbitrary zero-point. In general, you need to compare samples at two different times and subtract the energy values for energy consumption over that interval. 

5. To measure average power consumption, call [IOCTL_EMI_GET_MEASUREMENT](https://msdn.microsoft.com/library/windows/hardware/dn957434.aspx) at the beginning and end of the desired interval. Subtract the AbsoluteEnergy and AbsoluteTime values of the [EMI_MEASUREMENT_DATA](https://msdn.microsoft.com/library/windows/hardware/dn957426.aspx) returned by the latter sample from those of the earlier sample. 

For more information see these topics.

[EMI IOCTLs](https://msdn.microsoft.com/library/windows/hardware/dn957425.aspx) - 
 This section describes the I/O control codes (IOCTLs) that are supported by the Energy Measurement Interface (EMI).
 
[EMI Enumerations and Structures](https://msdn.microsoft.com/library/windows/hardware/dn957424.aspx) -
 This section describes the enumerations and structures that are supported by the Energy Measurement Interface (EMI).
 


 




