---
title: How to Test-Sign a Driver Package
description: How to Test-Sign a Driver Package
ms.assetid: 992f0974-0b0e-4c96-ad16-c5894067896c
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# How to Test-Sign a Driver Package


This section provides information about the basic steps that you have to follow when you test-sign a [driver package](driver-packages.md). 

Test-signing refers to using a test certificate to sign a prerelease version of a [driver package](driver-packages.md) for use on test computers. In particular, this allows developers to sign kernel-mode binaries by using self-signed certificates, such as those the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) tool generates. This capability allows developers to test kernel-mode binaries on Windows with driver signature verification enabled.

Windows supports test-signed drivers only for development and testing purposes. Test-signed drivers must not be used for production purposes or released to customers.

This section includes topics that describe these steps and provide examples, such as the following:

-   Creating a test certificate that is used to sign a driver package. In this section, steps are described to create and use a self-signed test certificate named *Contoso.com(Test)*. This certificate is used in many examples that are discussed in this section.

-   Preparing a [driver package](driver-packages.md) for test-signing. This includes creating a [catalog file](catalog-files.md) that contains the digital signature.

-   Test-signing the driver package's catalog file by using the *Contoso.com(Test)* certificate.

-   Test-signing a driver through an embedded signature by using the *Contoso.com(Test)* certificate.

    **Note**  You have to embed a digital signature within the driver if the driver is a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver).

     

Each topic in this section describes a separate procedure in the test-signing process, and provides the general information that you need to understand the procedure. In addition, each topic points you to other topics that provide detailed information about the procedure.

Throughout this section, separate computers are used for the various processes involved in test-signing a driver. These computers are referred to as follows:

<a href="" id="signing-computer"></a>**Signing computer**  
This is the computer that is used to test-sign a driver package for Windows Vista and later versions of Windows. This computer must be running Windows XP SP2 or later versions of Windows. In order to use the [driver signing tools](https://msdn.microsoft.com/library/windows/hardware/ff552958), this computer must have the Windows Vista and later versions of the Windows Driver Kit (WDK) installed.

<a href="" id="test-computer"></a>**Test computer**  
This is the computer that is used to install and test the test-signed driver package. This computer must be running Windows Vista or later versions of Windows.

The topics of this section use the *ToastPkg* sample driver package to introduce the test-signing process. Within the WDK installation directory, the *ToastPkg* driver package is located in the *src\\general\\toaster\\toastpkg* directory.

**Note**  The WDK contains a sample command script that shows the step-by-step procedure to correctly test-sign the *ToastPkg* sample [driver package](driver-packages.md). You can modify this script to test-sign your own driver package. Within the WDK installation directory, the example is located at *src\\general\\build\\driversigning\\selfsign_example.cmd*. Additional instructions for test-signing are described in *src\\general\\build\\driversigning\\selfsign_readme.htm*.

 

This section includes the following topics:

[Creating Test Certificates](creating-test-certificates.md)

[Viewing Test Certificates](viewing-test-certificates.md)

[Creating a Catalog File for Test-Signing a Driver Package](creating-a-catalog-file-for-test-signing-a-driver-package.md)

[Test-Signing a Driver Package's Catalog File](test-signing-a-driver-package-s-catalog-file.md)

[Test-Signing a Driver through an Embedded Signature](test-signing-a-driver-through-an-embedded-signature.md)

[Configuring the Test Computer to Support Test-Signing](configuring-the-test-computer-to-support-test-signing.md)

[Installing Test Certificates](installing-test-certificates.md)

[Verifying the Test Signature](verifying-the-test-signature.md)

[Installing a Test-Signed Driver Package on the Test Computer](installing-a-test-signed-driver-package-on-the-test-computer.md)

 

 





