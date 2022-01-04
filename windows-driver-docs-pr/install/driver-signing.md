---
title: Driver Signing
description: Driver Signing
keywords:
- driver signing WDK
ms.date: 04/20/2017
---

# Driver Signing


Driver signing associates a [digital signature](digital-signatures.md) with a [driver package](driver-packages.md).

Windows device installation uses [digital signatures](digital-signatures.md) to verify the integrity of driver packages and to verify the identity of the vendor (software publisher) who provides the driver packages. In addition, the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) for 64-bit versions of Windows Vista and later versions of Windows specifies that a kernel-mode driver must be signed for the driver to load.

**Note**  Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows Server 2016 kernel-mode drivers must be signed by the Windows Hardware Dev Center Dashboard, which requires an EV certificate. For details, see [Driver Signing Policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md).

All drivers for Windows 10 (starting with version 1507, Threshold 1) signed by the Hardware Dev Center are SHA2 signed.  For details specific to operating system versions, see [Signing requirements by version](kernel-mode-code-signing-policy--windows-vista-and-later-.md#signing-requirements-by-version).

Kernel-mode driver binaries embed signed with dual (SHA1 and SHA2) certificates from a third party certificate vendor for operating systems earlier than Windows 10 may not load, or may cause a system crash on Windows 10. To fix this problem, install [KB 3081436](https://support.microsoft.com/help/3081436/cumulative-update-for-windows-10-august-11-2015).

## In this section


-   [Windows 10 in S mode Driver Requirements](Windows10SDriverRequirements.md)
-   [Managing the Signing Process](managing-the-signing-process.md)
-   [Signing Drivers during Development and Test](./introduction-to-test-signing.md)
-   [Signing Drivers for Public Release](signing-drivers-for-public-release--windows-vista-and-later-.md)
-   [Troubleshooting Install and Load Problems with Signed Driver Packages](./detecting-driver-load-errors.md)
-   [Microsoft Security Advisory 2880823](/security-updates/SecurityAdvisories/2016/2880823)

For general information about driver signing on Windows Vista and later versions of Windows, see the white paper [Digital Signatures for Kernel Modules on Systems Running Windows Vista](/previous-versions/dotnet/articles/bb530195(v=msdn.10)).


