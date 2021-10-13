---
title: Power-Down and Removal Sequence for a Bus Driver
description: Power-Down and Removal Sequence for a Bus Driver
ms.date: 03/28/2019
ms.localizationpriority: medium
---

# Power-Down and Removal Sequence for a Bus Driver


The following figure shows the order in which the framework calls a KMDF bus driver's event callback functions when powering down and removing a device that is connected to the bus. The sequence starts at the top of the figure with an operational device that is in the working power state (D0):

![power-down and removal sequence for a bus driver.](images/pdo-powerdown.png)

The framework does not delete the PDO until the device is physically removed from the system. For example, if a user disables the device in Device Manager or stops it in the Safely Remove Hardware utility but does not physically remove the device, the framework retains the PDO. If the device is later re-enabled, the framework uses the same PDO and begins the startup sequence by calling the [*EvtDevicePrepareHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_prepare_hardware) callback, as shown in [Power-Up Sequence for a Physical Device Object](power-up-sequence-for-a-bus-driver.md).

**Note**: Typically, the framework calls a bus driver's [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback function after it has called the [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) function for all child devices that the driver enumerates.  In the event of the parent encountering a device power-up or power-down failure, the framework might call the driver's [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) before it has called the [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) functions for all child devices.  Consider calling [WdfDeviceInitSetReleaseHardwareOrderOnFailure](/windows-hardware/drivers/ddi/wdfdevice/nf-wdfdevice-wdfdeviceinitsetreleasehardwareorderonfailure) to ensure that the framework calls the bus driver's [*EvtDeviceReleaseHardware*](/windows-hardware/drivers/ddi/wdfdevice/nc-wdfdevice-evt_wdf_device_release_hardware) callback only after all child devices have been removed.



