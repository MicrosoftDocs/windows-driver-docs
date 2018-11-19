---
title: Setting Up ControllerControl Routines
description: Setting Up ControllerControl Routines
ms.assetid: 007247c1-b51e-4677-9a46-78ff9f1c8996
keywords: ["controller objects WDK kernel , writing ControllerControl routines", "ControllerControl routines, writing", "ControllerControl routines, setting up"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Setting Up ControllerControl Routines





A driver's [*DispatchPnP*](https://msdn.microsoft.com/library/windows/hardware/ff543341) routine must do the following when it receives an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request, to set up a [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049) routine:

1.  Call [**IoCreateController**](https://msdn.microsoft.com/library/windows/hardware/ff548395) to set up the controller object, specifying the driver-determined *Size* for the controller extension, which the system allocates from nonpaged pool and initializes with zeros.

2.  Save the *ControllerObject* pointer returned by **IoCreateController**, usually in the device extension of each device object representing a physical or logical device that is controlled by the hardware represented by the controller object.

3.  Set up and/or initialize the driver-determined contents of the *ControllerObject***-&gt;ControllerExtension**.

The returned *ControllerObject* pointer, the entry point of the driver's *ControllerControl* routine, the *DeviceObject* pointer representing the target device for the current IRP, and a *Context* pointer to an area already set up for the *ControllerControl* routine must be passed in the driver's calls to [**IoAllocateController**](https://msdn.microsoft.com/library/windows/hardware/ff548224). Usually, a driver's [*StartIo*](https://msdn.microsoft.com/library/windows/hardware/ff563858) routine sets up the area at *Context* before it calls **IoAllocateController**.

 

 




