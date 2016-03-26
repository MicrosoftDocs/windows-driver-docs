---
title: Supporting PnP and Power Management in Software-only Drivers
description: Supporting PnP and Power Management in Software-only Drivers
ms.assetid: bcfca8b2-68d6-4875-8687-27351becd6f4
keywords: ["PnP WDK KMDF , software-only drivers", "Plug and Play WDK KMDF , software-only drivers", "power management WDK KMDF , software-only drivers", "software-only drivers WDK KMDF", "filter drivers WDK KMDF"]
---

# Supporting PnP and Power Management in Software-only Drivers


*Software-only drivers* are drivers that do not access any hardware. Some software-only drivers reside in a driver stack that does not access hardware. Because these drivers do not access hardware, they typically do not have to perform any PnP or power management operations.

Other software-only drivers are filter drivers: they reside in a stack of drivers that do access hardware, but the filter drivers do not access hardware. When a filter driver receives an I/O request that specifies a PnP or power management operation, the driver typically just passes the request to the next driver. The framework intercepts these requests and passes them on, so framework-based drivers never see the requests.

If you are writing a software-only driver, your driver [creates device objects](creating-a-framework-device-object.md) but you typically do not need to provide any event callback functions to handle PnP or power management events. If the driver uses [framework queue objects](framework-queue-objects.md), you will need to set the **PowerManaged** member of the queue's [**WDF\_IO\_QUEUE\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff552359) structure to **WdfFalse** or **WdfUseDefault**.

A few software-only drivers are also [function drivers](supporting-pnp-and-power-management-in-function-drivers.md). In other words, a single driver might act as a software-only driver to support a virtual device that does not access hardware, and as a function driver to support a hardware device.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Supporting%20PnP%20and%20Power%20Management%20in%20Software-only%20Drivers%20%20RELEASE:%20%283/25/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




