---
title: DriverEntry's Required Responsibilities
author: windows-driver-content
description: DriverEntry's Required Responsibilities
ms.assetid: 6e997875-e7b7-43e2-8398-f0574f3a5816
keywords: ["DriverEntry WDK kernel , required responsibilities"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DriverEntry's Required Responsibilities


## <a href="" id="ddk-driverentry-s-required-responsibilities-kg"></a>


The required, ordered responsibilities of a [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine are as follows:

1.  Supply entry points for the driver's standard routines.

    The driver stores entry points for many of its standard routines in the driver object or driver extension. Such entry points include those for the driver's [*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521) routine, dispatch routines, [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine, and [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine. For example, a driver would set the entry points for its *AddDevice*, [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341), and [*DispatchPower*](https://msdn.microsoft.com/library/windows/hardware/ff543354) routines with statements like the following (*Xxx* is a placeholder for a vendor-supplied prefix identifying the driver):

    ```
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20DriverEntry's%20Required%20Responsibilities%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


