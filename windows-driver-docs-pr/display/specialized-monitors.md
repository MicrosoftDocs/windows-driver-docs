---
title: Head-mounted and Specialized Monitors
description: Head-mounted and specialized monitors
keywords:
- display devices WDK
- monitor drivers WDK
- display drivers WDK , monitor drivers
- monitors
- HMD
- virtual reality
ms.date: 06/27/2024
ms.topic: concept-article
---

# Head-mounted and specialized monitors

Windows has built-in support for head-mounted displays (HMDs) and other kinds of specialized display scenarios. Only custom compositors can address these displays because the Desktop Windows Manager (DWM), which is the standard Windows system compositor, ignores them. In addition, HMDs and specialized displays are given the following properties by Windows:

* Since DWM ignores them, the Windows shell can't be extended to these displays (for example, wallpaper, desktop icons, taskbar).
* The OS doesn't automatically power them on while the PC is in use.
* They don't receive touch or mouse input.
* Apps can acquire them for dedicated control and presentation, subject to an access model.

Windows Mixed Reality headsets are one example of HMDs controlled by a custom compositor. Partner IHVs can build similar solutions using this documentation.

## Articles

[EDID extension for head-mounted and specialized monitors](specialized-monitors-edid-extension.md)

[Building custom compositors for HMDs and specialized displays](specialized-monitors-compositor.md)

## Version History

This section provides a history of changes to the specialized monitors feature in Windows. Not all versions of Windows have changes.

### Windows 10, version 2004

The following apply to Windows 10 Enterprise, Windows 10 Pro for Workstations, and Windows 10 IoT Enterprise:

* Added support for specialized displays with version 3 of the Microsoft EDID extension for HMDs and specialized displays.
* Added support for users to designate any monitor as a "specialized" display through Settings.

### Windows 10, version 1809

* Added support for building partner HMD compositors using the `Windows.Devices.Display.Core` family of APIs. Supported devices must conform to the Microsoft EDID extension for HMDs version 2.

### Windows 10, version 1709 (Fall Creators' Update)

* Windows Mixed Reality ships with support for virtual reality devices. Windows Mixed Reality devices must conform to the Microsoft EDID extension for HMDs version 1.
