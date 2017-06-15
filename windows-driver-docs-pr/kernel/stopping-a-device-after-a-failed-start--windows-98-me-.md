---
title: Stopping a Device after a Failed Start (Windows 98/Me)
author: windows-driver-content
description: Stopping a Device after a Failed Start (Windows 98/Me)
MS-HAID:
- 'PlugPlay\_659fbaff-ca7f-4a79-909b-eaa47b2540c8.xml'
- 'kernel.stopping\_a\_device\_after\_a\_failed\_start\_\_windows\_98\_me\_'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 373a1797-6479-4b99-b577-c74494f1774c
keywords: ["failed starts WDK PnP"]
---

# Stopping a Device after a Failed Start (Windows 98/Me)


## <a href="" id="ddk-stopping-a-device-after-a-failed-start-kg"></a>


On Windows 98/Me, the PnP manager issues an [**IRP\_MN\_STOP\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551755) request without a preceding query when the drivers for a device fail an [**IRP\_MN\_START\_DEVICE**](https://msdn.microsoft.com/library/windows/hardware/ff551749) request. (On Windows 2000 and later, the PnP manager sends remove IRPs in this situation. See [Understanding When Remove IRPs Are Issued](understanding-when-remove-irps-are-issued.md).)

In response to the stop IRP, drivers release the device's hardware resources (such as its I/O ports), disable and deregister any user-mode interfaces, and fail any incoming I/O requests that require access to the device.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Stopping%20a%20Device%20after%20a%20Failed%20Start%20%28Windows%2098/Me%29%20%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


