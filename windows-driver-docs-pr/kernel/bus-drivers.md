---
title: Bus Drivers
author: windows-driver-content
description: Bus Drivers
ms.assetid: d1a92c06-882d-49dc-befa-5b9a9e8aecd7
keywords: ["bus drivers WDK WDM", "enumerating bus devices WDK WDM", "bus controllers WDK WDM", "adapters WDK WDM", "bridges WDK WDM", "WDM bus drivers WDK"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Bus Drivers


## <a href="" id="ddk-bus-drivers-kg"></a>


A *bus driver* services a bus controller, adapter, or bridge (see the [Possible Driver Layers](types-of-wdm-drivers.md#possible-driver-layers) figure). Microsoft provides bus drivers for most common buses, such as PCI, PnpISA, SCSI, and USB. Other bus drivers can be provided by IHVs or OEMs. Bus drivers are required drivers; there is one bus driver for each type of bus on a machine. A bus driver can service more than one bus if there is more than one bus of the same type on the machine.

The primary responsibilities of a bus driver are to:

-   Enumerate the devices on its bus.

-   Respond to Plug and Play IRPs and power management IRPs.

-   Multiplex access to the bus (for some buses).

-   Generically administer the devices on its bus.

Bus drivers are essentially [function drivers](function-drivers.md) that also enumerate children.

During enumeration, a bus driver identifies the devices on its bus and creates device objects for them. (For information about device objects, see [Device Objects and Device Stacks](device-objects-and-device-stacks.md).) The method a bus driver uses to identify connected devices depends on the particular bus.

A bus driver performs certain operations on behalf of the devices on its bus, including accessing device registers to physically change the power state of a device. For example, when the device goes to sleep, the bus driver sets device registers to put the device in the proper device power state.

Note, however, that a bus driver does not handle read and write requests for the child devices that are connect to its bus. Read and write requests to a child device are handled by the child device's [function driver](function-drivers.md). Only if the child device is being used in [*raw mode*](https://msdn.microsoft.com/library/windows/hardware/ff556331#wdkgloss-raw-mode) does the parent bus driver handle reads and writes for the device.

Because a bus driver acts as the function driver for its controller, adapter, or bridge, it also manages device power policy for these components.

A bus driver can be implemented as a driver/minidriver pair, the way a SCSI port/miniport driver pair drives a SCSI host bus adapter (HBA). In such driver pairs, the minidriver is linked to the second driver, which is a DLL.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Bus%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


