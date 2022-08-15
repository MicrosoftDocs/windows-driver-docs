---
title: Head-mounted and specialized monitors
description: Head-mounted and specialized monitors
keywords:
- display devices WDK
- monitor drivers WDK
- display drivers WDK , monitor drivers
- monitors
- HMD
- virtual reality
ms.date: 11/30/2018
ms.topic: article
---

# Head-mounted and specialized monitors

Windows has built-in support for head-mounted displays (HMDs) and other kinds of "specialized" display scenarios. These displays can only be addressed by custom compositors, as they are ignored by the standard Windows system compositor (DWM). In addition, HMDs and specialized displays are given the following properties by Windows:

* Since they are ignored by the system compositor (DWM), the Windows shell cannot be extended to these displays (e.g. wallpaper, desktop icons, taskbar).
* They are not powered on automatically by the OS while the PC is in use.
* They do not receive touch or mouse input.
* They can be acquired for control by apps for dedicated control and presentation, subject to an access model.

Windows Mixed Reality headsets are one example of HMDs controlled by a custom compositor. Similar solutions can be built by third-parties using this documentation.

## Topics

[EDID extension for head-mounted and specialized monitors](specialized-monitors-edid-extension.md)

[Building custom compositors for HMDs and specialized displays](specialized-monitors-compositor.md)

## Version History

### Windows 10, version 2004

The following apply to Windows 10 Enterprise, Windows 10 Pro for Workstations, and Windows 10 IoT Enterprise:

* Added support for "specialized" displays with version 3 of the Microsoft EDID extension for HMDs and specialized displays.
* Added support for users to designate any monitor as a "specialized" display through Settings.

### Windows 10, version 1809

* Added support for building third-party HMD compositors using the `Windows.Devices.Display.Core` family of APIs. Supported devices must conform to the Microsoft EDID extension for HMDs version 2.

### Windows 10, version 1709 (Fall Creators' Update)

* Windows Mixed Reality ships with support for virtual reality devices. Windows Mixed Reality devices must conform to the Microsoft EDID extension for HMDs version 1.
