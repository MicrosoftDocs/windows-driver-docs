---
title: Kernel-Mode Code Signing Requirements
description: Kernel-Mode Code Signing Requirements
ms.assetid: da02fcb3-d073-42cd-8247-71e2e9e93f65
keywords: ["driver signing WDK , kernel-mode code signing requirements", "signing drivers WDK , kernel-mode code signing requirements", "digital signatures WDK , kernel-mode code signing requirements", "signatures WDK , kernel-mode code signing requirements", "kernel-mode code signing requirements WDK", "kernel-mode driver signing WDK"]
---

# Kernel-Mode Code Signing Requirements


Starting with Windows Vista, the kernel-mode code signing policy controls whether a kernel-mode driver will be loaded. The signing requirements depend on the version of the Windows operating system and on whether the driver is being signed for public release or by a development team during the development and test of a driver. There are also [signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) that pertain to the installation of a PnP device and driver.

### <a href="" id="kernel-mode-code-signing-requirements-for-public-release-of-a-driver"></a> Kernel-Mode Code Signing Requirements for Public Release of a Driver

<a href="" id="--------64-bit-versions-of-windows-starting-with-"></a> **64-bit versions of Windows starting with Windows Vista**  
The kernel-mode code signing policy requires that a kernel-mode driver be signed as follows:

-   A kernel-mode [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) must have an embedded [Software Publisher Certificate (SPC)](software-publisher-certificate.md) signature. This applies to any type of PnP or non-PnP kernel-mode boot-start driver.

-   A non-PnP kernel-mode driver that is not a boot-start driver must have either a [catalog file](catalog-files.md) with an SPC signature or the driver file must include an embedded SPC signature.

-   A PnP kernel-mode driver that is not a boot-start driver must have either an embedded SPC signature, a catalog file with a [WHQL release signature](whql-release-signature.md), or a catalog file with an SPC signature. Although the kernel-mode code signing policy does not require that the catalog file of a PnP driver be signed, PnP device installation treats a driver as signed only if the catalog file of the driver is also signed.

<a href="" id="32-bit-versions-of-windows"></a>**32-bit versions of Windows**  
Windows Vista and later versions of Windows enforce the kernel-mode driver signing policy only for the following drivers:

-   Drivers that stream protected media. For more information about these requirements, see [Code-signing for Protected Media Components (Windows Vista and Later)](http://go.microsoft.com/fwlink/p/?linkid=69258)

-   Kernel-mode [*boot-start drivers*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver).

### <a href="" id="kernel-mode-code-signing-requirements-during-development-and-test"></a> Kernel-Mode Code Signing Requirements during Development and Test

<a href="" id="--------64-bit-versions-of-windows-starting-with-"></a> **64-bit versions of Windows starting with Windows Vista**  
The kernel-mode code signing policy requires that a kernel-mode driver be [test-signed](test-signing-driver-packages.md) and that test-signing is [enabled](the-testsigning-boot-configuration-option.md). A test signature can be a [WHQL test signature](whql-test-signature-program.md) or generated in-house by a [test certificate](test-certificates.md). Drivers must be test-signed as follows:

-   A kernel-mode [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) must have an embedded test signature. This applies to any type of PnP or non-PnP kernel-mode driver.

-   A kernel-mode driver that is not a [*boot-start driver*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver) must have either a test-signed [catalog file](catalog-files.md) or the driver file must include an embedded test signature. This applies to any type of PnP or non-PnP kernel-mode driver.

<a href="" id="32-bit-versions-of-windows"></a>**32-bit versions of Windows**  
Windows Vista and later versions of Windows enforce the kernel-mode driver signing policy only for the following drivers:

-   Drivers that stream protected media. For more information about these requirements, see [Code-signing for Protected Media Components (Windows Vista and Later)](http://go.microsoft.com/fwlink/p/?linkid=69258)

-   Kernel-mode [*boot-start drivers*](https://msdn.microsoft.com/library/windows/hardware/ff556272#wdkgloss-boot-start-driver).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Kernel-Mode%20Code%20Signing%20Requirements%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




