---
title: Writing ControllerControl Routines
author: windows-driver-content
description: Writing ControllerControl Routines
MS-HAID:
- 'ioprogleg\_aefcc614-0fc0-4a3c-bd92-fa5b53e83e4a.xml'
- 'kernel.writing\_controllercontrolroutines'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 9330e0ff-c4bb-4aa6-985e-ef89791f74df
keywords: ["controller objects WDK kernel , writing ControllerControl routines", "ControllerControl routines, writing"]
---

# Writing ControllerControl Routines


## <a href="" id="ddk-writing-controllercontrol-routines-kg"></a>


Drivers that use a controller object must supply a [*ControllerControl*](https://msdn.microsoft.com/library/windows/hardware/ff542049) routine to initiate I/O operations.

A lowest-level device driver that must synchronize operations through a physical controller, such as an "AT" disk controller, to similar devices can have a *ControllerControl* routine.

When a driver calls [**IoAllocateController**](https://msdn.microsoft.com/library/windows/hardware/ff548224), its *ControllerControl* routine is run immediately if the hardware represented by the controller object is available for an I/O operation. Otherwise, the *ControllerControl* routine is queued until the controller is free.

**Note**  WDM drivers cannot use controller objects and *ControllerControl* routines.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20ControllerControl%20Routines%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


