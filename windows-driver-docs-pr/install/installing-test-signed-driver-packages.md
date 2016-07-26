---
title: Installing Test-Signed Driver Packages
description: Installing Test-Signed Driver Packages
ms.assetid: 6abbe51c-0fdf-465f-b1f2-d48e593a4f0e
keywords: ["test signing drivers WDK , installing test-signed driver packages", "driver signing WDK , driver packages", "signing drivers WDK , driver packages", "digital signatures WDK , driver packages", "signatures WDK , driver packages", "driver package digital signatures WDK", "package digital signatures WDK", "test signing drivers WDK , driver packages", "installing test-signed driver packages WDK"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Installing%20Test-Signed%20Driver%20Packages%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




