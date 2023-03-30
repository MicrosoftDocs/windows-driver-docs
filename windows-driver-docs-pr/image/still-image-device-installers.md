---
title: Still Image Device Installers
description: Microsoft provides a class installer for still image devices
ms.date: 03/24/2023
---

# Still Image Device Installers

> [!IMPORTANT]
> Starting with the WDK for Windows 11, version 22H2, WDF redistributable co-installers are no longer supported.
> To learn how to work around this change, see [WDF redistributable co-installers don't work](/windows-hardware/drivers/wdk-known-issues#wdf-redistributable-co-installers-dont-work) in the *WDK known issues* article.

Microsoft provides a class installer for still image devices, with the following features:

- WDM PnP detection when a device is installed.

- Installation wizard for legacy devices connected to parallel and serial ports.

- Support for special INF file entries (see [INF Files for Still Image Devices](inf-files-for-still-image-devices.md)).

- Support for vendor-supplied co-installer extensions. For more information, see [Writing a Co-installer](../install/writing-a-co-installer.md).

If necessary, vendors can provide customized installation programs that can be used instead of the Microsoft-supplied class installer.
