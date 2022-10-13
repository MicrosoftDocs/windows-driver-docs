---
title: INF SharedDriver Entry
description: INF SharedDriver Entry
keywords:
- INF files WDK non-HID keyboard/mouse
- SharedDriver entry WDK non-HID keyboard/mouse
ms.date: 10/11/2022
---

# INF SharedDriver Entry

**\[ControlFlags\]**

*SharedDriver* **=** *install-section-name* **,** *warning-text-string*

Before the keyboard or mouse class installer installs a PS/2 device, it checks for a *SharedDriver* entry in the [INF ControlFlags section](../install/inf-controlflags-section.md) for the device. If such an entry value exists, the class installer notifies the user by displaying the warning text string, and provides the user the option to cancel changing the PS/2 port driver.

## Entries and Values

- *SharedDriver*: Specifies that the device driver is shared by both a PS/2 keyboard and mouse device.
- *install-section-name*: Specifies a device's *DDInstall* section.
- *warning-text-string*: Specifies a string the class installer uses to warn a user before changing the PS/2 port driver.
