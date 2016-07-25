---
title: PnP Device Installation Signing Requirements
description: PnP Device Installation Signing Requirements
ms.assetid: 92527b24-b29a-4a78-886d-fafd620090d1
keywords: ["driver signing WDK , PnP device installations", "signing drivers WDK , PnP device installations", "digital signatures WDK , PnP device installations", "signatures WDK , PnP device installations", "PnP WDK driver signing", "Plug and Play WDK driver signing"]
---

# PnP Device Installation Signing Requirements


The driver signing requirements for Plug and Play (PnP) device installation depend on the version of Windows and on whether the driver is being signed for public release or by a development team during the development and test of the driver. All 64-bit versions of Windows enforce [kernel-mode code signing requirements](kernel-mode-code-signing-requirements--windows-vista-and-later-.md) that determine whether a kernel-mode driver can be loaded.

### <a href="" id="pnp-signing-requirements-for-public-release-of-a-driver"></a> PnP Signing Requirements for Public Release of a Driver

The [Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=227016) has [test categories](http://go.microsoft.com/fwlink/p/?linkid=189178) for a variety of device types. If a test category for the device type is included in this list, you should obtain a [WHQL release signature](whql-release-signature.md).

A valid WHQL release signature verifies that the driver complies with the requirements of the HCK, verifies the identity of the publisher, and verifies that the driver has not been altered.

To be considered signed by PnP device installation, the [catalog file](catalog-files.md) of the [driver package](driver-packages.md) must be signed by WHQL or signed by a third-party [release certificate](release-certificates.md) (a [Software Publisher Certificate (SPC)](software-publisher-certificate.md) or a commercial release certificate). A WHQL release signature should be used if one can be obtained. A third-party release signature verifies the identity of the publisher and that the driver has not been altered. However, unlike a WHQL release signature, a third-party release signature does not verify driver functionality.

Also be aware that for 64-bit versions of Windows Vista and later versions of Windows, the kernel-mode code signing policy further requires that a kernel-mode driver be signed by WHQL or by an SPC.

For more information about release-signing, see [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md).

### <a href="" id="pnp-signing-requirements-for-development-and-test-of-a-driver"></a> PnP Signing Requirements for Development and Test of a Driver

In 64-bit versions of Windows Vista and later versions of Windows, a driver must have a [WHQL test signature](whql-test-signature-program.md) or must be signed by a [test certificate](test-certificates.md). For more information about test-signing drivers, see [Signing Drivers during Development and Test](signing-drivers-during-development-and-test--windows-vista-and-later-.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20PnP%20Device%20Installation%20Signing%20Requirements%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




