---
title: Tools for Signing Drivers
description: Tools for Signing Drivers
ms.assetid: 2654388d-b39e-4009-bcba-56b318fd5119
---

# Tools for Signing Drivers


The Microsoft Windows Driver Kit (WDK) includes the following tools that you can use to create a code-signing certificate, to sign the [catalog file](https://msdn.microsoft.com/library/windows/hardware/ff537872) of a [driver package](https://msdn.microsoft.com/library/windows/hardware/ff544840), and to embed a signature in a driver file:

[**CertMgr**](certmgr.md)

[**Inf2Cat**](inf2cat.md)

[**MakeCat**](makecat.md)

[**MakeCert**](makecert.md)

[**Pvk2Pfx**](pvk2pfx.md)

[**SignTool**](signtool.md)

These tools are located in the following directories:

-   The Inf2Cat tool is located in the %WindowsSdkDir%\\bin\\x86 directory.

-   The other tools are located in the directories for 32-bit Windows platforms (%WindowsSdkDir%\\bin\\x86) and 64-bit Windows platforms (%WindowsSdkDir%\\bin\\x64).

**Note**  The Visual Studio environment variable, %WindowsSdkDir%, represents the path to the Windows kits directory where this version of the WDK is installed, for example, C:\\Program Files (x86)\\Windows Kits\\10.

 

The Microsoft Windows SDK includes information about the services, components, and tools that enable you to add cryptographic security to your applications. This includes the [**CertMgr**](certmgr.md), [**MakeCert**](makecert.md), and [**SignTool**](signtool.md) tools.

For more information on signing drivers and [driver packages](https://msdn.microsoft.com/library/windows/hardware/ff544840), see [Driver Signing](https://msdn.microsoft.com/library/windows/hardware/ff544865).

For information on test-signing a driver package, see [Signing Drivers during Development and Test](https://msdn.microsoft.com/library/windows/hardware/ff552264).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Tools%20for%20Signing%20Drivers%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




