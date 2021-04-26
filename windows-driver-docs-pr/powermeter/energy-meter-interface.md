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

On-board energy meters periodically measure voltage and current on a rail, calculate a power product, and integrate the total energy consumed over time. These meters are distinct from the existing [Power Meter Interface](./power-meter-interface.md) concept because power meters have a global averaging interval. Energy meters allow multiple consumers to determine average power over different intervals according to their needs by returning total energy consumption up to the present.  

The EMI interface provides the conduit for energy data to be consumed by interested client applications and services.  Clients calculate energy consumed since their last query by subtracting the previous values from the latest values, and optionally convert to average power by simple division. 

## Discovering devices that implement EMI

Clients discover devices that support the EMI through calls to [SetupDiEnumDeviceInterfaces](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces) and [SetupDiGetDeviceInterfaceDetail](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacedetaila). One instance of an EMI device interface is created for each energy metering device that is EMI-compliant and is present in the system. 

The GUID for the EMI device interface is **{45BD8344-7ED6-49cf-A440-C276C933B053}**, as defined in emi.h. Code can alternatively use GUID_DEVICE_ENERGY_METER to specify this GUID. 

## Using the EMI interface

Client code typically interacts with the EMI using the following process:

1. Call [IOCTL_EMI_GET_VERSION](/windows/win32/api/emi/ni-emi-ioctl_emi_get_version) and verify the EMI interface version supported by the device in the returned [EMI_VERSION](/windows/win32/api/emi/ns-emi-emi_version) value. In Windows 10, devices can support EMI_VERSION_V1. In Windows 10 Version 1809, devices can also support EMI_VERSION_V2. Future operating system releases may introduce later versions. 

2. Call IOCTL_EMI_GET_METADATA_SIZE to get size of the EMI metadata. 

3. Allocate a buffer of the required EMI metadata size and call [IOCTL_EMI_GET_METADATA](/windows/win32/api/emi/ni-emi-ioctl_emi_get_metadata). Verify that the returned EMI_MEASUREMENT_UNIT is EmiMeasurementUnitPicowattHours. Releases after Windows 10 may define additional unit types. 

4. To measure total energy consumption, call [IOCTL_EMI_GET_MEASUREMENT](/windows/win32/api/emi/ni-emi-ioctl_emi_get_measurement). The AbsoluteEnergy value in the returned [EMI_CHANNEL_MEASUREMENT_DATA structure](/windows/win32/api/emi/ns-emi-emi_channel_measurement_data) is the total accumulated energy in picowatt-hours with some arbitrary zero-point. In general, you need to compare samples at two different times and subtract the energy values for energy consumption over that interval. 

5. To measure average power consumption, call [IOCTL_EMI_GET_MEASUREMENT](/windows/win32/api/emi/ni-emi-ioctl_emi_get_measurement) at the beginning and end of the desired interval. Subtract the AbsoluteEnergy and AbsoluteTime values of the [EMI_CHANNEL_MEASUREMENT_DATA structure](/windows/win32/api/emi/ns-emi-emi_channel_measurement_data) returned by the latter sample from those of the earlier sample.

For more information see these topics.

[EMI IOCTLs](/previous-versions/windows/hardware/drivers/dn957425(v=vs.85)) - 
 This section describes the I/O control codes (IOCTLs) that are supported by the Energy Measurement Interface (EMI).
 
[EMI Enumerations and Structures](/previous-versions/windows/hardware/drivers/dn957424(v=vs.85)) -
 This section describes the enumerations and structures that are supported by the Energy Measurement Interface (EMI).
 


