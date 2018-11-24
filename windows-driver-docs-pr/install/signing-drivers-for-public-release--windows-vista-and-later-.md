---
title: Signing Drivers for Public Release
description: Signing Drivers for Public Release
ms.assetid: 29e465b4-42f2-4c41-afa7-3f0adf579b0c
keywords:
- driver signing WDK , public release
- signing drivers WDK , public release
- digital signatures WDK , public release
- signatures WDK , public release
- public release driver signing WDK
- release signing WDK
- public release driver signing WDK , release signing
- release signing WDK , about release signing
- release signatures WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





