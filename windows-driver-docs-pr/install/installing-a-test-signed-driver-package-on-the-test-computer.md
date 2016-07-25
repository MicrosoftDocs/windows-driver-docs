---
title: Installing a Test-Signed Driver Package on the Test Computer
description: Installing a Test-Signed Driver Package on the Test Computer
ms.assetid: d825acb6-d1de-4fc5-bde2-ea27bd706f61
---

# Installing a Test-Signed Driver Package on the Test Computer


You can install the test-signed [driver package](driver-packages.md) on the test computer once:

-   The test computer is prepared to install test-signed drivers or driver packages. For more information, see [Configuring the Test Computer to Support Test-Signing](configuring-the-test-computer-to-support-test-signing.md).

-   The test certificate is copied to the Trusted Root Certification Authorities certificate store on the test computer. For more information, see [Installing Test Certificates](installing-test-certificates.md).

You can install the test-signed [driver package](driver-packages.md) on the computer through:

-   The [DevCon](https://msdn.microsoft.com/library/windows/hardware/ff544707) tool, which is a WDK command line tool for installing drivers.

This topic will first review the process of test-signing a driver package, and then describe how you can install the driver package on the test computer. This topic uses the *ToastPkg* sample driver package. Within the WDK installation directory, the package's source files are located in the *src\\general\\toaster\\toastpkg* directory.

Follow these steps to build and test-sign the *ToastPkg* sample driver package:

1.  On the signing computer, build the *ToastPkg* sample driver package's kernel-mode binaries. For more information about how to build drivers, see [Building a Driver](https://msdn.microsoft.com/windows-drivers/develop/building_a_driver).

2.  On the signing computer, create the *Contoso.com(Test)* certificate as described in [Creating Test Certificates](creating-test-certificates.md).

3.  On the signing computer, create a [catalog file](catalog-files.md) for the *ToastPkg* sample driver package as described in [Creating a Catalog File for Test-Signing a Driver Package](creating-a-catalog-file-for-test-signing-a-driver-package.md).

4.  On the signing computer, test-sign the *ToastPkg* sample driver package's catalog file as described in [Test-Signing a Driver Package's Catalog File](test-signing-a-driver-package-s-catalog-file.md). When signing the driver package, use the *Contoso.com (Test)* certificate from the *PrivateCertStor*e for the test signature.

5.  Prepare the test computer to support test-signing, as described in [Configuring the Test Computer to Support Test-Signing](configuring-the-test-computer-to-support-test-signing.md).

6.  Copy the *Contoso.com(Test)* certificate to the Trusted Root Certification Authorities certificate store on the test computer, as described in [Installing Test Certificates](installing-test-certificates.md).

The following topics describe how the *ToastPkg* sample driver package can be installed on the test computer:

-   [Using the DevCon Tool to Install a Driver Package](using-the-devcon-tool-to-install-a-driver-package.md)

Once the [driver package](driver-packages.md) is installed, you can troubleshoot problems with the loading of test-signed drivers through the methods described in [Troubleshooting Install and Load Problems with Signed Driver Packages](troubleshooting-install-and-load-problems-with-signed-driver-packages.md).

For more information about how to install a test-signed driver package, see [Installing Test-Signed Driver Packages](installing-test-signed-driver-packages.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20a%20Test-Signed%20Driver%20Package%20on%20the%20Test%20Computer%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




