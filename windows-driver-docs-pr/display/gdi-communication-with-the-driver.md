---
title: GDI Communication with the Driver
description: GDI Communication with the Driver
ms.assetid: 81d9e87f-883b-4019-86fc-bccde861de46
keywords:
- GDI WDK Windows 2000 display , driver communication
- graphics drivers WDK Windows 2000 display , driver communication
- drawing WDK GDI , driver communication
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# GDI Communication with the Driver


## <span id="ddk_gdi_communication_with_the_driver_gg"></span><span id="DDK_GDI_COMMUNICATION_WITH_THE_DRIVER_GG"></span>


The driver exports only one function to GDI: [**DrvEnableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff556210). All other driver-supported functions, including the [**DrvDisableDriver**](https://msdn.microsoft.com/library/windows/hardware/ff556196) function, are exposed to GDI through an array of pointers. A GDI call to **DrvEnableDriver** initializes the driver and passes back the list of driver-supported graphics DDI functions. While there are some functions a driver must support, GDI will handle those operations not included in the function list received from the driver's **DrvEnableDriver** routine. GDI calls *DrvDisableDriver* when the driver is to be unloaded. Graphics DDI functions are discussed in depth in [Using the Graphics DDI](using-the-graphics-ddi.md).

GDI makes a large number of objects and services available to the driver. These fall into two categories: user objects and service routines.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20GDI%20Communication%20with%20the%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




