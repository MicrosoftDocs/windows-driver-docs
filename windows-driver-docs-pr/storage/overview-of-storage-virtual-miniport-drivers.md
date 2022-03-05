---
title: About Storport virtual miniport drivers
description: Overview of Storage Virtual Miniport Drivers
keywords:
- storage virtual miniport drivers WDK , about
- virtual miniport drivers WDK
- miniport drivers WDK storage , virtual
ms.date: 03/01/2022
---

# About Storport virtual miniport drivers

The Storport virtual miniport (VMiniport) driver interface is designed for Storport miniport drivers that have no strict association with the physical hardware. Unlike hardware-associated ("physical") miniport drivers, virtual miniport drivers can make calls to Windows Driver Model (WDM) routines.

> [!NOTE]
> The VMiniport extension does not remove the restriction on physical miniport drivers to call only Storport routines.

The VMiniport interface frees the VMiniport from relying on the Storport port driver for handling memory and synchronization. The interface enables VMiniport to do I/O in more efficient ways than some physical miniports. These changes were targeted at, but not limited to, enabling storage technologies such as iSCSI and Infiniband as well as non-standard storage interfaces.

Use caution when you [implement a VMiniport driver](initialization-of-storage-virtual-miniport-drivers.md). Though this extension give greater flexibility, it demands greater care in detecting errors, validating paths, and I/O timing.
