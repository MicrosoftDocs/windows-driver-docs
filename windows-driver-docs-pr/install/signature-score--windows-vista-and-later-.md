---
title: Signature Score
description: Signature Score
ms.assetid: 5e8dbbf8-6282-4299-80d9-5f886d01b1bf
keywords: ["signature score WDK device installations"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Signature%20Score%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




