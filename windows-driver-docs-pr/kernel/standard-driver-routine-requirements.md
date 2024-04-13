---
title: Standard Driver Routine Requirements
description: Standard Driver Routine Requirements
keywords: ["standard driver routines WDK kernel , requirements", "driver routines WDK kernel , requirements", "routines WDK kernel , requirements"]
ms.date: 06/16/2017
---

# Standard Driver Routine Requirements





Keep the following points in mind when designing a kernel-mode driver:

-   Each driver must have a [**DriverEntry**](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_initialize) routine, which initializes driver-wide data structures and resources. The I/O manager calls the **DriverEntry** routine when it loads the driver.

-   Every driver must have at least one dispatch routine that receives and processes I/O request packets (IRPs). Each driver must place a dispatch routine's entry point in its [**DRIVER\_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_driver_object) structure, for each [IRP major function code](./irp-major-function-codes.md) that the driver can receive. A driver can have a separate dispatch routine for each IRP major function code, or it can have one or more dispatch routines that handle several function codes.

-   Every WDM driver must have an [*Unload*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) routine. The driver must place the *Unload* routine's entry point in the driver's driver object. The responsibilities of a [PnP driver's Unload routine](pnp-driver-s-unload-routine.md) are minimal, but a [non-PnP driver's unload routine](non-pnp-driver-s-unload-routine.md) is responsible for releasing any system resources that the driver is using.

-   Every WDM driver must have an [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine and define its entry point in the *driver extension* of the driver object. An *AddDevice* routine is responsible for creating and initializing device objects for each PnP device the driver controls.

-   A driver can have a [*StartIo*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_startio) routine, which the I/O manager calls to start I/O operations for IRPs the driver has queued to a system-supplied IRP queue. Any driver that does not have a *StartIo* routine must either set up and manage internal queues for the IRPs it receives, or it must complete every IRP within its dispatch routines. Higher-level drivers might not have a *StartIo* routine, if they simply pass IRPs to lower-level drivers directly from their dispatch routines.

-   Certain miniport drivers are exceptions to the preceding requirements. See the device-type-specific documentation in the Windows Driver Kit (WDK) for information about the requirements for miniport drivers.

-   Whether a driver has any other kind of standard routine depends on its functionality and on how that driver fits into the system (for example, whether it interoperates with system-supplied drivers). See the device-type specific documentation in the WDK for details.

