---
title: Release Certificates
description: Release Certificates
keywords:
- public release driver signing WDK , release certificates
- release signing WDK , release certificates
- release certificates WDK
- certificates WDK , release
ms.date: 04/20/2017
---

# Release Certificates


To comply with the kernel-mode code signing policy of 64-bit versions of Windows Vista and later versions of Windows, you must obtain a [WHQL release signature](whql-release-signature.md) or use a [Software Publisher Certificate (SPC)](./deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md) to sign the [catalog file](catalog-files.md) of kernel-mode [driver packages](driver-packages.md).

If the driver is a *boot-start driver* for 64-bit systems, you must also [embed](embedded-signatures-in-a-driver-file.md) an SPC signature in the driver file. This applies to any type of Plug and Play (PnP) or non-PnP kernel-mode driver.

The [Hardware Certification Kit (HCK)](/previous-versions/windows/hardware/hck/jj124227(v=vs.85)) has [test categories](/windows-hardware/test/hlk/) for a variety of device types. To comply with the [PnP device installation requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) of 32-bit versions of Windows Vista and later versions of Windows, you should obtain a WHQL release signature if the HCK has a test category for the device type. If you cannot obtain a WHQL release signature, you must use either an SPC or a [commercial release certificate](./deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md) to sign a PnP kernel-mode driver.