---
title: Registering and Enabling an IoTimer Routine
description: Registering and Enabling an IoTimer Routine
keywords: ["IoTimer", "IoInitializeTimer", "IoStartTimer", "registering IoTimer routines"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Registering and Enabling an IoTimer Routine





Any driver can register an [*IoTimer*](/windows-hardware/drivers/ddi/wdm/nc-wdm-io_timer_routine) routine, after it creates one or more device objects, by calling [**IoInitializeTimer**](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioinitializetimer). The driver can then start the timer by calling [**IoStartTimer**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostarttimer). The following figure illustrates these calls.

![diagram illustrating using an iotimer routine.](images/3iotmer.png)

After calling [**IoCreateDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocreatedevice) to create device objects, a driver can call **IoInitializeTimer** with the entry point of its *IoTimer* routine, along with pointers to a driver-created device object and a context area in which the driver maintains whatever context its *IoTimer* routine uses. The I/O manager associates the device object with a kernel-allocated timer object and sets up the timer object to time out every second.

After the driver calls **IoStartTimer**, its *IoTimer* routine is called once per second until the driver calls [**IoStopTimer**](/windows-hardware/drivers/ddi/ntifs/nf-ntifs-iostoptimer). A driver can reenable calls to its *IoTimer* routine with **IoStartTimer**. (Frequently, when a driver calls **IoStartTimer**, it supplies the device object pointer obtained from the I/O stack location of the current IRP.)

On entry, the *IoTimer* routine is passed the device object pointer<em>,</em> along with the context pointer that the driver supplied when it called **IoInitializeTimer**.

Drivers must not call **IoStopTimer** from within an *IoTimer* routine.

The I/O manager unregisters the timer routine for a specified device object and frees its associated context when the driver calls [**IoDeleteDevice**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iodeletedevice).

 

