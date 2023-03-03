---
title: INF SharedDriver entry
description: INF SharedDriver entry
keywords:
- INF files WDK non-HID keyboard/mouse
- SharedDriver entry WDK non-HID keyboard/mouse
ms.date: 03/02/2023
ms.topic: reference
---

# INF SharedDriver entry

**\[ControlFlags\]**

*SharedDriver* **=** *install-section-name* **,** *warning-text-string*

Before the keyboard or mouse class installer installs a PS/2 device, it checks for a *SharedDriver* entry in the [INF ControlFlags section](../install/inf-controlflags-section.md) for the device. If such an entry value exists, the class installer notifies the user by displaying the warning text string, and provides the user the option to cancel changing the PS/2 port driver.

## Entries and Values

- *SharedDriver*: Specifies that the device driver is shared by both a PS/2 keyboard and mouse device.
- *install-section-name*: Specifies a device's *DDInstall* section.
- *warning-text-string*: Specifies a string the class installer uses to warn a user before changing the PS/2 port driver.
