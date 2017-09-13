---
title: Setting Up ControllerControl Routines
author: windows-driver-content
description: Setting Up ControllerControl Routines
ms.assetid: 007247c1-b51e-4677-9a46-78ff9f1c8996
keywords: ["controller objects WDK kernel , writing ControllerControl routines", "ControllerControl routines, writing", "ControllerControl routines, setting up"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Setting Up ControllerControl Routines


## <a href="" id="ddk-setting-up-controllercontrol-routines-kg"></a>


A driver's [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine must do the following when it receives an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request, to set up a [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049) routine:

1.  Call [**IoCreateController**](https://msdn.microsoft.com/library/windows/hardware/ff548395) to set up the controller object, specifying the driver-determined *Size* for the controller extension, which the system allocates from nonpaged pool and initializes with zeros.

2.  Save the *ControllerObject* pointer returned by **IoCreateController**, usually in the device extension of each device object representing a physical or logical device that is controlled by the hardware represented by the controller object.

3.  Set up and/or initialize the driver-determined contents of the *ControllerObject***-&gt;ControllerExtension**.

The returned *ControllerObject* pointer, the entry point of the driver's *ControllerControl* routine, the *DeviceObject* pointer representing the target device for the current IRP, and a *Context* pointer to an area already set up for the *ControllerControl* routine must be passed in the driver's calls to [**IoAllocateController**](https://msdn.microsoft.com/library/windows/hardware/ff548224). Usually, a driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine sets up the area at *Context* before it calls **IoAllocateController**.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Setting%20Up%20ControllerControl%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


