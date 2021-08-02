---
title: Introduction to Standard Driver Routines
description: Introduction to Standard Driver Routines
keywords: ["standard driver routines WDK kernel , about standard driver routines", "driver routines WDK kernel , about standard driver routines", "routines WDK kernel , about standard driver routines", "IRPs WDK kernel , standard driver routines", "required standard routines WDK kernel", "optional standard routines WDK kernel"]
ms.date: 08/02/2021
ms.localizationpriority: medium
---

# Introduction to Standard Driver Routines

Each kernel-mode driver is constructed around a set of system-defined, standard driver routines. Kernel-mode drivers process *I/O request packets* (IRPs) within these standard routines by calling system-supplied driver support routines.

All drivers, regardless of their level in a chain of attached drivers, must have a basic set of standard routines in order to process IRPs. Whether a driver must implement additional standard routines depends on whether the driver controls a physical device or is layered over a physical device driver, as well as on the nature of the underlying physical device. Lowest-level drivers that control physical devices have more required routines than higher-level drivers, which typically pass IRPs to a lower driver for processing.

Standard driver routines can be divided into two groups: those that each kernel-mode driver must have, and those that are optional, depending on the driver type and location in the *device stack*.

The following table lists required standard routines.

| Required standard driver routines | Purpose | Where described |
|--|--|--|
| [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) | Initializes the driver and its driver object. | [Writing a DriverEntry Routine](writing-a-driverentry-routine.md) |
| [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) | Initializes devices and creates device objects. | [Writing an AddDevice Routine](writing-an-adddevice-routine.md) |
| [Dispatch Routines](/windows-hardware/drivers/kernel/dispatchcreate--dispatchclose--and-dispatchcreateclose-routines) | Receive and process IRPs. | [Writing Dispatch Routines](writing-dispatch-routines.md) |
| *Unload* | Release system resources acquired by the driver. | [Writing an Unload Routine](writing-an-unload-routine.md) |

The following table lists several optional routines.

| Optional standard driver routines | Purpose | Where described |
|--|--|--|
| *Reinitialize* | Completes driver initialization if **DriverEntry** cannot. | [Writing a Reinitialize Routine](writing-a-reinitialize-routine.md) |
| *StartIo* | Starts an I/O operation on a physical device. | [Writing a StartIo Routine](writing-a-startio-routine.md) |
| Interrupt Service Routine | Saves the state of a device when it interrupts. | [Writing an ISR](writing-an-isr.md) |
| Deferred Procedure Calls | Completes the processing of a device interrupt after an ISR saves the device state. | [DPC Objects and DPCs](/windows-hardware/drivers/kernel/introduction-to-dpc-objects) |
| *SynchCritSection* | Synchronizes access to driver data. | [Using Critical Sections](using-critical-sections.md) |
| *AdapterControl* | Initiates DMA operations. | [Adapter Objects and DMA](./introduction-to-adapter-objects.md) |
| *IoCompletion* | Completes a driver's processing of an IRP. | [Completing IRPs](completing-irps.md) |
| *Cancel* | Cancels a driver's processing of an IRP. | [Canceling IRPs](canceling-irps.md) |
| *CustomTimerDpc*, *IoTimer* | Timing and synchronizing events. | [Synchronization Techniques](/windows-hardware/drivers/kernel/introduction-to-kernel-dispatcher-objects) |

The current IRP and target device object are input parameters to many standard routines. Every driver processes each IRP in stages through its set of standard routines.

By convention, the system-supplied drivers prepend an identifying, driver-specific or device-specific prefix to the name of every standard routine except **DriverEntry**. As an example, this documentation uses "DD", as shown in the illustration in [Introduction to Driver Objects](introduction-to-driver-objects.md). Following this convention makes it easier to debug and maintain drivers.
