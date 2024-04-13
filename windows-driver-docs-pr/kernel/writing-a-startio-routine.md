---
title: Writing a StartIo Routine
description: Writing a StartIo Routine
keywords: ["StartIo routines, about StartIo routines", "StartIo routines, writing", "starting I/O operations", "I/O operation starting WDK kernel", "IRPs WDK kernel , queuing", "queuing IRPs", "dequeuing IRPs"]
ms.date: 06/16/2017
---

# Writing a StartIo Routine





As its name suggests, a [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine is responsible for starting an I/O operation on the physical device.

Most lowest-level drivers provide a *StartIo* routine and rely on the I/O manager to queue IRPs to a system-supplied device queue. Some lowest-level drivers are designed to set up and manage their own supplemental IRP queues, but even these usually also provide a *StartIo* routine. (For more information about supplemental queues, see [Setting up and Using Device Queues](setting-up-and-using-device-queues.md) and [Managing Device Queues](managing-device-queues.md).)

Higher-level drivers, including FSDs and PnP function and filter drivers, seldom have a *StartIo* routine because it can hamper performance. Instead, most file system drivers set up and maintain internal queues of IRPs. Other higher-level drivers either have internal queues for IRPs or simply pass IRPs on to lower drivers from their dispatch routines. See [Driver-Managed IRP Queues](driver-managed-irp-queues.md) for more information.

You can use the [**IoSetStartIoAttributes**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iosetstartioattributes) routine to set attributes that modify *StartIo* handling for your driver.

This section contains the following topics:

[StartIo Routines in Lowest-Level Drivers](startio-routines-in-lowest-level-drivers.md)

[StartIo Routines in Higher-Level Drivers](startio-routines-in-higher-level-drivers.md)

[Points to Consider for StartIo Routines](points-to-consider-for-startio-routines.md)

 

