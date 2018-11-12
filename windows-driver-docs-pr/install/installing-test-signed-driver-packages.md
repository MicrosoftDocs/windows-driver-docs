---
title: Installing Test-Signed Driver Packages
description: Installing Test-Signed Driver Packages
ms.assetid: 6abbe51c-0fdf-465f-b1f2-d48e593a4f0e
keywords:
- test signing drivers WDK , installing test-signed driver packages
- driver signing WDK , driver packages
- signing drivers WDK , driver packages
- digital signatures WDK , driver packages
- signatures WDK , driver packages
- driver package digital signatures WDK
- package digital signatures WDK
- test signing drivers WDK , driver packages
- installing test-signed driver packages WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Test-Signed Driver Packages


Starting with Windows Vista, a test-signed [driver package](driver-packages.md) should install and load without user interaction if the following conditions are true:

-   The driver package complies with the generic requirements of Windows Vista and later versions of Windows.

-   The driver package is signed and the signature is verified, as described in [Test-Signing Driver Packages](test-signing-driver-packages.md).

-   The driver package is not altered after it is signed.

-   The test certificates that were used to sign the driver package are installed correctly on the test computer, as described in [Installing a Test Certificate on a Test Computer](installing-a-test-certificate-on-a-test-computer.md).

-   If a non-PnP driver has a signed [catalog file](catalog-files.md) instead of an embedded signature, the installation application that installs the driver has installed the catalog file in the system catalog root directory, as described in [Installing a Test-Signed Catalog File for a Non-PnP Driver](installing-a-test-signed-catalog-file-for-a-non-pnp-driver.md).

-   Test-signing is enabled on the test computer. For more information, see [the TESTSIGNING Boot Configuration Option](the-testsigning-boot-configuration-option.md).

For an overview of how to install a test-signed driver package, see [Installing a Test-Signed Driver Package on the Test Computer](installing-a-test-signed-driver-package-on-the-test-computer.md).

For more information about how to troubleshoot installation problems, see [Troubleshooting Install and Load Problems with Signed Driver Packages](troubleshooting-install-and-load-problems-with-signed-driver-packages.md).

 

 





