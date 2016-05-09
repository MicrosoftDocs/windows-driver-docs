---
title: Using the Tape Class Driver
author: windows-driver-content
description: Using the Tape Class Driver
ms.assetid: 72ed3fd9-d46f-400e-9816-f9f48b5a85c0
keywords: ["tape drivers WDK storage , about tape drivers", "storage tape drivers WDK , about tape drivers"]
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Using%20the%20Tape%20Class%20Driver%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


