---
title: Steps in Porting
description: Steps in Porting
ms.date: 04/20/2017
---

# Steps in Porting


Depending on the type of driver, porting involves performing the following steps:

1.  [Port the DriverEntry routine](porting-driver-entry.md) and add code to create the WDFDRIVER object.
2.  [Port the AddDevice routine](porting-adddevice-to-evtdriverdeviceadd.md) to an [*EvtDriverDeviceAdd*](/windows-hardware/drivers/ddi/wdfdriver/nc-wdfdriver-evt_wdf_driver_device_add) callback, and add code to create the WDFDEVICE objects.
3.  Add support for [interrupts](porting-interrupt-functionality.md) if the driver supports interrupt handling.

At this point, you can perform the remaining steps incrementally and in any order, testing and debugging after each addition. For example, you can start by implementing the I/O queues and using the framework defaults for Plug and Play and power management. After you have debugged the basic I/O support, you can add support for more extensive Plug and Play and power management requests. The remaining steps are as follows:

-   Add support for [Plug and Play and power management](porting-pnp-and-power-management-functionality.md).
-   Add [I/O support](porting-i-o-handling.md).
-   Add support for [DMA](porting-dma.md), if the device performs DMA.<sup>†</sup>
-   [Port WMI code](porting-wmi-code.md).<sup>†</sup>
-   Port code to [handle requests that the framework does not handle on behalf of KMDF drivers](requests-that-kmdf-does-not-support.md).<sup>†</sup>
-   [Revise the INF](./building-and-loading-a-kmdf-driver.md) that installs the driver.

† This functionality is only available to Kernel-Mode Driver Framework (KMDF) drivers.

Except as noted, the information in this section applies to all types of drivers (PDO, FDO, and filter DO). However, if you are porting a bus driver (PDO) to KMDF, you will also need to port the device enumeration code. For information about enumerating devices, see [Enumerating the Devices on a Bus](enumerating-the-devices-on-a-bus.md).

For reference information describing the ways that the various WDF objects, methods, and event callback functions map to common WDM objects and functions, see [Summary of KMDF and WDM Equivalents](summary-of-kmdf-and-wdm-equivalents.md).