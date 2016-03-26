---
title: Steps in Porting
description: Steps in Porting
ms.assetid: D8B7E534-7CFC-45EC-93E9-4B046598D82B
---

# Steps in Porting


Depending on the type of driver, porting involves performing the following steps:

1.  [Port the DriverEntry routine](porting-driver-entry.md) and add code to create the WDFDRIVER object.
2.  [Port the AddDevice routine](porting-adddevice-to-evtdriverdeviceadd.md) to an [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback, and add code to create the WDFDEVICE objects.
3.  Add support for [interrupts](porting-interrupt-functionality.md) if the driver supports interrupt handling.

At this point, you can perform the remaining steps incrementally and in any order, testing and debugging after each addition. For example, you can start by implementing the I/O queues and using the framework defaults for Plug and Play and power management. After you have debugged the basic I/O support, you can add support for more extensive Plug and Play and power management requests. The remaining steps are as follows:

-   Add support for [Plug and Play and power management](porting-pnp-and-power-management-functionality.md).
-   Add [I/O support](porting-i-o-handling.md).
-   Add support for [DMA](porting-dma.md), if the device performs DMA.<sup>†</sup>
-   [Port WMI code](porting-wmi-code.md).<sup>†</sup>
-   Port code to [handle requests that the framework does not handle on behalf of KMDF drivers](requests-that-kmdf-does-not-support.md).<sup>†</sup>
-   [Revise the INF](installation-procedure.md) that installs the driver.

† This functionality is only available to Kernel-Mode Driver Framework (KMDF) drivers.

Except as noted, the information in this section applies to all types of drivers (PDO, FDO, and filter DO). However, if you are porting a bus driver (PDO) to KMDF, you will also need to port the device enumeration code. For information about enumerating devices, see [Enumerating the Devices on a Bus](enumerating-the-devices-on-a-bus.md).

For reference information describing the ways that the various WDF objects, methods, and event callback functions map to common WDM objects and functions, see [Summary of KMDF and WDM Equivalents](summary-of-kmdf-and-wdm-equivalents.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Steps%20in%20Porting%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




