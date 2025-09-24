---
title: What's New in Driver Development for Windows 11, Version 25H2
description: This section describes new features for driver development in Windows 11, version 25H2.
ms.date: 09/23/2025
ms.topic: whats-new
---

# <a name="top"></a>What's new in driver development for Windows 11, version 25H2

This section describes new features and updates for driver development in Windows 11, version 25H2. To target this version of Windows, you can use [WDK 10.0.26100.6584](./download-the-wdk.md) (released September 23, 2025).

## WDK NuGet package support

The WDK NuGet package consists of essential libraries, headers, DLL, tools and metadata used for building Windows drivers that can be shared and supported by modern CI/CD pipelines. Users can access and consume the NuGet packages directly from nuget.org within Visual Studio. Using NuGet with the WDK provides a convenient solution for WDK acquisition and updates. It manages dependencies such as the SDK, to help keep the driver development tool chain up to date. For more information, see [Install the latest WDK using NuGet - Step by Step](install-the-wdk-using-nuget.md).

## Audio

### SoundWire Device Class for Audio (SDCA)

The SDCA driver stack now supports the SDCA Companion Amp Function and Multichannel Capture scenarios. All SDCA drivers are included Inbox.
Enable connectivity to Wi-Fi 7 enterprise networks.

## Network drivers

- The WDK adds changes to the WiFiCx public header and library to enable IHV drivers to connect to Wi-Fi 7 enterprise networks. The WiFiCx driver TLV parser version is bumped up to 2.0.13 and capabilities are added to enable both Windows and the driver to be aware of Wi-Fi 7 enterprise connectivity support from the other.

### Packet Monitor Clnt NPIs

Pktmon Clnt NPIs are available for kernel-mode drivers to push network packet notifications into the PktMon platform. You can use these NPIs to diagnose performance and network connectivity issues. The NPIs allow run-time registration with the PktMon platform so that drivers can safely run on systems without Pktmon support.

## Kernel

### usermode_accessors.h

Contains dedicated functions for the kernel to use when reading from and writing to the user-mode virtual address space.

## Storage drivers

### Icekeymaninterface.h

- Adds new flag to capabilities structure for implementation to attest FIPS module compliance. 
- Introduces new interface API for validating a wrapped key can be unwrapped by the system.

## Related articles

For information on what was new for drivers in past Windows releases, see the following pages:

- [Driver development changes for Windows 11, version 24H2](driver-changes-for-windows-11-version-24h2.md)
- [Driver development changes for Windows 11, version 23H2](driver-changes-for-windows-11-version-23h2.md)
- [Driver development changes for Windows 11, version 22H2](driver-changes-for-windows-11-version-22h2.md)
- [Driver development changes for Windows 11, version 21H2](driver-changes-for-windows-11-version-21h2.md)
- [Driver development changes for Windows Server 2022](driver-changes-for-windows-server-2022.md)

[Back to Top](#top)
