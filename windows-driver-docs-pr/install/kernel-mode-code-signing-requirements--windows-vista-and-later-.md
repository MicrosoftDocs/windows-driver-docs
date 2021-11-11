---
title: Kernel-Mode Code Signing Requirements
description: Kernel-Mode Code Signing Requirements
keywords:
- driver signing WDK , kernel-mode code signing requirements
- signing drivers WDK , kernel-mode code signing requirements
- digital signatures WDK , kernel-mode code signing requirements
- signatures WDK , kernel-mode code signing requirements
- kernel-mode code signing requirements WDK
- kernel-mode driver signing WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Kernel-Mode Code Signing Requirements


Starting with Windows Vista, the kernel-mode code signing policy controls whether a kernel-mode driver will be loaded. The signing requirements depend on the version of the Windows operating system and on whether the driver is being signed for public release or by a development team during the development and test of a driver. There are also [signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) that pertain to the installation of a PnP device and driver.

Virtual drivers have the same requirements as actual hardware drivers. In other words, they must comply with the requirements for the OS version for which they are targeted.

For info about signing and dashboard submission, see [Get drivers signed by Microsoft for multiple Windows versions](../dashboard/get-drivers-signed-by-microsoft-for-multiple-windows-versions.md).

### <a href="" id="kernel-mode-code-signing-requirements-for-public-release-of-a-driver"></a> Kernel-Mode Code Signing Requirements for Public Release of a Driver

> [!NOTE]
> Starting with Windows 10, version 1607, Windows will not load any new kernel mode drivers which are not signed by the Microsoft through the [Hardware Dev Center](../dashboard/register-for-the-hardware-program.md).  Valid signatures can be obtained by either [Hardware Certification](../dashboard/hardware-certification-submissions.md) or [Attestation](../dashboard/attestation-signing-a-kernel-driver-for-public-release.md). 


<a href="" id="--------64-bit-versions-of-windows-starting-with-"></a> **64-bit versions of Windows starting with Windows Vista**  
The kernel-mode code signing policy requires that a kernel-mode driver be signed as follows:

-   A kernel-mode boot-start driver must have an embedded [Software Publisher Certificate (SPC)](/windows-hardware/drivers/install/deprecation-of-software-publisher-certificates-and-commercial-release-certificates) signature. This applies to any type of PnP or non-PnP kernel-mode boot-start driver.

-   A non-PnP kernel-mode driver that is not a boot-start driver must have either a [catalog file](catalog-files.md) with an SPC signature or the driver file must include an embedded SPC signature.

-   A PnP kernel-mode driver that is not a boot-start driver must have either an embedded SPC signature, a catalog file with a [WHQL release signature](whql-release-signature.md), or a catalog file with an SPC signature. Although the kernel-mode code signing policy does not require that the catalog file of a PnP driver be signed, PnP device installation treats a driver as signed only if the catalog file of the driver is also signed.

<a href="" id="32-bit-versions-of-windows"></a>**32-bit versions of Windows**  
Windows Vista and later versions of Windows enforce the kernel-mode driver signing policy only for the following drivers:

-   Drivers that stream protected media. For more information about these requirements, see [Code-signing for Protected Media Components (Windows Vista and Later)](/windows-hardware/test/hlk/)

-   Kernel-mode *boot-start drivers*.

### <a href="" id="kernel-mode-code-signing-requirements-during-development-and-test"></a> Kernel-Mode Code Signing Requirements during Development and Test

<a href="" id="--------64-bit-versions-of-windows-starting-with-"></a> **64-bit versions of Windows starting with Windows Vista**  
The kernel-mode code signing policy requires that a kernel-mode driver be [test-signed](test-signing-driver-packages.md) and that test-signing is [enabled](the-testsigning-boot-configuration-option.md). A test signature can be a [WHQL test signature](whql-test-signature-program.md) or generated in-house by a [test certificate](./makecert-test-certificate.md). Drivers must be test-signed as follows:

-   A kernel-mode *boot-start driver* must have an embedded test signature. This applies to any type of PnP or non-PnP kernel-mode driver.

-   A kernel-mode driver that is not a *boot-start driver* must have either a test-signed [catalog file](catalog-files.md) or the driver file must include an embedded test signature. This applies to any type of PnP or non-PnP kernel-mode driver.

<a href="" id="32-bit-versions-of-windows"></a>**32-bit versions of Windows**  
Windows Vista and later versions of Windows enforce the kernel-mode driver signing policy only for the following drivers:

-   Drivers that stream protected media. For more information about these requirements, see [Code-signing for Protected Media Components (Windows Vista and Later)](/windows-hardware/test/hlk/)

-   Kernel-mode *boot-start drivers*.