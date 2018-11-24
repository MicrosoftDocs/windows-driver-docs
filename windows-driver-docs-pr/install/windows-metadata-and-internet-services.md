---
title: Windows Metadata and Internet Services
description: Windows Metadata and Internet Services
ms.assetid: 9e814be5-e22a-48d5-b46b-d22baa89e229
keywords:
- WMIS
- Metadata Information Server WDK
- metadata server WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Windows Metadata and Internet Services


The Windows Metadata and Internet Services (WMIS) manages device metadata packages that OEMs submit to the [Windows Quality Online Services (Winqual)](http://go.microsoft.com/fwlink/p/?linkid=62651) website over the Internet. By using the Winqual site, you can certify hardware devices and software applications for Windows.

When the OEM submits a device metadata package, Winqual completes the following process:

1.  Validates the XML documents that are contained within a device metadata package, and digitally signs those packages that pass validation.

2.  Makes the package available so that WMIS can distribute and install on remote computers.

In Windows 7 and later versions of Windows, the operating system uses WMIS to discover, index, and match device metadata packages for specific devices that are connected to the computer. For more information about this process, see [Installing Device Metadata Packages from WMIS](installing-device-metadata-packages-from-wmis.md).

 

 





