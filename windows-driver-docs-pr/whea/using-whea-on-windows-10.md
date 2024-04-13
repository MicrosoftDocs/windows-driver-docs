---
title: Using WHEA on Windows 10
description: Describes how to report a WHEA error on Windows 10
keywords:
- Windows Hardware Error Architecture WDK , Windows 10 changes
ms.date: 03/03/2023
---

# Using WHEA on Windows 10

In Windows 10, version 2004, Windows Hardware Error Architecture (WHEA) includes a new interface (v2).  This page describes how to register as an error source and report errors.

## Adding an Error Source

To register with WHEA as an error source using WHEA v2, the driver should do the following:

1. Specify a configuration for your device driver by instantiating a [**WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-whea_error_source_configuration_device_driver) structure, providing pointers to [*WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-_whea_error_source_initialize_device_driver) and [*WHEA_ERROR_SOURCE_UNINITIALIZE_DEVICE_DRIVER*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-_whea_error_source_uninitialize_device_driver) event callback functions.
2. Call [**WheaAddErrorSourceDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheaadderrorsourcedevicedriver), providing the configuration structure.  Typically, the driver calls this routine from *DriverEntry*.

    To remove an error source at a later time, call [**WheaRemoveErrorSourceDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-whearemoveerrorsourcedevicedriver).

3. WHEA calls the the driver's [*WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-_whea_error_source_initialize_device_driver) event callback function when the error source is ready to report errors. The driver receives an *ErrorSourceId* as a parameter to the callback.

## Reporting an Error

To report an error, perform the following steps in sequence at the same time:

1. Call [**WheaCreateHwErrorReportDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheacreatehwerrorreportdevicedriver), providing the *ErrorSourceId* and, optionally, a *DeviceObject* for the driver.  The routine returns a handle to the in progress error.

2. To add data to the error, call [**WheaAddHwErrorReportSectionDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheaaddhwerrorreportsectiondevicedriver), providing the error handle.  This function adds a single section to the error report and configures a driver-supplied data buffer.  The driver can call this routine up to **MaxSectionsPerReport** times as specified in [**WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-whea_error_source_configuration_device_driver).

    Optionally, the driver can call [**WheaHwErrorReportSetSeverityDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportsetseveritydevicedriver) to set the error severity of the packet and sections. Also see [**WheaHwErrorReportSetSectionNameDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportsetsectionnamedevicedriver), which is a helper function for updating the FRUText field of the [**WHEA_ERROR_RECORD_SECTION_DESCRIPTOR**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-_whea_error_record_section_descriptor) structure.

3. Copy error data into the buffer set.

4. Call [**WheaHwErrorReportSubmitDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportsubmitdevicedriver), again providing the error handle. After this call, buffers in the buffer sets are unavailable and the handle is invalid.

5. If an error occurs or the error is no longer valid, the driver can optionally call [**WheaHwErrorReportAbandonDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportabandondevicedriver). In this case, no report is submitted to WHEA.

The driver must call either [**WheaHwErrorReportSubmitDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportsubmitdevicedriver) or [**WheaHwErrorReportAbandonDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportabandondevicedriver) on every handle created by [**WheaCreateHwErrorReportDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheacreatehwerrorreportdevicedriver). Otherwise, [**WheaRemoveErrorSourceDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-whearemoveerrorsourcedevicedriver) might return STATUS_RESOURCE_IN_USE.
