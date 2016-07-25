---
title: Introduction to Test-Signing
description: Introduction to Test-Signing
ms.assetid: 63d4627d-b92c-489d-accf-16cfb5ac1410
keywords: ["test signing driver packages WDK , about test signing driver packages"]
---

# Introduction to Test-Signing


Drivers should be test-signed with a [digital signature](digital-signatures.md) during development and test for the following reasons:

-   To facilitate and automate installation.

    If a driver is not signed, the [Plug and Play (PnP) driver installation policy](digital-signatures-and-pnp-device-installation--windows-vista-and-late.md) of Windows Vista and later versions of Windows require that a system administrator manually authorize the installation of an unsigned driver, adding an extra step to the installation process. This extra step can adversely affect the productivity of developers and testers. This requirement cannot be overridden.

-   To be able to load kernel-mode drivers on 64-bit versions of Windows Vista and later versions of Windows.

    By default, the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) for 64-bit versions of Windows Vista and later versions of Windows require that a kernel-mode driver be signed in order for the driver to be loaded. This requirement can be temporarily overridden to facilitate the development or debugging of a driver.

-   To play back certain types of next-generation premium content, all kernel-mode components in Windows Vista and later versions of Windows must be signed. In addition, all the user-mode and kernel-mode components in the Protected Media Path (PMP) must comply with PMP signing policy. For information about PMP signing policy, see the white paper [Code-signing for Protected Media Components in Windows Vista](http://go.microsoft.com/fwlink/p/?linkid=69258).

For these reasons, drivers for Windows Vista and later versions of Windows should be test-signed with a digital certificate that is created by using Microsoft Authenticode. Such a digital certificate is referred to as a *test certificate* and a signature generated with a test certificate is referred to as a *test signature*.

**Note**  Windows Vista and later versions of Windows support test-signed drivers only for development and testing purposes. Test signatures must not be used for production purposes or released to customers.

 

A development and test team can participate in the [WHQL Test Signature program](whql-test-signature-program.md), where the Windows Hardware Quality Labs (WHQL) will sign PnP [driver packages](driver-packages.md) for testing purposes. Alternatively, a development and test team can manage their own in-house signing process and use the following types of [test certificates](test-certificates.md) to test-sign drivers:

-   [MakeCert test certificate](makecert-test-certificate.md), which is a digital certificate created by the [**MakeCert**](https://msdn.microsoft.com/library/windows/hardware/ff548309) tool.

-   [Commercial test certificate](commercial-test-certificate.md), which is a digital certificate that is issued by a CA that is a member of the Microsoft Root Certificate Program.

-   [Enterprise CA test certificate](enterprise-ca-test-certificate.md), which is a digital certificate that is deployed by an Enterprise CA.

For information about how a test team signs a driver package after the team creates, obtains, or is provided a test certificate, see [Test-Signing Driver Packages](test-signing-driver-packages.md).

For information about how to install driver packages that are test-signed, see [Installing Test-Signed Driver Packages](installing-test-signed-driver-packages.md).

To facilitate early driver development and debugging, you can temporarily disable the kernel-mode code signing requirement to load and test an unsigned kernel-mode driver. However, you cannot disable the PnP driver installation policy that requires a system administrator to authorize the installation of an unsigned driver. For more information about how to install an unsigned driver, see [Installing an Unsigned Driver during Development and Test](installing-an-unsigned-driver-during-development-and-test.md).

For information about the most appropriate tools to use to test-sign driver packages, see [Tools for Signing Drivers](https://msdn.microsoft.com/library/windows/hardware/ff552958).

**Note**  To get a better understanding of the steps that are involved in test-signing driver packages, see [How to Test-Sign a Driver Package](how-to-test-sign-a-driver-package.md). This topic provides a summary of the test-signing process, and steps through many examples of test-signing by using the *ToastPkg* sample [driver package](driver-packages.md) within the Windows Driver Kit (WDK).

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Introduction%20to%20Test-Signing%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




