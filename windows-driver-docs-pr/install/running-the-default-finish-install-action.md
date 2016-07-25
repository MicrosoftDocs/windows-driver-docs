---
title: Running the Default Finish-Install Action
description: Running the Default Finish-Install Action
ms.assetid: a66d418e-9a66-4c11-854d-6e597ffa01f7
---

# Running the Default Finish-Install Action


In Windows 7, the default finish-install action is provided by the system-supplied [**SetupDiFinishInstallAction**](https://msdn.microsoft.com/library/windows/hardware/ff551022) function.

If a device does not have a class installer, or a class installer returns ERROR\_DI\_DO\_DEFAULT in response to a [**DIF\_FINISHINSTALL\_ACTION**](https://msdn.microsoft.com/library/windows/hardware/ff543684) request, Windows calls **SetupDiFinishInstallAction** after all the installers for a device complete their finish-install actions.

In Windows 8 and later versions, there are no default finish-install actions.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Running%20the%20Default%20Finish-Install%20Action%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




