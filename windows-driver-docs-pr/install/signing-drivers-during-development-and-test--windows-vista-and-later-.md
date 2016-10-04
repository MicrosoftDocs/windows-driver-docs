---
title: Signing Drivers during Development and Test
description: Signing Drivers during Development and Test
ms.assetid: 632a42e6-98e3-44c5-87b1-7bafff1963de
keywords: ["driver signing WDK , test signing", "signing drivers WDK , test signing", "digital signatures WDK , test signing", "signatures WDK , test signing", "test signing drivers WDK", "test signatures WDK", "test signing drivers WDK , about test signing drivers", "driver signing WDK , test certificates", "signing drivers WDK , test certificates"]
---

# Signing Drivers during Development and Test


Test-signing refers to using a test certificate to sign a prerelease version of a [driver package](driver-packages.md) for use on test computers. In particular, this allows developers to sign kernel-mode binaries by using self-signed certificates, such as those the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) tool generates. Starting with Windows Vista, this capability allows developers to test kernel-mode binaries on Windows with driver signature verification enabled.

**Note**  Windows Vista and later versions of Windows support test-signed drivers only for development and testing purposes. Test-signed drivers must not be used for production purposes or released to customers.

 

To get a better understanding of the steps that are involved to test-sign [driver packages](driver-packages.md), review the following topics in this section:

<a href="" id="introduction-to-test-signing"></a>[Introduction to Test-Signing](introduction-to-test-signing.md)  
This topic describes the reasons why test-signing a driver package is important, and provides a high-level summary of the test-signing process.

<a href="" id="how-to-test-sign-a-driver-package"></a>[How to Test-Sign a Driver Package](how-to-test-sign-a-driver-package.md)  
This topic provides a high-level overview of the test-signing process, and reviews many examples of test-signing by using the ToastPkg sample driver package within the Windows Driver Kit (WDK).

For more information about the test-signing process, see the following topics:

[WHQL Test Signature Program](whql-test-signature-program.md)

[Test Certificates](test-certificates.md)

[Test-Signing Driver Packages](test-signing-driver-packages.md)

[Installing Test-Signed Driver Packages](installing-test-signed-driver-packages.md)

[Installing an Unsigned Driver during Development and Test](installing-an-unsigned-driver-during-development-and-test.md)

 

 





