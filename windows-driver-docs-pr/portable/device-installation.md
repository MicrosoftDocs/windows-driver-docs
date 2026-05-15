---
description: Device Installation
title: Device Installation
ms.date: 12/09/2024
ms.topic: overview
---

# Device Installation

Windows Portable Devices (WPD) are User-Mode Driver Framework (UMDF) compliant drivers. Therefore they will use the Windows Plug and Play (PnP) infrastructure for installation.

There are also various ways to create a PnP experience on buses that are not traditionally PnP. For example, using PnP-X for network devices. This enables discovery of the devices over arbitrary buses and lets the PnP component perform the installation as before.

Once the driver for the device is installed on the system, clients will use WPD APIs to enumerate all installed and currently active WPD Devices.

## Related topics

[WPD Drivers Overview](wpd-drivers-overview.md)

 

 





