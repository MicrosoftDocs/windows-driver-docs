---
title: DriverEntry's Required Responsibilities
description: DriverEntry's Required Responsibilities
ms.assetid: 6e997875-e7b7-43e2-8398-f0574f3a5816
keywords: ["DriverEntry WDK kernel , required responsibilities"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# DriverEntry's Required Responsibilities





The required, ordered responsibilities of a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine are as follows:

1.  Supply entry points for the driver's standard routines.

    The driver stores entry points for many of its standard routines in the driver object or driver extension. Such entry points include those for the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, dispatch routines, [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, and [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine. For example, a driver would set the entry points for its *AddDevice*, [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341), and [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routines with statements like the following (*Xxx* is a placeholder for a vendor-supplied prefix identifying the driver):

    ```cpp
        :
    DriverObject->DriverExtension->AddDevice = XxxAddDevice;
    DriverObject->MajorFunction[IRP_MJ_PNP] = XxxDispatchPnp;
    DriverObject->MajorFunction[IRP_MJ_POWER] = XxxDispatchPower;
        :
    ```

    Additional standard routines, such as ISRs or [*IoCompletion*](https://msdn.microsoft.com/library/windows/hardware/ff548354) routines, are specified by calling system support routines. For more information, see the descriptions of individual [standard driver routines](https://msdn.microsoft.com/library/windows/hardware/ff563842).

2.  Create and/or initialize various driver-wide objects, types, or resources the driver uses. Note that most standard routines use objects on a per-device basis, so drivers should set up such objects in their *AddDevice* routines or after receiving an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request.

    If the driver has a device-dedicated thread or waits on any kernel-defined dispatcher objects, the **DriverEntry** routine might initialize [kernel dispatcher objects](kernel-dispatcher-objects.md). (Depending on how the driver uses the object(s), it might instead perform this task in its *AddDevice* routine or after receiving an **IRP\_MN\_START\_DEVICE** request.)

3.  Free any memory that it allocated and is no longer required.

4.  Return NTSTATUS indicating whether the driver successfully loaded and can accept and process requests from the PnP manager to configure, add, and start its devices. (See [DriverEntry Return Values](driverentry-return-values.md).)

 

 




