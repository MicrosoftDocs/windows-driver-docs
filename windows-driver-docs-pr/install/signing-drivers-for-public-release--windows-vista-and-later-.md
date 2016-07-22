---
title: Signing Drivers for Public Release
description: Signing Drivers for Public Release
ms.assetid: 29e465b4-42f2-4c41-afa7-3f0adf579b0c
keywords: ["driver signing WDK , public release", "signing drivers WDK , public release", "digital signatures WDK , public release", "signatures WDK , public release", "public release driver signing WDK", "release signing WDK", "public release driver signing WDK , release signing", "release signing WDK , about release signing", "release signatures WDK"]
---

# Signing Drivers for Public Release


Release-signing identifies the publisher of a kernel-mode binary (for example, driver or *.dll*) that loads into Windows Vista and later versions of Windows. Kernel-mode binaries are release-signed through either:

-   A [WHQL Release Signature](whql-release-signature.md) obtained through the [Windows Logo Program](https://msdn.microsoft.com/windows-drivers/develop/testing_a_driver).

-   A release signature created through a [Software Publisher Certificate (SPC)](software-publisher-certificate.md).

To understand the steps that are involved in release-signing [driver packages](driver-packages.md), review the following topics:

<a href="" id="introduction-to-release-signing"></a>[Introduction to Release-Signing](introduction-to-release-signing.md)  
This topic describes the reasons why release-signing a driver package is important, and provides a high-level summary of the release-signing process.

<a href="" id="how-to-release-sign-a-driver-package"></a>[How to Release-Sign a Driver Package](how-to-release-sign-a-driver-package.md)  
This topic provides a high-level overview of the release-signing process, and reviews many examples of release-signing by using the *ToastPkg* sample driver package within the Windows Driver Kit (WDK).

For more information about the release-signing process, see the following topics:

[WHQL Release Signature](whql-release-signature.md)

[Release Certificates](release-certificates.md)

[Release-Signing Driver Packages](release-signing-driver-packages.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Signing%20Drivers%20for%20Public%20Release%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




