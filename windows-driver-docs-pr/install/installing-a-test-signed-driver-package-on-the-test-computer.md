---
title: Installing a Test-Signed Driver Package on the Test Computer
description: Installing a Test-Signed Driver Package on the Test Computer
ms.date: 02/11/2022
---

# Installing a Test-Signed Driver Package on the Test Computer

You can install the test-signed [driver package](driver-packages.md) on the test computer once:

-   The test computer is prepared to install test-signed drivers or driver packages. For more information, see [Configuring the Test Computer to Support Test-Signing](configuring-the-test-computer-to-support-test-signing.md).

-   The test certificate is copied to the Trusted Root Certification Authorities certificate store on the test computer. For more information, see [Installing Test Certificates](installing-test-certificates.md).

This topic will first review the process of test-signing a driver package, and then describe how you can install the driver package on the test computer. This topic uses the *ToastPkg* sample driver package. Within the WDK installation directory, the package's source files are located in the *src\\general\\toaster\\toastpkg* directory.

Follow these steps to build and test-sign the *ToastPkg* sample driver package:

1.  On the signing computer, build the *ToastPkg* sample driver package's kernel-mode binaries. For more information about how to build drivers, see [Building a Driver](../develop/building-a-driver.md).

2.  On the signing computer, create the *Contoso.com(Test)* certificate as described in [Creating Test Certificates](creating-test-certificates.md).

3.  On the signing computer, create a [catalog file](catalog-files.md) for the *ToastPkg* sample driver package as described in [Creating a Catalog File for Test-Signing a Driver Package](creating-a-catalog-file-for-test-signing-a-driver-package.md).

4.  On the signing computer, test-sign the *ToastPkg* sample driver package's catalog file as described in [Test-Signing a Driver Package's Catalog File](test-signing-a-driver-package-s-catalog-file.md). When signing the driver package, use the *Contoso.com (Test)* certificate from the *PrivateCertStor*e for the test signature.

5.  Prepare the test computer to support test-signing, as described in [Configuring the Test Computer to Support Test-Signing](configuring-the-test-computer-to-support-test-signing.md).

6.  Copy the *Contoso.com(Test)* certificate to the Trusted Root Certification Authorities certificate store on the test computer, as described in [Installing Test Certificates](installing-test-certificates.md).

You can install the test-signed [driver package](driver-packages.md) on the computer through the [PnPUtil](../devtest/pnputil.md) tool.

Once the [driver package](driver-packages.md) is installed, you can troubleshoot problems with the loading of test-signed drivers through the methods described in [Troubleshooting Install and Load Problems with Signed Driver Packages](./detecting-driver-load-errors.md).

For more information about how to install a test-signed driver package, see [Installing Test-Signed Driver Packages](installing-test-signed-driver-packages.md).

 

