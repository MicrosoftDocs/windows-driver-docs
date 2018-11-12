---
title: Tools for Signing Drivers
description: Tools for Signing Drivers
ms.assetid: 2654388d-b39e-4009-bcba-56b318fd5119
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





