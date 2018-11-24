---
title: How to Release-Sign a Driver Package
description: How to Release-Sign a Driver Package
ms.assetid: f02c0a50-01f1-456c-b432-c4d9e8cbc566
keywords:
- release-signing drivers WDK
- driver signing WDK , release-signing packages
- signing drivers WDK , release-signing packages
- digital signatures WDK , release-signing driver packages
- signatures WDK , release-signing driver packages
- release-signing drivers WDK
- release-signing drivers WDK , driver packages
- release-signing driver packages WDK
- release-signing driver packages WDK , about test signing driver packages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Release-Sign a Driver Package


This section provides the basic steps that you have to follow when you release-sign a [driver package](driver-packages.md). This includes the following:

-   Obtaining a [Software Publisher Certificate (SPC)](software-publisher-certificate.md) from a commercial certificate authority (CA).

-   Preparing a [driver package](driver-packages.md) for release-signing. This includes creating a [catalog file](catalog-files.md), which contains the digital signature for the driver package.

-   Release-signing the driver package's catalog file.

-   Release-signing a driver through an embedded signature. You have to embed a digital signature within the driver if the driver is a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver).

Each topic in this section describes a separate procedure in the release-signing process, and provides the general information that you have to understand about the procedure. In addition, each topic points you to other topics that provide detailed information about the procedure.

**Note**  This section discusses the steps involved when a driver publisher has to manually release-sign a driver package. The [Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=227016) has [test categories](http://go.microsoft.com/fwlink/p/?linkid=189178) for a variety of device types. If a test category for the device type is included in this list, the driver publisher should obtain a [WHQL release signature](whql-release-signature.md) for the driver package instead of manually release-signing the driver package.

 

Throughout this section, separate computers are used for the various processes involved in release-signing a driver. These computers are referred to as follows:

<a href="" id="--------signing-computer"></a> **Signing computer**  
This is the computer that is used to release-sign a driver package for Windows Vista and later versions of Windows. This computer must be running Windows XP SP2 or later versions of Windows. To use the [driver signing tools](https://msdn.microsoft.com/library/windows/hardware/ff552958), this computer must have the Windows Vista and later versions of the Windows Driver Kit (WDK) installed.

<a href="" id="test-computer"></a>**Test computer**  
This is the computer that is used to install and test the release-signed driver package. This computer must be running Windows Vista or later versions of Windows.

When discussing the release-signing process, the topics of this section use the *ToastPkg* sample driver package. Within the WDK installation directory, the *ToastPkg* driver package is located in the *src\\general\\toaster\\toastpkg* directory.

This section contains the following topics:

[Obtaining a Software Publisher Certificate (SPC)](obtaining-a-software-publisher-certificate--spc-.md)

[Creating a Catalog File for Release-Signing a Driver Package](creating-a-catalog-file-for-release-signing-a-driver-package.md)

[Release-Signing a Driver Package's Catalog File](release-signing-a-driver-package-s-catalog-file.md)

[Release-Signing a Driver Through an Embedded Signature](release-signing-a-driver-through-an-embedded-signature.md)

[Verifying the Release-Signature](verifying-the-release-signature.md)

[Configuring a Computer to Support Release-Signing](configuring-a-computer-to-support-release-signing.md)

[Installing a Release-Signed Driver Package](installing-a-release-signed-driver-package.md)

 

 





