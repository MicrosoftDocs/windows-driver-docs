---
title: Driver Signing
description: Driver Signing
ms.assetid: 1f7d5340-c7be-4b6a-a85e-246dcc78b1fa
keywords:
- driver signing WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Driver Signing


Driver signing associates a [digital signature](digital-signatures.md) with a [driver package](driver-packages.md).

Windows device installation uses [digital signatures](digital-signatures.md) to verify the integrity of driver packages and to verify the identity of the vendor (software publisher) who provides the driver packages. In addition, the [kernel-mode code signing policy](kernel-mode-code-signing-policy--windows-vista-and-later-.md) for 64-bit versions of Windows Vista and later versions of Windows specifies that a kernel-mode driver must be signed for the driver to load.

**Note**  Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows Server 2016 kernel-mode drivers must be signed by the Windows Hardware Dev Center Dashboard, which requires an EV certificate. For details, see [Driver Signing Changes in Windows 10](http://blogs.msdn.com/b/windows_hardware_certification/archive/2015/04/01/driver-signing-changes-in-windows-10.aspx).

 

Kernel-mode driver binaries embed signed with dual (SHA1 and SHA2) certificates from a third party certificate vendor for operating systems earlier than Windows 10 may not load, or may cause a system crash on Windows 10. To fix this problem, install [KB 3081436](https://support.microsoft.com/kb/3081436).

## In this section


-   [Overview of Digital Signatures for Driver Installation](overview-of-digital-signatures-for-driver-installation.md)
-   [Windows 10 in S mode Driver Requirements](Windows10SDriverRequirements.md)
-   [Managing the Signing Process](managing-the-signing-process.md)
-   [Signing Drivers during Development and Test](signing-drivers-during-development-and-test.md)
-   [Signing Drivers for Public Release](signing-drivers-for-public-release.md)
-   [Troubleshooting Install and Load Problems with Signed Driver Packages](troubleshooting-install-and-load-problems-with-signed-driver-packages.md)

For general information about driver signing on Windows Vista and later versions of Windows, see the white paper [Digital Signatures for Kernel Modules on Systems Running Windows Vista](https://msdn.microsoft.com/library/bb530195).


 





