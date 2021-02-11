---
title: Tools for Signing Drivers
description: Tools for Signing Drivers
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Tools for Signing Drivers


The Microsoft Windows Driver Kit (WDK) includes the following tools that you can use to create a code-signing certificate, to sign the [catalog file](../install/catalog-files.md) of a [driver package](../install/driver-packages.md), and to embed a signature in a driver file:

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

For more information on signing drivers and [driver packages](../install/driver-packages.md), see [Driver Signing](../install/driver-signing.md).

For information on test-signing a driver package, see [Signing Drivers during Development and Test](../install/introduction-to-test-signing.md).

 

