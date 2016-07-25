---
title: Device Installations on 64-Bit Systems
description: Device Installations on 64-Bit Systems
ms.assetid: 76d9bff7-6429-4d20-9790-a41ed2cb1bdd
keywords: ["64-bit WDK device installations", "device installations WDK , 64-bit systems"]
---

# Device Installations on 64-Bit Systems


## <a href="" id="ddk-installing-devices-on-64-bit-systems-dg"></a>


If your device will be installed on both 32-bit platforms and 64-bit platforms, you must follow these steps when you create a [driver package](driver-packages.md):

-   Provide both 32-bit and 64-bit compilations of all kernel-mode drivers, [*device installation application*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-device-installation-application), [*class installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-class-installer), and [*co-installers*](https://msdn.microsoft.com/library/windows/hardware/ff556274#wdkgloss-co-installer). For more information, see [Porting Your Driver to 64-Bit Windows](https://msdn.microsoft.com/library/windows/hardware/ff559747).

-   Provide one or more cross-platform INF files that use [*decorated INF sections*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-decorated-inf-section) to control platform-specific installation behavior.

If you are [writing a device installation application](writing-a-device-installation-application.md), the 32-bit version must be the default version. That is, the 32-bit version should be invoked by Autorun (described in the Microsoft Windows SDK documentation), so that it starts automatically when a user inserts your distribution disk.

The 32-bit version of the application must check the value returned by [**UpdateDriverForPlugAndPlayDevices**](https://msdn.microsoft.com/library/windows/hardware/ff553534). If the return value is ERROR\_IN\_WOW64, the 32-bit application is executing on a 64-bit platform and cannot update inbox drivers. Instead, it must call [**CreateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms682425) (described in the Windows SDK documentation) to start the 64-bit version of the application. The 64-bit version can then call **UpdateDriverForPlugAndPlayDevices**, specifying a *FullInfPath* parameter that identifies the location of the 64-bit versions of all files.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Device%20Installations%20on%2064-Bit%20Systems%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




