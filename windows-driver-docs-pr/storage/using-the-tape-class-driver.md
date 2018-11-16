---
title: Using the Tape Class Driver
description: Using the Tape Class Driver
ms.assetid: 72ed3fd9-d46f-400e-9816-f9f48b5a85c0
keywords:
- tape drivers WDK storage , about tape drivers
- storage tape drivers WDK , about tape drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Using the Tape Class Driver


## <span id="ddk_using_the_tape_class_driver_kg"></span><span id="DDK_USING_THE_TAPE_CLASS_DRIVER_KG"></span>


The system-supplied tape class driver implements device-independent, operating system-specific tape support and exports support routines for device-specific tape miniclass drivers.

The tape class driver:

-   Initializes the tape miniclass driver using device-specific information provided by the miniclass driver's **DriverEntry** routine, including allocating and initializing operating system resources for the miniclass driver and the devices it supports, creating a device object (FDO) to represent the device and attaching it to the device stack, and starting the device on receipt of a start request from the PnP manager.

-   Exports memory allocation and initialization routines.

-   Splits transfer requests when necessary to fit within the maximum transfer size for the HBA.

-   Handles IRP\_MJ\_CREATE, IRP\_MJ\_READ, IRP\_MJ\_WRITE, IRP\_MJ\_PNP, and IRP\_MJ\_POWER requests.

-   Performs device-independent preprocessing for IRP\_MJ\_DEVICE\_CONTROL requests and dispatches to the corresponding device-specific routines in the tape miniclass drivers.

-   Allocates SRBs and sends them to the underlying storage port driver after the tape miniclass driver has filled in the CDB and any other SRB members appropriate to the request.

-   Translates between Windows NT status codes and tape status codes, provides device-independent tape-specific error handing, and calls the tape miniclass driver's device-specific error handling routines.

-   Allocates driver context areas for tape miniclass drivers (minitape extension and command extension).

See [Tape Class Driver Routines](https://msdn.microsoft.com/library/windows/hardware/ff567959) for descriptions of the **TapeClass***Xxx* routines that can be called by a tape miniclass driver.

 

 




