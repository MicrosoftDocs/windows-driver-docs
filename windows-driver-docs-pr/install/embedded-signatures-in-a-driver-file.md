---
title: Embedded Signatures in a Driver File
description: Embedded Signatures in a Driver File
keywords:
- embedded signatures WDK driver signing
- driver signing WDK , embedded
- signing drivers WDK , embedded
- digital signatures WDK , embedded
- signatures WDK , embedded
ms.date: 03/04/2024
ms.topic: concept-article
---

# Embedded Signatures in a Driver File

Starting in Windows 10 desktop editions (Home, Pro, Enterprise, and Education) and Windows Server 2016, kernel-mode drivers must be signed by the Windows Hardware Dev Center. To [register for the Windows Hardware Dev Center](../dashboard/hardware-program-register.md), you will need an EV certificate.

For more info about these changes, see [Driver Signing Changes in Windows 10](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Driver-Signing-changes-in-Windows-10-version-1607/ba-p/364894).

> [!NOTE]
> [Software Publisher Certificate (SPC)](./deprecation-of-software-publisher-certificates-and-commercial-release-certificates.md) were deprecated in 2021, and kernel-mode code signing requirements for 64-bit versions of Windows no longer require that a released kernel-mode *boot-start driver* have an embedded signature. 

[PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) do state that a [driver package](driver-packages.md) for a PnP device must have a signed catalog file. Driver files are signed by using the [SignTool](installing-a-catalog-file-by-using-signtool.md) tool.
