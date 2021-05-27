---
title: Reporting Device Failures
description: Reporting Device Failures
keywords:
- PnP WDK KMDF , device failures
- Plug and Play WDK KMDF , device failures
- device failures WDK KMDF
- failed devices WDK KMDF
- WdfDeviceFailedAttemptRestart
- WdfDeviceFailedNoRestart
- reporting device failures WDK KMDF
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Reporting Device Failures


There are three ways to report device failures:

-  When returning from [device object callback functions](/windows-hardware/drivers/ddi/wdfdevice/#device-callbacks), the driver can supply a return value for which [NT\_SUCCESS](../kernel/using-ntstatus-values.md)(*status*) equals **FALSE**.

-  The driver can call [**WdfDeviceSetFailed**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetfailed).

-  When returning from its [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback routine, a function driver can supply a return value for which [NT\_SUCCESS](../kernel/using-ntstatus-values.md)(*status*) equals **FALSE**. If a driver that is installed as a [filter]( ../install/installing-a-filter-driver.md) fails [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add), the operating system skips the filter device object and does not indicate a PnP error.

Each of the above methods results in the framework effectively removing the device. If the device's drivers are not supporting other devices on the system, the I/O manager unloads the drivers.

If a driver's device object callback function returns a value for which NT\_SUCCESS(*status*) equals **FALSE**, the framework notifies the PnP manager, which then attempts to restart the device by requesting the bus driver to reenumerate its devices. Your driver will be reloaded, if it was unloaded.

If your driver calls [**WdfDeviceSetFailed**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetfailed), it supplies an input argument that determines whether the device will be restarted. The argument values are **WdfDeviceFailedAttemptRestart** and **WdfDeviceFailedNoRestart**.

**UMDF** Before UMDF 2.15 a UMDF driver must set this value to **WdfDeviceFailedNoRestart**. Starting in UMDF version 2.15, a UMDF driver can request that the underlying bus driver re-enumerate it by calling [**WdfDeviceSetFailed**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetfailed) with *FailedAction* set to **WdfDeviceFailedAttemptRestart**. For more information, see [**WdfDeviceSetFailed**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetfailed). 

For more information about these argument values, see [**WDF\_DEVICE\_FAILED\_ACTION**](/windows-hardware/drivers/ddi/wdfdevice/ne-wdfdevice-_wdf_device_failed_action).
Before a driver's device object callback function returns with a value for which NT\_SUCCESS(*status*) equals **FALSE**, the callback function can prevent restarts by calling [**WdfDeviceSetFailed**](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdevicesetfailed) with an input argument of **WdfDeviceFailedNoRestart**. Otherwise, these callback functions do not have to call **WdfDeviceSetFailed**.

If, within a short period of time, several consecutive restart attempts fail (because the restarted driver again reports an error), the framework stops trying to restart the device.

If a bus driver's [*EvtDeviceD0Entry*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_d0_entry) function returns a value for which NT\_SUCCESS(*status*) equals **FALSE**, the framework might still call the *EvtDeviceD0Entry* functions of drivers associated with the bus driver's child devices.

 

