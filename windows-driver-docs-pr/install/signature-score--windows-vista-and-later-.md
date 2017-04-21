---
title: Signature Score
description: Signature Score
ms.assetid: 5e8dbbf8-6282-4299-80d9-5f886d01b1bf
keywords:
- signature score WDK device installations
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Signature Score


A driver rank is formatted as 0x*SSGGTHHH*, where the value of 0x*SS*000000 is the signature score, the value of 0x00*GG*0000 is the [feature score](feature-score--windows-vista-and-later-.md), and the value of 0x0000*THHH* is the [identifier score](identifier-score--windows-vista-and-later-.md).

The signature score ranks a driver according to how the driver is signed, as follows:

-   Windows assigns the best signature score (lowest signature score value) to drivers that have a signature from a Windows signing authority. This includes the following:

    -   Premium WHQL signatures and standard WHQL signatures.
    -   Signatures for inbox drivers.
    -   Windows Sustained Engineering (Windows SE) signatures.
    -   A WHQL signature for a Windows version that is the same or later than the [LowerLogoVersion](lowerlogoversion.md) value of the driver's [device setup class](device-setup-classes.md).
-   Windows assigns the second best signature score to a driver that was signed by a third-party using Authenticode technology or a driver that has a WHQL signature for a Windows version that is earlier than the version that is specified by the **LowerLogoVersion** value that is set for the device setup class of the driver.

    Valid third-party signature types include the following:

    -   Drivers signed by using a code signing certificate from an Enterprise Certificate Authority (CA).
    -   Drivers signed by using a code signing certificate issued by a Class 3 CA.
    -   Drivers signed by using a code signing certificate created by the [**MakeCert Tool**](https://msdn.microsoft.com/library/windows/hardware/ff548309).
-   Windows assigns the third best signature score to [driver packages](driver-packages.md) that do not have a valid signature, but the driver is installed by an [**INF *DDInstall* section**](inf-ddinstall-section.md) that has an **.nt** platform extension.

    For more information about the **.nt** extension, see [Creating INF Files for Multiple Platforms and Operating Systems](creating-inf-files-for-multiple-platforms-and-operating-systems.md).

-   Windows assigns the fourth best signature score to driver packages that do not have a valid signature, and the driver is not installed by an INF *DDInstall* section that has an **.nt** platform extension.

-   Windows assigns the fifth and worst signature score (highest signature score value) to drivers that are not signed or whose signing state is unknown.

For more information about driver ranking, see [How Windows Ranks Drivers](how-setup-ranks-drivers--windows-vista-and-later-.md).

 

 





