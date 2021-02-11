---
title: Embedded Signatures in a Driver File
description: Embedded Signatures in a Driver File
keywords:
- embedded signatures WDK driver signing
- driver signing WDK , embedded
- signing drivers WDK , embedded
- digital signatures WDK , embedded
- signatures WDK , embedded
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Embedded Signatures in a Driver File


In 64-bit versions of Windows Vista and later versions of Windows, the kernel-mode code signing requirements state that a released kernel-mode *boot-start driver* must have an embedded [Software Publisher Certificate (SPC)](software-publisher-certificate.md) signature. An embedded signature is not required for drivers that are not boot-start drivers.

> [!NOTE]
> Windows 10 for desktop editions (Home, Pro, Enterprise, and Education) and Windows Server 2016 kernel-mode drivers must be signed by the Windows Hardware Dev Center Dashboard, which requires an EV certificate. For more info about these changes, see [Driver Signing Changes in Windows 10](https://techcommunity.microsoft.com/t5/Windows-Hardware-Certification/Driver-Signing-changes-in-Windows-10-version-1607/ba-p/364894).

 

Having an embedded signature saves significant time during system startup because there is no need for the system loader to locate the [catalog file](catalog-files.md) for the driver at system startup. A typical computer might have many different catalog files in the catalog root store (*%System%\\CatRoot*). Locating the correct catalog file to verify the thumbprint of a driver file can require a substantial amount of time.

In addition to the load-time signature requirement that is enforced by the kernel-mode code signing policy, Plug and Play (PnP) device installation also enforces an install-time signing requirement. To comply with the [PnP device installation signing requirements](pnp-device-installation-signing-requirements--windows-vista-and-later-.md) of Windows Vista and later versions of Windows, a [driver package](driver-packages.md) for a PnP device must have a signed catalog file.

Embedded signatures do not interfere with the signature of a catalog file because the thumbprints that are contained in a catalog file and the thumbprint in an embedded signature selectively exclude the signature part of the driver file.

Driver files are signed by using the [SignTool](installing-a-catalog-file-by-using-signtool.md) tool.

 

 





