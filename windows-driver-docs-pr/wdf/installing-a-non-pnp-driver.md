---
title: Installing a Non PnP Driver
description: Installing a Non PnP Driver
MSHAttr: PreferredLib /library/windows/hardware
ms.assetid: 99676d85-feb2-482c-a91b-cfc48be5904c
keywords: ["Kernel Mode Driver Framework WDK installing drivers", "framework based drivers WDK KMDF installing", "INF files WDK KMDF non PnP drivers", "non PnP drivers WDK KMDF"]
---

# Installing a Non-PnP Driver


If your driver does not support a Plug and Play (PnP) device, your driver package must include an INF file that contains an INF *DDInstall***.CoInstallers** section and INF *DDInstall***.WDF** section that are described in [Using the KMDF Co-installer](installing-the-framework-s-co-installer.md).

In addition, you must provide an installer that loads your driver and the framework's co-installer. The co-installer provides [**WdfPreDeviceInstall**](https://msdn.microsoft.com/library/windows/hardware/ff548835), [**WdfPreDeviceInstallEx**](https://msdn.microsoft.com/library/windows/hardware/ff548839), [**WdfPostDeviceInstall**](https://msdn.microsoft.com/library/windows/hardware/ff548829), [**WdfPreDeviceRemove**](https://msdn.microsoft.com/library/windows/hardware/ff548840), and [**WdfPostDeviceRemove**](https://msdn.microsoft.com/library/windows/hardware/ff548833) functions that the driver's installer must call.

For an example of how to write an installer for a non-PnP driver, see the installer that is included with the [NONPNP](sample-kmdf-drivers.md) sample.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwdf\wdf%5D:%20Installing%20a%20Non-PnP%20Driver%20%20RELEASE:%20%283/15/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




