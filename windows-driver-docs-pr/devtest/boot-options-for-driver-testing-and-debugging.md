---
title: Tools for Changing Boot Options for Driver Testing and Debugging
description: Tools for Changing Boot Options for Driver Testing and Debugging
keywords:
- tools WDK , boot options
- driver development tools WDK , boot options
- boot options WDK
- driver testing WDK boot options
- testing drivers WDK boot options
- debugging drivers WDK boot options
- driver debugging WDK boot options
- operating system boot options WDK
- load configurations WDK boot options
ms.date: 04/19/2019
---

# Tools for Changing Boot Options for Driver Testing and Debugging

To test and debug drivers on a Microsoft Windows operating system, you must enable and configure features that are established when the operating system loads. The settings for these features are included in the *boot options*--values that determine how the boot loader loads and configures the operating system and other bootable programs and devices.


This section explains how to add, delete, and change boot options to create new load configurations for an operating system and how to use the boot entry parameters to customize a load configuration for driver testing and debugging.

By editing boot options, you can:

- Enable and configure debugging

- Load a particular kernel or hardware abstraction layer (HAL) file

- Limit the physical memory available to Windows

- Enable, disable, and configure Physical Address Extension (PAE) on 32-bit versions of Windows

- Reapportion virtual address space between user-mode and kernel-mode components (3GB) to test a driver in a very small kernel-mode address space

- Enable and configure Data Execution Prevention (/noexecute)

- Designate ports for Emergency Management Services (EMS) console redirection on headless servers

- Display the names of drivers as they load

This section includes:

- [Overview of Boot Options in Windows](boot-options-in-windows.md).
- [Boot Options Identifiers](boot-options-identifiers.md)
- [Editing Boot Options](editing-boot-options.md)
- [BCD Boot Options Reference](./bcd-boot-options-reference.md)
- [Using Boot Parameters](using-boot-parameters.md)
- [BCD Boot Options Reference](bcd-boot-options-reference.md)
- [Boot Options in Previous Versions of Windows](boot-options-in-previous-versions-of-windows.md)
