---
title: Installing Device Metadata Packages from WMIS
description: Installing Device Metadata Packages from WMIS
ms.assetid: e2466b8a-c9c7-4d0d-9ce7-4648c83fc272
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Installing Device Metadata Packages from WMIS


When the operating system detects a new device, it queries an online service called the [Windows Metadata and Internet Services](windows-metadata-and-internet-services.md) (WMIS) for a metadata package for the device. If a device metadata package is available, the Device Metadata Retrieval Client (DMRC) that runs on the local computer downloads the package from WMIS and installs the package on the local computer.

**Note**  Device metadata packages are not downloaded from WMIS if the current user is logged in by using any account with only guest privileges, such as the built-in Guest account.

 

If you submit your device metadata package to [Windows Quality Online Services (Winqual)](http://go.microsoft.com/fwlink/p/?linkid=62651) when you submit your [driver package](driver-packages.md) to the [Hardware Certification Kit (HCK)](http://go.microsoft.com/fwlink/p/?linkid=227016) for digital signing, your package will be available to WMIS for download requests made by DMRC on any computer that runs Windows 7 and later versions of Windows.

**Important**  We highly recommended that OEMs distribute device metadata packages only through WMIS. Distribution of device metadata packages through WMIS supports the *hardware-first* installation scenario. In this scenario, a new device is installed before the driver and device-specific software for the device is installed. For more information about this scenario, see [Hardware-First Installation](hardware-first-installation.md).

 

A device metadata package is installed through WMIS in the following way:

1.  When the user opens the gallery-view window of the Devices and Printers user interface, the [Device Metadata Retrieval Client](device-metadata-retrieval-client.md) (DMRC) tries to obtain device metadata for the devices that the Devices and Printers user interface displays.

    DMRC first searches the local computer's [device metadata cache](device-metadata-cache.md) and [device metadata store](device-metadata-store.md) for device metadata. If the device is newly installed, or if the device is scheduled for a periodic metadata update, DMRC queries WMIS for available metadata packages for the device.

2.  If a device metadata package is available, DMRC automatically downloads the package from WMIS, extracts the package's device metadata components, and saves them within the [device metadata cache](device-metadata-cache.md).

 

 





