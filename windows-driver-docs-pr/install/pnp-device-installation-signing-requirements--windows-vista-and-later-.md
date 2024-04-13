---
title: PnP Device Installation Signing Requirements
description: PnP Device Installation Signing Requirements
keywords:
- driver signing WDK , PnP device installations
- signing drivers WDK , PnP device installations
- digital signatures WDK , PnP device installations
- signatures WDK , PnP device installations
- PnP WDK driver signing
- Plug and Play WDK driver signing
ms.date: 03/03/2022
---

# PnP Device Installation Signing Requirements

The [driver package](driver-packages.md) signing requirements for Plug and Play (PnP) device installation depend on the version of Windows and on whether the driver is being signed for public release or by a development team during the development and test of the driver. These signing requirements need to be met in order for the driver package to be staged to the [Driver Store](driver-store.md). In addition to these requirements placed upon the driver package [catalog's](catalog-files.md) signature, in order for a kernel mode driver to be loaded, there are restrictions placed upon the signature that is used to verify the integrity of that kernel-mode driver binary.  All 64-bit versions of Windows enforce [kernel-mode code signing requirements](kernel-mode-code-signing-requirements--windows-vista-and-later-.md) that determine whether a kernel-mode driver can be loaded.  If the kernel-mode driver binary does not have an [embedded signature](embedded-signatures-in-a-driver-file.md), then the driver package catalog's signature needs to conform to [kernel-mode code signing requirements](kernel-mode-code-signing-requirements--windows-vista-and-later-.md) in order for the kernel-mode binary to be able to load.

## <a href="" id="pnp-signing-requirements-for-public-release-of-a-driver"></a> PnP Signing Requirements for Public Release of a Driver

The [Windows Hardware Lab Kit (Windows HLK)](/windows-hardware/test/hlk/windows-hardware-lab-kit) has [test categories](/windows-hardware/test/hlk/testref/hardware-lab-kit-test-reference) for a variety of device types. If a test category for the device type is included in this list, you should obtain a [WHQL release signature](whql-release-signature.md).

A valid WHQL release signature verifies that the driver complies with the requirements of the [Windows Hardware Compatibilty Program](/windows-hardware/design/compatibility), verifies the identity of the publisher, and verifies that the driver has not been altered.

To be considered signed by PnP device installation, the [catalog file](catalog-files.md) of the [driver package](driver-packages.md) must be signed by WHQL or signed by a third-party [release certificate](release-certificates.md) (a [Software Publisher Certificate (SPC)](./deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md) or a commercial release certificate). A WHQL release signature should be used if one can be obtained. A third-party release signature verifies the identity of the publisher and that the driver has not been altered. However, unlike a WHQL release signature, a third-party release signature does not verify driver functionality.

Also be aware that for 64-bit versions of Windows Vista and later versions of Windows, the kernel-mode code signing policy further requires that a kernel-mode driver be signed by WHQL or by an SPC.

For more information about release-signing, see [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md).

> [!NOTE]
> Some editions of Windows may require that the [catalog file](catalog-files.md) be signed by WHQL and may not accept a catalog signed by a third-party release certificate.  For example, [Windows 10 in S mode](windows10sdriverrequirements.md) and editions for architectures other than x86 and amd64 require catalog files for driver packages signed for release to have been signed by WHQL.

## <a href="" id="pnp-signing-requirements-for-development-and-test-of-a-driver"></a> PnP Signing Requirements for Development and Test of a Driver

In 64-bit versions of Windows Vista and later versions of Windows, a driver must have a [WHQL test signature](whql-test-signature-program.md) or must be signed by a [test certificate](./makecert-test-certificate.md). For more information about test-signing drivers, see [Signing Drivers during Development and Test](./introduction-to-test-signing.md).
