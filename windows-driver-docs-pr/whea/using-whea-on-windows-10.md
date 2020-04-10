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

To get set up to report WHEA errors on Windows 10, the driver should do the following:

1. Start by specifying a configuration for your device driver using [**WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-whea_error_source_configuration_device_driver).
2. Call [**WheaAddErrorSourceDeviceDriver**](), providing the configuration structure.  If you ever need to remove it, call [**WheaRemoveErrorSourceDeviceDriver**]().
3. WHEA calls the the driver's [*WHEA_ERROR_SOURCE_INITIALIZE_DEVICE_DRIVER*](/windows-hardware/drivers/ddi/ntddk/nc-ntddk-_whea_error_source_initialize_device_driver.md) event callback function when your error source is ready to be used for reporting errors. WHEA provides an *ErrorSourceId* value as a parameter to the callback.

## Reporting an Error

Reporting an error involves the following stages:

* Prepare an error packet.
* Add data to the error packet.
* Submit the error packet.

> [!NOTE]
> Reporting an error should be an atomic operation. Don't prepare an error on driver entry and hold onto it until an error occurs. Instead, create and submit errors all at once.

To report an error, use the following procedure:

1. Call **WheaCreateHwErrorReportDeviceDriver**.  Provide the *ErrorSourceId* and, optionally, a *DeviceObject* for your driver.  The routine returns a handle to the in progress error.

2. To add data to the error, call **WheaAddHwErrorReportSectionDeviceDriver**, providing the error handle.  This function adds a single section to the error report and configures a driver-supplied data buffer.  The driver can call this routine up to **MaxSectionsPerReport** times as specified in [**WHEA_ERROR_SOURCE_CONFIGURATION_DEVICE_DRIVER**](/windows-hardware/drivers/ddi/ntddk/ns-ntddk-whea_error_source_configuration_device_driver).

3. The driver calls **WheaHwErrorReportSubmitDeviceDriver**, again providing the error handle. After this call, buffers in the buffer sets are unavailable and the handle is invalid.

4. If an error has occurred or the error is no longer valid, the driver can optionally call **WheaHwErrorReportAbandonDeviceDriver**.  No report is submitted to WHEA.

> [!NOTE]
> The driver must call either **WheaHwErrorReportSubmitDeviceDriver** or **WheaHwErrorReportAbandonDeviceDriver** on every handle created by **WheaCreateHwErrorReportDeviceDriver**. Failing to do so leaks resources. Driver error sources keep track of the number of open handles and will fail to remove if any handle is still open.

To set the error severity of the packet and sections, the driver can call [**WheaHwErrorReportSetSeverityDeviceDriver**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-wheahwerrorreportsetseveritydevicedriver).

**WheaHwErrorReportSetSectionNameDeviceDriver** is a helper function for updating the FRUText without having to do it manually.
