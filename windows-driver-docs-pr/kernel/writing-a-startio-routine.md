---
title: Writing a StartIo Routine
author: windows-driver-content
description: Writing a StartIo Routine
MS-HAID:
- 'IRPs\_5cab3871-b277-4e65-bca4-b6a45ba50b02.xml'
- 'kernel.writing\_a\_startio\_routine'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b2a380ae-549c-4ca2-9c69-1e20c17ed2e6
keywords: ["StartIo routines, about StartIo routines", "StartIo routines, writing", "starting I/O operations", "I/O operation starting WDK kernel", "IRPs WDK kernel , queuing", "queuing IRPs", "dequeuing IRPs"]
---

# Writing a StartIo Routine


## <a href="" id="ddk-writing-a-startio-routine-kg"></a>


As its name suggests, a [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine is responsible for starting an I/O operation on the physical device.

Most lowest-level drivers provide a *StartIo* routine and rely on the I/O manager to queue IRPs to a system-supplied device queue. Some lowest-level drivers are designed to set up and manage their own supplemental IRP queues, but even these usually also provide a *StartIo* routine. (For more information about supplemental queues, see [Setting up and Using Device Queues](setting-up-and-using-device-queues.md) and [Managing Device Queues](managing-device-queues.md).)

Higher-level drivers, including FSDs and PnP function and filter drivers, seldom have a *StartIo* routine because it can hamper performance. Instead, most file system drivers set up and maintain internal queues of IRPs. Other higher-level drivers either have internal queues for IRPs or simply pass IRPs on to lower drivers from their dispatch routines. See [Driver-Managed IRP Queues](driver-managed-irp-queues.md) for more information.

You can use the [**IoSetStartIoAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff550330) routine to set attributes that modify *StartIo* handling for your driver.

This section contains the following topics:

[StartIo Routines in Lowest-Level Drivers](startio-routines-in-lowest-level-drivers.md)

[StartIo Routines in Higher-Level Drivers](startio-routines-in-higher-level-drivers.md)

[Points to Consider for StartIo Routines](points-to-consider-for-startio-routines.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20a%20StartIo%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


