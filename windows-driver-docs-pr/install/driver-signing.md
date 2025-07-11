---
title: Driver Signing With Digital Signatures
description: Explore how driver signing associates a digital signature with a driver package.
keywords:
- driver signing WDK
ms.date: 07/11/2025
---

# Driver signing

Driver signing associates a [digital signature](digital-signatures.md) with a [driver package](driver-packages.md).

Windows device installation uses digital signatures to verify the integrity of driver packages and the identity of the vendor (software publisher) provider of the driver packages. In addition, the [kernel-mode driver signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) for 64-bit versions of Windows Vista and later versions of Windows specifies that a kernel-mode driver must be signed for the driver to load.

> [!CAUTION]
> Starting in Windows 10 and Windows Server 2016, the Windows Hardware Developer Center Dashboard must sign kernel-mode drivers. The process requires an extended validation (EV) certificate. For more information, see [Driver signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md).

Starting in Windows 10 version 1507, all drivers signed by the Hardware Dev Center are SHA2 signed. For details specific to operating system versions, see [Signing requirements by version](kernel-mode-code-signing-policy--windows-vista-and-later-.md#signing-requirements-by-version).

Kernel-mode driver binaries embed-signed with dual (SHA1 and SHA2) certificates from a non-Microsoft certificate vendor for operating systems earlier than Windows 10 might not load. The binaries can also cause a system crash on Windows 10 and later. To fix this problem, install [KB 3081436](https://support.microsoft.com/help/3081436/cumulative-update-for-windows-10-august-11-2015). The SHA hash values are provided in the **More information** - **File hash information** section of the KB article.

## In this section

- [Windows 10 in S mode driver requirements](windows10sdriverrequirements.md)
- [Managing the signing process](managing-the-signing-process.md)
- [Test-signing drivers during development and test](introduction-to-test-signing.md)
- [Signing drivers for public release](signing-drivers-for-public-release--windows-vista-and-later-.md)
- [Troubleshooting install and load problems with signed driver packages](detecting-driver-load-errors.md)
- [Microsoft Security Advisory 2880823](/security-updates/SecurityAdvisories/2016/2880823)

For general information about driver signing on Windows Vista and later versions of Windows, see the white paper [Digital signatures for kernel modules on systems running Windows Vista](/previous-versions/dotnet/articles/bb530195(v=msdn.10)).