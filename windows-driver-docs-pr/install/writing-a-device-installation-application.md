---
title: Writing a Device Installation Application
description: Writing a Device Installation Application
keywords:
- installation applications WDK , about writing installation applications
- device installation applications WDK , about writing installation applications
- Device setup WDK device installations , writing installation applications
- installing devices WDK , writing installation applications
- writing device installation applications
- installation applications WDK
- device installation applications WDK
- applications WDK device installation
- device installations WDK , applications
ms.date: 03/23/2022
---

# Writing a Device Installation Application

It is preferred for driver packages to be submitted to the [Windows Hardware Developer Center portal](../dashboard/index.yml) and published to Windows Update to be delivered to systems.  However, if you need to write a *device installation application* to stage [driver packages](driver-packages.md) to the [Driver Store](driver-store.md) or update the driver packages installed on a device, see [Guidelines for Writing Device Installation Applications](guidelines-for-writing-device-installation-applications.md).

Your *device installation application* must handle two situations:

1.  The user plugs in your hardware before running your *device installation application*. This is commonly referred to as a [hardware-first installation](hardware-first-installation.md).

2.  The user runs your *device installation application* before plugging in your hardware. This is commonly referred to as a [software-first installation](software-first-installation.md).

If you would like to pair a device specific application with your driver package, it is recommended to create a Universal Windows Platform (UWP) app and associate it with your driver package.  See [Pairing a driver with a Universal Windows Platform (UWP) app](./pairing-app-and-driver-versions.md) for more information.