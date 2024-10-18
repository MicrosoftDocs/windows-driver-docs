---
title: Microsoft Basic Display Driver
description: The Microsoft Basic Display Driver is the in-box display driver that replaces the XDDM VGA Save and VGA PnP drivers.
keywords:
- BasicDisplay , Microsoft Basic Display Driver
- BasicRender , Microsoft Basic Render Driver
ms.date: 10/17/2024
---

# Microsoft Basic Display Driver

The Microsoft Basic Display Driver (*BasicDisplay.sys*) is a generic display driver that ships with the Windows operating system. It's the default display driver that the system loads in safe mode during setup when one of the following conditions occurs:

* An IHV graphics driver isn't present.
* The inbox installed graphics IHV driver isn't working or is disabled.

*BasicDisplay*'s primary purpose is to enable Windows to write to the display controller's linear frame buffer.

The key benefits of using *BasicDisplay* are:

* *BasicDisplay* helps to enable a consistent end user and developer experience because it's compatible with DirectX APIs and technologies such as the Desktop Composition.
* Server scenarios can benefit from the higher functionality (specifically, features like reboot-less updates, dynamic start and stop, and so on) that are provided by the WDDM driver model.
* *BasicDisplay* supports Unified Extensible Firmware Interface (UEFI) Graphics Output Protocol (GOP).
* *BasicDisplay* works on both WDDM and legacy XDDM hardware.

*BasicDisplay* can use the video BIOS to manage modes and resolutions on a single monitor. On UEFI platforms, *BasicDisplay* inherits the linear frame buffer that is set during boot. In this case, no mode or resolution changes are possible. As shown in the following figure, *BasicDisplay* is used in the following scenarios:

* Windows Server configurations that lack WDDM-capable graphics hardware can use *BasicDisplay*.
* In the early phases of Windows setup, just before the final boot, only the *BasicDisplay* is loaded.

  For example, a user has an older platform that is currently in working condition although it has no in-box graphics driver support for Windows 8 or later. The user upgrades to the current version of Windows and uses *BasicDisplay* for the setup, installation, and to retrieve an IHV driver if one is available.

* During driver installation, in the following cases:
  * When a user is installing a new WDDM IHV driver, *BasicDisplay* is used during the transition (from the point when the old WDDM IHV driver is uninstalled to the point before the new IHV driver is installed).
  * When a user encounters problems installing the latest WDDM IHV driver, the user or system can disable the current graphics driver and fallback to using *BasicDisplay*.
  * Driver upgrade: By using *BasicDisplay*, there's no need to go through a system reboot when upgrading to the IHV-recommended driver.
  * Safe mode: In this mode, only trusted drivers get loaded, including *BasicDisplay*.

:::image type="content" source="images/scenariossupportedmicrosoftbasicdisplaydriver.jpg" alt-text="Diagram showing driver installation scenarios in which the Microsoft Basic Display Driver is used.":::

*BasicDisplay* is always used with *BasicRender*, which is the system-supplied module that exposes the functionality of [WARP](/windows/win32/direct3darticles/directx-warp#enabling-maximum-performance-from-graphics-hardware) from an adapter in the kernel.

*BasicRender* can also be used on systems that don't have a render-capable driver installed (for example, display-only devices such as Matrox or DisplayLink that don't have a GPU).

Starting in Windows 11, both *BasicDisplay* and *BasicRender* run from their *DriverStore* locations in c:\Windows\System32\DriverStore.
