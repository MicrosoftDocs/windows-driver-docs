---
title: Release-Signing Driver Packages
description: Release-Signing Driver Packages
ms.assetid: 57125c3b-55f0-4b60-b4d9-1408e26faccb
keywords:
- driver signing WDK , driver packages
- signing drivers WDK , driver packages
- digital signatures WDK , driver packages
- signatures WDK , driver packages
- CAT files
- .cat files
- catalog files WDK driver signing , release signing
- public release driver signing WDK , about release signing
- release signing WDK , about release signing
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Release-Signing Driver Packages


In this section, a computer that signs drivers for release on Windows Vista and later versions of Windows is referred to as the *signing computer*. The signing computer must be running Windows XP SP2 or later versions of the Windows operating system. For example, a driver intended for release on Windows 7 can be signed on a computer that is running Windows Vista.

In addition, the signing computer must have the [driver signing tools](https://msdn.microsoft.com/library/windows/hardware/ff552958) installed.

**Note**  You must use the version of the [**SignTool**](https://msdn.microsoft.com/library/windows/hardware/ff551778) tool that is provided in the Windows Vista and later versions of the Windows Driver Kit (WDK). Earlier versions of this tool do not support the kernel-mode code signing policy for Windows Vista and later versions of Windows.

 

To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) and the [Plug and Play (PnP) device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) of Windows Vista and later versions of Windows, sign a driver for release as follows, based on the type of driver.

**Note**   The Windows code-signing policy requires that a signed [catalog file](catalog-files.md) for a driver be installed in the system component and driver database. PnP device installation automatically installs the catalog file of a PnP driver in the driver database. However, if you use a signed catalog file to sign a non-PnP driver, the installation application that installs the driver must also install the catalog file in the driver database.

 

### <a href="" id="pnp-kernel-mode-boot-start-driver"></a> PnP Kernel-Mode Boot-Start Driver

To comply with the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) of 64-bit versions of Windows Vista and later versions of Windows, embed a signature in the [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) file as follows:

1.  [Release-sign the driver file](release-signing-a-driver-file.md) with a [Software Publisher Certificate (SPC)](software-publisher-certificate.md).

2.  [Verify the SPC signature of the driver file](verifying-the-signature-of-a-release-signed-driver-file.md).

Starting with Windows Vista, embedding a signature in a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) file is optional for 32-bit versions of Windows. Although Windows will check whether a kernel-mode driver file has an embedded signature, an embedded signature is not required.

To comply with the [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) of Windows Vista and later versions of Windows, you must obtain a signed [catalog file](catalog-files.md) or sign the catalog file of the [driver package](driver-packages.md). If a driver file will also include an embedded signature, embed the signature in the driver file before signing the driver package's catalog file.

If the [Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=227016) has a test program for the driver, obtain a [WHQL Release Signature](whql-release-signature.md) for the driver package. If the HCK does not have a test program for the driver, [create a catalog file](creating-a-catalog-file-for-a-pnp-driver-package.md) and sign the [catalog file](catalog-files.md) as follows:

**Signing a catalog file for 64-bit versions**

You can sign a catalog file for 64-bit operating systems as follows:

1.  [Sign the catalog file with the SPC](signing-a-catalog-file-with-an-spc.md) that was used to embed a signature in the driver file.

2.  [Verify the SPC signature of the catalog file](verifying-the-spc-signature-of-a-catalog-file.md). You can verify the signature of a catalog file or you can verify the signatures of the individual file entries in the catalog file.

**Signing a catalog file for 32-bit versions**

You can either sign the [catalog file](catalog-files.md) with an SPC, as described in the section for 64-bit versions, or with a [commercial release certificate](commercial-release-certificate.md) as follows:

1.  [Sign the catalog file with a commercial release certificate](signing-a-catalog-file-with-a-commercial-release-certificate.md).

2.  [Verify the signature of the catalog file](verifying-the-signature-of-a-catalog-file-signed-by-a-commercial-relea.md). You can verify the signature of a catalog file or you can verify the signatures of the individual file entries in the catalog file.

### <a href="" id="non-pnp-kernel-mode-boot-start-driver"></a> Non-PnP Kernel-Mode Boot-Start Driver

To comply with the kernel-mode code signing policy of 64-bit versions of Windows Vista and later versions of Windows, embed a signature in a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) file as follows:

1.  [Release-sign the driver file](release-signing-a-driver-file.md) with an SPC.

2.  [Verify the SPC signature of the driver file](verifying-the-signature-of-a-release-signed-driver-file.md).

Starting with Windows Vista, embedding a signature in a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) file is optional for 32-bit versions of Windows. Although Windows will check whether a kernel-mode driver file has an embedded signature, an embedded signature is not required.

The PnP device installation signing requirements do not apply to non-PnP drivers.

### <a href="" id="pnp-kernel-mode-driver-that-is-not-a-boot-start-driver"></a> PnP Kernel-Mode Driver that is not a Boot-Start Driver

The kernel-mode code signing policy on 64-bit versions of Windows Vista and later versions of Windows does not require a non-boot PnP driver have an embedded signature. However, if the driver file will include an embedded signature, embed the signature in the driver file before signing the [driver package's](driver-packages.md) [catalog file](catalog-files.md).

To comply with the PnP device installation signing requirements, you must obtain a signed catalog file or sign the catalog file of the driver package.

If the [Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=227016) has a test program for the driver, obtain a [WHQL release signature](whql-release-signature.md) for the driver package. If the HCK does not have a test program for the driver, [create a catalog file](creating-a-catalog-file-for-a-pnp-driver-package.md) and sign the [catalog file](catalog-files.md) in the same manner as described in this section for signing the catalog file of a PnP kernel-mode [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver).

### <a href="" id="non-pnp-kernel-mode-driver-that-is-not-a-boot-start-driver"></a> Non-PnP Kernel-Mode Driver that is not a Boot-Start Driver

To comply with the kernel-mode code signing policy of 64-bit versions Windows Vista and later versions of Windows , embed a signature in the driver file or sign a catalog file for the [driver package](driver-packages.md).

Starting with Windows Vista, embedding a signature in a driver file is optional for 32-bit versions of Windows. Although Windows will check whether a kernel-mode driver file has an embedded signature, an embedded signature is not required.

The PnP device installation signing requirements do not apply to non-PnP drivers.

**Note**   Using embedded signatures is generally simpler and more efficient than by using a signed catalog file. For more information about the advantages and disadvantages of using embedded signatures versus signed catalog files, see [Test Signing a Driver](https://msdn.microsoft.com/windows-drivers/develop/signing_a_driver).

 

To embed a release signature in a file for a non-PnP kernel-mode driver that is not a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver), follow these steps:

1.  [Sign the driver file](release-signing-a-driver-file.md) with an SPC.

2.  [Verify the signature of the driver file](verifying-the-signature-of-a-release-signed-driver-file.md).

To release-sign a catalog file for a non-PnP kernel-mode driver that is not a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver), follow these steps:

1.  [Create a catalog file for the non-PnP driver](creating-a-catalog-file-for-a-non-pnp-driver-package.md).

2.  [Sign the catalog file with an SPC](signing-a-catalog-file-with-an-spc.md).

3.  [Verify the SPC signature of the catalog file](verifying-the-spc-signature-of-a-catalog-file.md).

If this type of driver has a signed [catalog file](catalog-files.md) instead of an embedded signature, the installation application that installs the driver must install the catalog file in the system component and driver database. For more information, see [Installing a Release-Signed Catalog File for a Non-PnP Driver](installing-a-release-signed-catalog-file-for-a-non-pnp-driver.md).

 

 





