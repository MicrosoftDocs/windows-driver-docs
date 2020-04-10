---
title: Using WHEA on Windows 10
description: Describes how to report a WHEA error on Windows 10
ms.assetid: ace3230c-3e41-4290-a1fe-74a6cfc1eb0b
keywords:
- Windows Hardware Error Architecture WDK , Windows 10 changes
ms.date: 04/28/2020
ms.localizationpriority: medium
---

# Using WHEA on Windows 10

In Windows 10, version 2004,  Windows Hardware Error Architecture (WHEA) includes a new interface (v2).  This page describes how to register as an error source and report errors.

## Registering as an Error Source

To register with WHEA as an error source on Windows 10, the driver should do the following:

1. Specify a configuration for your device driver by instantiating a [**WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-whea_error_source_configuration_device_driver) structure.
2. Call [**WheaAddErrorSourceDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheaadderrorsourcedevicedriver), providing the configuration structure.  To remove an error source at a later time, call [**WheaRemoveErrorSourceDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-whearemoveerrorsourcedevicedriver).
3. WHEA calls the the driver's [*WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-_whea_error_source_initialize_device_driver.md) event callback function when the error source is ready to report errors. The driver receives an *ErrorSourceId* as a parameter to the callback.

## Reporting an Error

After WHEA calls the initialize callback, follow these steps to report an error:

1. Call [**WheaCreateHwErrorReportDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheacreatehwerrorreportdevicedriver).  Provide the *ErrorSourceId* and, optionally, a *DeviceObject* for your driver.  The routine returns a handle to the in progress error.

2. To add data to the error, call [**WheaAddHwErrorReportSectionDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheaaddhwerrorreportsectiondevicedriver), providing the error handle.  This function adds a single section to the error report and configures a driver-supplied data buffer.  The driver can call this routine up to **MaxSectionsPerReport** times as specified in [**WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-whea_error_source_configuration_device_driver).

3. The driver calls [**WheaHwErrorReportSubmitDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportsubmitdevicedriver), again providing the error handle. After this call, buffers in the buffer sets are unavailable and the handle is invalid.

4. If an error has occurred or the error is no longer valid, the driver can optionally call [**WheaHwErrorReportAbandonDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportabandondevicedriver).  No report is submitted to WHEA.

Reporting an error should be an atomic operation. Create and submit errors all at once.

The driver must call either [**WheaHwErrorReportSubmitDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportsubmitdevicedriver) or [**WheaHwErrorReportAbandonDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportabandondevicedriver) on every handle created by [**WheaCreateHwErrorReportDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheacreatehwerrorreportdevicedriver). Failing to do so leaks resources. Driver error sources keep track of the number of open handles and will fail to remove if any handle is still open.

To set the error severity of the packet and sections, the driver can call [**WheaHwErrorReportSetSeverityDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportsetseveritydevicedriver).

[**WheaHwErrorReportSetSectionNameDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportsetsectionnamedevicedriver) is a helper function for updating the FRUText without having to do it manually.
