---
title: Test-Signing Driver Packages
description: Test-Signing Driver Packages
ms.assetid: 84727762-5ba0-48ea-8d5a-7ac54aadbb7e
keywords:
- driver signing WDK , driver packages
- signing drivers WDK , driver packages
- digital signatures WDK , driver packages
- signatures WDK , driver packages
- driver package digital signatures WDK
- package digital signatures WDK
- test signing drivers WDK , driver packages
- test signing driver packages WDK
- test signing driver packages WDK , about test signing driver packages
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Test-Signing Driver Packages


In this section, a computer that test-signs drivers for release on Windows Vista and later versions of Windows is referred to as the *signing computer*. The signing computer must be running Windows XP SP2 or later versions of Windows. For example, a driver intended for release on Windows 7 can be signed on a computer running Windows Vista.

In order to use the [driver signing tools](https://msdn.microsoft.com/library/windows/hardware/ff552958), the signing computer must have the Windows Vista and later versions of the WDK installed.

**Note**  You must use the version of the [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) tool that is provided in the Windows Vista and later versions of the Windows Driver Kit (WDK). Earlier versions of the SignTool do not support the kernel-mode code signing policy for Windows Vista and later versions of Windows.

 

To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) and the [Plug and Play (PnP) device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) of Windows Vista and later versions of Windows, you must sign a driver during the development and test of that driver. You can sign the driver on the signing computer as follows, based on the driver type.

**Note**   The Windows code-signing policy requires that a signed [catalog file](catalog-files.md) for a [driver package](driver-packages.md) be installed in the system component and driver database. PnP device installation automatically installs the catalog file of a PnP driver in the driver database. However, if you use a signed catalog file to sign a non-PnP driver, the installation application that installs the driver must also install the catalog file in the driver database.

 

### <a href="" id="pnp-kernel-mode-boot-start-driver"></a> PnP Kernel-Mode Boot-Start Driver

To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) of 64-bit versions of Windows Vista and later versions of Windows, embed a signature in the [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) file as follows:

1.  [Test-sign the driver file](test-signing-a-driver-file.md).

2.  [Verify the signature of the test-signed driver file](verifying-the-signature-of-a-test-signed-driver-file.md).

Starting with Windows Vista, embedding a signature in a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) file is optional for 32-bit versions of Windows. Although Windows will check if a kernel-mode driver file has an embedded signature, an embedded signature is not required.

To comply with the [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) of Windows Vista and later versions of Windows, you must also test-sign a [catalog file](catalog-files.md) for the [driver package](driver-packages.md). If a driver file will also include an embedded signature, embed the signature in the driver file before signing the driver package's catalog file.

You can submit a request to have the [Windows Hardware Quality Labs (WHQL) test-sign](whql-test-signature-program.md) the [catalog file](catalog-files.md). Alternatively, you can test-sign a catalog file yourself with a test certificate, as follows:

1.  [Create a catalog file](creating-a-catalog-file-for-a-test-signed-driver-package.md).

2.  [Test-sign the catalog file](test-signing-a-catalog-file.md).

3.  [Verify the signature of the test-signed catalog file](verifying-the-signature-of-a-test-signed-catalog-file.md).

    You can verify the signature of the catalog file itself or the signature of individual files that have corresponding entries in the catalog file.

### <a href="" id="non-pnp-kernel-mode-boot-start-driver"></a> Non-PnP Kernel-Mode Boot-Start Driver

To comply with the kernel-mode code signing policy of 64-bit versions of Windows Vista and later versions of Windows, embed a signature in a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) file as follows:

1.  [Test-sign the driver file](test-signing-a-driver-file.md).

2.  [Verify the signature of the test-signed driver file](verifying-the-signature-of-a-test-signed-driver-file.md).

Starting with Windows Vista, embedding a signature in a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) file is optional for 32-bit versions of Windows. Although Windows will check if a kernel-mode driver file has an embedded signature, an embedded signature is not required.

The [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) do not apply to non-PnP drivers.

### <a href="" id="pnp-kernel-mode-driver-that-is-not-a-boot-start-driver"></a> PnP Kernel-Mode Driver that is not a Boot-Start Driver

The kernel-mode code signing policy on 64-bit versions of Windows Vista and later versions of Windows does not require a non-boot PnP driver to have an embedded signature. However, if the driver file will include an embedded signature, embed the signature in the driver file before signing the [driver package's](driver-packages.md) [catalog file](catalog-files.md).

For a PnP kernel-mode driver that is not a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver), signing the catalog file for the driver package complies with the kernel-mode code signing policy on 64-bit versions of Windows Vista and later versions of Windows, as well as the PnP device installation signing requirements for all versions of Windows Vista and later.

You can submit a request to have the [Windows Hardware Quality Labs (WHQL) test-sign](whql-test-signature-program.md) the catalog file. Alternatively, you can test-sign a catalog file yourself with a test certificate in the same manner as described in this section for test-signing the catalog file of a PnP kernel-mode [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver).

### <a href="" id="non-pnp-kernel-mode-driver-that-is-not-a-boot-start-driver"></a> Non-PnP Kernel-Mode Driver that is not a Boot-Start Driver

To comply with the kernel-mode code signing policy of 64-bit versions of Windows Vista and later versions of Windows, embed a signature in the driver file or sign the [driver package's](driver-packages.md) [catalog file](catalog-files.md).

Starting with Windows Vista, embedding a signature in a driver file is optional for 32-bit versions of Windows. Although Windows will check if a kernel-mode driver file has an embedded signature, an embedded signature is not required.

The PnP device installation signing requirements do not apply to non-PnP drivers.

**Note**   Using embedded signatures is generally simpler and more efficient than using a signed catalog file. For more information about the advantages and disadvantages of using embedded signatures versus signed catalog files, see [Test Signing a Driver](https://msdn.microsoft.com/windows-drivers/develop/signing_a_driver).

 

### To embed a test signature in a file for a non-PnP kernel-mode driver that is not a boot-start driver

1.  [Test-sign the driver file](test-signing-a-driver-file.md).

2.  [Verify the signature of the test-signed driver file](verifying-the-signature-of-a-test-signed-driver-file.md).

### To test-sign a catalog file for a non-PnP kernel-mode driver that is not a boot-start driver

1.  [Create a catalog file for the non-PnP driver](creating-a-catalog-file-for-a-non-pnp-driver-package.md).

2.  [Test-sign the catalog file](test-signing-a-catalog-file.md).

3.  [Verify the signature of the test-signed catalog file](verifying-the-signature-of-a-test-signed-catalog-file.md).

 

 





