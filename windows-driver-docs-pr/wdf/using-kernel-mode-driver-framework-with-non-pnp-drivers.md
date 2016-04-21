---
title: Using Kernel-Mode Driver Framework with Non-PnP Drivers
author: windows-driver-content
description: Using Kernel-Mode Driver Framework with Non-PnP Drivers
ms.assetid: b4b6add2-0e27-4af7-b6bf-5e47db7db560
keywords: ["non-PnP drivers WDK KMDF", "kernel-mode drivers WDK KMDF , PnP", "KMDF WDK , PnP", "Kernel-Mode Driver Framework WDK , PnP", "Plug and Play WDK KMDF , non-PnP drivers", "PnP WDK KMDF , non-PnP drivers", "framework-based drivers WDK KMDF , PnP"]
---

# Using Kernel-Mode Driver Framework with Non-PnP Drivers


## <a href="" id="ddk-using-windows-driver-framework-with-non-pnp-drivers-df"></a>


If you are writing a driver for a device that does not support Plug and Play (PnP), the driver must:

-   Set the [**WdfDriverInitNonPnpDriver**](https://msdn.microsoft.com/library/windows/hardware/ff551303) flag in the [**WDF\_DRIVER\_CONFIG**](https://msdn.microsoft.com/library/windows/hardware/ff551300) structure's **DriverInitFlags** member.

-   Provide an [*EvtDriverUnload*](https://msdn.microsoft.com/library/windows/hardware/ff541694) event callback function.

-   Create framework device objects that only represent [control device objects](using-control-device-objects.md).

If your device does not support PnP, your driver does *not* provide an [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) callback function. Instead, the driver must determine if its device is present.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Using%20Kernel-Mode%20Driver%20Framework%20with%20Non-PnP%20Drivers%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




